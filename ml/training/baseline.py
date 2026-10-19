"""The rule baseline: "requires attention if the last score on the topic was below 50%".

Wrapped as a scikit-learn classifier so it is scored on exactly the same test
rows and cross-validation folds as the two models. It learns nothing in fit().
"""

import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin

from app.config import ATTENTION_THRESHOLD


class LastScoreRule(ClassifierMixin, BaseEstimator):
    def fit(self, X, y=None):
        self.classes_ = np.array([0, 1])
        return self

    def predict(self, X):
        return (np.asarray(X["last_score"], dtype=float) < ATTENTION_THRESHOLD).astype(int)

    def predict_proba(self, X):
        p = self.predict(X).astype(float)
        return np.column_stack([1 - p, p])
