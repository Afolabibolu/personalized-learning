"""Phase 5 check: the dashboard for both demo accounts, in Chrome.

Active Student: streak, 14-day activity strip, weakest topic first, a reminder,
the progress chart and "Keep it up" suggestions. New Student: the introductory
"Getting started" list. Also presses Accept and Dismiss and confirms the status
changed in the database, then puts the demo data back as it was.

Needs the Vite dev server, the ML service, seed_demo.py and training.train.

    python scripts/phase5_check.py [--shots DIR] [--mobile]
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
WEAK = {"Cognitive Psychology and Perception", "Fuzzy Logic Systems"}
# Cold start per course: topic 1's note and lecture, then topic 2's note.
INTRO_TOPICS = {
    "HCI, Interactive Systems and Usability", "Understanding the Problem Space and User-Centred Design",
    "Introduction to Intelligent Systems and Agents", "Problem Solving and Search",
}

results: list[bool] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append(passed)
    print(f"{'PASS' if passed else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""))


def sign_in_and_refresh(page: Page, email: str) -> None:
    page.goto(f"{APP}/login")
    page.get_by_label("Email").fill(email)
    page.get_by_label("Password").fill(PASSWORD)
    page.get_by_role("button", name="Sign in").click()
    page.wait_for_url(f"{APP}/")
    expect(page.get_by_role("heading", name="Recommended for you")).to_be_visible()
    # Wait for the ML service and for the list to reload before reading it.
    with page.expect_response(lambda r: "/recommend" in r.url and r.request.method == "POST", timeout=30_000):
        page.get_by_role("button", name="Refresh").click()
    page.wait_for_load_state("networkidle")
    expect(page.get_by_role("button", name="Refresh")).to_be_enabled()
    expect(page.get_by_test_id("recommendation").first).to_be_visible()


def recs(page: Page) -> list[dict]:
    rows = page.get_by_test_id("recommendation")
    return [
        {
            "kind": rows.nth(i).get_attribute("data-kind"),
            "topic": rows.nth(i).get_by_test_id("recommendation-topic").inner_text(),
            "text": rows.nth(i).inner_text(),
        }
        for i in range(rows.count())
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--shots", type=Path)
    parser.add_argument("--mobile", action="store_true")
    args = parser.parse_args()
    if args.shots:
        args.shots.mkdir(parents=True, exist_ok=True)

    db = testkit.admin()
    # Start the New Student from a clean slate, whatever earlier runs left behind.
    new_id = next(u.id for u in db.auth.admin.list_users(page=1, per_page=1000) if u.email == NEW)
    db.table("recommendations").delete().eq("student_id", new_id).execute()
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=True)
        viewport = {"width": 390, "height": 844} if args.mobile else {"width": 1280, "height": 900}

        print("-- Active Student")
        page = browser.new_page(viewport=viewport)
        page.set_default_timeout(20_000)
        sign_in_and_refresh(page, ACTIVE)
        streak = int(page.get_by_test_id("streak").inner_text())
        check("dashboard shows a streak", streak >= 1, f"{streak}-day streak")
        strip = page.get_by_test_id("activity-strip").locator("li")
        active_days = page.get_by_test_id("activity-strip").locator("[data-active=true]").count()
        check("14-day activity strip", strip.count() == 14, f"{active_days} active days")
        rows = recs(page)
        check("weakest topic is first", rows[0]["topic"] in WEAK and rows[0]["kind"] == "attention",
              f"#1 {rows[0]['topic']} ({rows[0]['kind']})")
        attention = [r["topic"] for r in rows if r["kind"] == "attention"]
        check("both weak topics flagged 'Needs attention', and nothing else", set(attention) == WEAK, ", ".join(attention))
        keep = [r for r in rows if r["kind"] == "keep-it-up"]
        check("only the top 3 overall are shown", len(rows) == 3, f"{len(rows)} recommendations")
        reason = page.get_by_test_id("recommendation").nth(2).get_by_test_id("recommendation-reason")
        check("the third says 'Keep it up' with a suggestion",
              len(keep) == 1 and "Keep it up" in keep[0]["text"] and reason.count() == 1,
              reason.inner_text() if reason.count() else "none")
        reminders = page.get_by_test_id("reminder")
        check("at least one reminder", reminders.count() >= 1,
              reminders.first.inner_text().split("\n")[0] if reminders.count() else "none")
        bars = page.get_by_test_id("progress-chart").locator(".recharts-bar-rectangle")
        check("progress chart has a bar per topic", bars.count() == 6, f"{bars.count()} bars")
        if args.shots:
            page.screenshot(path=str(args.shots / "dashboard-active.png"), full_page=True)
        page.close()

        print("\n-- New Student")
        page = browser.new_page(viewport=viewport)
        page.set_default_timeout(20_000)
        sign_in_and_refresh(page, NEW)
        rows = recs(page)
        check("every recommendation is 'Getting started'", rows and all(r["kind"] == "getting-started" for r in rows),
              f"{len(rows)} items")
        check("introductory list: topic 1's note and lecture, then topic 2's note, for each course",
              {r["topic"] for r in rows} == INTRO_TOPICS and len(rows) == 6
              and sum("Study note" in r["text"] for r in rows) == 4 and sum("Lecture" in r["text"] for r in rows) >= 2,
              f"{len(rows)} items")
        reminder_text = " ".join(page.get_by_test_id("reminder").all_inner_texts())
        check("new student is reminded to take a diagnostic", "diagnostic quiz" in reminder_text)
        check("no streak yet", page.get_by_test_id("streak").inner_text() == "0")
        if args.shots:
            page.screenshot(path=str(args.shots / "dashboard-new.png"), full_page=True)

        print("\n-- Accept and Dismiss")
        first, second = page.get_by_test_id("recommendation").nth(0), page.get_by_test_id("recommendation").nth(1)
        accepted_id, dismissed_id = first.get_attribute("data-id"), second.get_attribute("data-id")
        accepted_topic = first.get_by_test_id("recommendation-topic").inner_text()
        dismissed_topic = second.get_by_test_id("recommendation-topic").inner_text()
        # Dismiss the second first (Accept navigates to the resource).
        second.get_by_role("button", name="Dismiss").click()
        expect(page.get_by_test_id("recommendation")).to_have_count(5)
        page.get_by_test_id("recommendation").first.get_by_role("button", name="Accept and open").click()
        page.wait_for_url(f"{APP}/resources/**")
        page.go_back()
        expect(page.get_by_test_id("recommendation")).to_have_count(4)

        statuses = {r["id"]: r["status"] for r in db.table("recommendations").select(
            "id, status").eq("student_id", new_id).execute().data}
        check("Accept sets status to accepted and opens the resource", statuses.get(accepted_id) == "accepted", accepted_topic)
        check("Dismiss sets status to dismissed and moves it to History", statuses.get(dismissed_id) == "dismissed", dismissed_topic)
        page.close()
        browser.close()

    # Put the demo account back: statuses to pending, so the next demo starts clean.
    db.table("recommendations").update({"status": "pending"}).eq("student_id", new_id).execute()

    print(f"\n{sum(results)}/{len(results)} checks passed")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
