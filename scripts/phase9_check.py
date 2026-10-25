"""Phase 9 check: the course ingestion pipeline, from raw files to the app.

    python scripts/phase9_check.py [--shots DIR]

1. Pipeline commands: inventory.py finds the courses, extract.py extracts one,
   validate.py passes for every sample course.
2. Database: sample courses are loaded with is_reviewed = false, each with
   topics, study notes, practice questions and quizzes.
3. In Chrome: a new student picks a sample course at onboarding, sees it in
   the course list grouped by level, the Knowledge Base (collapsible course
   sections) with the "Sample content" badge, opens a study note and
   past questions, takes a topic quiz, gets a getting-started list for that
   course (and picks it in the progress chart's dropdown), and can remove it
   again; the demo accounts are unchanged.
Needs the Vite dev server and the ML service. Cleans up its test student.
"""

import argparse
import csv
import json
import subprocess
import sys
import time
from pathlib import Path

from playwright.sync_api import Page, expect, sync_playwright

import testkit

ROOT = Path(__file__).resolve().parent.parent
PY = str(ROOT / ".venv" / "bin" / "python")
APP = "http://localhost:5173"
DEMO_PASSWORD = "DemoPass2026!"
LAPTOP = {"width": 1280, "height": 900}
PHONE = {"width": 375, "height": 812}
SAMPLE = "CSC 551"  # the course the browser checks use

