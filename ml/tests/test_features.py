import pandas as pd
import pytest

from training.features import FEATURES, NEVER_STUDIED_DAYS, NO_ATTEMPT_SCORE, prediction_rows, training_rows

T0 = pd.Timestamp("2026-09-01T10:00:00Z")


def day(n: float) -> pd.Timestamp:
    return T0 + pd.Timedelta(days=n)


def frames(scores, logs=()):
    s = pd.DataFrame(scores, columns=["student_id", "topic_id", "completed_at", "score"])
    l = pd.DataFrame(list(logs), columns=["student_id", "topic_id", "logged_at", "duration_minutes"])
    return s, l


def test_label_attempt_is_not_part_of_its_features():
    scores, logs = frames([("s", "t", day(0), 80.0), ("s", "t", day(5), 60.0), ("s", "t", day(9), 20.0)])
    row = training_rows(scores, logs).iloc[0]
    assert row["attempt_count"] == 2
    assert row["mean_score"] == 70.0
    assert row["last_score"] == 60.0
    assert row["label_score"] == 20.0
    assert row["requires_attention"] == 1


def test_label_rule_is_below_fifty_percent():
    at_fifty, _ = frames([("s", "t", day(0), 10.0), ("s", "t", day(1), 50.0)])
    below, _ = frames([("s", "t", day(0), 90.0), ("s", "t", day(1), 49.9)])
    assert training_rows(at_fifty, frames([])[1]).iloc[0]["requires_attention"] == 0
    assert training_rows(below, frames([])[1]).iloc[0]["requires_attention"] == 1


def test_pairs_with_no_next_attempt_are_left_out():
    scores, logs = frames([("s", "only-one", day(0), 30.0), ("s", "two", day(0), 30.0), ("s", "two", day(3), 70.0)])
    rows = training_rows(scores, logs)
    assert list(rows["topic_id"]) == ["two"]


def test_study_logs_after_the_predicted_moment_are_ignored():
    scores, logs = frames(
        [("s", "t", day(0), 40.0), ("s", "t", day(10), 90.0)],
        [("s", "t", day(4), 30.0), ("s", "t", day(8), 60.0), ("s", "t", day(11), 120.0)],
    )
    row = training_rows(scores, logs).iloc[0]
    assert row["session_count"] == 2
    assert row["total_minutes"] == 90.0
    assert row["days_since_last_studied"] == pytest.approx(2.0)


def test_other_students_and_topics_do_not_leak_in():
    scores, logs = frames(
        [("a", "t", day(0), 40.0), ("a", "t", day(10), 90.0), ("b", "t", day(1), 100.0), ("b", "t", day(2), 0.0)],
        [("b", "t", day(5), 60.0), ("a", "other", day(5), 60.0)],
    )
    row = training_rows(scores, logs).set_index("student_id").loc["a"]
    assert row["mean_score"] == 40.0
    assert row["session_count"] == 0
    assert row["days_since_last_studied"] == NEVER_STUDIED_DAYS


def test_prediction_rows_cover_every_topic_with_neutral_defaults():
    scores, logs = frames([("s", "t1", day(0), 20.0)], [("s", "t1", day(1), 45.0)])
    rows = prediction_rows(scores, logs, ["t1", "t2"], day(3)).set_index("topic_id")
    assert list(rows.columns) == FEATURES
    assert rows.loc["t1", "last_score"] == 20.0
    assert rows.loc["t1", "days_since_last_studied"] == pytest.approx(2.0)
    assert rows.loc["t2", "attempt_count"] == 0
    assert rows.loc["t2", "mean_score"] == NO_ATTEMPT_SCORE
    assert rows.loc["t2", "days_since_last_studied"] == NEVER_STUDIED_DAYS
