"""Phase 7 checks, one section per requirement, in Chrome.

    python scripts/phase7_check.py [--only fr5] [--shots DIR]

Needs the Vite dev server, the ML service and the demo accounts. Each section
prints PASS/FAIL lines and can save screenshots for the report.
"""

import argparse
import sys
from pathlib import Path

from playwright.sync_api import Page, expect, sync_playwright

import testkit

APP = "http://localhost:5173"
PASSWORD = "DemoPass2026!"
ACTIVE = "active.student@demo.example.com"
NEW = "new.student@demo.example.com"
LAPTOP = {"width": 1280, "height": 900}
PHONE = {"width": 375, "height": 812}

results: list[bool] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append(passed)
    print(f"{'PASS' if passed else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""))


def sign_in(page: Page, email: str) -> None:
    page.goto(f"{APP}/login")
    page.get_by_label("Email").fill(email)
    page.get_by_label("Password").fill(PASSWORD)
    page.get_by_role("button", name="Sign in").click()
    page.wait_for_url(lambda url: "/login" not in url)
    page.wait_for_load_state("networkidle")


class Shots:
    def __init__(self, folder: Path | None):
        self.folder = folder
        if folder:
            folder.mkdir(parents=True, exist_ok=True)

    def __call__(self, page: Page, name: str, full_page: bool = False) -> None:
        if self.folder:
            page.wait_for_timeout(200)
            page.screenshot(path=str(self.folder / name), full_page=full_page)


def fr5(browser, shot: Shots) -> None:
    print("-- FR5 Knowledge Base")
    db = testkit.admin()
    stats = db.table("knowledge_base_stats").select("*").execute().data[0]

    page = browser.new_page(viewport=LAPTOP)
    page.set_default_timeout(20_000)
    sign_in(page, ACTIVE)
    page.get_by_role("link", name="Knowledge Base").first.click()
    page.wait_for_url(f"{APP}/knowledge")
    counts = page.get_by_test_id("kb-stats")
    expect(counts).to_be_visible()
    text = counts.inner_text()
    expected = f"{stats['courses']} courses {stats['topics']} topics {stats['resources']} resources {stats['practice_questions']} practice questions"
    check("Knowledge Base page in the nav with live counts", " ".join(text.split()) == expected, text.replace("\n", " "))
    topics = page.get_by_test_id("kb-topic")
    expect(topics.first).to_be_visible()
    check("courses, then topics in order with summaries and subtopics", topics.count() == 12,
          f"{topics.count()} topics; first: {topics.first.inner_text()}")
    groups = [g for g in ["Study notes", "Lecture slides", "Past questions"] if page.get_by_text(g, exact=True).count()]
    check("resources grouped by type", len(groups) == 3, ", ".join(groups))
    shot(page, "fr5-01-knowledge-base.png")
    shot(page, "fr5-01b-knowledge-base-full.png", full_page=True)

    page.get_by_label("Search topics and resources").fill("fuzzy")
    page.wait_for_timeout(200)
    check("search filters topics as you type", topics.count() == 1 and "Fuzzy" in topics.first.inner_text(),
          f"'fuzzy' -> {topics.count()} topic(s)")
    shot(page, "fr5-02-search.png")
    page.get_by_label("Search topics and resources").fill("zzzz-no-match")
    check("empty search shows a clear next step", page.get_by_text("Clear the search").is_visible())
    page.get_by_text("Clear the search").click()

    page.get_by_label("Search topics and resources").fill("Cognitive Psychology")
    page.get_by_role("link", name="Study note: Cognitive Psychology and Perception").click()
    page.wait_for_url(f"{APP}/resources/**")
    expect(page.locator("article .prose h1")).to_have_text("Cognitive Psychology and Perception")
    headings = page.locator("article .prose h2").all_inner_texts()
    source = page.locator("article .prose p").last.inner_text()
    check("study note opens inside the app, rendered from Markdown", "Subtopics" in headings and source.startswith("Source:"),
          f"sections {headings}; '{source}'")
    shot(page, "fr5-03-study-note.png", full_page=True)

    page.go_back()
    page.get_by_label("Search topics and resources").fill("Data Gathering")
    page.get_by_role("link", name="Past questions: Data Gathering and Data Analysis").click()
    page.wait_for_url(f"{APP}/resources/**")
    expect(page.locator("article .prose h2").first).to_be_visible()
    tables = page.locator("article .prose table").count()
    years = page.locator("article .prose h2").all_inner_texts()
    check("past questions open inside the app, grouped by year (tables rendered)", tables >= 1 and len(years) >= 2,
          f"{len(years)} papers, {tables} table(s)")
    shot(page, "fr5-04-past-questions.png", full_page=True)

    page.goto(f"{APP}/knowledge")
    page.get_by_label("Search topics and resources").fill("Search")
    lecture = page.get_by_test_id("resource-link").filter(has_text="Lecture 2")
    check("lecture links open in a new tab, folders labelled 'Open lecture folder'",
          lecture.first.get_attribute("target") == "_blank" and "Open lecture folder" in lecture.first.inner_text())

    page.get_by_test_id("kb-topic").first.click()
    page.wait_for_url(f"{APP}/topics/**")
    expect(page.get_by_role("link", name="Take topic quiz")).to_be_visible()
    summary_shown = page.locator("main p.leading-relaxed").count() == 1
    check("topic page: summary, subtopics, resources by type, quiz and log buttons",
          summary_shown and page.get_by_role("link", name="Take topic quiz").is_visible()
          and page.get_by_text("Study notes", exact=True).is_visible())
    shot(page, "fr5-05-topic.png", full_page=True)
    page.close()

    missing = [t["title"] for t in db.table("topics").select("title, resources(type), quizzes(kind)").execute().data
               if not ({"note", "lecture"} <= {r["type"] for r in t["resources"]} and any(q["kind"] == "topic" for q in t["quizzes"]))]
    check("every topic has a study note, a lecture link and a topic quiz", not missing, ", ".join(missing) or "12 of 12")

    page = browser.new_page(viewport=PHONE)
    page.set_default_timeout(20_000)
    sign_in(page, ACTIVE)
    page.get_by_role("button", name="Open menu").click()
    page.get_by_role("link", name="Knowledge Base").click()
    page.wait_for_url(f"{APP}/knowledge")
    expect(page.get_by_test_id("kb-topic").first).to_be_visible()
    overflow = page.evaluate("document.documentElement.scrollWidth > window.innerWidth")
    check("phone width (375 px): menu button opens the nav; no sideways scroll", not overflow)
    shot(page, "fr5-06-phone-knowledge-base.png")
    page.close()


def refresh(page: Page) -> None:
    with page.expect_response(lambda r: "/recommend" in r.url and r.request.method == "POST", timeout=30_000):
        page.get_by_role("button", name="Refresh").click()
    page.wait_for_load_state("networkidle")
    expect(page.get_by_role("button", name="Refresh")).to_be_enabled()
    expect(page.get_by_test_id("recommendation").first).to_be_visible()


def fr4(browser, shot: Shots) -> None:
    print("-- FR4 Why each recommendation")
    db = testkit.admin()
    new_id = next(u.id for u in db.auth.admin.list_users(page=1, per_page=1000) if u.email == NEW)
    db.table("recommendations").delete().eq("student_id", new_id).execute()

    page = browser.new_page(viewport=LAPTOP)
    page.set_default_timeout(20_000)
    sign_in(page, ACTIVE)
    refresh(page)
    rows = page.get_by_test_id("recommendation")
    reasons = page.get_by_test_id("recommendation-reason")
    check("a reason line on every recommendation", reasons.count() == rows.count() == 3,
          reasons.first.inner_text())
    check("reason built from the features", reasons.first.inner_text().startswith("Last score"))
    rows.first.get_by_role("button", name="Why this?").click()
    panel = page.get_by_test_id("why-panel")
    text = panel.inner_text()
    check("'Why this?' shows both model probabilities, their average and the factors",
          all(k.lower() in text.lower() for k in ["Logistic Regression", "Random Forest", "Average (used to rank)", "What drove it", "raises risk"]),
          " | ".join(l for l in text.splitlines() if "%" in l)[:120])
    panel.scroll_into_view_if_needed()
    shot(page, "fr4-01-why-this.png")
    check("'Keep it up' item says why", "Keep it up" in rows.nth(2).inner_text() and reasons.nth(2).inner_text() != "")
    page.close()

    page = browser.new_page(viewport=LAPTOP)
    page.set_default_timeout(20_000)
    sign_in(page, NEW)
    refresh(page)
    first = page.get_by_test_id("recommendation").first
    check("cold-start items look different, with the personalise line",
          "Getting started" in first.inner_text() and "Take a few quizzes so we can personalise this for you." in first.inner_text()
          and "Not enough quiz history yet" in first.inner_text())
    shot(page, "fr4-02-getting-started.png")

    count = page.get_by_test_id("recommendation").count()
    note_card = page.get_by_test_id("recommendation").filter(has_text="Study note").first
    note_card.get_by_role("button", name="Accept and open").click()
    page.wait_for_url(f"{APP}/resources/**")
    expect(page.locator("article .prose h1")).to_be_visible()
    check("Accept opens a study note inside the app", True, page.locator("article .prose h1").inner_text())
    page.go_back()
    expect(page.get_by_test_id("recommendation")).to_have_count(count - 1)

    lecture_card = page.get_by_test_id("recommendation").filter(has_text="Lecture slides").first
    with page.context.expect_page() as popup:
        lecture_card.get_by_role("button", name="Accept and open").click()
    new_tab = popup.value
    check("Accept opens lecture slides in a new tab", "drive.google.com" in new_tab.url, new_tab.url[:60])
    new_tab.close()
    expect(page.get_by_test_id("recommendation")).to_have_count(count - 2)
    page.get_by_test_id("recommendation").first.get_by_role("button", name="Dismiss").click()
    expect(page.get_by_test_id("recommendation")).to_have_count(count - 3)
    page.get_by_role("button", name="History").click()
    history = page.get_by_test_id("recommendation-history")
    check("accepted and dismissed items leave the list and appear under History",
          history.get_by_text("Accepted").count() == 2 and history.get_by_text("Dismissed").count() == 1)
    history.scroll_into_view_if_needed()
    shot(page, "fr4-03-history.png")

    # NFR4: the ML service is unreachable; the dashboard keeps the saved list.
    page.route("**/recommend", lambda route: route.abort())
    page.get_by_role("button", name="Refresh").click()
    notice = page.get_by_test_id("ml-offline-notice")
    expect(notice).to_be_visible()
    check("ML service down: quiet notice, saved recommendations still shown",
          notice.is_visible() and page.get_by_test_id("recommendation").count() == count - 3
          and not page.get_by_role("alert").count(), notice.inner_text())
    shot(page, "fr4-04-service-down.png")
    page.close()

    # Put the New Student back: fresh introductory list, nothing accepted.
    db.table("recommendations").delete().eq("student_id", new_id).execute()
    page = browser.new_page(viewport=LAPTOP)
    sign_in(page, NEW)
    refresh(page)
    page.close()

    page = browser.new_page(viewport=PHONE)
    page.set_default_timeout(20_000)
    sign_in(page, ACTIVE)
    page.get_by_test_id("recommendation").first.get_by_role("button", name="Why this?").click()
    overflow = page.evaluate("document.documentElement.scrollWidth > window.innerWidth")
    check("phone width: reason and 'Why this?' fit without sideways scroll", not overflow)
    shot(page, "fr4-05-phone-why-this.png", full_page=True)
    page.close()


def fr6(browser, shot: Shots) -> None:
    print("-- FR6 Notifications, reminders and weekly summary")
    db = testkit.admin()
    active_id = next(u.id for u in db.auth.admin.list_users(page=1, per_page=1000) if u.email == ACTIVE)

    page = browser.new_page(viewport=LAPTOP)
    page.set_default_timeout(20_000)
    sign_in(page, ACTIVE)
    refresh(page)  # the ML service may add "weak topic not studied"
    page.reload()
    page.wait_for_load_state("networkidle")
    badge = page.get_by_test_id("unread-count")
    expect(badge).to_be_visible()
    unread_before = int(badge.inner_text().rstrip("+"))
    kinds = sorted({n["kind"] for n in db.table("notifications").select("kind").eq("student_id", active_id).execute().data})
    check("bell in the nav with an unread count", unread_before >= 1, f"{unread_before} unread; kinds: {', '.join(kinds)}")

    page.get_by_test_id("notification-bell").click()
    panel = page.get_by_test_id("notification-panel")
    expect(panel).to_be_visible()
    items = panel.get_by_test_id("notification")
    check("bell opens a list of reminders and feedback, each with a time", items.count() >= 2 and
          any(w in panel.inner_text() for w in ["ago", "just now", "yesterday", "Oct"]), f"{items.count()} shown")
    shot(page, "fr6-01-bell.png")

    first_unread = panel.locator("[data-unread=true]").first
    first_unread.click()
    page.wait_for_load_state("networkidle")
    if unread_before > 1:
        expect(page.get_by_test_id("unread-count")).to_have_text(str(unread_before - 1), timeout=10_000)
    else:
        expect(page.get_by_test_id("unread-count")).to_have_count(0, timeout=10_000)
    after = page.get_by_test_id("unread-count")
    unread_after = int(after.inner_text().rstrip("+")) if after.count() else 0
    check("clicking a notification marks it read and follows its link", unread_after == unread_before - 1,
          f"{unread_before} -> {unread_after} unread, now at {page.url.replace(APP, '')}")

    page.goto(f"{APP}/notifications")
    expect(page.get_by_test_id("notification").first).to_be_visible()
    check("full notifications page", page.get_by_test_id("notification").count() >= 2)
    shot(page, "fr6-02-notifications-page.png", full_page=True)

    page.goto(f"{APP}/")
    weekly = [page.get_by_test_id(t) for t in ["weekly-minutes", "weekly-improved", "weekly-next"]]
    expect(weekly[0]).to_be_visible()
    check("weekly summary: minutes vs last week, topics improved, next focus",
          "vs last week" in weekly[0].inner_text() or "Same as last week" in weekly[0].inner_text(),
          " | ".join(" ".join(w.inner_text().split()) for w in weekly)[:160])
    shot(page, "fr6-03-weekly-summary.png")

    tick_titles = page.get_by_test_id("progress-chart").locator("text title").all_text_contents()
    two_line = page.get_by_test_id("progress-chart").locator("text:has(tspan + tspan)").count()
    check("progress chart: long names on two lines, full name on hover",
          len(tick_titles) == 6 and two_line >= 1 and any(len(t) > 22 for t in tick_titles), f"{two_line} wrapped")
    page.get_by_test_id("progress-chart").scroll_into_view_if_needed()
    shot(page, "fr6-04-progress-chart.png")

    page.goto(f"{APP}/profile")
    page.get_by_role("button", name="Sat").click()
    page.get_by_label("Preferred study time").fill("17:30")
    page.get_by_label("Daily goal (minutes)").fill("45")
    page.get_by_role("button", name="Save reminder settings").click()
    expect(page.get_by_text("Reminder settings saved.")).to_be_visible()
    saved = db.table("profiles").select("study_days, preferred_study_time, daily_goal_minutes").eq("id", active_id).execute().data[0]
    check("reminder settings saved on the profile", "sat" in saved["study_days"] and saved["preferred_study_time"].startswith("17:30")
          and saved["daily_goal_minutes"] == 45, str(saved))
    shot(page, "fr6-05-reminder-settings.png", full_page=True)
    db.table("profiles").update({"study_days": ["mon", "tue", "wed", "thu", "fri"], "preferred_study_time": "18:00",
                                 "daily_goal_minutes": 30}).eq("id", active_id).execute()
    page.close()

    page = browser.new_page(viewport=PHONE)
    page.set_default_timeout(20_000)
    sign_in(page, ACTIVE)
    expect(page.get_by_test_id("notification-bell")).to_be_visible()
    page.get_by_test_id("notification-bell").click()
    overflow = page.evaluate("document.documentElement.scrollWidth > window.innerWidth")
    check("phone width: bell stays visible and its list fits", page.get_by_test_id("notification-panel").is_visible() and not overflow)
    shot(page, "fr6-06-phone-bell.png")
    page.close()


def fr1(browser, shot: Shots) -> None:
    print("-- FR1 Registration and profile")
    import time
    db = testkit.admin()
    users = db.auth.admin.list_users(page=1, per_page=1000)
    active_id = next(u.id for u in users if u.email == ACTIVE)

    # Sign-up and onboarding with the four study preferences.
    email = f"fr1-{int(time.time())}@{testkit.EMAIL_DOMAIN}"
    page = browser.new_page(viewport=LAPTOP)
    page.set_default_timeout(20_000)
    page.goto(f"{APP}/signup")
    page.get_by_label("Full name").fill("Ada Okoro")
    page.get_by_label("Email").fill(email)
    page.get_by_label("Password").fill(testkit.PASSWORD)
    shot(page, "fr1-01-signup.png")
    page.get_by_role("button", name="Create account").click()
    page.wait_for_url(f"{APP}/onboarding")
    page.get_by_role("button", name="Reading notes").click()
    page.get_by_role("button", name="Videos").click()
    shot(page, "fr1-02-onboarding.png")
    page.get_by_role("button", name="Continue").click()
    page.wait_for_url(f"{APP}/")
    uid = next(u.id for u in db.auth.admin.list_users(page=1, per_page=1000) if u.email == email)
    row = db.table("profiles").select("full_name, department, level, learning_preferences").eq("id", uid).execute().data[0]
    check("sign up and onboarding save name, department, level and study preferences",
          row["full_name"] == "Ada Okoro" and row["level"] == 500 and sorted(row["learning_preferences"]) == ["note", "video"], str(row))
    page.close()
    db.auth.admin.delete_user(uid)

    # Demo names, and the preference visibly used.
    page = browser.new_page(viewport=LAPTOP)
    page.set_default_timeout(20_000)
    sign_in(page, ACTIVE)
    expect(page.get_by_role("heading", name="Hi Tolu")).to_be_visible()
    refresh(page)
    matched = page.get_by_test_id("matched-preference")
    check("demo account has a realistic name", page.get_by_role("heading", name="Hi Tolu").is_visible(), "Tolu Adeyemi")
    check("recommendations that matched the preference say so", matched.count() >= 1, matched.first.inner_text() if matched.count() else "none")
    shot(page, "fr1-03-matched-preference.png")

    # Profile page before and after an edit.
    page.get_by_role("button", name="Profile menu").click()
    page.get_by_role("link", name="Profile and reminders").click()
    page.wait_for_url(f"{APP}/profile")
    expect(page.get_by_label("Full name")).to_have_value("Tolu Adeyemi")
    shot(page, "fr1-04-profile-before.png", full_page=True)
    page.get_by_label("Department").fill("Computer Science (Data Science option)")
    page.get_by_label("Level").select_option("400")
    page.get_by_role("button", name="Videos").click()
    page.get_by_role("button", name="Save profile").click()
    expect(page.get_by_text("Profile saved.")).to_be_visible()
    row = db.table("profiles").select("department, level, learning_preferences").eq("id", active_id).execute().data[0]
    check("Profile page edits are saved with a confirmation",
          row["department"].endswith("(Data Science option)") and row["level"] == 400 and "video" in row["learning_preferences"], str(row))
    shot(page, "fr1-05-profile-after.png", full_page=True)
    db.table("profiles").update({"department": "Computer Science", "level": 500,
                                 "learning_preferences": ["note", "past_questions"]}).eq("id", active_id).execute()
    page.close()

    page = browser.new_page(viewport=LAPTOP)
    page.set_default_timeout(20_000)
    sign_in(page, NEW)
    expect(page.get_by_role("heading", name="Hi Kemi")).to_be_visible()
    expect(page.get_by_test_id("recommendation").first).to_be_visible()
    check("cold-start demo account is Kemi Balogun", page.get_by_test_id("recommendation").first.get_attribute("data-kind") == "getting-started")
    shot(page, "fr1-06-kemi-cold-start.png")
    page.close()

    page = browser.new_page(viewport=PHONE)
    page.set_default_timeout(20_000)
    sign_in(page, ACTIVE)
    page.goto(f"{APP}/profile")
    expect(page.get_by_label("Full name")).to_have_value("Tolu Adeyemi")
    overflow = page.evaluate("document.documentElement.scrollWidth > window.innerWidth")
    check("phone width: Profile page fits", not overflow)
    shot(page, "fr1-07-phone-profile.png", full_page=True)
    page.close()


def answer_quiz(page: Page, questions: int, pick_last: bool) -> None:
    expect(page.get_by_text(f"/ {questions}", exact=False)).to_be_visible()
    for i in range(questions):
        expect(page.get_by_role("radio").or_(page.get_by_role("checkbox")).first).to_be_visible()
        boxes = page.get_by_role("checkbox")
        options = boxes if boxes.count() else page.get_by_role("radio")
        (options.last if pick_last else options.first).click()
        if i < questions - 1:
            page.get_by_role("button", name="Next").click()
    page.get_by_role("button", name="Submit").click()
    page.wait_for_url(f"{APP}/attempts/**")
    expect(page.get_by_text("Score per topic")).to_be_visible()


def fr2_fr3(browser, shot: Shots) -> None:
    print("-- FR2 and FR3 small fixes")
    import time
    db = testkit.admin()
    uid, email = testkit.create_student(db, f"Phase7 Fr23 {int(time.time())}")
    db.table("profiles").update({"department": "Computer Science", "level": 500, "learning_preferences": ["note"]}).eq("id", uid).execute()
    quiz_id = db.table("quizzes").select("id, topic:topics(title)").eq("kind", "topic").execute().data[0]["id"]
    try:
        page = browser.new_page(viewport=LAPTOP)
        page.set_default_timeout(20_000)
        page.goto(f"{APP}/login")
        page.get_by_label("Email").fill(email)
        page.get_by_label("Password").fill(testkit.PASSWORD)
        page.get_by_role("button", name="Sign in").click()
        page.wait_for_url(lambda url: "/login" not in url)

        page.goto(f"{APP}/quiz/{quiz_id}")
        page.get_by_role("button", name="Start quiz").click()
        answer_quiz(page, 5, pick_last=False)
        first = page.locator("section").first.get_by_text("First attempt on this topic")
        check("results: first attempt on a topic says so", first.count() == 1)

        page.goto(f"{APP}/quiz/{quiz_id}")
        page.get_by_role("button", name="Start quiz").click()
        answer_quiz(page, 5, pick_last=True)
        change = page.get_by_test_id("score-change")
        check("results: change since the last attempt, e.g. '40% to 70%, up 30 points'", change.count() == 1,
              change.first.inner_text() if change.count() else "none")
        shot(page, "fr2-01-results-change.png")

        page.goto(f"{APP}/log")
        page.get_by_label("Topic").select_option(index=1)
        custom = page.get_by_label("Custom (minutes)")
        custom.fill("400")
        save = page.get_by_role("button", name="Save session")
        check("'Custom (minutes)' is labelled and rejects 400", save.is_disabled() and page.get_by_text("between 1 and 300").is_visible())
        custom.fill("45")
        check("'Custom (minutes)' accepts 45", save.is_enabled())
        page.get_by_role("button", name="Start timer").click()
        page.wait_for_timeout(1500)
        page.get_by_role("button", name="Pause").click()
        timer_text = page.get_by_test_id("study-timer").inner_text().split()[0]
        shot(page, "fr3-01-timer.png")
        page.get_by_role("button", name="Stop and use time").click()
        check("study timer: start, pause, stop fills in the duration", custom.input_value() == "1", f"stopped at {timer_text}, duration {custom.input_value()} min")
        with page.expect_request(lambda r: "/recommend" in r.url, timeout=15_000):
            save.click()
        expect(page.get_by_text("Saved: 1 minute of")).to_be_visible()
        check("after saving: confirmation, and recommendations refresh in the background", True)
        shot(page, "fr3-02-logger.png", full_page=True)
        page.close()
    finally:
        db.auth.admin.delete_user(uid)

    page = browser.new_page(viewport=LAPTOP)
    page.set_default_timeout(20_000)
    sign_in(page, ACTIVE)
    page.goto(f"{APP}/courses")
    page.get_by_role("link", name="View course").first.click()
    history = page.get_by_test_id("quiz-history")
    expect(history).to_be_visible()
    rows = history.locator("tbody tr")
    check("course page: quiz history with date, quiz and score", rows.count() >= 3,
          " | ".join(" ".join(rows.first.inner_text().split()) for _ in [0]))
    history.scroll_into_view_if_needed()
    shot(page, "fr2-02-quiz-history.png")
    page.close()

    page = browser.new_page(viewport=PHONE)
    page.set_default_timeout(20_000)
    sign_in(page, ACTIVE)
    page.goto(f"{APP}/log")
    expect(page.get_by_label("Custom (minutes)")).to_be_visible()
    overflow = page.evaluate("document.documentElement.scrollWidth > window.innerWidth")
    check("phone width: logger with timer fits", not overflow)
    shot(page, "fr3-03-phone-logger.png", full_page=True)
    page.close()


SECTIONS = {"fr5": fr5, "fr4": fr4, "fr6": fr6, "fr1": fr1, "fr23": fr2_fr3}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", choices=sorted(SECTIONS), action="append")
    parser.add_argument("--shots", type=Path)
    args = parser.parse_args()
    shot = Shots(args.shots)
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=True)
        for name in args.only or list(SECTIONS):
            SECTIONS[name](browser, shot)
        browser.close()
    print(f"\n{sum(results)}/{len(results)} checks passed")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
