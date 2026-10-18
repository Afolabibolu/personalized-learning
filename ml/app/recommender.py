"""Decides a student's recommendations for one course.

Pure functions only: the data comes in as plain values, so the cold-start
branch and the ranking can be tested without a database.
"""

from dataclasses import dataclass
from typing import Protocol

import pandas as pd

from app.config import COLD_START_THRESHOLD, MODEL_VERSION, TOP_TOPICS
from training.features import FEATURES


class Classifier(Protocol):
    def predict_proba(self, X: pd.DataFrame): ...


@dataclass
class Models:
    lr: Classifier
    rf: Classifier
    version: str = MODEL_VERSION


@dataclass
class ResourceInfo:
    id: str
    topic_id: str
    title: str
    is_introductory: bool
    intro_order: int | None


@dataclass
class CourseData:
    course_id: str
    topic_ids: list[str]  # in teaching order
    resources: list[ResourceInfo]
    topic_quiz_ids: dict[str, str]  # topic_id -> quiz_id


@dataclass
class Recommendation:
    topic_id: str
    rank: int
    source: str  # "ml" or "cold_start"
    resource_id: str | None = None
    quiz_id: str | None = None
    priority_score: float | None = None
    model_version: str | None = None


def is_cold_start(completed_attempts: int, models: Models | None) -> bool:
    return models is None or completed_attempts < COLD_START_THRESHOLD


def cold_start(course: CourseData, used_resource_ids: set[str]) -> list[Recommendation]:
    """The course's introductory resources, in order."""
    intro = sorted(
        (r for r in course.resources if r.is_introductory and r.id not in used_resource_ids),
        key=lambda r: (r.intro_order is None, r.intro_order),
    )
    return [
        Recommendation(topic_id=r.topic_id, rank=i, source="cold_start", resource_id=r.id)
        for i, r in enumerate(intro, start=1)
    ]


def attention_probabilities(models: Models, features: pd.DataFrame) -> pd.Series:
    """Average of both models' probability that each topic requires attention."""
    X = features[FEATURES]
    lr = models.lr.predict_proba(X)[:, 1]
    rf = models.rf.predict_proba(X)[:, 1]
    return pd.Series((lr + rf) / 2, index=features["topic_id"].values)


def ml_recommendations(
    course: CourseData,
    features: pd.DataFrame,
    models: Models,
    used_resource_ids: set[str],
    top_n: int = TOP_TOPICS,
) -> list[Recommendation]:
    """Ranks the course's topics by averaged probability and recommends the top ones.

    For each of the top topics: its first resource the student has not already
    accepted or dismissed, or the topic quiz when none is left.
    """
    probabilities = attention_probabilities(models, features)
    order = {topic_id: i for i, topic_id in enumerate(course.topic_ids)}
    # Highest probability first; teaching order breaks ties.
    ranked = sorted(probabilities.items(), key=lambda item: (-item[1], order.get(item[0], 0)))

    recs = []
    for rank, (topic_id, probability) in enumerate(ranked[:top_n], start=1):
        unused = sorted(
            (r for r in course.resources if r.topic_id == topic_id and r.id not in used_resource_ids),
            key=lambda r: (not r.is_introductory, r.title),
        )
        recs.append(Recommendation(
            topic_id=topic_id,
            rank=rank,
            source="ml",
            resource_id=unused[0].id if unused else None,
            quiz_id=None if unused else course.topic_quiz_ids.get(topic_id),
            priority_score=round(float(probability), 4),
            model_version=models.version,
        ))
    return recs


def recommend_course(
    course: CourseData,
    completed_attempts: int,
    features: pd.DataFrame,
    models: Models | None,
    used_resource_ids: set[str],
) -> list[Recommendation]:
    if is_cold_start(completed_attempts, models):
        return cold_start(course, used_resource_ids)
    return ml_recommendations(course, features, models, used_resource_ids)
