"""Supabase access for the ML service and training, with the service role key."""

import os
from functools import lru_cache
from pathlib import Path

import joblib
from dotenv import load_dotenv
from supabase import Client, create_client

from app.config import LR_MODEL_PATH, MODEL_VERSION, RF_MODEL_PATH
from app.recommender import CourseData, Models, Recommendation, ResourceInfo

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

PAGE_SIZE = 1000  # Supabase returns at most 1000 rows per request


@lru_cache
def service_client() -> Client:
    return create_client(os.environ["SUPABASE_URL"], os.environ["SUPABASE_SERVICE_ROLE_KEY"])


def fetch_all(make_query) -> list[dict]:
    """Pages through a query. make_query() must return a fresh, ordered query builder."""
    rows, start = [], 0
    while True:
        page = make_query().range(start, start + PAGE_SIZE - 1).execute().data
        rows.extend(page)
        if len(page) < PAGE_SIZE:
            return rows
        start += PAGE_SIZE


# --- models ---

_models_cache: dict[str, tuple[float, Models]] = {}


def load_models() -> Models | None:
    """Loads both saved models, or None when either file is missing (cold start for everyone)."""
    if not (LR_MODEL_PATH.exists() and RF_MODEL_PATH.exists()):
        return None
    stamp = max(LR_MODEL_PATH.stat().st_mtime, RF_MODEL_PATH.stat().st_mtime)
    cached = _models_cache.get("models")
    if cached and cached[0] == stamp:
        return cached[1]
    lr, rf = joblib.load(LR_MODEL_PATH), joblib.load(RF_MODEL_PATH)
    models = Models(lr=lr["model"], rf=rf["model"], version=lr.get("version", MODEL_VERSION))
    _models_cache["models"] = (stamp, models)
    return models


# --- one student's data for /recommend ---

def load_courses(db: Client) -> list[CourseData]:
    topics = db.table("topics").select("id, course_id, sequence_order").order("sequence_order").execute().data
    resources = db.table("resources").select("id, topic_id, title, is_introductory, intro_order, type").execute().data
    quizzes = db.table("quizzes").select("id, topic_id").eq("kind", "topic").execute().data
    course_of_topic = {t["id"]: t["course_id"] for t in topics}

    courses: dict[str, CourseData] = {}
    for t in topics:
        course = courses.setdefault(t["course_id"], CourseData(t["course_id"], [], [], {}))
        course.topic_ids.append(t["id"])
    for r in resources:
        courses[course_of_topic[r["topic_id"]]].resources.append(ResourceInfo(**r))
    for q in quizzes:
        courses[course_of_topic[q["topic_id"]]].topic_quiz_ids[q["topic_id"]] = q["id"]
    return list(courses.values())


def completed_attempts_per_course(db: Client, student_id: str) -> dict[str, int]:
    rows = db.table("quiz_attempts").select("quizzes(course_id)").eq("student_id", student_id).not_.is_(
        "completed_at", "null").execute().data
    counts: dict[str, int] = {}
    for r in rows:
        course_id = r["quizzes"]["course_id"]
        counts[course_id] = counts.get(course_id, 0) + 1
    return counts


def student_history(db: Client, student_id: str) -> tuple[list[dict], list[dict]]:
    scores = fetch_all(lambda: db.table("ml_attempt_topic_scores").select(
        "student_id, topic_id, attempt_id, completed_at, score").eq("student_id", student_id).order("attempt_id"))
    logs = fetch_all(lambda: db.table("study_logs").select(
        "student_id, topic_id, logged_at, duration_minutes").eq("student_id", student_id).order("id"))
    return scores, logs


def used_resource_ids(db: Client, student_id: str) -> set[str]:
    """Resources the student already accepted or dismissed."""
    rows = db.table("recommendations").select("resource_id").eq("student_id", student_id).in_(
        "status", ["accepted", "dismissed"]).not_.is_("resource_id", "null").execute().data
    return {r["resource_id"] for r in rows}


def replace_pending(db: Client, student_id: str, recs: list[Recommendation]) -> None:
    """Deletes the student's pending recommendations, then writes the new ones."""
    db.table("recommendations").delete().eq("student_id", student_id).eq("status", "pending").execute()
    if recs:
        db.table("recommendations").insert([
            {
                "student_id": student_id,
                "topic_id": r.topic_id,
                "resource_id": r.resource_id,
                "quiz_id": r.quiz_id,
                "rank": r.rank,
                "priority_score": r.priority_score,
                "source": r.source,
                "model_version": r.model_version,
            }
            for r in recs
        ]).execute()
