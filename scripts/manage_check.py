"""Check of course management (Prompt 7) in Chrome, with a temporary student and course manager.

    Student   no Manage link; /manage says "Course managers only"; sends a request with two files
    Manager   Manage link; sees the request and opens its files; marks it in progress, then added
    Student   sees "In progress", then "Added", with notifications
    Manager   Courses grouped by level with Sample/Reviewed; on the throwaway test course: edits a topic,
              hides a question, adds a link, marks it reviewed; each edit appears in Edit history
    Decline   a second request declined with a reason the student sees

Everything it creates (users, files, the test course) is removed at the end.
Needs the Vite dev server.

    python scripts/manage_check.py [--shots DIR] [--mobile]
"""

import argparse
import struct
import sys
import tempfile
import zlib
from pathlib import Path

import httpx
from playwright.sync_api import Page, expect, sync_playwright

import testkit

APP = "http://localhost:5173"
BUCKET = "course-request-files"
results: list[bool] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append(passed)
    print(f"{'PASS' if passed else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""))


def tiny_png() -> bytes:
    raw = b"\x00\xff\xff\xff"
    chunk = lambda t, d: struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d) & 0xffffffff)
    return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", 1, 1, 8, 2, 0, 0, 0)) + \
        chunk(b"IDAT", zlib.compress(raw)) + chunk(b"IEND", b"")


def account(db, name: str, role: str) -> tuple[str, str]:
    uid, email = testkit.create_student(db, name)
    db.table("profiles").update({"full_name": name, "department": "Computer Science", "level": 500, "role": role}).eq("id", uid).execute()
    return uid, email


def sign_in(page: Page, email: str) -> None:
    page.goto(f"{APP}/login")
    page.get_by_label("Email").fill(email)
    page.get_by_label("Password").fill(testkit.PASSWORD)
    page.get_by_role("button", name="Sign in").click()
    page.wait_for_url(f"{APP}/")


def nav_has_manage(page: Page, mobile: bool) -> bool:
    expect(page.get_by_role("heading", name="Recommended for you")).to_be_visible()
    page.wait_for_load_state("networkidle")  # the nav reads the profile's role
    if mobile:
        page.get_by_role("button", name="Open menu").click()
    found = page.get_by_role("link", name="Manage", exact=True).count() > 0
    if mobile:
        page.get_by_role("button", name="Close menu").click()
    return found


