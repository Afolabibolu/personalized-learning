"""Feature building for the weak-topic models.

Inputs are two DataFrames:
  scores: student_id, topic_id, completed_at, score  (one row per completed attempt per topic,
          from the ml_attempt_topic_scores view; a diagnostic gives one row per topic it covered)
  logs:   student_id, topic_id, logged_at, duration_minutes

Every feature is computed only from rows strictly before the moment being
predicted, and the attempt that defines a label is never part of its features.
"""

import pandas as pd

from app.config import ATTENTION_THRESHOLD

FEATURES = [
    "mean_score",
    "last_score",
    "attempt_count",
    "session_count",
    "total_minutes",
    "days_since_last_studied",
]

# Used for days_since_last_studied when the student has never studied the topic.
NEVER_STUDIED_DAYS = 60.0
# Used for mean_score and last_score when the topic has no attempts yet.
NO_ATTEMPT_SCORE = 50.0


def features_at(scores: pd.DataFrame, logs: pd.DataFrame, moment: pd.Timestamp) -> dict:
    """Features for one student and one topic from the history before `moment`.

    `scores` and `logs` must already be filtered to that student and topic.
    """
    past = scores[scores["completed_at"] < moment].sort_values("completed_at")
    studied = logs[logs["logged_at"] < moment]

    if studied.empty:
        days_since = NEVER_STUDIED_DAYS
    else:
        days_since = (moment - studied["logged_at"].max()).total_seconds() / 86400
        days_since = min(days_since, NEVER_STUDIED_DAYS)

    return {
        "mean_score": float(past["score"].mean()) if len(past) else NO_ATTEMPT_SCORE,
        "last_score": float(past["score"].iloc[-1]) if len(past) else NO_ATTEMPT_SCORE,
        "attempt_count": int(len(past)),
        "session_count": int(len(studied)),
        "total_minutes": float(studied["duration_minutes"].sum()),
        "days_since_last_studied": float(days_since),
    }


def training_rows(scores: pd.DataFrame, logs: pd.DataFrame) -> pd.DataFrame:
    """One row per student per topic, for training.

    The label is the student's last attempt on the topic (below 50% means the
    topic requires attention). Features come from everything before that
    attempt. Student-topic pairs with a single attempt have no "next" attempt
    and are left out.
    """
    rows = []
    logs_by_key = {key: group for key, group in logs.groupby(["student_id", "topic_id"])}
    empty_logs = logs.iloc[0:0]
    for (student_id, topic_id), group in scores.groupby(["student_id", "topic_id"]):
        if len(group) < 2:
            continue
        group = group.sort_values("completed_at")
        label_attempt = group.iloc[-1]
        moment = label_attempt["completed_at"]
        feats = features_at(group.iloc[:-1], logs_by_key.get((student_id, topic_id), empty_logs), moment)
        rows.append({
            "student_id": student_id,
            "topic_id": topic_id,
            **feats,
            "label_score": float(label_attempt["score"]),
            "requires_attention": int(label_attempt["score"] < ATTENTION_THRESHOLD),
        })
    return pd.DataFrame(rows, columns=["student_id", "topic_id", *FEATURES, "label_score", "requires_attention"])


def prediction_rows(scores: pd.DataFrame, logs: pd.DataFrame, topic_ids: list[str], now: pd.Timestamp) -> pd.DataFrame:
    """One row per topic for a single student, describing them as of `now`."""
    rows = []
    for topic_id in topic_ids:
        feats = features_at(scores[scores["topic_id"] == topic_id], logs[logs["topic_id"] == topic_id], now)
        rows.append({"topic_id": topic_id, **feats})
    return pd.DataFrame(rows, columns=["topic_id", *FEATURES])


def to_frames(score_rows: list[dict], log_rows: list[dict]) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Builds typed DataFrames from rows as returned by Supabase."""
    scores = pd.DataFrame(score_rows, columns=["student_id", "topic_id", "attempt_id", "completed_at", "score"])
    scores["completed_at"] = pd.to_datetime(scores["completed_at"], utc=True, format="ISO8601")
    scores["score"] = scores["score"].astype(float)
    logs = pd.DataFrame(log_rows, columns=["student_id", "topic_id", "logged_at", "duration_minutes"])
    logs["logged_at"] = pd.to_datetime(logs["logged_at"], utc=True, format="ISO8601")
    logs["duration_minutes"] = logs["duration_minutes"].astype(float)
    return scores, logs
