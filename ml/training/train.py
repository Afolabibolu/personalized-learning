"""Trains Logistic Regression and Random Forest on simulated students and
compares them with the rule baseline.

    cd ml && python -m training.train
    cd ml && python -m training.train --real-test rows.csv   # optional, real student rows

Reads simulated students' attempts and study logs from Supabase and builds one
row per student per topic (features.training_rows). The rule baseline ("last
score below 50%"), Logistic Regression and Random Forest are scored on the
same stratified hold-out split and the same 5-fold cross-validation folds.
Saves the models to ml/models/ and the results, all labelled "simulated
data", to ml/results/.

--real-test scores the already-trained models and the rule on a CSV of real
student rows (from scripts/export_real_rows.py) and saves a separate table
titled "real student data". It does not retrain.
"""

import argparse
from datetime import datetime, timezone

import joblib
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from sklearn.ensemble import RandomForestClassifier  # noqa: E402
from sklearn.linear_model import LogisticRegression  # noqa: E402
from sklearn.metrics import (  # noqa: E402
    ConfusionMatrixDisplay,
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import StratifiedKFold, cross_validate, train_test_split  # noqa: E402
from sklearn.pipeline import Pipeline  # noqa: E402
from sklearn.preprocessing import StandardScaler  # noqa: E402

from app import data  # noqa: E402
from app.config import LR_MODEL_PATH, MODEL_VERSION, MODELS_DIR, RESULTS_DIR, RF_MODEL_PATH  # noqa: E402
from training.baseline import LastScoreRule  # noqa: E402
from training.features import FEATURES, to_frames, training_rows  # noqa: E402

SEED = 42
TAG = "simulated_data"
METRICS = ["accuracy", "precision", "recall", "f1"]
METRIC_LABELS = {"accuracy": "Accuracy", "precision": "Precision", "recall": "Recall", "f1": "F1"}
RULE, LR, RF = "Rule baseline (last score < 50%)", "Logistic Regression", "Random Forest"
COLOURS = {RULE: "#94a3b8", LR: "#4f46e5", RF: "#10b981"}


def make_models() -> dict:
    return {
        RULE: LastScoreRule(),
        LR: Pipeline([
            ("scale", StandardScaler()),
            ("model", LogisticRegression(max_iter=1000, random_state=SEED)),
        ]),
        RF: RandomForestClassifier(n_estimators=300, min_samples_leaf=5, random_state=SEED),
    }


def slug(name: str) -> str:
    return {RULE: "rule_baseline", LR: "logistic_regression", RF: "random_forest"}[name]


def load_training_data() -> pd.DataFrame:
    db = data.service_client()
    simulated = {r["id"] for r in data.fetch_all(
        lambda: db.table("profiles").select("id").eq("is_simulated", True).order("id"))}
    scores = data.fetch_all(lambda: db.table("ml_attempt_topic_scores").select(
        "student_id, topic_id, attempt_id, completed_at, score").order("attempt_id").order("topic_id"))
    logs = data.fetch_all(lambda: db.table("study_logs").select(
        "student_id, topic_id, logged_at, duration_minutes").order("id"))
    scores = [r for r in scores if r["student_id"] in simulated]
    logs = [r for r in logs if r["student_id"] in simulated]
    if not scores:
        raise SystemExit("No simulated students found. Run python scripts/seed_demo.py first.")
    return training_rows(*to_frames(scores, logs))


def scores_for(y_true, y_pred) -> dict:
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred, zero_division=0),
        "recall": recall_score(y_true, y_pred, zero_division=0),
        "f1": f1_score(y_true, y_pred, zero_division=0),
    }


def markdown_table(df: pd.DataFrame) -> str:
    header = "| " + " | ".join(df.columns) + " |"
    rule = "| " + " | ".join("---" for _ in df.columns) + " |"
    body = ["| " + " | ".join(str(v) for v in row) + " |" for row in df.itertuples(index=False)]
    return "\n".join([header, rule, *body])


