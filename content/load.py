"""Loads courses, topics, resources, quizzes and questions into Supabase.

Resources per topic: the study note (content/notes/, shown in the app), a
past-questions set built from content/past_questions/ (if the topic has any),
and the links in content/resources/ (from content/sources/links.csv). The
cold-start sequence per course is: topic 1's note, topic 1's lecture (or, for a
sample course with no lecture links, topic 1's past questions), topic 2's note.
Sample courses ("is_reviewed": false) load with courses.is_reviewed = false.

    python content/validate.py && python content/load.py [--course "CSC 551"]

Uses the service role key from content/.env. Safe to run again: rows are
matched on their natural keys (course code, topic slug, resource url, quiz
kind, question stem) and updated in place. A question removed from its file
is set back to draft rather than deleted, because old answers may point to it.
"""

import json
import os
import re
import sys
from pathlib import Path

from dotenv import load_dotenv
from supabase import create_client

CONTENT = Path(__file__).parent
DIAGNOSTIC_PER_TOPIC = 3
TOPIC_QUIZ_QUESTIONS = 5


def course_level(course: dict) -> int | None:
    """The course file's "level", else the first digit of the course number times 100 (CSC 551 -> 500)."""
    if course.get("level"):
        return int(course["level"])
    digits = re.search(r"\d", course["code"])
    return int(digits.group()) * 100 if digits and digits.group() in "12345" else None


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


def note_resource(course_file: str, topic: dict) -> dict:
    text = (CONTENT / "notes" / course_file / f"{topic['slug']}.md").read_text().strip()
    source = text.splitlines()[-1].removeprefix("Source:").strip()
    return {"title": f"Study note: {topic['title']}", "type": "note", "body": text, "source": source}


def past_questions_resource(course_file: str, topic: dict) -> dict | None:
    path = CONTENT / "past_questions" / f"{course_file}.json"
    if not path.exists():
        return None
    data = json.loads(path.read_text())
    questions = [q for q in data["questions"] if q["topic"] == topic["slug"]]
    if not questions:
        return None
    papers = {p["year"]: p for p in data["papers"]}
    parts = [f"# Past questions: {topic['title']}", "",
             "Copied as written from past papers. Figures are in the original papers."]
    for year in [y for y in papers if any(q["year"] == y for q in questions)]:
        parts += ["", f"## {year} · {papers[year]['paper']}", ""]
        for q in (q for q in questions if q["year"] == year):
            marks = f" ({q['marks']} marks)" if q.get("marks") else ""
            parts += [f"**Question {q['number']}**{marks}", "", q["text"], ""]
    sources = sorted({papers[q["year"]]["source"] for q in questions})
    return {"title": f"Past questions: {topic['title']}", "type": "past_questions",
            "body": "\n".join(parts).strip() + "\n", "source": "; ".join(sources)}


def topic_resources(course_file: str, topic: dict, order: int, links: list[dict]) -> list[dict]:
    """Note first, then past questions, then links; flags the cold-start sequence."""
    note = note_resource(course_file, topic)
    resources = [note]
    past = past_questions_resource(course_file, topic)
    if past:
        resources.append(past)
    resources += [dict(link) for link in links]
    lecture = next((r for r in resources if r["type"] == "lecture"), None)
    # Cold start: topic 1's note (1) and lecture (2), then topic 2's note (3).
    # No lecture link (sample courses): topic 1's past questions take its place.
    if order == 1:
        note |= {"is_introductory": True, "intro_order": 1}
        second = lecture or past
        if second:
            second |= {"is_introductory": True, "intro_order": 2}
    elif order == 2:
        note |= {"is_introductory": True, "intro_order": 3}
    return resources


def sync_resources(db, topic_id: str, resources: list[dict]) -> None:
    """Makes the topic's resources match the course file, matching rows by title.

    Matching by title (not url) means a changed link updates the existing row,
    so recommendations that point at it keep working. Rows no longer in the
    file are deleted, together with pending recommendations that point at
    them (the next /recommend call recomputes those). A row that an accepted
    or dismissed recommendation still points at is kept but taken out of the
    introductory sequence.
    """
    current = db.table("resources").select("id, title, url").eq("topic_id", topic_id).execute().data
    existing = {r["title"]: r["id"] for r in current}
    by_url = {r["url"]: r["id"] for r in current if r["url"]}
    for r in resources:
        row = {
            "topic_id": topic_id, "title": r["title"], "type": r["type"], "url": r.get("url"),
            "body": r.get("body"), "source": r.get("source"),
            "is_introductory": bool(r.get("is_introductory")),
            "intro_order": r.get("intro_order") if r.get("is_introductory") else None,
        }
        # Same title, or failing that the same link (a renamed resource), updates in place.
        match = existing.get(r["title"]) or (by_url.get(r["url"]) if r.get("url") else None)
        if match:
            db.table("resources").update(row).eq("id", match).execute()
            existing = {t: i for t, i in existing.items() if i != match}
            by_url = {u: i for u, i in by_url.items() if i != match}
        else:
            db.table("resources").insert(row).execute()
    for stale_id in existing.values():
        db.table("recommendations").delete().eq("resource_id", stale_id).eq("status", "pending").execute()
        referenced = db.table("recommendations").select("id").eq("resource_id", stale_id).limit(1).execute().data
        if referenced:
            db.table("resources").update({"is_introductory": False, "intro_order": None}).eq("id", stale_id).execute()
        else:
            db.table("resources").delete().eq("id", stale_id).execute()


def main() -> int:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--course", help='only this course, e.g. "CSC 551"')
    args = parser.parse_args()
    load_dotenv(CONTENT / ".env")
    db = create_client(os.environ["SUPABASE_URL"], os.environ["SUPABASE_SERVICE_ROLE_KEY"])

    course_files = sorted((CONTENT / "courses").glob("*.json"))
    if args.course:
        course_files = [p for p in course_files if json.loads(p.read_text())["code"] == args.course]
    if not course_files:
        print(f"no course files in content/courses/{' for ' + args.course if args.course else ''}")
        return 1

    for path in course_files:
        course = json.loads(path.read_text())
        course_id = db.table("courses").upsert(
            {"code": course["code"], "title": course["title"], "description": course.get("description"),
             "is_reviewed": course.get("is_reviewed", True), "level": course_level(course)},
            on_conflict="code",
        ).execute().data[0]["id"]

        topics = course["topics"]
        links_path = CONTENT / "resources" / f"{path.stem}.json"
        links_by_topic = json.loads(links_path.read_text())["topics"] if links_path.exists() else {}
        question_total = 0
        for order, topic in enumerate(topics, start=1):
            topic_id = db.table("topics").upsert(
                {
                    "course_id": course_id, "slug": topic["slug"], "title": topic["title"],
                    "subtopics": topic.get("subtopics", []), "sequence_order": order,
                    "summary": topic.get("summary"),
                },
                on_conflict="course_id,slug",
            ).execute().data[0]["id"]

            sync_resources(db, topic_id, topic_resources(path.stem, topic, order, links_by_topic.get(topic["slug"], [])))

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