def remove_files(db) -> None:
    store = db.storage.from_(BUCKET)
    for u in db.auth.admin.list_users(page=1, per_page=1000):
        if (u.email or "").endswith("@" + testkit.EMAIL_DOMAIN):
            paths = [f"{u.id}/{d['name']}/{f['name']}" for d in store.list(u.id) for f in store.list(f"{u.id}/{d['name']}")]
            if paths:
                store.remove(paths)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--shots", type=Path)
    parser.add_argument("--mobile", action="store_true")
    args = parser.parse_args()
    if args.shots:
        args.shots.mkdir(parents=True, exist_ok=True)
    db = testkit.admin()
    remove_files(db)
    fx = testkit.setup(db)
    db.table("courses").update({"level": 500, "semester": 1, "is_reviewed": False, "title": "Test course (temporary)"}).eq("id", fx.course_id).execute()
    sid, student_email = account(db, "Amaka Obi", "student")
    _, manager_email = account(db, "Dr Test Manager", "course_manager")
    files = Path(tempfile.mkdtemp())
    (files / "TEST000-outline.pdf").write_bytes(b"%PDF-1.4\n% course outline\n%%EOF\n")
    (files / "past-question-2023.png").write_bytes(tiny_png())
    viewport = {"width": 390, "height": 844} if args.mobile else {"width": 1280, "height": 900}

    def shot(page: Page, name: str, full: bool = True) -> None:
        if args.shots:
            page.evaluate("window.scrollTo(0, 0)")
            page.wait_for_timeout(300)
            page.screenshot(path=str(args.shots / f"{name}.png"), full_page=full)

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(channel="chrome", headless=True)
            stu = browser.new_context(viewport=viewport).new_page()
            mgr = browser.new_context(viewport=viewport).new_page()
            for page in (stu, mgr):
                page.set_default_timeout(20_000)

            print("-- Student: blocked from /manage, sends a request with files")
            sign_in(stu, student_email)
            check("a student has no Manage link", not nav_has_manage(stu, args.mobile))
            stu.goto(f"{APP}/manage")
            expect(stu.get_by_test_id("manage-forbidden")).to_be_visible()
            check("/manage tells a student it is for course managers only", stu.get_by_role("heading", name="Course managers only").count() == 1)
            stu.goto(f"{APP}/manage/courses/TEST%20000")
            expect(stu.get_by_test_id("manage-forbidden")).to_be_visible()
            check("so does a deep link into /manage", stu.get_by_test_id("manage-course").count() == 0)

            stu.goto(f"{APP}/courses/request")
            stu.get_by_label("Course code").fill("TEST 000")
            stu.get_by_label("Course title").fill("Test course")
            stu.get_by_label("Lecturer (optional)").fill("Dr A. Lecturer")
            stu.get_by_label("Details (optional)").fill("Taught in the first semester. The outline and a past question are attached.")
            stu.get_by_test_id("request-files").set_input_files([str(files / "TEST000-outline.pdf"), str(files / "past-question-2023.png")])
            chosen = stu.get_by_test_id("chosen-files").locator("li")
            check("two files chosen and listed before sending", chosen.count() == 2)
            stu.get_by_test_id("request-files").set_input_files([str(files / "TEST000-outline.pdf")])  # a third file, then Remove it
            stu.get_by_test_id("chosen-files").locator("li").nth(2).get_by_role("button", name="Remove").click()
            shot(stu, "request-form-with-files")
            stu.get_by_role("button", name="Send request").click()
            expect(stu.get_by_text("Request sent.")).to_be_visible()
            mine = stu.get_by_test_id("course-request").first
            check("the request shows Pending with its two files",
                  mine.get_by_test_id("request-status").inner_text() == "Pending" and mine.get_by_test_id("request-file").count() == 2)
            rows = db.table("course_request_files").select("path, name").eq("student_id", sid).execute().data
            check("both files are in the private bucket under the student's folder",
                  len(rows) == 2 and all(r["path"].startswith(sid + "/") for r in rows), ", ".join(r["name"] for r in rows))
            shot(stu, "request-sent")

            print("\n-- Manager: requests")
            sign_in(mgr, manager_email)
            check("a course manager has the Manage link", nav_has_manage(mgr, args.mobile))
            mgr.goto(f"{APP}/manage")
            card = mgr.get_by_test_id("manage-request").filter(has_text="TEST 000").first
            expect(card).to_be_visible()
            check("the request shows the student, details and both files",
                  "Amaka Obi" in card.inner_text() and card.get_by_test_id("request-file").count() == 2)
            # The link downloads the file, so record the URL the page opens instead of following it.
            # (ends with "; 0": a string that evaluates to a function would be called by Playwright)
            mgr.evaluate("window.__opened = []; window.open = (u) => { window.__opened.push(u); return null }; 0")
            card.get_by_test_id("request-file").first.click()
            mgr.wait_for_function("window.__opened.length > 0")
            file_url = mgr.evaluate("window.__opened[0]")
            path = db.table("course_request_files").select("path").eq("student_id", sid).limit(1).execute().data[0]["path"]
            check("the manager opens a file through a short-lived signed link",
                  "token=" in file_url and httpx.get(file_url, timeout=30).status_code == 200)
            card.get_by_role("button", name="Mark in progress").click()
            expect(card.get_by_test_id("request-status")).to_have_text("In progress")
            check("marked in progress", True)
            shot(mgr, "manage-requests")

            stu.goto(f"{APP}/courses/request")
            check("the student sees In progress", stu.get_by_test_id("request-status").first.inner_text() == "In progress")
            kinds = [n["kind"] for n in db.table("notifications").select("kind").eq("student_id", sid).execute().data]
            check("and gets a notification", "course_request_in_progress" in kinds)

            card.get_by_role("button", name="Mark added").click()
            card.get_by_role("button", name="Mark added and notify").click()
            mgr.get_by_role("button", name="All").click()
            done = mgr.get_by_test_id("manage-request").filter(has_text="TEST 000").first
            expect(done.get_by_test_id("request-status")).to_have_text("Added")
            enrolled = db.table("enrollments").select("course_id").eq("student_id", sid).eq("course_id", fx.course_id).execute().data
            check("marked added: the student is enrolled and notified",
                  bool(enrolled) and "course_added" in [n["kind"] for n in db.table("notifications").select("kind").eq("student_id", sid).execute().data])

            print("\n-- Manager: courses")
            mgr.goto(f"{APP}/manage/courses")
            expect(mgr.get_by_test_id("manage-course").first).to_be_visible()
            levels = mgr.locator("h2").filter(has_text="level").all_inner_texts()
            check("courses grouped by level", len(levels) >= 2, ", ".join(levels))
            sample = mgr.get_by_test_id("manage-course").filter(has_text="TEST 000")
            check("the test course shows as Sample", sample.get_attribute("data-reviewed") == "false")
            check("reviewed courses show as Reviewed", mgr.locator("[data-testid=manage-course][data-reviewed=true]").count() >= 2)
            shot(mgr, "manage-courses")

            sample.click()
            topic = mgr.get_by_test_id("manage-topic").first
            topic.get_by_role("button", name="Edit").click()
            topic.get_by_label("Topic title").fill("Alpha: the basics")
            topic.get_by_label("Summary").fill("What alpha is and why it matters. The first topic of the test course.")
            topic.get_by_role("button", name="Save topic").click()
            expect(topic.get_by_text("Saved")).to_be_visible()
            check("a topic's title and summary edited",
                  db.table("topics").select("title").eq("id", fx.topic_ids["alpha"]).single().execute().data["title"] == "Alpha: the basics")

            question = topic.get_by_test_id("manage-question").first
            expect(question).to_be_visible()
            question.get_by_test_id("toggle-hidden").click()
            expect(topic.locator("[data-testid=manage-question][data-status=hidden]")).to_have_count(1)
            check("a practice question hidden from quizzes", True)

            topic.get_by_role("button", name="Add a link").click()
            form = topic.get_by_test_id("resource-form").last
            form.get_by_label("Title").fill("Video: Alpha explained")
            form.get_by_label("Link").fill("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            form.get_by_role("button", name="Add link").click()
            expect(topic.get_by_test_id("manage-resource").filter(has_text="Video: Alpha explained")).to_be_visible()
            check("a resource link added", True)

            mgr.get_by_test_id("toggle-reviewed").click()
            expect(mgr.get_by_test_id("course-reviewed")).to_be_visible()
            check("the course marked reviewed (Sample badge gone)",
                  db.table("courses").select("is_reviewed").eq("id", fx.course_id).single().execute().data["is_reviewed"] is True)
            mgr.evaluate("window.scrollTo(0, 0)")
            fits = mgr.evaluate("document.documentElement.scrollWidth <= window.innerWidth")
            check("the course editor fits the screen (no sideways scroll, even with a long link)", fits)
            shot(mgr, "manage-course-editing")

            mgr.goto(f"{APP}/manage/history")
            expect(mgr.get_by_test_id("audit-entry").first).to_be_visible()
            entries = mgr.get_by_test_id("audit-entry").all_inner_texts()
            mine = [e for e in entries if "Dr Test Manager" in e]
            check("every edit is in Edit history with the manager's name", len(mine) >= 6, f"{len(mine)} entries")
            audit = db.table("content_audit").select("action").in_("row_id", [fx.course_id, fx.topic_ids["alpha"]]).execute().data
            check("audit rows for the course and the topic", {"course.review", "topic.update"} <= {a["action"] for a in audit})
            shot(mgr, "manage-history")

            print("\n-- Decline with a reason")
            stu.goto(f"{APP}/courses/request")
            stu.get_by_label("Course code").fill("ZZZ 999")
            stu.get_by_label("Course title").fill("A course that does not exist")
            stu.get_by_role("button", name="Send request").click()
            expect(stu.get_by_text("Request sent.")).to_be_visible()
            mgr.goto(f"{APP}/manage")
            card = mgr.get_by_test_id("manage-request").filter(has_text="ZZZ 999").first
            card.get_by_role("button", name="Decline").click()
            card.get_by_label("Reason (the student sees this)").fill("No department offers ZZZ 999. Check the code on your course form.")
            card.get_by_role("button", name="Decline and notify").click()
            expect(mgr.get_by_test_id("manage-request").filter(has_text="ZZZ 999")).to_have_count(0)
            stu.reload()
            declined = stu.get_by_test_id("course-request").filter(has_text="ZZZ 999")
            check("the student sees Declined with the reason",
                  declined.get_by_test_id("request-status").inner_text() == "Declined" and "No department offers" in declined.inner_text())
            shot(stu, "request-declined")
            browser.close()
    finally:
        remove_files(db)
        testkit.cleanup(db)

    print(f"\n{sum(results)}/{len(results)} checks passed")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
