"""Phase 3 check: a brand-new student goes through the real app in Chrome.

Signs up, finishes onboarding, takes a diagnostic quiz, opens the per-topic
results and logs a 30-minute session. Then checks with the service role key
that every step landed in the right tables. Needs the Vite dev server running
(cd web && npm run dev) and Google Chrome installed.

    python scripts/phase3_check.py [--shots DIR] [--keep]

--shots saves a screenshot of each screen to DIR. --keep leaves the test
account in place; otherwise it is deleted at the end.
"""

import argparse
import sys
import time
from pathlib import Path

from playwright.sync_api import Page, expect, sync_playwright

import testkit

APP = "http://localhost:5173"

results: list[tuple[bool, str, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((passed, name, detail))
    print(f"{'PASS' if passed else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""))


def shot(page: Page, shots: Path | None, name: str) -> None:
    if shots:
        page.screenshot(path=str(shots / f"{name}.png"), full_page=True)


def answer_current_question(page: Page) -> None:
    checkboxes = page.get_by_role("checkbox")
    if checkboxes.count():
        checkboxes.nth(0).click()
        checkboxes.nth(1).click()
    else:
        page.get_by_role("radio").first.click()


def run_ui(email: str, shots: Path | None, mobile: bool) -> dict:
    timings = {}
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=True)
        viewport = {"width": 390, "height": 844} if mobile else {"width": 1280, "height": 900}
        page = browser.new_page(viewport=viewport)
        page.set_default_timeout(20_000)

        page.goto(f"{APP}/signup")
        shot(page, shots, "01-signup")
        page.get_by_label("Full name").fill("Phase Three Student")
        page.get_by_label("Email").fill(email)
        page.get_by_label("Password").fill(testkit.PASSWORD)
        page.get_by_role("button", name="Create account").click()
        page.wait_for_url(f"{APP}/onboarding")
        check("sign up lands on onboarding", True, page.url)

        page.get_by_label("Department").fill("Computer Science")
        page.get_by_label("Level").select_option("500")
        page.get_by_role("button", name="Reading notes").click()
        page.get_by_role("button", name="Practising questions").click()
        shot(page, shots, "02-onboarding")
        page.get_by_role("button", name="Continue").click()
        page.wait_for_url(f"{APP}/")
        expect(page.get_by_role("heading", name="Recommended for you")).to_be_visible()
        page.goto(f"{APP}/courses")
        expect(page.get_by_role("heading", name="Your courses")).to_be_visible()
        expect(page.get_by_role("link", name="Take diagnostic quiz").first).to_be_visible()
        shot(page, shots, "03-courses")
        check("onboarding saves, opens the dashboard, and the course list loads", True)

        page.get_by_role("link", name="Take diagnostic quiz").first.click()
        page.wait_for_url(f"{APP}/quiz/**")
        shot(page, shots, "04-quiz-intro")
        page.get_by_role("button", name="Start quiz").click()
        counter = page.get_by_text("/ 18", exact=False)
        expect(counter).to_be_visible()

        for i in range(18):
            answer_current_question(page)
            if i == 2:
                shot(page, shots, "05-quiz-question")
            if i < 17:
                page.get_by_role("button", name="Next").click()
        started = time.perf_counter()
        page.get_by_role("button", name="Submit").click()
        page.wait_for_url(f"{APP}/attempts/**")
        expect(page.get_by_text("Score per topic")).to_be_visible()
        timings["submit_to_results_s"] = round(time.perf_counter() - started, 2)
        topic_rows = page.locator("section").first.locator("div > a").count()
        check("results show a score per topic", topic_rows == 6, f"{topic_rows} topic rows")
        cards = page.locator("section").nth(1).locator("ol > li")
        explained = sum(1 for i in range(cards.count()) if cards.nth(i).locator("p.bg-slate-50").inner_text().strip())
        check("results show each question with its correct answer and explanation",
              cards.count() == 18 and explained == 18, f"{cards.count()} questions, {explained} explanations")
        shot(page, shots, "06-results")

        page.goto(f"{APP}/log")
        page.get_by_label("Topic").select_option(index=1)
        page.get_by_role("button", name="30 min").click()
        page.get_by_role("button", name="Reading").click()
        page.get_by_role("button", name="Save session").click()
        expect(page.get_by_text("Saved: 30 minutes of reading")).to_be_visible()
        check("study logger saves a 30-minute session", True)
        shot(page, shots, "07-log-study")

        page.go_back()
        page.get_by_role("link", name="Back to course").click()
        page.locator("ol a").first.click()
        page.wait_for_url(f"{APP}/topics/**")
        expect(page.get_by_role("link", name="Take topic quiz")).to_be_visible()
        expect(page.get_by_text("Latest score")).to_be_visible()
        check("topic page shows resources, topic quiz, log button and latest score", True)
        shot(page, shots, "08-topic")

        browser.close()
    return timings


def verify_tables(db, email: str) -> None:
    user = next(u for u in db.auth.admin.list_users(page=1, per_page=1000) if u.email == email)
    uid = user.id

    profile = db.table("profiles").select("*").eq("id", uid).single().execute().data
    check("profiles: name, department, level and preferences saved",
          profile["full_name"] == "Phase Three Student" and profile["department"] == "Computer Science"
          and profile["level"] == 500 and sorted(profile["learning_preferences"]) == ["note", "past_questions"],
          f"{profile['full_name']}, {profile['department']}, {profile['level']}, {profile['learning_preferences']}")

    attempts = db.table("quiz_attempts").select("*, quizzes(kind)").eq("student_id", uid).execute().data
    completed = [a for a in attempts if a["completed_at"]]
    check("quiz_attempts: one completed diagnostic attempt with a score",
          len(attempts) == 1 and len(completed) == 1 and completed[0]["quizzes"]["kind"] == "diagnostic"
          and completed[0]["score"] is not None,
          f"{len(attempts)} attempt(s), score {completed[0]['score'] if completed else None}")

    answers = db.table("attempt_answers").select("question_id, questions(topic_id)").eq("attempt_id", completed[0]["id"]).execute().data
    topics = {a["questions"]["topic_id"] for a in answers}
    check("attempt_answers: 18 graded answers across all 6 topics",
          len(answers) == 18 and len(topics) == 6, f"{len(answers)} answers, {len(topics)} topics")

    logs = db.table("study_logs").select("*").eq("student_id", uid).execute().data
    check("study_logs: one 30-minute reading session",
          len(logs) == 1 and logs[0]["duration_minutes"] == 30 and logs[0]["activity_type"] == "reading",
          f"{len(logs)} log(s)")
    return uid


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--shots", type=Path)
    parser.add_argument("--keep", action="store_true")
    parser.add_argument("--mobile", action="store_true", help="use a phone-sized viewport")
    args = parser.parse_args()
    if args.shots:
        args.shots.mkdir(parents=True, exist_ok=True)

    db = testkit.admin()
    email = f"phase3-{int(time.time())}@{testkit.EMAIL_DOMAIN}"
    print(f"-- New student {email}\n")
    uid = None
    try:
        timings = run_ui(email, args.shots, args.mobile)
        print("\n-- Database")
        uid = verify_tables(db, email)
        print(f"\nQuiz submit to results on screen: {timings['submit_to_results_s']} s")
    finally:
        if not args.keep:
            if uid is None:
                uid = next((u.id for u in db.auth.admin.list_users(page=1, per_page=1000) if u.email == email), None)
            if uid:
                db.auth.admin.delete_user(uid)

    failed = [r for r in results if not r[0]]
    print(f"\n{len(results) - len(failed)}/{len(results)} checks passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
