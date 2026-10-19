"""Tests for generate_reminders(), get_topic_progress() and notification privacy,
run against the linked Supabase project as real signed-in students.

    pytest scripts/test_reminders.py
"""

from datetime import datetime, timedelta, timezone

import pytest
from postgrest.exceptions import APIError

import testkit


@pytest.fixture(scope="module")
def db():
    return testkit.admin()


@pytest.fixture(scope="module")
def fx(db):
    fixture = testkit.setup(db)
    yield fixture
    testkit.cleanup(db)


@pytest.fixture
def student(db, fx, request):
    """(client, user id) for a fresh student; study days and time set so 'today' always counts."""
    user_id, email = testkit.create_student(db, f"Reminders {request.node.name[:36]}")
    db.table("profiles").update({
        "study_days": ["mon", "tue", "wed", "thu", "fri", "sat", "sun"],
        "preferred_study_time": "00:00",
        "daily_goal_minutes": 30,
    }).eq("id", user_id).execute()
    return testkit.sign_in(email), user_id


def kinds(client) -> list[str]:
    return sorted(n["kind"] for n in client.table("notifications").select("kind").execute().data)


def test_streak_at_risk_when_nothing_logged_today(student):
    client, _ = student
    unread = client.rpc("generate_reminders").execute().data
    assert "streak_at_risk" in kinds(client)
    assert unread == len(kinds(client))


def test_each_kind_fires_at_most_once_a_day(student):
    client, _ = student
    client.rpc("generate_reminders").execute()
    client.rpc("generate_reminders").execute()
    found = kinds(client)
    assert len(found) == len(set(found))


def test_daily_goal_reached_and_no_streak_warning_after_studying(student, fx):
    client, user_id = student
    client.table("study_logs").insert({"student_id": user_id, "topic_id": fx.topic_ids["alpha"],
                                       "duration_minutes": 40, "activity_type": "reading"}).execute()
    client.rpc("generate_reminders").execute()
    found = kinds(client)
    assert "daily_goal_reached" in found and "streak_at_risk" not in found
    body = client.table("notifications").select("body").eq("kind", "daily_goal_reached").execute().data[0]["body"]
    assert "40 minutes today (goal: 30)" in body


def test_inactive_for_three_days(db, student, fx):
    client, user_id = student
    long_ago = (datetime.now(timezone.utc) - timedelta(days=5)).isoformat()
    db.table("study_logs").insert({"student_id": user_id, "topic_id": fx.topic_ids["alpha"], "duration_minutes": 20,
                                   "activity_type": "video", "logged_at": long_ago}).execute()
    client.rpc("generate_reminders").execute()
    body = client.table("notifications").select("body").eq("kind", "inactive_3_days").execute().data[0]["body"]
    assert body.startswith("No quiz or study session in 5 days")


def test_score_improved_by_twenty_points_and_topic_progress(student, fx):
    client, _ = student
    first = client.rpc("start_quiz", {"p_quiz_id": fx.topic_quiz_id}).execute().data
    client.rpc("submit_quiz", {"p_attempt_id": first["attempt_id"], "p_responses": {}}).execute()
    second = client.rpc("start_quiz", {"p_quiz_id": fx.topic_quiz_id}).execute().data
    client.rpc("submit_quiz", {"p_attempt_id": second["attempt_id"],
                               "p_responses": {q["id"]: fx.correct[q["id"]] for q in second["questions"]}}).execute()

    progress = client.rpc("get_topic_progress").execute().data
    alpha = next(p for p in progress if p["topic_id"] == fx.topic_ids["alpha"])
    assert (float(alpha["previous_score"]), float(alpha["latest_score"])) == (0.0, 100.0)

    client.rpc("generate_reminders").execute()
    note = client.table("notifications").select("body, link").eq("kind", "score_improved").execute().data[0]
    assert note["body"] == "Alpha: 0% to 100%, up 100 points."
    assert note["link"] == f"/topics/{fx.topic_ids['alpha']}"


def test_notifications_are_private_and_only_read_at_can_change(db, student, fx):
    client, _ = student
    client.rpc("generate_reminders").execute()
    mine = client.table("notifications").select("id").execute().data
    assert mine

    _, other_email = testkit.create_student(db, "Reminders other")
    other = testkit.sign_in(other_email)
    assert other.table("notifications").select("id").in_("id", [n["id"] for n in mine]).execute().data == []
    assert other.table("notifications").update({"read_at": datetime.now(timezone.utc).isoformat()}).eq(
        "id", mine[0]["id"]).execute().data == []

    with pytest.raises(APIError):
        client.table("notifications").update({"title": "hacked"}).eq("id", mine[0]["id"]).execute()
    with pytest.raises(APIError):
        client.table("notifications").insert({"student_id": "00000000-0000-0000-0000-000000000000", "kind": "score_improved",
                                              "title": "x", "body": "x"}).execute()
    marked = client.table("notifications").update({"read_at": datetime.now(timezone.utc).isoformat()}).eq(
        "id", mine[0]["id"]).execute().data
    assert marked and marked[0]["read_at"]
