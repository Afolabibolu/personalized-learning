"""Captures every screen in docs/screenshots.md from the running app.

    python scripts/capture_screenshots.py

Writes docs/screenshots/*.png and regenerates docs/screenshots.md (the ordered
checklist: which account, what should be visible, file name). Needs the Vite
dev server, the ML service and the demo accounts. A temporary "Demo Student"
account is created for the sign-up flow and deleted at the end; the demo
accounts are left as they were.
"""

import sys
import time
from dataclasses import dataclass
from pathlib import Path

from playwright.sync_api import Page, expect, sync_playwright

import testkit

APP = "http://localhost:5173"
DOCS = Path(__file__).resolve().parent.parent / "docs"
SHOTS = DOCS / "screenshots"
ACTIVE = "active.student@demo.example.com"
NEW = "new.student@demo.example.com"
DEMO_PASSWORD = "DemoPass2026!"
LAPTOP = {"width": 1280, "height": 900}
PHONE = {"width": 390, "height": 844}


@dataclass
class Shot:
    file: str
    screen: str
    account: str
    visible: str


CHECKLIST = [
    Shot("01-signup.png", "Sign-up page", "None (signed out)", "Full name, email and password fields; link to sign in (FR1)"),
    Shot("02-login.png", "Log-in page", "None (signed out)", "Email and password fields; link to create an account (FR1)"),
    Shot("03-onboarding.png", "Onboarding", "New sign-up (Demo Student)", "Department, level and learning-preference cards, two selected (FR1)"),
    Shot("04-courses.png", "Course list", "New sign-up (Demo Student)", "CSC 531 and CSC 574 with 'Take diagnostic quiz' buttons (FR2, FR5)"),
    Shot("05-quiz-intro.png", "Diagnostic quiz start", "New sign-up (Demo Student)", "18 questions, 'Every topic', Start quiz button (FR2)"),
    Shot("06-quiz-single-choice.png", "Quiz question: single choice", "New sign-up (Demo Student)", "Progress bar, 'Single choice' label, one option selected (FR2)"),
    Shot("07-quiz-true-false.png", "Quiz question: true or false", "New sign-up (Demo Student)", "Two large True/False buttons (FR2)"),
    Shot("08-quiz-multi-select.png", "Quiz question: multiple answers", "New sign-up (Demo Student)", "'Select all that apply', two boxes ticked (FR2)"),
    Shot("09-quiz-odd-one-out.png", "Quiz question: odd one out", "New sign-up (Demo Student)", "'Pick the one that does not belong' hint (FR2)"),
    Shot("10-results-summary.png", "Diagnostic results: score per topic", "New sign-up (Demo Student)", "Overall score, a coloured bar per topic, weakest topic called out (FR2)"),
    Shot("11-results-answers.png", "Diagnostic results: answer review", "New sign-up (Demo Student)", "Each question with your answer, the correct answer and the explanation (FR2)"),
    Shot("12-topic.png", "Topic page", "New sign-up (Demo Student)", "Summary, latest score, Take topic quiz, Log study session, resources grouped by type, subtopics (FR5)"),
    Shot("13-log-study.png", "Study logger", "New sign-up (Demo Student)", "Topic, 30 min and Reading selected, 'Custom (minutes)', optional timer, 'Saved' confirmation, recent sessions (FR3)"),
    Shot("14-dashboard-new.png", "Dashboard, cold start", "Kemi Balogun (new.student@demo.example.com)", "'Hi Kemi'; reminders to log study and take diagnostics; six 'Getting started' items (topic 1 note and lecture, topic 2 note, per course) with 'Not enough quiz history yet'; empty streak (FR4, NFR4)"),
    Shot("15-dashboard-active.png", "Dashboard, ML recommendations", "Tolu Adeyemi (active.student@demo.example.com)", "'Hi Tolu'; bell with unread count; weekly summary; Cognitive Psychology and Fuzzy Logic 'Needs attention' with reason lines and 'Matched to your preference'; one 'Keep it up'; streak, 14-day strip, progress chart (FR1, FR4, FR6)"),
    Shot("16-why-this.png", "'Why this?' panel", "Tolu Adeyemi", "Logistic Regression and Random Forest probabilities, their average, and the factors that raise risk (FR4)"),
    Shot("17-progress-csc574.png", "Progress chart, CSC 574 picked in the course dropdown", "Tolu Adeyemi", "Fuzzy Logic Systems bar in red below the 50% line; names on two lines (FR6)"),
    Shot("18-phone-dashboard.png", "Dashboard on a phone (390 px)", "Tolu Adeyemi", "One column; menu button and bell stay in the header (NFR1)"),
    Shot("19-phone-quiz.png", "Quiz on a phone (390 px)", "Tolu Adeyemi", "Question and options fit the screen, Back/Next reachable (NFR1)"),
]