def train_and_compare() -> None:
    RESULTS_DIR.mkdir(exist_ok=True)
    MODELS_DIR.mkdir(exist_ok=True)
    for old in RESULTS_DIR.glob(f"*_{TAG}.*"):
        old.unlink()  # so nothing stale from an earlier run is left behind

    rows = load_training_data()
    X, y = rows[FEATURES], rows["requires_attention"]
    n_students = rows["student_id"].nunique()
    print(f"{len(rows)} rows ({y.mean():.1%} require attention) from {n_students} simulated students")

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, stratify=y, random_state=SEED)
    models = make_models()
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)

    records, probabilities = [], {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        test = scores_for(y_test, model.predict(X_test))
        probabilities[name] = model.predict_proba(X_test)[:, 1]
        folds = cross_validate(make_models()[name], X, y, cv=cv, scoring=METRICS)
        record = {"model": name}
        for m in METRICS:
            record[f"{m}_test"] = round(test[m], 3)
            record[f"{m}_cv_mean"] = round(folds[f"test_{m}"].mean(), 3)
            record[f"{m}_cv_sd"] = round(folds[f"test_{m}"].std(), 3)
        records.append(record)
    metrics = pd.DataFrame(records)

    # How the app actually ranks: the average of both models' probabilities.
    average = (probabilities[LR] + probabilities[RF]) / 2
    system = scores_for(y_test, (average >= 0.5).astype(int))

    # Tables
    metrics.to_csv(RESULTS_DIR / f"metrics_{TAG}.csv", index=False)
    display = pd.DataFrame({
        "Model": metrics["model"],
        **{METRIC_LABELS[m]: [f"{r[f'{m}_cv_mean']:.3f} ± {r[f'{m}_cv_sd']:.3f}" for _, r in metrics.iterrows()] for m in METRICS},
    })
    holdout = pd.DataFrame({
        "Model": [*metrics["model"], "System ranking (average of LR and RF probabilities)"],
        **{METRIC_LABELS[m]: [*(f"{v:.3f}" for v in metrics[f"{m}_test"]), f"{system[m]:.3f}"] for m in METRICS},
    })
    trained_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    (RESULTS_DIR / f"metrics_{TAG}.md").write_text(
        "# Model comparison (simulated data)\n\n"
        "All figures come from simulated students created by `scripts/seed_demo.py` (rules in "
        "`simulation_rules.md`), not from real students.\n\n"
        f"- Rows: {len(rows)} student-topic pairs from {n_students} simulated students\n"
        f"- Positive class (requires attention: next attempt below 50%): {y.mean():.1%}\n"
        f"- Features: {', '.join(FEATURES)}\n"
        "- The rule baseline uses only last_score; the models use all six features.\n"
        f"- Trained: {trained_at}, model version {MODEL_VERSION}\n\n"
        "## 5-fold stratified cross-validation, mean ± standard deviation (simulated data)\n\n"
        f"{markdown_table(display)}\n\n"
        "## Hold-out test set: 25%, stratified, the same rows for all three (simulated data)\n\n"
        f"{markdown_table(holdout)}\n"
    )

    # Confusion matrices, one per model, on the hold-out rows
    for name, model in models.items():
        fig, ax = plt.subplots(figsize=(5.2, 4.6))
        ConfusionMatrixDisplay.from_predictions(
            y_test, model.predict(X_test), display_labels=["Adequately\nmastered", "Requires\nattention"],
            cmap="Blues", ax=ax, colorbar=False)
        ax.set_title(f"{name}: confusion matrix\n(simulated data)")
        fig.tight_layout()
        fig.savefig(RESULTS_DIR / f"confusion_{slug(name)}_{TAG}.png", dpi=150)
        plt.close(fig)

    # All three on the four metrics (cross-validation mean, error bar = one standard deviation)
    fig, ax = plt.subplots(figsize=(8, 4.2))
    width = 0.26
    xs = np.arange(len(METRICS))
    for i, row in metrics.iterrows():
        means = [row[f"{m}_cv_mean"] for m in METRICS]
        sds = [row[f"{m}_cv_sd"] for m in METRICS]
        bars = ax.bar(xs + (i - 1) * width, means, width, yerr=sds, capsize=3,
                      label=row["model"], color=COLOURS[row["model"]])
        ax.bar_label(bars, fmt="%.2f", fontsize=7, padding=2)
    ax.set_xticks(xs, [METRIC_LABELS[m] for m in METRICS])
    ax.set_ylim(0, 1.1)
    ax.set_ylabel("5-fold cross-validation mean")
    ax.set_title("Rule baseline vs Logistic Regression vs Random Forest (simulated data)")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False, fontsize=8)
    fig.tight_layout()
    fig.savefig(RESULTS_DIR / f"model_comparison_{TAG}.png", dpi=150)
    plt.close(fig)

    # What each model relies on: LR coefficients (standardised features) and RF importances
    lr_coef = pd.Series(models[LR].named_steps["model"].coef_[0], index=FEATURES)
    rf_imp = pd.Series(models[RF].feature_importances_, index=FEATURES)
    weights = pd.DataFrame({
        "feature": FEATURES,
        "lr_coefficient_standardised": lr_coef.round(3).values,
        "rf_importance": rf_imp.round(3).values,
    })
    weights.to_csv(RESULTS_DIR / f"feature_weights_{TAG}.csv", index=False)
    with open(RESULTS_DIR / f"metrics_{TAG}.md", "a") as f:
        f.write(
            "\n## What each model relies on (simulated data)\n\n"
            "Logistic Regression coefficients are on standardised features: positive means a higher value makes "
            "\"requires attention\" more likely. Random Forest importances sum to 1.\n\n"
            + markdown_table(weights.rename(columns={
                "feature": "Feature", "lr_coefficient_standardised": "LR coefficient",
                "rf_importance": "RF importance"})) + "\n"
        )
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 3.8))
    order = rf_imp.sort_values().index
    ax1.barh(order, lr_coef[order], color=["#ef4444" if v > 0 else "#4f46e5" for v in lr_coef[order]])
    ax1.axvline(0, color="#475569", linewidth=0.8)
    ax1.set_title("Logistic Regression coefficients")
    ax1.set_xlabel("← less likely   requires attention   more likely →")
    ax2.barh(order, rf_imp[order], color="#10b981")
    ax2.set_title("Random Forest feature importances")
    ax2.set_xlabel("Importance")
    ax2.set_yticklabels([])
    fig.suptitle("What each model relies on (simulated data)")
    fig.tight_layout()
    fig.savefig(RESULTS_DIR / f"feature_weights_{TAG}.png", dpi=150)
    plt.close(fig)

    # Models, versioned
    meta = {"version": MODEL_VERSION, "features": FEATURES, "trained_at": trained_at, "rows": len(rows)}
    joblib.dump({"model": models[LR], **meta}, LR_MODEL_PATH)
    joblib.dump({"model": models[RF], **meta}, RF_MODEL_PATH)

    print("\n5-fold cross-validation (simulated data):")
    print(display.to_string(index=False))
    print("\nHold-out test set (simulated data):")
    print(holdout.to_string(index=False))
    print("\nWhat each model relies on (simulated data):")
    print(weights.to_string(index=False))
    print(f"\nSaved {LR_MODEL_PATH.name}, {RF_MODEL_PATH.name} and results in {RESULTS_DIR}")


