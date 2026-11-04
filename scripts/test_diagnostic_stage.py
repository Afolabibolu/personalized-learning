"""Tests for the three recommendation stages in the database, run against the
linked Supabase project as a real signed-in student:

    pytest scripts/test_diagnostic_stage.py

Stage 1 (no diagnostic) gives the introductory list; Stage 2 (diagnostic taken,
below the threshold) gives the weakest diagnostic topics, without the ML service;
Stage 3 (at the threshold) is left to the ML service.
"""

import pytest
from postgrest.exceptions import APIError

import testkit


@pytest.fixture(scope="module")
def db():
    return testkit.admin()


@pytest.fixture(scope="module")
def fx(db):
    fixture = testkit.setup(db)
    # Beta needs something to recommend; alpha already has its introductory notes.
    db.table("resources").insert({"topic_id": fixture.topic_ids["beta"], "title": "Beta notes", "type": "note",
                                  "body": "Beta.", "is_introductory": False}).execute()
    yield fixture
    testkit.cleanup(db)


@pytest.fixture
def student(db, fx, request):
    user_id, email = testkit.create_student(db, f"Stage {request.node.name[:40]}")
    # Only the test course: new profiles are also enrolled in the reviewed courses.
    db.table("enrollments").delete().eq("student_id", user_id).execute()
    db.table("enrollments").insert({"student_id": user_id, "course_id": fx.course_id}).execute()
    return user_id, testkit.sign_in(email)


def pending(db, user_id, course_topics):
    rows = db.table("recommendations").select("topic_id, rank, source, resource_id, quiz_id, explanation").eq(
        "student_id", user_id).eq("status", "pending").order("rank").execute().data
    return [r for r in rows if r["topic_id"] in course_topics]


def take_diagnostic(client, fx, right_topics):
    started = client.rpc("start_quiz", {"p_quiz_id": fx.diagnostic_quiz_id}).execute().data
    responses = {
        q["id"]: fx.correct[q["id"]] if q["topic_id"] in right_topics else ["zzz"]
        for q in started["questions"]
    }
    client.rpc("submit_quiz", {"p_attempt_id": started["attempt_id"], "p_responses": responses}).execute()
    return started["questions"]


def test_threshold_is_one_readable_setting(db, student):
    _, client = student
    assert client.rpc("cold_start_threshold").execute().data == 3
    rows = client.table("app_settings").select("key, value").execute().data
    assert {"key": "cold_start_threshold", "value": 3} in rows
    with pytest.raises(APIError):
        client.table("app_settings").update({"value": 1}).eq("key", "cold_start_threshold").execute()
    assert db.rpc("cold_start_threshold").execute().data == 3


def test_stage_1_without_a_diagnostic_gets_the_introductory_list(db, fx, student):
    user_id, client = student
    client.rpc("refresh_fallback_recommendations").execute()
    rows = pending(db, user_id, set(fx.topic_ids.values()))
    assert [(r["source"], r["resource_id"]) for r in rows] == [("cold_start", fx.resource_id)]


def test_stage_2_ranks_the_weakest_diagnostic_topic_and_skips_fully_right_ones(db, fx, student):
    user_id, client = student
    questions = take_diagnostic(client, fx, right_topics={fx.topic_ids["alpha"]})
    beta_count = sum(q["topic_id"] == fx.topic_ids["beta"] for q in questions)

    written = client.rpc("refresh_fallback_recommendations").execute().data
    rows = pending(db, user_id, set(fx.topic_ids.values()))
    assert written == 1
    assert [(r["topic_id"], r["rank"], r["source"]) for r in rows] == [(fx.topic_ids["beta"], 1, "diagnostic")]
    explanation = rows[0]["explanation"]
    assert explanation["reason"] == f"You got 0 of {beta_count} right on this topic in the diagnostic."
    assert explanation["probabilities"] is None
    assert explanation["threshold"] == 3 and explanation["completed_quizzes"] == 1


def test_stage_2_shows_fully_right_topics_when_nothing_else_is_left(db, fx, student):
    user_id, client = student
    take_diagnostic(client, fx, right_topics=set(fx.topic_ids.values()))
    client.rpc("refresh_fallback_recommendations").execute()
    rows = pending(db, user_id, set(fx.topic_ids.values()))
    # Both fully right: teaching order decides, alpha first.
    assert [r["topic_id"] for r in rows] == [fx.topic_ids["alpha"], fx.topic_ids["beta"]]


def test_stage_3_is_left_to_the_ml_service(db, fx, student):
    user_id, client = student
    take_diagnostic(client, fx, right_topics=set())
    for _ in range(2):  # 3 completed quizzes in all, the diagnostic included
        started = client.rpc("start_quiz", {"p_quiz_id": fx.topic_quiz_id}).execute().data
        client.rpc("submit_quiz", {"p_attempt_id": started["attempt_id"], "p_responses": {}}).execute()
    stages = db.rpc("recommendation_stages", {"p_student": user_id}).execute().data
    assert [s["stage"] for s in stages if s["course_id"] == fx.course_id] == [3]
    assert client.rpc("refresh_fallback_recommendations").execute().data == 0


def test_students_cannot_read_another_students_stage_2_list(student):
    user_id, client = student
    with pytest.raises(APIError):
        client.rpc("diagnostic_recommendations", {"p_student": user_id}).execute()