# Not taken by this script; captured from files or the terminal.
OTHER = [
    ("ml/results/model_comparison_simulated_data.png", "Rule baseline vs LR vs RF on four metrics (simulated data)", "FR4"),
    ("ml/results/confusion_rule_baseline_simulated_data.png", "Rule baseline confusion matrix (simulated data)", "FR4"),
    ("ml/results/confusion_logistic_regression_simulated_data.png", "LR confusion matrix (simulated data)", "FR4"),
    ("ml/results/confusion_random_forest_simulated_data.png", "RF confusion matrix (simulated data)", "FR4"),
    ("ml/results/feature_weights_simulated_data.png", "LR coefficients and RF importances (simulated data)", "FR4"),
    ("ml/results/metrics_simulated_data.md", "Three-row metrics table (simulated data)", "FR4"),
    ("ml/results/simulation_rules.md", "How the simulated students were generated", "FR4"),
    ("terminal: python scripts/rls_check.py", "Output ending '46/46 checks passed'", "NFR3"),
    ("docs/results/performance.md", "Response-time table (20 runs each)", "NFR2"),
    ("docs/results/security.md", "Row-level security check, 46 checks", "NFR3"),
    ("docs/results/courses.md", "Every course in the knowledge base, with files used and skipped", "NFR5"),
    ("ml/results/summary.md", "Results in plain words, for Chapter Four (simulated data)", "FR4"),
    ("Supabase dashboard: Authentication → Policies (taken by hand)", "RLS enabled on every table, with its policies", "NFR3"),
]


def save(page: Page, name: str, full_page: bool = False) -> None:
    page.wait_for_timeout(250)
    page.screenshot(path=str(SHOTS / name), full_page=full_page)
    print(f"  saved {name}")


def sign_in(page: Page, email: str, password: str) -> None:
    page.goto(f"{APP}/login")
    page.get_by_label("Email").fill(email)
    page.get_by_label("Password").fill(password)
    page.get_by_role("button", name="Sign in").click()
    page.wait_for_url(lambda url: "/login" not in url)
    page.wait_for_load_state("networkidle")


def refresh_recommendations(page: Page) -> None:
    with page.expect_response(lambda r: "/recommend" in r.url and r.request.method == "POST", timeout=30_000):
        page.get_by_role("button", name="Refresh").click()
    page.wait_for_load_state("networkidle")
    expect(page.get_by_role("button", name="Refresh")).to_be_enabled()