results: list[bool] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append(passed)
    print(f"{'PASS' if passed else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""))


def shot(folder: Path | None, page: Page, name: str, full_page: bool = False) -> None:
    if folder:
        folder.mkdir(parents=True, exist_ok=True)
        page.wait_for_timeout(250)
        page.screenshot(path=str(folder / name), full_page=full_page)


def run(args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run([PY, "-I", "-W", "ignore", *args], capture_output=True, text=True, cwd=ROOT, timeout=900)


def pipeline() -> list[str]:
    print("-- Pipeline commands")
    inv = run(["content/ingest/inventory.py"])
    rows = list(csv.DictReader((ROOT / "content/ingest/inventory.csv").open()))
    codes = sorted({r["code"] for r in rows if r["code"] != "UNKNOWN"})
    check("inventory.py finds the courses in sources/raw/ and writes inventory.csv",
          inv.returncode == 0 and len(codes) >= 10, f"{len(rows)} files, {len(codes)} courses: {', '.join(codes)}")
    ext = run(["content/ingest/extract.py", "--course", SAMPLE])
    manifest = list(csv.DictReader((ROOT / "content/ingest/extracted" / SAMPLE.replace(" ", "") / "manifest.csv").open()))
    statuses = sorted({m["status"] for m in manifest})
    check(f"extract.py extracts {SAMPLE} and marks scanned PDFs", ext.returncode == 0 and "text" in statuses,
          f"{len(manifest)} files: {', '.join(statuses)}")
    sample = sorted(json.loads(p.read_text())["code"] for p in (ROOT / "content/courses").glob("*.json")
                    if json.loads(p.read_text()).get("is_reviewed") is False)
    failed = [c for c in sample if "\n0 error(s)" not in run(["content/validate.py", "--course", c]).stdout]
    check("validate.py passes for every sample course", not failed and len(sample) >= 1,
          f"{len(sample)} sample courses" + (f"; failing: {failed}" if failed else ""))
    return sample


def database(sample: list[str]) -> None:
    print("-- Database")
    db = testkit.admin()
    courses = db.table("courses").select(
        "code, is_reviewed, topics(id, resources(type), quizzes(kind), questions(status))").in_("code", sample).execute().data
    loaded = {c["code"]: c for c in courses}
    check("every sample course is loaded with is_reviewed = false",
          set(loaded) == set(sample) and not any(c["is_reviewed"] for c in courses), f"{len(loaded)} of {len(sample)}")
    weak = [c["code"] for c in courses if not all(
        any(r["type"] == "note" for r in t["resources"]) and any(q["kind"] == "topic" for q in t["quizzes"])
        and sum(q["status"] == "approved" for q in t["questions"]) >= 8 for t in c["topics"])]
    topics = sum(len(c["topics"]) for c in courses)
    check("each topic has a study note, a topic quiz and at least 8 practice questions", not weak,
          f"{topics} topics" + (f"; incomplete: {weak}" if weak else ""))
    reviewed = db.table("courses").select("code").eq("is_reviewed", True).neq("code", testkit.COURSE_CODE).execute().data
    check("the reviewed courses are unchanged", sorted(c["code"] for c in reviewed) == ["CSC 531", "CSC 574"])


def browser_checks(folder: Path | None) -> None:
    print("-- In the app")
    db = testkit.admin()
    course_id = db.table("courses").select("id").eq("code", SAMPLE).execute().data[0]["id"]
    email = f"phase9-{int(time.time())}@{testkit.EMAIL_DOMAIN}"
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=True)
        page = browser.new_page(viewport=LAPTOP)
        page.set_default_timeout(20_000)
        try:
            # Sign up; onboarding lists every course, the reviewed ones ticked.
            page.goto(f"{APP}/signup")
            page.get_by_label("Full name").fill("Phase Nine Student")
            page.get_by_label("Email").fill(email)
            page.get_by_label("Password").fill(testkit.PASSWORD)
            page.get_by_role("button", name="Create account").click()
            page.wait_for_url(f"{APP}/onboarding")
            boxes = page.get_by_role("checkbox")
            expect(boxes.first).to_be_visible()
            ticked = [boxes.nth(i).is_checked() for i in range(boxes.count())]
            sample_label = page.get_by_text("Sample content, pending lecturer review").count()
            check("onboarding lists every course, with the two reviewed courses ticked and sample courses labelled",
                  boxes.count() >= 3 and sum(ticked) == 2 and sample_label >= 1, f"{boxes.count()} courses, {sum(ticked)} ticked")
            page.get_by_label(f"{SAMPLE}").check() if page.get_by_label(SAMPLE).count() else \
                page.locator("label", has_text=SAMPLE).get_by_role("checkbox").check()
            page.get_by_role("button", name="Reading notes").click()
            shot(folder, page, "p9-01-onboarding-courses.png", full_page=True)
            page.get_by_role("button", name="Continue").click()
            page.wait_for_url(f"{APP}/")
            uid = next(u.id for u in db.auth.admin.list_users(page=1, per_page=1000) if u.email == email)
            mine = sorted(r["courses"]["code"] for r in db.table("enrollments").select("courses(code)").eq("student_id", uid).execute().data)
            check(f"choosing {SAMPLE} at onboarding enrols the student", SAMPLE in mine, ", ".join(mine))

            # Courses page: my courses and more courses.
            page.goto(f"{APP}/courses")
            cards = page.get_by_test_id("course-card")
            expect(cards.first).to_be_visible()
            check("course list shows my courses, then more courses with the sample badge",
                  page.get_by_role("heading", name="More courses").is_visible()
                  and page.get_by_text("Sample content, pending lecturer review").count() >= 1,
                  f"{cards.count()} course cards")
            groups = page.locator("[id^=level-]").all_inner_texts()
            check("more courses are grouped by level, highest first",
                  [g.lower() for g in groups] == ["500 level", "400 level", "200 level"], " | ".join(groups))
            shot(folder, page, "p9-02-courses.png", full_page=True)

            # Knowledge Base: the sample course with its badge; a study note and past questions.
            page.goto(f"{APP}/knowledge")
            heading = page.get_by_role("heading", name=f"{SAMPLE} · Design and Analysis of Algorithms")
            expect(heading).to_be_visible()
            badge = heading.locator("xpath=..").get_by_text("Sample content, pending lecturer review")
            check("Knowledge Base shows the sample course with the 'Sample content' badge", badge.is_visible())
            heading.scroll_into_view_if_needed()
            shot(folder, page, "p9-03-knowledge-base.png")
            other = page.get_by_role("button", name="CSC 412 · Microprocessor")
            closed = other.get_attribute("aria-expanded") == "false"
            other.click()
            opened = other.get_attribute("aria-expanded") == "true"
            page.get_by_role("button", name="Collapse all").click()
            none_open = page.get_by_test_id("kb-topic").count() == 0
            page.evaluate("window.scrollTo(0, 0)")
            shot(folder, page, "p9-03b-knowledge-base-collapsed.png", full_page=True)
            page.get_by_role("button", name="Expand all").click()
            all_open = page.get_by_test_id("kb-topic").count() == db.table("knowledge_base_stats").select("topics").execute().data[0]["topics"]
            check("Knowledge Base: other courses start collapsed; a header, Expand all and Collapse all toggle them",
                  closed and opened and none_open and all_open)
            page.get_by_role("button", name="My courses").click()
            shown = page.locator("section h2").all_inner_texts()
            check("'My courses' filter shows only the student's courses", len(shown) == len(mine), " | ".join(shown))
            page.get_by_role("button", name="All courses").click()
            page.get_by_label("Search topics and resources").fill("Divide and Conquer")
            page.get_by_role("link", name="Study note: Divide and Conquer").click()
            page.wait_for_url(f"{APP}/resources/**")
            expect(page.locator("article .prose h1")).to_have_text("Divide and Conquer")
            source = page.locator("article .prose p").last.inner_text()
            check("a sample course's study note opens in the app", source.startswith("Source:"), source)
            shot(folder, page, "p9-04-study-note.png", full_page=True)
            page.goto(f"{APP}/knowledge")
            page.get_by_label("Search topics and resources").fill("Graphs, Spanning")
            page.get_by_role("link", name="Past questions: Graphs, Spanning Trees and NP-Completeness").click()
            page.wait_for_url(f"{APP}/resources/**")
            expect(page.locator("article .prose h2").first).to_be_visible()
            years = page.locator("article .prose h2").all_inner_texts()
            check("its past questions open in the app, grouped by paper", len(years) >= 2, "; ".join(years))
            shot(folder, page, "p9-05-past-questions.png", full_page=True)

            # Topic page and a topic quiz on the sample course.
            page.goto(f"{APP}/knowledge")
            page.get_by_label("Search topics and resources").fill("Divide and Conquer")
            page.get_by_test_id("kb-topic").first.click()
            page.wait_for_url(f"{APP}/topics/**")
            expect(page.get_by_role("link", name="Take topic quiz")).to_be_visible()
            check("topic page shows the badge and the topic quiz button",
                  page.get_by_text("Sample content, pending lecturer review").is_visible()
                  and page.get_by_role("link", name="Take topic quiz").is_visible())
            shot(folder, page, "p9-06-topic.png", full_page=True)
            page.get_by_role("link", name="Take topic quiz").click()
            page.wait_for_url(f"{APP}/quiz/**")
            page.get_by_role("button", name="Start quiz").click()
            expect(page.get_by_text("/ 5", exact=False)).to_be_visible()
            for i in range(5):
                if i == 1:
                    shot(folder, page, "p9-07-quiz.png")
                checkboxes = page.get_by_role("checkbox")
                if checkboxes.count():
                    checkboxes.nth(0).click()
                    checkboxes.nth(1).click()
                else:
                    page.get_by_role("radio").first.click()
                if i < 4:
                    page.get_by_role("button", name="Next").click()
            with page.expect_response(lambda r: "/recommend" in r.url, timeout=30_000):
                page.get_by_role("button", name="Submit").click()
            page.wait_for_url(f"{APP}/attempts/**")
            expect(page.get_by_text("Score per topic")).to_be_visible()
            check("a sample course's topic quiz is graded and shows results", True, page.url.split("/")[-1][:8])
            shot(folder, page, "p9-08-results.png")

            # Recommendations: a getting-started list for the sample course.
            recs = db.table("recommendations").select("source, topics(course_id), resources(title)").eq(
                "student_id", uid).eq("status", "pending").execute().data
            sample_recs = [r for r in recs if r["topics"]["course_id"] == course_id]
            check(f"{SAMPLE} gets its own getting-started list (fewer than 3 attempts)",
                  len(sample_recs) >= 2 and all(r["source"] == "cold_start" for r in sample_recs),
                  "; ".join(r["resources"]["title"] for r in sample_recs if r["resources"]))
            page.goto(f"{APP}/")
            expect(page.get_by_test_id("recommendation").first).to_be_visible()
            picker = page.get_by_role("combobox", name="Course")
            options = picker.locator("option").all_inner_texts()
            picker.select_option(label=next(o for o in options if o.startswith(SAMPLE)))
            check("progress chart: a course dropdown lists only my courses and switches the chart",
                  len(options) == len(mine) and page.get_by_test_id("progress-chart").get_by_text("Divide and Conquer").count() >= 1,
                  " | ".join(options))
            shot(folder, page, "p9-09-dashboard.png", full_page=True)

            # Remove the course again from its course page.
            page.goto(f"{APP}/courses/{course_id}")
            page.get_by_role("button", name="Remove from my courses").click()
            expect(page.get_by_role("button", name="Add to my courses")).to_be_visible()
            still = db.table("enrollments").select("course_id").eq("student_id", uid).eq("course_id", course_id).execute().data
            check("a course can be removed from my courses", not still)
            shot(folder, page, "p9-10-course-page.png")
            page.close()

            # Phone width.
            page = browser.new_page(viewport=PHONE)
            page.set_default_timeout(20_000)
            page.goto(f"{APP}/login")
            page.get_by_label("Email").fill(email)
            page.get_by_label("Password").fill(testkit.PASSWORD)
            page.get_by_role("button", name="Sign in").click()
            page.wait_for_url(f"{APP}/")
            page.goto(f"{APP}/courses")
            expect(page.get_by_test_id("course-card").first).to_be_visible()
            overflow = page.evaluate("document.documentElement.scrollWidth > window.innerWidth")
            check("phone width: course list with more courses fits", not overflow)
            shot(folder, page, "p9-11-phone-courses.png")
            page.close()
        finally:
            for u in db.auth.admin.list_users(page=1, per_page=1000):
                if u.email == email:
                    db.auth.admin.delete_user(u.id)

        # The demo accounts still see only their two courses.
        page = browser.new_page(viewport=LAPTOP)
        page.set_default_timeout(20_000)
        page.goto(f"{APP}/login")
        page.get_by_label("Email").fill("new.student@demo.example.com")
        page.get_by_label("Password").fill(DEMO_PASSWORD)
        page.get_by_role("button", name="Sign in").click()
        page.wait_for_url(f"{APP}/")
        items = page.get_by_test_id("recommendation")
        expect(items.first).to_be_visible()
        check("Kemi's dashboard is unchanged: six getting-started items for CSC 531 and CSC 574",
              items.count() == 6, f"{items.count()} items")
        browser.close()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--shots", type=Path)
    args = parser.parse_args()
    sample = pipeline()
    database(sample)
    browser_checks(args.shots)
    print(f"\n{sum(results)}/{len(results)} checks passed")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
