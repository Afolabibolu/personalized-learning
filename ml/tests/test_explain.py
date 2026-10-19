import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from app import data
from app.explain import COLD_START_REASON, keep_it_up_reason, reason_from_features, top_factors
from app.recommender import CourseData, Models, ResourceInfo, recommend_course
from training.features import FEATURES, NEVER_STUDIED_DAYS


def row(**values):
    base = {"mean_score": 50.0, "last_score": 40.0, "attempt_count": 2, "session_count": 1,
            "total_minutes": 20.0, "days_since_last_studied": 9.4}
    return pd.Series(base | values)


def test_reason_line_reads_like_the_spec():
    assert reason_from_features(row()) == "Last score 40%. Not studied for 9 days. 20 minutes studied in total."


def test_reason_line_handles_never_studied_and_no_attempts():
    text = reason_from_features(row(attempt_count=0, days_since_last_studied=NEVER_STUDIED_DAYS, total_minutes=0))
    assert text == "No quiz attempts on this topic yet. Not studied yet. 0 minutes studied in total."
    assert "Studied today." in reason_from_features(row(days_since_last_studied=0.2))
    assert "Not studied for 1 day." in reason_from_features(row(days_since_last_studied=1.5))


def test_keep_it_up_suggestions():
    assert "15-minute review" in keep_it_up_reason(row(days_since_last_studied=8), True)
    assert keep_it_up_reason(row(last_score=85, days_since_last_studied=2), True).startswith("Scoring 85%. Try the topic quiz")
    assert keep_it_up_reason(row(days_since_last_studied=NEVER_STUDIED_DAYS), True).startswith("Not studied yet.")
    assert keep_it_up_reason(row(last_score=60, days_since_last_studied=2), True).startswith("On track.")


def fitted_lr():
    rng = np.random.default_rng(0)
    X = pd.DataFrame(rng.uniform(0, 100, size=(200, len(FEATURES))), columns=FEATURES)
    y = (X["last_score"] < 50).astype(int)  # low last score -> requires attention
    return Pipeline([("scale", StandardScaler()), ("model", LogisticRegression())]).fit(X, y)


def test_top_factors_name_the_biggest_contributions_with_direction():
    factors = top_factors(fitted_lr(), row(last_score=5.0))
    assert len(factors) == 3
    assert factors[0]["feature"] == "last_score"
    assert factors[0]["direction"] == "raises risk" and factors[0]["label"] == "Last score"
    assert abs(factors[0]["contribution"]) >= abs(factors[1]["contribution"]) >= abs(factors[2]["contribution"])


def test_top_factors_empty_for_models_without_a_scaler():
    assert top_factors(object(), row()) == []


class Fixed:
    def __init__(self, p):
        self.p = p

    def predict_proba(self, X):
        return np.column_stack([1 - np.full(len(X), self.p), np.full(len(X), self.p)])


class Broken:
    def predict_proba(self, X):
        raise RuntimeError("model exploded")


COURSE = CourseData("c", ["t1"], [ResourceInfo("note", "t1", "Study note", True, 1, "note")], {"t1": "quiz-t1"})
FEATURES_T1 = pd.DataFrame([{"topic_id": "t1", **row().to_dict()}])


def test_ml_rows_carry_reason_and_both_probabilities():
    rec = recommend_course(COURSE, 10, FEATURES_T1, Models(Fixed(0.8), Fixed(0.9)), set())[0]
    assert rec.explanation["reason"].startswith("Last score 40%.")
    assert rec.explanation["probabilities"] == {"logistic_regression": 0.8, "random_forest": 0.9, "average": 0.85}


def test_low_probability_rows_get_a_keep_it_up_reason():
    rec = recommend_course(COURSE, 10, FEATURES_T1, Models(Fixed(0.1), Fixed(0.2)), set())[0]
    assert rec.explanation["reason"] == "Last studied 9 days ago. A 15-minute review keeps it fresh."


def test_cold_start_rows_explain_why_and_have_no_probabilities():
    rec = recommend_course(COURSE, 0, FEATURES_T1, None, set())[0]
    assert rec.explanation["reason"] == COLD_START_REASON and rec.explanation["probabilities"] is None


def test_a_failing_model_falls_back_to_cold_start_instead_of_an_error():
    recs = recommend_course(COURSE, 10, FEATURES_T1, Models(Broken(), Broken()), set())
    assert [r.source for r in recs] == ["cold_start"]


def test_corrupt_model_files_mean_cold_start(tmp_path, monkeypatch):
    bad = tmp_path / "lr.joblib"
    bad.write_text("not a model")
    monkeypatch.setattr(data, "LR_MODEL_PATH", bad)
    monkeypatch.setattr(data, "RF_MODEL_PATH", bad)
    data._models_cache.clear()
    assert data.load_models() is None


def test_supporting_factors_only_point_the_same_way_as_the_verdict():
    lr = fitted_lr()
    risky = top_factors(lr, row(last_score=5.0), supporting="raises risk")
    safe = top_factors(lr, row(last_score=95.0), supporting="lowers risk")
    assert risky and all(f["direction"] == "raises risk" for f in risky)
    assert safe and all(f["direction"] == "lowers risk" for f in safe)