def new_student_flow(browser, email: str) -> None:
    page = browser.new_page(viewport=LAPTOP)
    page.set_default_timeout(20_000)
    page.goto(f"{APP}/signup")
    save(page, "01-signup.png")
    page.goto(f"{APP}/login")
    save(page, "02-login.png")

    page.goto(f"{APP}/signup")
    page.get_by_label("Full name").fill("Demo Student")
    page.get_by_label("Email").fill(email)
    page.get_by_label("Password").fill(testkit.PASSWORD)
    page.get_by_role("button", name="Create account").click()
    page.wait_for_url(f"{APP}/onboarding")
    page.get_by_role("button", name="Reading notes").click()
    page.get_by_role("button", name="Practising questions").click()
    save(page, "03-onboarding.png")
    page.get_by_role("button", name="Continue").click()
    page.wait_for_url(f"{APP}/")

    page.goto(f"{APP}/courses")
    expect(page.get_by_text("CSC 574")).to_be_visible()
    save(page, "04-courses.png")
    page.get_by_role("link", name="Take diagnostic quiz").first.click()
    expect(page.get_by_role("button", name="Start quiz")).to_be_visible()
    save(page, "05-quiz-intro.png")
    page.get_by_role("button", name="Start quiz").click()

    wanted = {"Single choice": "06-quiz-single-choice.png", "True or false": "07-quiz-true-false.png",
              "Multiple answers": "08-quiz-multi-select.png", "Odd one out": "09-quiz-odd-one-out.png"}
    for i in range(18):
        label = page.locator("p.uppercase").first.inner_text().strip().capitalize()
        boxes = page.get_by_role("checkbox")
        if boxes.count():
            boxes.nth(0).click()
            boxes.nth(1).click()
        else:
            page.get_by_role("radio").first.click()
        match = next((k for k in wanted if k.lower() == label.lower()), None)
        if match:
            save(page, wanted.pop(match))
        if i < 17:
            page.get_by_role("button", name="Next").click()
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("Score per topic")).to_be_visible()
    save(page, "10-results-summary.png")
    page.get_by_text("Answers", exact=True).scroll_into_view_if_needed()
    page.evaluate("window.scrollBy(0, -80)")
    save(page, "11-results-answers.png")

    page.locator("section").first.locator("div > a").first.click()
    expect(page.get_by_text("Latest score")).to_be_visible()
    save(page, "12-topic.png")

    page.get_by_role("link", name="Log study session").click()
    page.get_by_role("button", name="30 min").click()
    page.get_by_role("button", name="Reading").click()
    page.get_by_role("button", name="Save session").click()
    expect(page.get_by_text("Saved: 30 minutes of reading")).to_be_visible()
    save(page, "13-log-study.png")
    page.close()
    if wanted:
        print(f"  note: no question of format(s) {list(wanted)} in this diagnostic")


def demo_flows(browser) -> None:
    page = browser.new_page(viewport=LAPTOP)
    page.set_default_timeout(20_000)
    sign_in(page, NEW, DEMO_PASSWORD)
    refresh_recommendations(page)
    save(page, "14-dashboard-new.png", full_page=True)
    page.close()

    page = browser.new_page(viewport=LAPTOP)
    page.set_default_timeout(20_000)
    sign_in(page, ACTIVE, DEMO_PASSWORD)
    refresh_recommendations(page)
    save(page, "15-dashboard-active.png", full_page=True)
    first = page.get_by_test_id("recommendation").first
    first.get_by_role("button", name="Why this?").click()
    expect(page.get_by_test_id("why-panel")).to_be_visible()
    first.scroll_into_view_if_needed()
    page.evaluate("window.scrollBy(0, -80)")
    save(page, "16-why-this.png")
    page.get_by_role("combobox", name="Course").select_option(label="CSC 574 · Intelligent Systems")
    page.get_by_test_id("progress-chart").scroll_into_view_if_needed()
    page.evaluate("window.scrollBy(0, 160)")
    save(page, "17-progress-csc574.png")
    page.close()

    page = browser.new_page(viewport=PHONE)
    page.set_default_timeout(20_000)
    sign_in(page, ACTIVE, DEMO_PASSWORD)
    expect(page.get_by_test_id("recommendation").first).to_be_visible()
    save(page, "18-phone-dashboard.png")
    page.goto(f"{APP}/courses")
    page.get_by_role("link", name="View course").first.click()
    page.locator("ol a").nth(4).click()
    page.get_by_role("link", name="Take topic quiz").click()
    page.get_by_role("button", name="Start quiz").click()
    page.get_by_role("radio").first.click() if page.get_by_role("checkbox").count() == 0 else page.get_by_role("checkbox").first.click()
    save(page, "19-phone-quiz.png")
    page.close()


