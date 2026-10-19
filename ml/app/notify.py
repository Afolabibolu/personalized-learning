"""Notifications the ML service writes after each /recommend run (FR6).

Pure decision logic; app/data.py writes the rows. The database allows each
kind at most once a day per student.
"""

from app.recommender import Recommendation
from training.features import NEVER_STUDIED_DAYS

WEAK_TOPIC_PROBABILITY = 0.7
WEAK_TOPIC_UNSTUDIED_DAYS = 7


def top_ml_topic(recs: list[Recommendation]) -> str | None:
    ml = [r for r in recs if r.source == "ml"]
    return max(ml, key=lambda r: r.priority_score or 0).topic_id if ml else None


def decide(previous_top: str | None, recs: list[Recommendation], days_since_studied: dict[str, float],
           titles: dict[str, str]) -> list[dict]:
    """previous_top: the top ML topic before this run (None if there was none)."""
    notes = []
    top = top_ml_topic(recs)
    if top and top != previous_top:
        notes.append({
            "kind": "new_recommendations",
            "title": "New recommendations ready",
            "body": f"Your top topic to work on is now {titles.get(top, 'a new topic')}.",
            "link": "/",
        })

    weak = [
        r for r in recs
        if r.source == "ml" and (r.priority_score or 0) > WEAK_TOPIC_PROBABILITY
        and days_since_studied.get(r.topic_id, NEVER_STUDIED_DAYS) >= WEAK_TOPIC_UNSTUDIED_DAYS
    ]
    if weak:
        worst = max(weak, key=lambda r: r.priority_score or 0)
        days = days_since_studied.get(worst.topic_id, NEVER_STUDIED_DAYS)
        studied = "you haven't studied it yet" if days >= NEVER_STUDIED_DAYS else f"you last studied it {int(days)} days ago"
        notes.append({
            "kind": "weak_topic_unstudied",
            "title": f"{titles.get(worst.topic_id, 'A topic')} needs attention",
            "body": f"{round((worst.priority_score or 0) * 100)}% likely to need work, and {studied}.",
            "link": f"/topics/{worst.topic_id}",
        })
    return notes