def real_test(path: str) -> None:
    """Scores the trained models and the rule on real student rows (no retraining)."""
    rows = pd.read_csv(path)
    missing = [c for c in [*FEATURES, "requires_attention"] if c not in rows.columns]
    if missing:
        raise SystemExit(f"{path} is missing columns: {missing}")
    if not (LR_MODEL_PATH.exists() and RF_MODEL_PATH.exists()):
        raise SystemExit("No trained models. Run python -m training.train first.")
    X, y = rows[FEATURES], rows["requires_attention"]
    models = {RULE: LastScoreRule().fit(X), LR: joblib.load(LR_MODEL_PATH)["model"], RF: joblib.load(RF_MODEL_PATH)["model"]}
    table = pd.DataFrame([{"Model": n, **{METRIC_LABELS[m]: f"{v:.3f}" for m, v in scores_for(y, mdl.predict(X)).items()}}
                          for n, mdl in models.items()])
    RESULTS_DIR.mkdir(exist_ok=True)
    table.to_csv(RESULTS_DIR / "metrics_real_student_data.csv", index=False)
    (RESULTS_DIR / "metrics_real_student_data.md").write_text(
        "# Model comparison on real student data\n\n"
        f"Models trained on simulated data, scored without retraining on {len(rows)} real student-topic rows "
        f"from {rows['student_id'].nunique() if 'student_id' in rows else 'unknown'} students "
        f"({y.mean():.1%} require attention). Source: `{path}`.\n\n{markdown_table(table)}\n"
    )
    print("Real student data:\n" + table.to_string(index=False))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--real-test", metavar="CSV", help="score trained models on real student rows instead")
    args = parser.parse_args()
    if args.real_test:
        real_test(args.real_test)
    else:
        train_and_compare()


if __name__ == "__main__":
    main()