# Taken by `python scripts/phase7_check.py --shots docs/screenshots/phase7`.
PHASE7 = [
    Shot("fr5-01-knowledge-base.png", "Knowledge Base", "Tolu Adeyemi", "Live counts, search box, topics with summaries and subtopics, resources grouped by type (FR5)"),
    Shot("fr5-02-search.png", "Knowledge Base search", "Tolu Adeyemi", "'fuzzy' filters to Fuzzy Logic Systems (FR5)"),
    Shot("fr5-03-study-note.png", "Study note in the resource viewer", "Tolu Adeyemi", "Cognitive Psychology note rendered in the app, ending 'Source: Lecture 6' (FR5)"),
    Shot("fr5-04-past-questions.png", "Past questions in the resource viewer", "Tolu Adeyemi", "Data Gathering past questions grouped by paper, with the data table (FR5)"),
    Shot("fr5-05-topic.png", "Topic page", "Tolu Adeyemi", "Summary, resources grouped by type, quiz and log buttons (FR5)"),
    Shot("fr5-06-phone-knowledge-base.png", "Knowledge Base on a phone (375 px)", "Tolu Adeyemi", "Menu button nav, no sideways scroll (FR5, NFR1)"),
    Shot("fr4-01-why-this.png", "'Why this?' panel", "Tolu Adeyemi", "Both model probabilities, their average, top factors (FR4)"),
    Shot("fr4-02-getting-started.png", "Cold-start items", "Kemi Balogun", "'Getting started', 'Not enough quiz history yet', 'Take a few quizzes so we can personalise this for you' (FR4)"),
    Shot("fr4-03-history.png", "Recommendation history", "Kemi Balogun", "Accepted and dismissed items under History (FR4)"),
    Shot("fr4-04-service-down.png", "ML service unreachable", "Kemi Balogun", "Quiet notice 'Recommendations will update shortly', saved list still shown (FR4, NFR4)"),
    Shot("fr4-05-phone-why-this.png", "'Why this?' on a phone", "Tolu Adeyemi", "Panel fits at 375 px (FR4, NFR1)"),
    Shot("fr6-01-bell.png", "Notifications bell", "Tolu Adeyemi", "Unread count and the list of reminders and feedback with times (FR6)"),
    Shot("fr6-02-notifications-page.png", "Notifications page", "Tolu Adeyemi", "Full list, mark all read, link to reminder settings (FR6)"),
    Shot("fr6-03-weekly-summary.png", "Weekly summary", "Tolu Adeyemi", "Minutes vs last week, topics improved, next focus (FR6)"),
    Shot("fr6-04-progress-chart.png", "Progress chart", "Tolu Adeyemi", "Long topic names on two lines (FR6)"),
    Shot("fr6-05-reminder-settings.png", "Reminder settings", "Tolu Adeyemi", "Study days, time, daily goal, browser notifications, 'saved' (FR6)"),
    Shot("fr6-06-phone-bell.png", "Bell on a phone", "Tolu Adeyemi", "Bell visible beside the menu button, list fits (FR6, NFR1)"),
    Shot("fr1-01-signup.png", "Sign-up form", "New sign-up (Ada Okoro)", "Name, email, password (FR1)"),
    Shot("fr1-02-onboarding.png", "Onboarding", "New sign-up (Ada Okoro)", "The four study preferences, two selected (FR1)"),
    Shot("fr1-03-matched-preference.png", "Matched to preference", "Tolu Adeyemi", "'Hi Tolu', '✓ Matched to your preference: study notes' (FR1)"),
    Shot("fr1-04-profile-before.png", "Profile, before an edit", "Tolu Adeyemi", "Your details and reminder settings (FR1)"),
    Shot("fr1-05-profile-after.png", "Profile, after an edit", "Tolu Adeyemi", "New department and level, 'Profile saved.' (FR1)"),
    Shot("fr1-06-kemi-cold-start.png", "Kemi's dashboard", "Kemi Balogun", "'Hi Kemi' with the introductory list (FR1, NFR4)"),
    Shot("fr1-07-phone-profile.png", "Profile on a phone", "Tolu Adeyemi", "Fits at 375 px (FR1, NFR1)"),
    Shot("fr2-01-results-change.png", "Results: change since last attempt", "Temporary student", "'0% to 20%, up 20 points' under the topic bar (FR2)"),
    Shot("fr2-02-quiz-history.png", "Quiz history", "Tolu Adeyemi", "Date, quiz and score for every CSC 531 attempt (FR2)"),
    Shot("fr3-01-timer.png", "Study timer", "Temporary student", "Timer paused, ready to stop and use the time (FR3)"),
    Shot("fr3-02-logger.png", "Study logger", "Temporary student", "'Custom (minutes)', timer, 'Saved' confirmation (FR3)"),
    Shot("fr3-03-phone-logger.png", "Study logger on a phone", "Tolu Adeyemi", "Fits at 375 px, recent sessions stacked (FR3, NFR1)"),
]


