"""Check for the 25 October additions: videos and textbooks in the recommendations,
exam-style question sets, CSC 572's seventh topic, and course requests.

    python scripts/phase10_check.py [--shots DIR]

1. Content: every topic has a textbook card; every video link is a YouTube link
   that YouTube's oEmbed endpoint still confirms; exam-style sets are labelled
   "not from a past paper"; CSC 572 has 7 topics.
2. In Chrome as the active demo student: each ML recommendation shows "Also
   recommended" with a video and a textbook; the textbook opens as a reading
   card; the topic page lists videos and textbooks.
3. Course requests: a new student sends a request from the Courses page, sees
   it as pending, scripts/course_requests.py adds it, and the student sees it
   added, gets a "course_added" notification and finds the course in their
   courses. The test student is removed afterwards.
Needs the Vite dev server and the ML service.
"""

import argparse
import json
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path

from playwright.sync_api import Page, expect, sync_playwright

import testkit

ROOT = Path(__file__).resolve().parent.parent
PY = str(ROOT / ".venv" / "bin" / "python")
APP = "http://localhost:5173"
DEMO_PASSWORD = "DemoPass2026!"
LAPTOP = {"width": 1280, "height": 900}
PHONE = {"width": 375, "height": 812}

results: list[bool] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append(passed)
    print(f"{'PASS' if passed else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""))


def shot(folder: Path | None, page: Page, name: str, full_page: bool = False) -> None:
    if folder:
        folder.mkdir(parents=True, exist_ok=True)
        page.wait_for_timeout(250)
        page.screenshot(path=str(folder / name), full_page=full_page)


def oembed_ok(url: str) -> bool:
    try:
        query = urllib.parse.urlencode({"url": url, "format": "json"})
        return urllib.request.urlopen(f"https://www.youtube.com/oembed?{query}", timeout=15).status == 200
    except Exception:
        return False


def content(db) -> None:
    print("-- Content")
    topics = db.table("topics").select("title, courses(code), resources(type, title, url, body)").execute().data
    no_book = [t["title"] for t in topics if not any(r["type"] == "textbook" for r in t["resources"])]
    check("every topic has a recommended textbook card", not no_book, ", ".join(no_book) or f"{len(topics)} topics")
    videos = [r for t in topics for r in t["resources"] if r["type"] == "video"]
    not_youtube = [v["url"] for v in videos if not v["url"].startswith("https://www.youtube.com/watch?v=")]
    dead = [v["url"] for v in videos if not oembed_ok(v["url"])]
    check("every video is a YouTube link that oEmbed confirms exists", videos and not not_youtube and not dead,
          f"{len(videos)} videos for {len(topics)} topics" + (f"; failing: {not_youtube + dead}" if not_youtube or dead else ""))
    exam = [r for t in topics for r in t["resources"] if r["type"] == "past_questions" and r["title"].startswith("Exam-style")]
    labelled = all("These are not from a past paper." in r["body"] for r in exam)
    courses = sorted({t["courses"]["code"] for t in topics for r in t["resources"] if r in exam})
    check("exam-style sets are labelled as not from a past paper", exam and labelled,
          f"{len(exam)} sets in {', '.join(courses)}")
    csc572 = [t for t in topics if t["courses"]["code"] == "CSC 572"]
    check("CSC 572 has 7 topics, including Decision Trees and Random Forests",
          len(csc572) == 7 and any(t["title"] == "Decision Trees and Random Forests" for t in csc572), f"{len(csc572)} topics")


def sign_in(page: Page, email: str, password: str) -> None:
    page.goto(f"{APP}/login")
    page.get_by_label("Email").fill(email)
    page.get_by_label("Password").fill(password)
    page.get_by_role("button", name="Sign in").click()
    page.wait_for_url(f"{APP}/")


def recommendations(browser, db, folder: Path | None) -> None:
    print("-- Videos and textbooks in the recommendations")
    page = browser.new_page(viewport=LAPTOP)
    page.set_default_timeout(20_000)
    sign_in(page, "active.student@demo.example.com", DEMO_PASSWORD)
    with page.expect_response(lambda r: "/recommend" in r.url and r.request.method == "POST", timeout=30_000):
        page.get_by_role("button", name="Refresh").click()
    recs = page.get_by_test_id("recommendation").filter(has=page.get_by_test_id("recommendation-topic"))
    expect(recs.first).to_be_visible()
    ml = [recs.nth(i) for i in range(recs.count()) if recs.nth(i).get_attribute("data-kind") != "getting-started"]
    with_both = [r for r in ml if r.get_by_test_id("also-link").filter(has_text="Video:").count()
                 and r.get_by_test_id("also-link").filter(has_text="Textbook:").count()]
    check("each ML recommendation also suggests a video and a textbook for its topic", ml and len(with_both) == len(ml),
          f"{len(with_both)} of {len(ml)} cards")
    video = page.get_by_test_id("also-link").filter(has_text="Video:").first
    check("the video opens on YouTube in a new tab",
          video.get_attribute("target") == "_blank" and "youtube.com/watch" in (video.get_attribute("href") or ""))
    recs.first.scroll_into_view_if_needed()
    page.evaluate("window.scrollBy(0, -90)")
    shot(folder, page, "p10-01-also-recommended.png")
    page.get_by_test_id("also-link").filter(has_text="Textbook:").first.click()
    page.wait_for_url(f"{APP}/resources/**")
    expect(page.get_by_text("Recommended textbook", exact=True)).to_be_visible()
    headings = page.locator("article .prose h2").all_inner_texts()
    check("the textbook opens as a reading card: what to read and why", any(h.startswith("What to read") for h in headings)
          and "Why this book" in headings, "; ".join(headings))
    shot(folder, page, "p10-02-textbook.png")
    fuzzy = db.table("topics").select("id").eq("title", "Fuzzy Logic Systems").execute().data[0]["id"]
    page.goto(f"{APP}/topics/{fuzzy}")
    expect(page.get_by_text("Recommended textbooks", exact=True)).to_be_visible()
    check("the topic page lists videos and recommended textbooks",
          page.get_by_text("Videos", exact=True).is_visible() and page.get_by_text("Recommended textbooks", exact=True).is_visible())
    shot(folder, page, "p10-03-topic-resources.png", full_page=True)
    page.goto(f"{APP}/knowledge")
    page.get_by_label("Search topics and resources").fill("8051 Timers")
    expect(page.get_by_text("Exam-style questions", exact=True).first).to_be_visible()
    check("a course with no past papers shows 'Exam-style questions', not 'Past questions'",
          page.get_by_text("Past questions", exact=True).count() == 0)
    page.close()


def course_requests(browser, db, folder: Path | None) -> None:
    print("-- Course requests")
    testkit.cleanup(db)
    email = f"request-{testkit.EMAIL_DOMAIN.split('.')[0]}@{testkit.EMAIL_DOMAIN}"
    user = db.auth.admin.create_user({"email": email, "password": testkit.PASSWORD, "email_confirm": True,
                                      "user_metadata": {"full_name": "Request Tester"}})
    # Onboarding is covered by phase 3; this student starts onboarded.
    db.table("profiles").update({"full_name": "Request Tester", "department": "Computer Science", "level": 400}).eq(
        "id", user.user.id).execute()
    try:
        page = browser.new_page(viewport=LAPTOP)
        page.set_default_timeout(20_000)
        sign_in(page, email, testkit.PASSWORD)
        page.goto(f"{APP}/courses")
        page.get_by_role("link", name="Request a course").click()
        page.wait_for_url(f"{APP}/courses/request")
        page.get_by_label("Course code").fill("csc 412")
        page.get_by_label("Course title").fill("Microprocessors and Microcontrollers")
        page.get_by_label("Level").select_option("400")
        page.get_by_label("Semester").select_option("1")
        page.get_by_label("Details (optional)").fill("8086 and 8051; slides are in the department folder.")
        page.get_by_role("button", name="Send request").click()
        expect(page.get_by_text("Request sent.")).to_be_visible()
        item = page.get_by_test_id("course-request").first
        check("a student can request a missing course from the Courses page; it shows as pending",
              "Pending" in item.inner_text() and "CSC 412" in item.inner_text(), " ".join(item.inner_text().split()))
        shot(folder, page, "p10-04-request-form.png", full_page=True)

        listing = subprocess.run([PY, "-W", "ignore", "scripts/course_requests.py"], capture_output=True, text=True, cwd=ROOT)
        line = next((l for l in listing.stdout.splitlines() if "Request Tester" in l), "")
        check("scripts/course_requests.py lists the pending request", bool(line), line.strip())
        added = subprocess.run([PY, "-W", "ignore", "scripts/course_requests.py", "add", line.split()[0],
                                "--course", "CSC 412", "--note", "Added from the course slides."],
                               capture_output=True, text=True, cwd=ROOT)
        check("adding it enrols the student and notifies them", added.returncode == 0 and "Added:" in added.stdout,
              added.stdout.strip() or added.stderr.strip()[-200:])
        page.reload()
        expect(page.get_by_test_id("course-request").first).to_contain_text("Added to your courses")
        check("the student sees the request as added, with a link to the course",
              page.get_by_role("link", name="Open the course").is_visible())
        page.goto(f"{APP}/notifications")
        expect(page.get_by_text("CSC 412 is ready").first).to_be_visible()
        check("the student gets a 'course is ready' notification", page.get_by_text("CSC 412 is ready").first.is_visible())
        page.goto(f"{APP}/courses")
        mine = page.locator("[aria-labelledby=my-courses]").get_by_test_id("course-card")
        expect(mine.first).to_be_visible()
        codes = [mine.nth(i).get_attribute("data-code") for i in range(mine.count())]
        check("the course is now in the student's courses", "CSC 412" in codes, ", ".join(c or "" for c in codes))
        page.close()

        page = browser.new_page(viewport=PHONE)
        page.set_default_timeout(20_000)
        sign_in(page, email, testkit.PASSWORD)
        page.goto(f"{APP}/courses/request")
        expect(page.get_by_label("Course code")).to_be_visible()
        check("phone width: the request form fits", not page.evaluate("document.documentElement.scrollWidth > window.innerWidth"))
        shot(folder, page, "p10-05-phone-request.png", full_page=True)
        page.close()
    finally:
        db.auth.admin.delete_user(user.user.id)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--shots", type=Path)
    args = parser.parse_args()
    db = testkit.admin()
    content(db)
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome")
        for name, step in (("recommendations", lambda: recommendations(browser, db, args.shots)),
                           ("course requests", lambda: course_requests(browser, db, args.shots))):
            try:
                step()
            except Exception as e:  # report a crash as a failed check, so the test-case table shows why
                check(f"{name} checks ran to the end", False, f"{type(e).__name__}: {str(e).splitlines()[0][:200]}")
        browser.close()
    print(f"\n{sum(results)}/{len(results)} checks passed")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
