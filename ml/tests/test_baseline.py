import pandas as pd

from training.baseline import LastScoreRule
from training.features import FEATURES


def test_rule_flags_only_last_scores_below_fifty():
    X = pd.DataFrame([{f: 0.0 for f in FEATURES} | {"last_score": s} for s in [0.0, 49.9, 50.0, 80.0]])
    rule = LastScoreRule().fit(X, None)
    assert list(rule.predict(X)) == [1, 1, 0, 0]
    assert rule.predict_proba(X)[:, 1].tolist() == [1.0, 1.0, 0.0, 0.0]


def test_rule_ignores_every_other_feature():
    base = {f: 0.0 for f in FEATURES} | {"last_score": 40.0}
    changed = base | {"mean_score": 100.0, "total_minutes": 900.0, "days_since_last_studied": 0.0}
    rule = LastScoreRule().fit(None)
    assert list(rule.predict(pd.DataFrame([base, changed]))) == [1, 1]