PHASE9 = [
    Shot("p9-01-onboarding-courses.png", "Onboarding with course choice", "New sign-up (Phase Nine Student)", "Every course listed, CSC 531 and CSC 574 ticked, CSC 551 added, sample courses labelled (NFR5)"),
    Shot("p9-02-courses.png", "Course list: my courses and more courses", "New sign-up", "My courses with Remove; More courses grouped by level (500, 400, 200) with 'Sample content, pending lecturer review' and Add to my courses (NFR5)"),
    Shot("p9-03-knowledge-base.png", "Knowledge Base with a sample course", "New sign-up", "CSC 551 section with the sample badge, topics, study notes and past questions (FR5, NFR5)"),
    Shot("p9-03b-knowledge-base-collapsed.png", "Knowledge Base, all courses collapsed", "New sign-up", "One header per course with its topic count and sample badge; Expand all and Collapse all (FR5, NFR5)"),
    Shot("p9-04-study-note.png", "Sample course study note", "New sign-up", "Divide and Conquer note ending 'Source: CSC 551 Design and Analysis of Algorithms.pdf, Study Session 2' (NFR5)"),
    Shot("p9-05-past-questions.png", "Sample course past questions", "New sign-up", "CSC 551 Graphs past questions grouped by paper (2024/25, 2023/24) (NFR5)"),
    Shot("p9-06-topic.png", "Sample course topic page", "New sign-up", "Badge, summary, Take topic quiz (NFR5)"),
    Shot("p9-07-quiz.png", "Sample course topic quiz", "New sign-up", "A CSC 551 question in the quiz player (NFR5)"),
    Shot("p9-08-results.png", "Sample course quiz results", "New sign-up", "Score per topic for the CSC 551 quiz (NFR5)"),
    Shot("p9-09-dashboard.png", "Dashboard with a sample course", "New sign-up", "Getting started items for CSC 531, CSC 551 and CSC 574; CSC 551 diagnostic reminder (FR4, NFR5)"),
    Shot("p9-10-course-page.png", "Course page after removing", "New sign-up", "'Not in your courses yet' with Add to my courses (NFR5)"),
    Shot("p9-11-phone-courses.png", "Course list on a phone (375 px)", "New sign-up", "Fits without sideways scroll (NFR1, NFR5)"),
]


