"""Course requests from students (scalability): list them, download their files, then mark them added or declined.

    python scripts/course_requests.py                      # list open requests (pending or in progress)
    python scripts/course_requests.py --all                # every request
    python scripts/course_requests.py files <id>           # download its files to content/sources/raw/requests/<CODE>/
    python scripts/course_requests.py add <id> --course "CSC 563" [--note "..."]
    python scripts/course_requests.py decline <id> --note "..."

A course manager can do the same from /manage in the app (docs/how-to-add-a-course.md);
both record the change in content_audit.

Add the course itself first, through the ingestion pipeline (content/CLAUDE.md:
inventory.py, extract.py, write the course files, publish.py). "add" then links
the request to that course, enrols the student in it and sends them a
"course_added" notification. <id> can be the first 8 characters shown by the list.
Uses the service role key from scripts/.env.
"""

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import testkit

RAW = Path(__file__).resolve().parent.parent / "content" / "sources" / "raw" / "requests"
BUCKET = "course-request-files"


def audit(db, request: dict, changes: dict) -> None:
    """The same audit row /manage writes, with no person (the admin script ran it)."""
    db.table("content_audit").insert({
        "actor_id": None, "action": "request.status", "table_name": "course_requests", "row_id": request["id"],
        "summary": f"Request {request['code']}: {changes['status']['to']} (admin script)", "changes": changes,
    }).execute()


def find(db, prefix: str) -> dict:
    rows = [r for r in db.table("course_requests").select("*").execute().data if r["id"].startswith(prefix)]
    if len(rows) != 1:
        sys.exit(f"{len(rows)} requests match '{prefix}'; give more of the id")
    return rows[0]


def show(db, everything: bool) -> None:
    query = db.table("course_requests").select("*, profiles(full_name)").order("created_at")
    rows = query.execute().data if everything else query.in_("status", ["pending", "in_progress"]).execute().data
    if not rows:
        print("No open requests." if not everything else "No requests.")
        return
    for r in rows:
        when = r["created_at"][:10]
        extra = " · ".join(str(x) for x in [f"{r['level']} level" if r["level"] else None,
                                             f"semester {r['semester']}" if r["semester"] else None,
                                             r["lecturer"]] if x)
        print(f"{r['id'][:8]}  {r['status']:11}  {when}  {r['code']} · {r['title']}  ({r['profiles']['full_name'] or 'no name'})")
        if extra:
            print(f"          {extra}")
        if r["details"]:
            print(f"          {r['details']}")
        files = db.table("course_request_files").select("name").eq("request_id", r["id"]).execute().data
        if files:
            print(f"          files: {', '.join(f['name'] for f in files)}")


def download(db, prefix: str) -> None:
    request = find(db, prefix)
    files = db.table("course_request_files").select("path, name").eq("request_id", request["id"]).execute().data
    if not files:
        print("This request has no files.")
        return
    folder = RAW / re.sub(r"[^A-Za-z0-9]+", "", request["code"]).upper()
    folder.mkdir(parents=True, exist_ok=True)
    for f in files:
        (folder / f["name"]).write_bytes(db.storage.from_(BUCKET).download(f["path"]))
        print(f"  {folder.relative_to(RAW.parents[2])}/{f['name']}")
    print(f"{len(files)} file(s) saved. Next: python content/ingest/inventory.py (see docs/how-to-add-a-course.md).")


def add(db, prefix: str, code: str, note: str | None) -> None:
    request = find(db, prefix)
    courses = db.table("courses").select("id, code, title").eq("code", code).execute().data
    if not courses:
        sys.exit(f"No course {code} yet: add it through the ingestion pipeline first (content/ingest/publish.py)")
    course = courses[0]
    now = datetime.now(timezone.utc).isoformat()
    db.table("course_requests").update({"status": "added", "course_id": course["id"], "admin_note": note,
                                        "updated_at": now}).eq("id", request["id"]).execute()
    db.table("enrollments").upsert({"student_id": request["student_id"], "course_id": course["id"]},
                                   ignore_duplicates=True).execute()
    db.table("notifications").insert({
        "student_id": request["student_id"], "kind": "course_added",
        "title": f"{course['code']} is ready",
        "body": f"{course['title']} has been added to your courses, with its topics, study notes and quizzes.",
        "link": f"/courses/{course['id']}",
    }).execute()
    audit(db, request, {"status": {"from": request["status"], "to": "added"}, "course_id": {"from": request["course_id"], "to": course["id"]}})
    print(f"Added: {course['code']} · {course['title']} is now in the student's courses, and they have been notified.")


def decline(db, prefix: str, note: str) -> None:
    request = find(db, prefix)
    db.table("course_requests").update({"status": "declined", "admin_note": note,
                                        "updated_at": datetime.now(timezone.utc).isoformat()}).eq("id", request["id"]).execute()
    db.table("notifications").insert({
        "student_id": request["student_id"], "kind": "course_request_declined",
        "title": f"Your request for {request['code']} was declined", "body": f"Reason: {note}", "link": "/courses/request",
    }).execute()
    audit(db, request, {"status": {"from": request["status"], "to": "declined"}, "admin_note": {"from": request["admin_note"], "to": note}})
    print(f"Declined: {request['code']} · {request['title']}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("action", nargs="?", choices=["files", "add", "decline"])
    parser.add_argument("id", nargs="?")
    parser.add_argument("--course")
    parser.add_argument("--note")
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()
    db = testkit.admin()
    if args.action is None:
        show(db, args.all)
    elif not args.id:
        parser.error("give the request id")
    elif args.action == "files":
        download(db, args.id)
    elif args.action == "add":
        if not args.course:
            parser.error("add needs --course")
        add(db, args.id, args.course, args.note)
    else:
        if not args.note:
            parser.error("decline needs --note, so the student sees why")
        decline(db, args.id, args.note)
    return 0


if __name__ == "__main__":
    sys.exit(main())
