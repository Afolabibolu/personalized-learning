"""Loads courses, topics, resources, quizzes and questions into Supabase.

    python content/validate.py && python content/load.py

Uses the service role key from content/.env. Safe to run again: rows are
matched on their natural keys (course code, topic slug, resource url, quiz
kind, question stem) and updated in place. A question removed from its file
is set back to draft rather than deleted, because old answers may point to it.
"""

import json
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from supabase import create_client

CONTENT = Path(__file__).parent
DIAGNOSTIC_PER_TOPIC = 3
TOPIC_QUIZ_QUESTIONS = 5


def upsert_quiz(db, course_id: str, topic_id: str | None, kind: str, title: str, count: int) -> None:
    # The one-per-course and one-per-topic rules are partial unique indexes,
    # which PostgREST upserts cannot target, so look the quiz up first.
    query = db.table("quizzes").select("id").eq("course_id", course_id).eq("kind", kind)
    query = query.is_("topic_id", "null") if topic_id is None else query.eq("topic_id", topic_id)
    existing = query.execute().data
    row = {"course_id": course_id, "topic_id": topic_id, "kind": kind, "title": title, "question_count": count}
    if existing:
        db.table("quizzes").update(row).eq("id", existing[0]["id"]).execute()
    else:
        db.table("quizzes").insert(row).execute()


def main() -> int:
    load_dotenv(CONTENT / ".env")
    db = create_client(os.environ["SUPABASE_URL"], os.environ["SUPABASE_SERVICE_ROLE_KEY"])

    course_files = sorted((CONTENT / "courses").glob("*.json"))
    if not course_files:
        print("no course files in content/courses/")
        return 1

    for path in course_files:
        course = json.loads(path.read_text())
        course_id = db.table("courses").upsert(
            {"code": course["code"], "title": course["title"], "description": course.get("description")},
            on_conflict="code",
        ).execute().data[0]["id"]

        topics = course["topics"]
        question_total = 0
        for order, topic in enumerate(topics, start=1):
            topic_id = db.table("topics").upsert(
                {
                    "course_id": course_id, "slug": topic["slug"], "title": topic["title"],
                    "subtopics": topic.get("subtopics", []), "sequence_order": order,
                },
                on_conflict="course_id,slug",
            ).execute().data[0]["id"]

            for r in topic.get("resources", []):
                db.table("resources").upsert(
                    {
                        "topic_id": topic_id, "title": r["title"], "type": r["type"], "url": r["url"],
                        "is_introductory": bool(r.get("is_introductory")),
                        "intro_order": r.get("intro_order") if r.get("is_introductory") else None,
                    },
                    on_conflict="topic_id,url",
                ).execute()

            upsert_quiz(db, course_id, topic_id, "topic", f"{topic['title']} quiz", TOPIC_QUIZ_QUESTIONS)

            question_path = CONTENT / "questions" / path.stem / f"{topic['slug']}.json"
            questions = json.loads(question_path.read_text())
            rows = [
                {
                    "topic_id": topic_id, "format": q["format"], "stem": q["stem"], "options": q["options"],
                    "correct_answer": q["correct_answer"], "explanation": q["explanation"],
                    "source": q["source"], "status": "approved",
                }
                for q in questions
            ]
            db.table("questions").upsert(rows, on_conflict="topic_id,stem").execute()
            stems = {q["stem"] for q in questions}
            stale = [
                q["id"]
                for q in db.table("questions").select("id, stem").eq("topic_id", topic_id).execute().data
                if q["stem"] not in stems
            ]
            if stale:
                db.table("questions").update({"status": "draft"}).in_("id", stale).execute()
            question_total += len(rows)

        upsert_quiz(db, course_id, None, "diagnostic", f"{course['code']} diagnostic",
                    DIAGNOSTIC_PER_TOPIC * len(topics))
        print(f"{course['code']}: {len(topics)} topics, {question_total} questions, "
              f"diagnostic of {DIAGNOSTIC_PER_TOPIC * len(topics)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
