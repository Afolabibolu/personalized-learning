"""Why a recommendation was made: the `explanation` stored on each row.

The frontend only displays these; it never computes reasons itself.
"""

import numpy as np
import pandas as pd

from training.features import FEATURES, NEVER_STUDIED_DAYS

COLD_START_REASON = "Not enough quiz history yet for this course."

FEATURE_LABELS = {
    "mean_score": "Average score",
    "last_score": "Last score",
    "attempt_count": "Quiz attempts",
    "session_count": "Study sessions",
    "total_minutes": "Minutes studied",
    "days_since_last_studied": "Days since last studied",
}


def _studied_phrase(days: float) -> str:
    if days >= NEVER_STUDIED_DAYS:
        return "Not studied yet."
    whole = int(days)
    if whole == 0:
        return "Studied today."
    return f"Not studied for {whole} day{'s' if whole != 1 else ''}."


def reason_from_features(row: pd.Series) -> str:
    """For example: "Last score 40%. Not studied for 9 days. 20 minutes studied in total." """
    parts = []
    if row["attempt_count"] > 0:
        parts.append(f"Last score {round(row['last_score'])}%.")
    else:
        parts.append("No quiz attempts on this topic yet.")
    parts.append(_studied_phrase(row["days_since_last_studied"]))
    minutes = int(row["total_minutes"])
    parts.append(f"{minutes} minute{'s' if minutes != 1 else ''} studied in total.")
    return " ".join(parts)


def keep_it_up_reason(row: pd.Series, has_topic_quiz: bool) -> str:
    """A concrete next step for a topic the models consider on track."""
    days = row["days_since_last_studied"]
    if days >= NEVER_STUDIED_DAYS:
        return "Not studied yet. A quick read of this resource will lock in what you already know."
    if days >= 7:
        return f"Last studied {int(days)} days ago. A 15-minute review keeps it fresh."
    if row["attempt_count"] > 0 and row["last_score"] >= 80 and has_topic_quiz:
        return f"Scoring {round(row['last_score'])}%. Try the topic quiz: questions you haven't seen come first."
    return "On track. One practice session this week keeps it that way."


def top_factors(lr_model, row: pd.Series, limit: int = 3, supporting: str | None = None) -> list[dict]:
    """The features that moved the Logistic Regression prediction most.

    Contribution = coefficient x standardised feature value. With supporting=
    "raises risk" (or "lowers risk") only factors pushing in that direction are
    kept, i.e. the reasons behind the verdict shown. Works for the
    StandardScaler + LogisticRegression pipeline from training; returns [] for
    anything else.
    """
    steps = getattr(lr_model, "named_steps", None)
    if not steps or "scale" not in steps or "model" not in steps:
        return []
    X = pd.DataFrame([row[FEATURES].astype(float)], columns=FEATURES)
    scaled = steps["scale"].transform(X)[0]
    contributions = scaled * steps["model"].coef_[0]
    order = np.argsort(-np.abs(contributions))
    if supporting:
        wanted = 1 if supporting == "raises risk" else -1
        order = [i for i in order if np.sign(contributions[i]) == wanted]
    order = order[:limit]
    return [
        {
            "feature": FEATURES[i],
            "label": FEATURE_LABELS[FEATURES[i]],
            "value": round(float(row[FEATURES[i]]), 1),
            "direction": "raises risk" if contributions[i] > 0 else "lowers risk",
            "contribution": round(float(contributions[i]), 3),
        }
        for i in order
    ]


def ml_explanation(row: pd.Series, lr_probability: float, rf_probability: float, lr_model,
                   needs_attention: bool, has_topic_quiz: bool) -> dict:
    return {
        "reason": reason_from_features(row) if needs_attention else keep_it_up_reason(row, has_topic_quiz),
        "probabilities": {
            "logistic_regression": round(float(lr_probability), 3),
            "random_forest": round(float(rf_probability), 3),
            "average": round(float((lr_probability + rf_probability) / 2), 3),
        },
        "top_factors": top_factors(lr_model, row, supporting="raises risk" if needs_attention else "lowers risk"),
        "matched_preference": None,
    }


def cold_start_explanation() -> dict:
    return {"reason": COLD_START_REASON, "probabilities": None, "top_factors": [], "matched_preference": None}
