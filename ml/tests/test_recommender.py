import numpy as np
import pandas as pd

from app.config import COLD_START_THRESHOLD
from app.recommender import CourseData, Models, Recommendation, ResourceInfo, recommend_course, top_overall
from training.features import FEATURES


class FixedProbabilities:
    """Stands in for a fitted classifier: returns a set probability per topic row."""

    def __init__(self, by_last_score: dict[float, float]):
        self.by_last_score = by_last_score

    def predict_proba(self, X: pd.DataFrame):
        p = np.array([self.by_last_score[s] for s in X["last_score"]])
        return np.column_stack([1 - p, p])


def course():
    resources = [
        ResourceInfo("intro-2", "t2", "Second intro", True, 2),
        ResourceInfo("intro-1", "t1", "Lecture 1", True, 1),
        ResourceInfo("t2-notes", "t2", "Topic 2 notes", False, None),
        ResourceInfo("t3-notes", "t3", "Topic 3 notes", False, None),
        ResourceInfo("t4-notes", "t4", "Topic 4 notes", False, None),
    ]
    return CourseData("c", ["t1", "t2", "t3", "t4"], resources, {f"t{i}": f"quiz-t{i}" for i in range(1, 5)})


def features(last_scores: dict[str, float]):
    rows = [{"topic_id": t, **{f: 0.0 for f in FEATURES}, "last_score": s} for t, s in last_scores.items()]
    return pd.DataFrame(rows, columns=["topic_id", *FEATURES])


# Each topic gets a distinct last_score, which the stub maps to a probability.
LAST = {"t1": 1.0, "t2": 2.0, "t3": 3.0, "t4": 4.0}


def models(lr: dict, rf: dict):
    return Models(lr=FixedProbabilities(lr), rf=FixedProbabilities(rf), version="test")


def test_below_threshold_gets_introductory_resources_in_order():
    m = models({1.0: 0.9, 2.0: 0.1, 3.0: 0.1, 4.0: 0.1}, {1.0: 0.9, 2.0: 0.1, 3.0: 0.1, 4.0: 0.1})
    recs = recommend_course(course(), COLD_START_THRESHOLD - 1, features(LAST), m, set())
    assert [(r.resource_id, r.rank, r.source) for r in recs] == [("intro-1", 1, "cold_start"), ("intro-2", 2, "cold_start")]
    assert all(r.model_version is None and r.priority_score is None for r in recs)


def test_missing_model_files_means_cold_start_even_with_history():
    recs = recommend_course(course(), 50, features(LAST), None, set())
    assert {r.source for r in recs} == {"cold_start"}


def test_at_threshold_ranks_topics_by_averaged_probability():
    # LR alone would put t1 first; the average puts t3 first.
    m = models({1.0: 0.9, 2.0: 0.2, 3.0: 0.7, 4.0: 0.1}, {1.0: 0.1, 2.0: 0.3, 3.0: 0.9, 4.0: 0.2})
    recs = recommend_course(course(), COLD_START_THRESHOLD, features(LAST), m, set())
    assert [r.topic_id for r in recs] == ["t3", "t1", "t2", "t4"]
    recs = top_overall(recs)
    assert [r.topic_id for r in recs] == ["t3", "t1", "t2"]
    assert [r.rank for r in recs] == [1, 2, 3]
    assert recs[0].priority_score == 0.8
    assert {r.source for r in recs} == {"ml"} and {r.model_version for r in recs} == {"test"}


def test_used_resources_are_skipped_and_topic_quiz_is_the_fallback():
    m = models({1.0: 0.9, 2.0: 0.8, 3.0: 0.1, 4.0: 0.1}, {1.0: 0.9, 2.0: 0.8, 3.0: 0.1, 4.0: 0.1})
    recs = recommend_course(course(), 10, features(LAST), m, used_resource_ids={"intro-1", "intro-2"})
    by_topic = {r.topic_id: r for r in recs}
    assert by_topic["t1"].resource_id is None and by_topic["t1"].quiz_id == "quiz-t1"
    assert by_topic["t2"].resource_id == "t2-notes"


def test_introductory_resource_is_preferred_within_a_weak_topic():
    m = models({1.0: 0.1, 2.0: 0.9, 3.0: 0.1, 4.0: 0.1}, {1.0: 0.1, 2.0: 0.9, 3.0: 0.1, 4.0: 0.1})
    recs = recommend_course(course(), 10, features(LAST), m, set())
    assert recs[0].topic_id == "t2" and recs[0].resource_id == "intro-2"


def test_cold_start_skips_resources_already_accepted_or_dismissed():
    recs = recommend_course(course(), 0, features(LAST), None, {"intro-1"})
    assert [r.resource_id for r in recs] == ["intro-2"]
    assert recs[0].rank == 1


def test_top_three_are_chosen_across_courses_and_cold_start_lists_are_kept():
    def ml(topic, p):
        return Recommendation(topic_id=topic, rank=9, source="ml", resource_id=topic, priority_score=p, model_version="v")

    candidates = [
        ml("a1", 0.20), ml("a2", 0.90), ml("a3", 0.10),  # course A
        ml("b1", 0.85), ml("b2", 0.40),  # course B
        Recommendation(topic_id="c1", rank=1, source="cold_start", resource_id="intro"),  # course C, new
    ]
    recs = top_overall(candidates)
    assert [(r.topic_id, r.rank) for r in recs if r.source == "ml"] == [("a2", 1), ("b1", 2), ("b2", 3)]
    assert [(r.topic_id, r.rank) for r in recs if r.source == "cold_start"] == [("c1", 1)]
