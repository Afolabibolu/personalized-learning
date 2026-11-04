"""Tests for the streak card (gamification_for, my_gamification, acknowledge_badges)
and the streak-at-risk reminder, run against the linked Supabase project.

gamification_for(student, p_now) takes the moment to compute at, so each test
fixes the clock in Nigerian time (Africa/Lagos) and inserts activity around it.

    pytest scripts/test_gamification.py
"""

from datetime import date, datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import pytest
from postgrest.exceptions import APIError

import testkit

LAGOS = ZoneInfo("Africa/Lagos")


def lagos(day: int, hour: int = 10, minute: int = 0, month: int = 10) -> datetime:
    return datetime(2026, month, day, hour, minute, tzinfo=LAGOS)


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
    user_id, email = testkit.create_student(db, f"Streak {request.node.name[:40]}")
    db.table("profiles").update({"daily_goal_minutes": 30}).eq("id", user_id).execute()
    return user_id, email


def log(db, fx, student_id: str, at: datetime, minutes: int = 20) -> None:
    db.table("study_logs").insert({"student_id": student_id, "topic_id": fx.topic_ids["alpha"],
                                   "duration_minutes": minutes, "activity_type": "reading",
                                   "logged_at": at.isoformat()}).execute()


def quiz(db, fx, student_id: str, at: datetime, correct: int, topic: str = "alpha", total: int = 4) -> None:
    """A completed topic quiz with `correct` of `total` right, all on one topic."""
    qids = [q for q in fx.correct if q in fx.topic_questions[topic]][:total]
    attempt = db.table("quiz_attempts").insert({
        "student_id": student_id, "quiz_id": fx.topic_quiz_id, "question_ids": qids,
        "score": round(100 * correct / len(qids), 2),
        "started_at": (at - timedelta(minutes=5)).isoformat(), "completed_at": at.isoformat(),
    }).execute().data[0]
    db.table("attempt_answers").insert([
        {"attempt_id": attempt["id"], "question_id": q, "response": fx.correct[q], "is_correct": i < correct}
        for i, q in enumerate(qids)]).execute()


def card(db, student_id: str, now: datetime) -> dict:
    return db.rpc("gamification_for", {"p_student": student_id, "p_now": now.isoformat()}).execute().data


def badges(c: dict) -> list[str]:
    return sorted(b["badge"] for b in c["badges"])


@pytest.fixture(scope="module", autouse=True)
def topic_questions(db, fx):
    """Question ids per topic, plus three one-question topics for the '5 topics mastered' badge."""
    fx.topic_questions = {}
    for q in db.table("questions").select("id, topic_id").in_("topic_id", list(fx.topic_ids.values())).execute().data:
        slug = next(s for s, t in fx.topic_ids.items() if t == q["topic_id"])
        fx.topic_questions.setdefault(slug, set()).add(q["id"])
    for order, slug in enumerate(("gamma", "delta", "epsilon"), start=3):
        topic = db.table("topics").insert({"course_id": fx.course_id, "slug": slug, "title": slug.title(),
                                           "sequence_order": order}).execute().data[0]
        fx.topic_ids[slug] = topic["id"]
        question = db.table("questions").insert({
            "topic_id": topic["id"], "format": "true_false", "stem": f"{slug} true/false", "options": testkit.TRUE_FALSE,
            "correct_answer": ["true"], "explanation": "Because.", "source": "test fixture", "status": "approved",
        }).execute().data[0]
        fx.correct[question["id"]] = ["true"]
        fx.topic_questions[slug] = {question["id"]}


# -- Part A: the streak rule ---------------------------------------------------------------

def test_five_day_run(db, fx, student):
    sid, _ = student
    for day in range(6, 11):
        log(db, fx, sid, lagos(day))
    c = card(db, sid, lagos(10, 18))
    assert (c["streak"], c["today_active"], c["at_risk"], c["longest_streak"]) == (5, True, False, 5)
    assert [d["active"] for d in c["strip"]][-5:] == [True] * 5 and len(c["strip"]) == 14


def test_a_missed_day_resets_the_streak(db, fx, student):
    sid, _ = student
    for day in (3, 4, 5, 7, 8):  # 6 Oct missed, and no freeze yet (a freeze needs a 7-day run)
        log(db, fx, sid, lagos(day))
    c = card(db, sid, lagos(8, 18))
    assert (c["streak"], c["longest_streak"], c["freezes"]) == (2, 3, 0)


