"""Decides a student's recommendations for one course.

Pure functions only: the data comes in as plain values, so the cold-start
branch and the ranking can be tested without a database.
"""

import logging
from dataclasses import dataclass, field
from typing import Protocol

import pandas as pd

from app.config import ATTENTION_PROBABILITY, COLD_START_THRESHOLD, MODEL_VERSION, TOP_TOPICS
from app.explain import cold_start_explanation, ml_explanation
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
    type: str = "lecture"  # note, past_questions, lecture or video


# For a weak topic, which kind of resource to recommend first.
RESOURCE_PREFERENCE = ["note", "past_questions", "lecture", "video"]


def resource_rank(resource: ResourceInfo, preferred: tuple[str, ...] = ()) -> tuple:
    """The student's preferred types first (FR1), then note, past questions, lecture, video."""
    kind = RESOURCE_PREFERENCE.index(resource.type) if resource.type in RESOURCE_PREFERENCE else len(RESOURCE_PREFERENCE)
    return (resource.type not in preferred, kind, not resource.is_introductory, resource.title)


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
    explanation: dict = field(default_factory=dict)


def is_cold_start(completed_attempts: int, models: Models | None) -> bool:
    return models is None or completed_attempts < COLD_START_THRESHOLD


def cold_start(course: CourseData, used_resource_ids: set[str]) -> list[Recommendation]:
    """The course's introductory resources, in order."""
    intro = sorted(
        (r for r in course.resources if r.is_introductory and r.id not in used_resource_ids),
        key=lambda r: (r.intro_order is None, r.intro_order),
    )
    return [
        Recommendation(topic_id=r.topic_id, rank=i, source="cold_start", resource_id=r.id,
                       explanation=cold_start_explanation())
        for i, r in enumerate(intro, start=1)
    ]


def model_probabilities(models: Models, features: pd.DataFrame) -> pd.DataFrame:
    """Each model's probability that each topic requires attention, and their average."""
    X = features[FEATURES]
    lr = models.lr.predict_proba(X)[:, 1]
    rf = models.rf.predict_proba(X)[:, 1]
    return pd.DataFrame({"lr": lr, "rf": rf, "average": (lr + rf) / 2}, index=features["topic_id"].values)


def attention_probabilities(models: Models, features: pd.DataFrame) -> pd.Series:
    """Average of both models' probability that each topic requires attention."""
    return model_probabilities(models, features)["average"]


def ml_recommendations(
    course: CourseData,
    features: pd.DataFrame,
    models: Models,
    used_resource_ids: set[str],
    top_n: int | None = TOP_TOPICS,
    preferred: tuple[str, ...] = (),
) -> list[Recommendation]:
    """Ranks the course's topics by averaged probability and recommends the top ones
    (every topic when top_n is None).

    For each of the top topics: its first resource the student has not already
    accepted or dismissed (the student's preferred types first, then study note,
    past questions, lecture, video), or the topic quiz when none is left.
    """
    probabilities = model_probabilities(models, features)
    rows = features.set_index("topic_id")
    order = {topic_id: i for i, topic_id in enumerate(course.topic_ids)}
    # Highest probability first; teaching order breaks ties.
    ranked = sorted(probabilities["average"].items(), key=lambda item: (-item[1], order.get(item[0], 0)))

    recs = []
    for rank, (topic_id, probability) in enumerate(ranked if top_n is None else ranked[:top_n], start=1):
        unused = sorted(
            (r for r in course.resources if r.topic_id == topic_id and r.id not in used_resource_ids),
            key=lambda r: resource_rank(r, preferred),
        )
        explanation = ml_explanation(
            rows.loc[topic_id], probabilities.loc[topic_id, "lr"], probabilities.loc[topic_id, "rf"], models.lr,
            needs_attention=probability >= ATTENTION_PROBABILITY,
            has_topic_quiz=topic_id in course.topic_quiz_ids,
        )
        if unused and unused[0].type in preferred:
            explanation["matched_preference"] = unused[0].type
        recs.append(Recommendation(
            topic_id=topic_id,
            rank=rank,
            source="ml",
            resource_id=unused[0].id if unused else None,
            quiz_id=None if unused else course.topic_quiz_ids.get(topic_id),
            priority_score=round(float(probability), 4),
            model_version=models.version,
            explanation=explanation,
        ))
    return recs


def recommend_course(
    course: CourseData,
    completed_attempts: int,
    features: pd.DataFrame,
    models: Models | None,
    used_resource_ids: set[str],
    preferred: tuple[str, ...] = (),
) -> list[Recommendation]:
    """Cold-start list, or every topic of the course ranked by the models.
    Use top_overall() to keep only the best ML topics across courses."""
    if is_cold_start(completed_attempts, models):
        return cold_start(course, used_resource_ids)
    try:
        return ml_recommendations(course, features, models, used_resource_ids, top_n=None, preferred=preferred)
    except Exception:  # never fail a student who exists: fall back to the introductory list (NFR4)
        logging.getLogger(__name__).warning("ML ranking failed for course %s; using cold start", course.course_id, exc_info=True)
        return cold_start(course, used_resource_ids)


def top_overall(recs: list[Recommendation], n: int = TOP_TOPICS) -> list[Recommendation]:
    """Keeps the n highest-probability ML recommendations across all courses,
    re-ranked 1..n. Cold-start lists stay as they are (one per course)."""
    cold = [r for r in recs if r.source == "cold_start"]
    ml = sorted((r for r in recs if r.source == "ml"), key=lambda r: -(r.priority_score or 0))[:n]
    for rank, rec in enumerate(ml, start=1):
        rec.rank = rank
    return cold + ml
