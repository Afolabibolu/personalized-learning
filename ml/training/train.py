"""Trains Logistic Regression and Random Forest on simulated students.

    cd ml && python -m training.train

Reads simulated students' attempts and study logs from Supabase, builds one
row per student per topic (features.training_rows), and evaluates both models
on the same stratified hold-out split plus 5-fold cross-validation. Saves the
models to ml/models/ and the results (all labelled "simulated data") to ml/results/.
"""

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
from training.features import FEATURES, to_frames, training_rows  # noqa: E402

SEED = 42
LABEL = "Simulated data"
TAG = "simulated_data"
METRICS = ["accuracy", "precision", "recall", "f1"]


def make_models() -> dict:
    return {
        "Logistic Regression": Pipeline([
            ("scale", StandardScaler()),
            ("model", LogisticRegression(max_iter=1000, random_state=SEED)),
        ]),
        "Random Forest": RandomForestClassifier(n_estimators=300, min_samples_leaf=5, random_state=SEED),
    }


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


def main() -> None:
    RESULTS_DIR.mkdir(exist_ok=True)
    MODELS_DIR.mkdir(exist_ok=True)

    rows = load_training_data()
    X, y = rows[FEATURES], rows["requires_attention"]
    print(f"{len(rows)} rows ({y.mean():.1%} require attention) from {rows['student_id'].nunique()} simulated students")

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, stratify=y, random_state=SEED)
    models = make_models()

    holdout, probabilities = [], {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        probabilities[name] = model.predict_proba(X_test)[:, 1]
        holdout.append({"model": name, **scores_for(y_test, model.predict(X_test))})
    # The system ranks topics by the average of both models' probabilities.
    average = (probabilities["Logistic Regression"] + probabilities["Random Forest"]) / 2
    holdout.append({"model": "Combined (average probability)", **scores_for(y_test, (average >= 0.5).astype(int))})
    holdout_df = pd.DataFrame(holdout)

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
    cv_rows = []
    for name, model in make_models().items():
        result = cross_validate(model, X, y, cv=cv, scoring=METRICS)
        cv_rows.append({
            "model": name,
            **{m: f"{result[f'test_{m}'].mean():.3f} ± {result[f'test_{m}'].std():.3f}" for m in METRICS},
        })
    cv_df = pd.DataFrame(cv_rows)

    # Tables
    holdout_rounded = holdout_df.round(3)
    holdout_rounded.to_csv(RESULTS_DIR / f"metrics_holdout_{TAG}.csv", index=False)
    cv_df.to_csv(RESULTS_DIR / f"metrics_cv5_{TAG}.csv", index=False)
    trained_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    (RESULTS_DIR / f"metrics_{TAG}.md").write_text(
        f"# Model comparison ({LABEL.lower()})\n\n"
        f"All figures come from simulated students created by `scripts/seed_demo.py`, not from real students.\n\n"
        f"- Rows: {len(rows)} student-topic pairs from {rows['student_id'].nunique()} simulated students\n"
        f"- Positive class (requires attention: next attempt below 50%): {y.mean():.1%}\n"
        f"- Features: {', '.join(FEATURES)}\n"
        f"- Trained: {trained_at}, model version {MODEL_VERSION}\n\n"
        f"## Hold-out test set (25%, stratified, same split for both models) — {LABEL.lower()}\n\n"
        f"{markdown_table(holdout_rounded)}\n\n"
        f"## 5-fold stratified cross-validation (mean ± std) — {LABEL.lower()}\n\n"
        f"{markdown_table(cv_df)}\n"
    )

    # Confusion matrices
    for name, model in models.items():
        fig, ax = plt.subplots(figsize=(5.2, 4.6))
        ConfusionMatrixDisplay.from_estimator(
            model, X_test, y_test, display_labels=["Adequately\nmastered", "Requires\nattention"], cmap="Blues", ax=ax, colorbar=False)
        ax.set_title(f"{name}: confusion matrix\n({LABEL.lower()})")
        fig.tight_layout()
        fig.savefig(RESULTS_DIR / f"confusion_{name.lower().replace(' ', '_')}_{TAG}.png", dpi=150)
        plt.close(fig)

    # Model comparison bar chart
    compare = holdout_df[holdout_df["model"] != "Combined (average probability)"]
    fig, ax = plt.subplots(figsize=(7, 4))
    width = 0.38
    xs = np.arange(len(METRICS))
    for i, (_, row) in enumerate(compare.iterrows()):
        bars = ax.bar(xs + (i - 0.5) * width, [row[m] for m in METRICS], width, label=row["model"])
        ax.bar_label(bars, fmt="%.2f", fontsize=8)
    ax.set_xticks(xs, [m.capitalize() if m != "f1" else "F1" for m in METRICS])
    ax.set_ylim(0, 1.05)
    ax.set_ylabel("Score on hold-out set")
    ax.set_title(f"Logistic Regression vs Random Forest ({LABEL.lower()})")
    ax.legend(loc="lower right")
    fig.tight_layout()
    fig.savefig(RESULTS_DIR / f"model_comparison_{TAG}.png", dpi=150)
    plt.close(fig)

    # Random Forest feature importances
    rf = models["Random Forest"]
    importances = pd.Series(rf.feature_importances_, index=FEATURES).sort_values()
    fig, ax = plt.subplots(figsize=(7.5, 3.8))
    ax.barh(importances.index, importances.values, color="#4f46e5")
    ax.set_xlabel("Importance")
    ax.set_title(f"Random Forest feature importances ({LABEL.lower()})")
    fig.tight_layout()
    fig.savefig(RESULTS_DIR / f"rf_feature_importances_{TAG}.png", dpi=150)
    plt.close(fig)

    # Models, versioned
    meta = {"version": MODEL_VERSION, "features": FEATURES, "trained_at": trained_at, "rows": len(rows)}
    joblib.dump({"model": models["Logistic Regression"], **meta}, LR_MODEL_PATH)
    joblib.dump({"model": models["Random Forest"], **meta}, RF_MODEL_PATH)

    print(f"\nHold-out test set ({LABEL.lower()}):")
    print(holdout_rounded.to_string(index=False))
    print(f"\n5-fold cross-validation ({LABEL.lower()}):")
    print(cv_df.to_string(index=False))
    print(f"\nSaved {LR_MODEL_PATH.name}, {RF_MODEL_PATH.name} and results in {RESULTS_DIR}")


if __name__ == "__main__":
    main()