def test_23_50_and_00_10_lagos_are_different_days(db, fx, student):
    sid, _ = student
    late, early = lagos(9, 23, 50), lagos(10, 0, 10)
    # Both fall on 9 Oct in UTC (22:50 and 23:10), so a UTC day boundary would count one day.
    assert late.astimezone(timezone.utc).date() == early.astimezone(timezone.utc).date() == date(2026, 10, 9)
    log(db, fx, sid, late)
    quiz(db, fx, sid, early, correct=2)
    c = card(db, sid, lagos(10, 12))
    assert c["streak"] == 2 and c["today"] == "2026-10-10"
    assert [(d["day"], d["active"]) for d in c["strip"][-2:]] == [("2026-10-09", True), ("2026-10-10", True)]


def test_no_activity_yet_today_keeps_yesterdays_run_at_risk(db, fx, student):
    sid, _ = student
    for day in (7, 8, 9):
        log(db, fx, sid, lagos(day))
    c = card(db, sid, lagos(10, 8))
    assert (c["streak"], c["today_active"], c["at_risk"]) == (3, False, True)
    assert c["strip"][-1] == {"day": "2026-10-10", "active": False, "frozen": False}


def test_no_activity_ever(db, student):
    sid, _ = student
    c = card(db, sid, lagos(10, 8))
    assert (c["streak"], c["at_risk"], c["xp_total"], c["badges"]) == (0, False, 0, [])
    assert len(c["strip"]) == 14


# -- Streak freezes ------------------------------------------------------------------------

def test_a_freeze_is_earned_at_seven_days_and_used_on_a_missed_day(db, fx, student):
    sid, _ = student
    for day in (*range(1, 8), 9):  # 1 to 7 Oct, 8 Oct missed, 9 Oct
        log(db, fx, sid, lagos(day))
    c = card(db, sid, lagos(9, 18))
    assert (c["streak"], c["freezes"], c["freezes_used_in_streak"]) == (8, 0, ["2026-10-08"])
    assert next(d for d in c["strip"] if d["day"] == "2026-10-08") == {"day": "2026-10-08", "active": False, "frozen": True}


def test_today_does_not_use_a_freeze(db, fx, student):
    sid, _ = student
    for day in range(1, 8):
        log(db, fx, sid, lagos(day))
    c = card(db, sid, lagos(8, 20))
    assert (c["streak"], c["at_risk"], c["freezes"], c["freezes_used_in_streak"], c["next_freeze_in"]) == (7, True, 1, [], 7)


def test_two_missed_days_with_one_freeze_reset_the_streak(db, fx, student):
    sid, _ = student
    for day in (*range(1, 8), 10):  # 8 and 9 Oct missed
        log(db, fx, sid, lagos(day))
    c = card(db, sid, lagos(10, 18))
    assert (c["streak"], c["freezes"], c["freezes_used_total"]) == (1, 0, 1)


def test_at_most_two_freezes(db, fx, student):
    sid, _ = student
    for day in range(1, 22):
        log(db, fx, sid, lagos(day))
    c = card(db, sid, lagos(21, 18))
    assert (c["streak"], c["freezes"], c["next_freeze_in"]) == (21, 2, None)


# -- XP and the daily goal -----------------------------------------------------------------

def test_xp_and_daily_goal(db, fx, student):
    sid, _ = student
    quiz(db, fx, sid, lagos(10, 9), correct=3)  # 10 + 3
    log(db, fx, sid, lagos(10, 11), minutes=32)  # 6, and the 30-minute goal is met: +10
    log(db, fx, sid, lagos(7, 11), minutes=10)  # 2, this week
    log(db, fx, sid, lagos(2, 11), minutes=50)  # 10 + 10 goal bonus, before this week
    c = card(db, sid, lagos(10, 18))
    assert (c["minutes_today"], c["daily_goal_minutes"], c["goal_met"]) == (32, 30, True)
    assert (c["xp_today"], c["xp_week"], c["xp_total"]) == (29, 31, 51)


def test_goal_bonus_only_once_a_day(db, fx, student):
    sid, _ = student
    log(db, fx, sid, lagos(10, 9), minutes=30)
    log(db, fx, sid, lagos(10, 15), minutes=30)
    c = card(db, sid, lagos(10, 18))
    assert c["xp_today"] == 6 + 6 + 10


# -- Badges --------------------------------------------------------------------------------

def test_badges(db, fx, student):
    sid, _ = student
    quiz(db, fx, sid, lagos(1, 9), correct=2)
    quiz(db, fx, sid, lagos(2, 9), correct=4)  # first 100%
    for day, topic in zip((3, 4, 5, 6), ("beta", "gamma", "delta", "epsilon")):
        quiz(db, fx, sid, lagos(day, 9), correct=4 if topic == "beta" else 1, topic=topic, total=4 if topic == "beta" else 1)
    c = card(db, sid, lagos(6, 18))
    earned = {b["badge"]: b["earned_at"] for b in c["badges"]}
    assert sorted(earned) == ["first_perfect", "first_quiz", "five_mastered", "streak_3"]
    assert earned["first_quiz"].startswith("2026-10-01T08:00")  # 09:00 Lagos
    assert earned["first_perfect"].startswith("2026-10-02T08:00")
    assert earned["streak_3"].startswith("2026-10-03T08:00")
    assert earned["five_mastered"].startswith("2026-10-06T08:00") and c["mastered_topics"] == 5