def write_checklist() -> None:
    rows = "\n".join(
        f"| {i} | {s.screen} | {s.account} | {s.visible} | [`{s.file}`](screenshots/{s.file}) |"
        for i, s in enumerate(CHECKLIST, start=1)
    )
    other = "\n".join(f"| {path} | {what} | {req} |" for path, what, req in OTHER)
    (DOCS / "screenshots.md").write_text(
        "# Screenshot checklist\n\n"
        "In capture order. All app screenshots are taken by `python scripts/capture_screenshots.py` "
        "(laptop 1280 px wide unless stated) and saved in `docs/screenshots/`. Before capturing by hand, reset the "
        "demo accounts with `python scripts/seed_demo.py --demo-only`.\n\n"
        "Demo logins (password `DemoPass2026!`): New Student `new.student@demo.example.com`, "
        "Active Student `active.student@demo.example.com`.\n\n"
        "| # | Screen | Account | What should be visible | File |\n| --- | --- | --- | --- | --- |\n"
        f"{rows}\n\n"
        "## Requirement screens (Phase 7)\n\n"
        "Taken by `python scripts/phase7_check.py --shots docs/screenshots/phase7` (laptop 1280 px unless stated). "
        "Run `python scripts/seed_demo.py --demo-only` first.\n\n"
        "| # | Screen | Account | What should be visible | File |\n| --- | --- | --- | --- | --- |\n"
        + "\n".join(f"| {i} | {s.screen} | {s.account} | {s.visible} | [`{s.file}`](screenshots/phase7/{s.file}) |"
                     for i, s in enumerate(PHASE7, start=len(CHECKLIST) + 1))
        + "\n\n"
        "## Course ingestion pipeline (Phase 9)\n\n"
        "Taken by `python scripts/phase9_check.py --shots docs/screenshots/phase9` with a temporary student, "
        "which is deleted afterwards.\n\n"
        "| # | Screen | Account | What should be visible | File |\n| --- | --- | --- | --- | --- |\n"
        + "\n".join(f"| {i} | {s.screen} | {s.account} | {s.visible} | [`{s.file}`](screenshots/phase9/{s.file}) |"
                     for i, s in enumerate(PHASE9, start=len(CHECKLIST) + len(PHASE7) + 1))
        + "\n\n"
        "## Figures from files and the terminal\n\n"
        "| Source | What | Requirement |\n| --- | --- | --- |\n"
        f"{other}\n\n"
        "Charts and tables from `ml/results/` come from simulated students; keep \"simulated data\" in every caption.\n"
    )


def main() -> int:
    SHOTS.mkdir(parents=True, exist_ok=True)
    db = testkit.admin()
    email = f"screens-{int(time.time())}@{testkit.EMAIL_DOMAIN}"
    active_id = next(u.id for u in db.auth.admin.list_users(page=1, per_page=1000) if u.email == ACTIVE)
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(channel="chrome", headless=True)
            print("-- New sign-up")
            new_student_flow(browser, email)
            print("-- Demo accounts")
            demo_flows(browser)
            browser.close()
    finally:
        uid = next((u.id for u in db.auth.admin.list_users(page=1, per_page=1000) if u.email == email), None)
        if uid:
            db.auth.admin.delete_user(uid)
        # Leave the demo accounts as they were: undo the Accept, and drop the
        # phone quiz attempt that was started but never submitted.
        db.table("recommendations").update({"status": "pending"}).eq("student_id", active_id).execute()
        db.table("quiz_attempts").delete().eq("student_id", active_id).is_("completed_at", "null").execute()

    write_checklist()
    missing = [s.file for s in CHECKLIST if not (SHOTS / s.file).exists()]
    missing7 = [s.file for s in PHASE7 if not (SHOTS / "phase7" / s.file).exists()]
    print(f"\n{len(CHECKLIST) - len(missing)}/{len(CHECKLIST)} screens captured" + (f"; missing {missing}" if missing else ""))
    print(f"{len(PHASE7) - len(missing7)}/{len(PHASE7)} Phase 7 screens present" + (f"; missing {missing7}" if missing7 else ""))
    missing += missing7
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
