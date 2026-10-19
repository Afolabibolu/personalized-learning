from app.notify import decide
from app.recommender import Recommendation


def rec(topic, p, source="ml"):
    return Recommendation(topic_id=topic, rank=1, source=source, resource_id=topic, priority_score=p)


TITLES = {"fuzzy": "Fuzzy Logic Systems", "search": "Problem Solving and Search"}


def test_new_recommendations_only_when_the_top_topic_changes():
    recs = [rec("fuzzy", 0.9), rec("search", 0.2)]
    assert [n["kind"] for n in decide("search", recs, {"fuzzy": 1, "search": 1}, TITLES)] == ["new_recommendations"]
    assert decide("fuzzy", recs, {"fuzzy": 1, "search": 1}, TITLES) == []
    assert "Fuzzy Logic Systems" in decide(None, recs, {"fuzzy": 1}, TITLES)[0]["body"]


def test_weak_topic_unstudied_above_point_seven_and_a_week_idle():
    recs = [rec("fuzzy", 0.89)]
    notes = decide("fuzzy", recs, {"fuzzy": 60.0}, TITLES)
    assert [n["kind"] for n in notes] == ["weak_topic_unstudied"]
    assert notes[0]["title"] == "Fuzzy Logic Systems needs attention"
    assert notes[0]["body"] == "89% likely to need work, and you haven't studied it yet."
    assert decide("fuzzy", recs, {"fuzzy": 3.0}, TITLES) == []
    assert decide("fuzzy", [rec("fuzzy", 0.65)], {"fuzzy": 60.0}, TITLES) == []


def test_cold_start_runs_send_nothing():
    assert decide(None, [rec("intro", None, source="cold_start")], {}, TITLES) == []
