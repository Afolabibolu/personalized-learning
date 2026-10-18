"""Throwaway data for scripts that test the database as real students.

setup() creates a test course with two topics, approved questions in all four
formats, a diagnostic quiz and a topic quiz. create_student() adds an auth user
on a test email domain. cleanup() removes all of it, and runs first in setup()
in case an earlier run crashed.
"""

import os
from dataclasses import dataclass, field
from pathlib import Path

from dotenv import load_dotenv
from supabase import Client, create_client

load_dotenv(Path(__file__).parent / ".env")

URL = os.environ["SUPABASE_URL"]
ANON_KEY = os.environ["SUPABASE_ANON_KEY"]
SERVICE_KEY = os.environ["SUPABASE_SERVICE_ROLE_KEY"]

COURSE_CODE = "TEST 000"
EMAIL_DOMAIN = "rls-check.example.com"
PASSWORD = "Check-pass-2026!"


def admin() -> Client:
    return create_client(URL, SERVICE_KEY)


def anon() -> Client:
    return create_client(URL, ANON_KEY)


def sign_in(email: str) -> Client:
    client = anon()
    client.auth.sign_in_with_password({"email": email, "password": PASSWORD})
    return client


def options(*texts: str) -> list[dict]:
    return [{"key": chr(ord("a") + i), "text": text} for i, text in enumerate(texts)]


TRUE_FALSE = [{"key": "true", "text": "True"}, {"key": "false", "text": "False"}]

# (format, stem, options, correct keys) per topic
QUESTIONS = {
    "alpha": [
        ("single_choice", "Alpha single 1", options("w", "x", "y", "z"), ["b"]),
        ("single_choice", "Alpha single 2", options("w", "x", "y", "z"), ["d"]),
        ("true_false", "Alpha true/false", TRUE_FALSE, ["true"]),
        ("multi_select", "Alpha multi 1", options("w", "x", "y", "z"), ["a", "c"]),
        ("multi_select", "Alpha multi 2", options("w", "x", "y", "z"), ["b", "c", "d"]),
        ("odd_one_out", "Alpha odd one out", options("cat", "dog", "car", "cow"), ["c"]),
    ],
    "beta": [
        ("single_choice", "Beta single", options("w", "x", "y"), ["a"]),
        ("true_false", "Beta true/false", TRUE_FALSE, ["false"]),
        ("multi_select", "Beta multi", options("w", "x", "y", "z"), ["a", "b"]),
        ("odd_one_out", "Beta odd one out", options("red", "blue", "green", "seven"), ["d"]),
    ],
}


@dataclass
class Fixture:
    course_id: str
    topic_ids: dict[str, str]
    diagnostic_quiz_id: str
    topic_quiz_id: str  # on topic "alpha", 4 of its 6 questions
    resource_id: str
    correct: dict[str, list[str]] = field(default_factory=dict)  # question id -> keys
    formats: dict[str, str] = field(default_factory=dict)  # question id -> format


def cleanup(db: Client) -> None:
    # Users first: their attempts, answers, logs and recommendations cascade
    # with them and would otherwise block deleting the course.
    page = 1
    while True:
        users = db.auth.admin.list_users(page=page, per_page=1000)
        for user in users:
            if user.email and user.email.endswith("@" + EMAIL_DOMAIN):
                db.auth.admin.delete_user(user.id)
        if len(users) < 1000:
            break
        page += 1
    db.table("courses").delete().eq("code", COURSE_CODE).execute()


def setup(db: Client) -> Fixture:
    cleanup(db)
    course = db.table("courses").insert({"code": COURSE_CODE, "title": "Test course"}).execute().data[0]
    topic_ids = {}
    for order, slug in enumerate(QUESTIONS, start=1):
        row = {"course_id": course["id"], "slug": slug, "title": slug.title(), "sequence_order": order}
        topic_ids[slug] = db.table("topics").insert(row).execute().data[0]["id"]

    fixture = Fixture(
        course_id=course["id"],
        topic_ids=topic_ids,
        diagnostic_quiz_id=db.table("quizzes").insert({
            "course_id": course["id"], "kind": "diagnostic", "title": "Test diagnostic", "question_count": 4,
        }).execute().data[0]["id"],
        topic_quiz_id=db.table("quizzes").insert({
            "course_id": course["id"], "topic_id": topic_ids["alpha"], "kind": "topic",
            "title": "Alpha quiz", "question_count": 4,
        }).execute().data[0]["id"],
        resource_id=db.table("resources").insert({
            "topic_id": topic_ids["alpha"], "title": "Alpha notes", "type": "link",
            "url": "https://example.com/alpha", "is_introductory": True, "intro_order": 1,
        }).execute().data[0]["id"],
    )

    for slug, questions in QUESTIONS.items():
        rows = [
            {
                "topic_id": topic_ids[slug], "format": fmt, "stem": stem, "options": opts,
                "correct_answer": correct, "explanation": f"Because {stem}.", "source": "test fixture",
                "status": "approved",
            }
            for fmt, stem, opts, correct in questions
        ]
        for q in db.table("questions").insert(rows).execute().data:
            fixture.correct[q["id"]] = q["correct_answer"]
            fixture.formats[q["id"]] = q["format"]
    return fixture


def create_student(db: Client, name: str) -> tuple[str, str]:
    """Returns (user id, email)."""
    email = f"{name.lower().replace(' ', '-')}@{EMAIL_DOMAIN}"
    response = db.auth.admin.create_user({
        "email": email,
        "password": PASSWORD,
        "email_confirm": True,
        "user_metadata": {"full_name": name},
    })
    return response.user.id, email
