"""Tests for start_quiz, submit_quiz and the grading rule, run against the
linked Supabase project as real signed-in students.

    pytest scripts
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
    yield fixture
    testkit.cleanup(db)


@pytest.fixture
def student(db, fx, request):
    """A fresh signed-in student per test, so earlier tests don't change which questions are 'seen'."""
    _, email = testkit.create_student(db, f"Quiz {request.node.name[:40]}")
    return testkit.sign_in(email)


def start(client, quiz_id):
    return client.rpc("start_quiz", {"p_quiz_id": quiz_id}).execute().data


def submit(client, attempt_id, responses):
    return client.rpc("submit_quiz", {"p_attempt_id": attempt_id, "p_responses": responses}).execute().data


@pytest.mark.parametrize(
    "response, correct, expected",
    [
        (["b"], ["b"], True),  # single_choice right
        (["a"], ["b"], False),  # single_choice wrong
        (["true"], ["true"], True),  # true_false
        (["false"], ["true"], False),
        (["c", "a"], ["a", "c"], True),  # multi_select, order does not matter
        (["a", "a", "c"], ["a", "c"], True),  # duplicates do not matter
        (["a"], ["a", "c"], False),  # partial multi_select is wrong
        (["a", "b", "c"], ["a", "c"], False),  # extra option is wrong
        ([], ["c"], False),  # no answer
    ],
)
def test_answer_is_correct(db, response, correct, expected):
    result = db.rpc("answer_is_correct", {"p_response": response, "p_correct": correct}).execute().data
    assert result is expected


def test_start_quiz_hides_answers(student, fx):
    started = start(student, fx.topic_quiz_id)
    assert len(started["questions"]) == 4
    for q in started["questions"]:
        assert set(q) == {"id", "topic_id", "format", "stem", "options"}


def test_submit_grades_only_the_attempt_questions(student, fx):
    started = start(student, fx.topic_quiz_id)
    ids = [q["id"] for q in started["questions"]]
    not_on_attempt = next(qid for qid in fx.correct if qid not in ids)

    responses = {
        ids[0]: list(reversed(fx.correct[ids[0]])),  # right
        ids[1]: ["zzz"],  # wrong
        ids[2]: fx.correct[ids[2]][0] if len(fx.correct[ids[2]]) == 1 else fx.correct[ids[2]],  # right
        # ids[3] left out: wrong
        not_on_attempt: fx.correct[not_on_attempt],  # ignored
    }
    review = submit(student, started["attempt_id"], responses)

    assert float(review["score"]) == 50.0
    assert [q["id"] for q in review["questions"]] == ids
    assert [q["is_correct"] for q in review["questions"]] == [True, False, True, False]
    assert all("correct_answer" in q and "explanation" in q for q in review["questions"])

    answers = student.table("attempt_answers").select("question_id").eq("attempt_id", started["attempt_id"]).execute().data
    assert sorted(a["question_id"] for a in answers) == sorted(ids)

    attempt = student.table("quiz_attempts").select("score, completed_at").eq("id", started["attempt_id"]).execute().data[0]
    assert float(attempt["score"]) == 50.0 and attempt["completed_at"] is not None


def test_completed_attempt_cannot_be_resubmitted(student, fx):
    started = start(student, fx.topic_quiz_id)
    submit(student, started["attempt_id"], {})
    with pytest.raises(APIError, match="already submitted"):
        submit(student, started["attempt_id"], {q["id"]: fx.correct[q["id"]] for q in started["questions"]})


def test_review_requires_a_submitted_attempt(student, fx):
    started = start(student, fx.topic_quiz_id)
    with pytest.raises(APIError, match="not been submitted"):
        student.rpc("get_attempt_review", {"p_attempt_id": started["attempt_id"]}).execute()


def test_unseen_questions_come_first(student, fx):
    first = {q["id"] for q in start(student, fx.topic_quiz_id)["questions"]}
    second = {q["id"] for q in start(student, fx.topic_quiz_id)["questions"]}
    alpha = {qid for qid in fx.correct if qid in first | second}
    # Alpha has 6 questions and the quiz takes 4, so the second attempt must
    # include the 2 the student has not seen, topped up with 2 already seen.
    assert len(alpha) == 6
    assert len(second - first) == 2


def test_diagnostic_covers_every_topic(student, fx):
    started = start(student, fx.diagnostic_quiz_id)
    per_topic = {}
    for q in started["questions"]:
        per_topic[q["topic_id"]] = per_topic.get(q["topic_id"], 0) + 1
    assert per_topic == {fx.topic_ids["alpha"]: 2, fx.topic_ids["beta"]: 2}


def test_diagnostic_review_scores_each_topic(student, fx):
    started = start(student, fx.diagnostic_quiz_id)
    alpha_first = [q for q in started["questions"] if q["topic_id"] == fx.topic_ids["alpha"]]
    # Alpha all right, beta all wrong.
    responses = {q["id"]: fx.correct[q["id"]] for q in alpha_first}
    review = submit(student, started["attempt_id"], responses)

    scores = {t["topic_id"]: float(t["score"]) for t in review["topic_scores"]}
    assert scores == {fx.topic_ids["alpha"]: 100.0, fx.topic_ids["beta"]: 0.0}
    assert float(review["score"]) == 50.0


def test_topic_scores_use_the_latest_attempt_per_topic(student, fx):
    # Diagnostic: alpha all right, beta all wrong.
    diag = start(student, fx.diagnostic_quiz_id)
    submit(student, diag["attempt_id"], {
        q["id"]: fx.correct[q["id"]] for q in diag["questions"] if q["topic_id"] == fx.topic_ids["alpha"]
    })
    # Later topic quiz on alpha: all wrong. Beta keeps its diagnostic score.
    later = start(student, fx.topic_quiz_id)
    submit(student, later["attempt_id"], {})

    rows = student.rpc("get_topic_scores", {"p_topic_ids": list(fx.topic_ids.values())}).execute().data
    scores = {r["topic_id"]: float(r["score"]) for r in rows}
    assert scores == {fx.topic_ids["alpha"]: 0.0, fx.topic_ids["beta"]: 0.0}

    # A third attempt on alpha, all right, replaces the 0.
    third = start(student, fx.topic_quiz_id)
    submit(student, third["attempt_id"], {q["id"]: fx.correct[q["id"]] for q in third["questions"]})
    rows = student.rpc("get_topic_scores", {"p_topic_ids": [fx.topic_ids["alpha"]]}).execute().data
    assert [float(r["score"]) for r in rows] == [100.0]


def test_topic_scores_are_private(db, fx, student):
    _, other_email = testkit.create_student(db, "Quiz other student")
    other = testkit.sign_in(other_email)
    started = start(student, fx.topic_quiz_id)
    submit(student, started["attempt_id"], {})
    assert other.rpc("get_topic_scores", {"p_topic_ids": list(fx.topic_ids.values())}).execute().data == []


def test_review_shows_the_previous_score_on_each_topic(student, fx):
    first = start(student, fx.topic_quiz_id)
    review1 = submit(student, first["attempt_id"], {})
    assert review1["topic_scores"][0]["previous_score"] is None  # first attempt on the topic

    second = start(student, fx.topic_quiz_id)
    review2 = submit(student, second["attempt_id"], {q["id"]: fx.correct[q["id"]] for q in second["questions"]})
    alpha = review2["topic_scores"][0]
    assert (float(alpha["previous_score"]), float(alpha["score"])) == (0.0, 100.0)