def test_streak_milestones(db, fx, student):
    sid, _ = student
    for day in range(1, 16):
        log(db, fx, sid, lagos(day))
    assert badges(card(db, sid, lagos(15, 18))) == ["streak_14", "streak_3", "streak_7"]


# -- Access rules --------------------------------------------------------------------------

def test_students_cannot_compute_or_write_badges_or_backdate_logs(db, fx, student):
    sid, email = student
    client = testkit.sign_in(email)
    with pytest.raises(APIError):
        client.rpc("gamification_for", {"p_student": sid}).execute()
    with pytest.raises(APIError):
        client.rpc("sync_student_badges", {"p_student": sid}).execute()
    with pytest.raises(APIError):
        client.table("student_badges").insert({"student_id": sid, "badge": "streak_100",
                                               "earned_at": datetime.now(timezone.utc).isoformat()}).execute()
    yesterday = (datetime.now(timezone.utc) - timedelta(days=1)).isoformat()
    with pytest.raises(APIError):
        client.table("study_logs").insert({"student_id": sid, "topic_id": fx.topic_ids["alpha"], "duration_minutes": 20,
                                           "activity_type": "reading", "logged_at": yesterday}).execute()
    # Without logged_at the database stamps it now.
    row = client.table("study_logs").insert({"student_id": sid, "topic_id": fx.topic_ids["alpha"], "duration_minutes": 20,
                                             "activity_type": "reading"}).execute().data[0]
    assert abs(datetime.fromisoformat(row["logged_at"]) - datetime.now(timezone.utc)) < timedelta(minutes=2)


def test_my_gamification_stores_badges_and_acknowledge_marks_them_seen(db, fx, student):
    sid, email = student
    client = testkit.sign_in(email)
    start = client.rpc("start_quiz", {"p_quiz_id": fx.topic_quiz_id}).execute().data
    client.rpc("submit_quiz", {"p_attempt_id": start["attempt_id"],
                               "p_responses": {q["id"]: fx.correct[q["id"]] for q in start["questions"]}}).execute()
    c = client.rpc("my_gamification").execute().data
    assert (c["streak"], c["today_active"]) == (1, True)
    assert {b["badge"]: b["seen"] for b in c["badges"]} == {"first_quiz": False, "first_perfect": False}
    assert len(client.table("student_badges").select("badge").execute().data) == 2

    client.rpc("acknowledge_badges", {"p_badges": ["first_quiz"]}).execute()
    c = client.rpc("my_gamification").execute().data
    assert {b["badge"]: b["seen"] for b in c["badges"]} == {"first_quiz": True, "first_perfect": False}

    # Another student sees none of them.
    _, other_email = testkit.create_student(db, "Streak other student")
    assert testkit.sign_in(other_email).table("student_badges").select("badge").execute().data == []


# -- Streak-at-risk reminder ---------------------------------------------------------------

def every_day(db, sid: str) -> None:
    db.table("profiles").update({"study_days": ["mon", "tue", "wed", "thu", "fri", "sat", "sun"],
                                 "preferred_study_time": "00:00"}).eq("id", sid).execute()


def test_streak_at_risk_reminder_names_the_streak(db, fx, student):
    sid, email = student
    every_day(db, sid)
    today = datetime.now(LAGOS).replace(hour=12, minute=0, second=0, microsecond=0)
    for days_back in (1, 2):
        log(db, fx, sid, today - timedelta(days=days_back))
    client = testkit.sign_in(email)
    client.rpc("generate_reminders").execute()
    note = client.table("notifications").select("title, body").eq("kind", "streak_at_risk").execute().data
    assert note == [{"title": "Keep your streak going", "body": "Do a quiz or log study today to keep your 2-day streak."}]


def test_a_quiz_today_means_no_streak_at_risk_reminder(db, fx, student):
    sid, email = student
    every_day(db, sid)
    client = testkit.sign_in(email)
    start = client.rpc("start_quiz", {"p_quiz_id": fx.topic_quiz_id}).execute().data
    client.rpc("submit_quiz", {"p_attempt_id": start["attempt_id"], "p_responses": {}}).execute()
    client.rpc("generate_reminders").execute()
    assert client.table("notifications").select("kind").eq("kind", "streak_at_risk").execute().data == []
