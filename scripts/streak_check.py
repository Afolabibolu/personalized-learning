"""Check of the streak card, badges and celebrations in Chrome (Prompt 4).

    Tolu Adeyemi       the seeded demo history: today done, a week-long run, badges
    "At risk"          active the three days before today, nothing yet today
    "Freeze used"      7 days in a row, yesterday missed, active today
    "Celebration"      a new student who logs study (streak moment), then finishes a quiz (badge pop-up)

The three test students are created on the test email domain and removed at the end.
Needs the Vite dev server and seed_demo.py.

    python scripts/streak_check.py [--shots DIR] [--mobile]
"""

import argparse
import sys
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from playwright.sync_api import Page, expect, sync_playwright

import testkit
from phase3_check import answer_current_question

APP = "http://localhost:5173"
ACTIVE = "active.student@demo.example.com"
DEMO_PASSWORD = "DemoPass2026!"
LAGOS = ZoneInfo("Africa/Lagos")

results: list[bool] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append(passed)
    print(f"{'PASS' if passed else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""))


def student(db, name: str) -> tuple[str, str]:
    user_id, email = testkit.create_student(db, name)
    db.table("profiles").update({
        "department": "Computer Science", "level": 500, "learning_preferences": ["note"],
        "study_days": ["mon", "tue", "wed", "thu", "fri", "sat", "sun"], "preferred_study_time": "00:00",
        "daily_goal_minutes": 30,
    }).eq("id", user_id).execute()
    return user_id, email


def log(db, student_id: str, topic_id: str, at: datetime, minutes: int = 20) -> None:
    db.table("study_logs").insert({"student_id": student_id, "topic_id": topic_id, "duration_minutes": minutes,
                                   "activity_type": "reading", "logged_at": at.isoformat()}).execute()


def sign_in(page: Page, email: str, password: str) -> None:
    page.goto(f"{APP}/login")
    page.get_by_label("Email").fill(email)
    page.get_by_label("Password").fill(password)
    page.get_by_role("button", name="Sign in").click()
    page.wait_for_url(f"{APP}/")
    expect(page.get_by_test_id("streak")).to_be_visible()
    page.wait_for_load_state("networkidle")


def card_shot(page: Page, shots: Path | None, name: str) -> None:
    if shots:
        page.add_style_tag(content="header { position: static !important; }")
        page.get_by_test_id("streak").locator("xpath=ancestor::div[contains(@class,'rounded-2xl')][1]") \
            .screenshot(path=str(shots / f"{name}-card.png"))
        page.evaluate("window.scrollTo(0, 0)")
        page.screenshot(path=str(shots / f"{name}.png"), full_page=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--shots", type=Path)
    parser.add_argument("--mobile", action="store_true")
    args = parser.parse_args()
    if args.shots:
        args.shots.mkdir(parents=True, exist_ok=True)

    db = testkit.admin()
    testkit.cleanup(db)
    topic = db.table("topics").select("id, course:courses!inner(code)").eq("course.code", "CSC 531") \
        .order("sequence_order").limit(1).execute().data[0]["id"]
    now = datetime.now(LAGOS)
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    earlier_today = midnight + (now - midnight) / 2  # today, but not "just now" (no celebration)

    at_risk_id, at_risk = student(db, "Streak at risk")
    for back in (1, 2, 3):
        log(db, at_risk_id, topic, (midnight - timedelta(days=back)).replace(hour=19))
    frozen_id, frozen = student(db, "Streak freeze used")
    for back in (*range(2, 9), 0):  # 8 to 2 days ago, yesterday missed, today
        log(db, frozen_id, topic, earlier_today if back == 0 else (midnight - timedelta(days=back)).replace(hour=19), 15)
    _, fresh = student(db, "Streak celebration")
    # The state shots show the card, not the pop-ups (the celebration test covers those).
    for sid in (at_risk_id, frozen_id):
        db.rpc("sync_student_badges", {"p_student": sid}).execute()
        db.table("student_badges").update({"seen_at": now.isoformat()}).eq("student_id", sid).execute()

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(channel="chrome", headless=True)
            viewport = {"width": 390, "height": 844} if args.mobile else {"width": 1280, "height": 900}

            def new_page() -> Page:
                page = browser.new_context(viewport=viewport).new_page()
                page.set_default_timeout(20_000)
                return page

            print("-- Done today (Tolu)")
            page = new_page()
            sign_in(page, ACTIVE, DEMO_PASSWORD)
            streak = int(page.get_by_test_id("streak").inner_text())
            check("flame lit and a run of several days", page.get_by_test_id("streak-flame").get_attribute("data-lit") == "true"
                  and streak >= 3, f"{streak}-day streak")
            check("message says today counts", page.get_by_test_id("streak-message").inner_text().startswith("Today counts"))
            goal = page.get_by_test_id("goal-minutes").inner_text()
            check("daily goal ring shows today's minutes against the goal", goal.endswith("/30"), goal)
            check("today's and this week's XP", int(page.get_by_test_id("xp-today").inner_text()) > 0
                  and page.get_by_test_id("xp-week").inner_text().endswith("XP"),
                  f"{page.get_by_test_id('xp-today').inner_text()} today, {page.get_by_test_id('xp-week').inner_text()} this week")
            check("14-day strip", page.get_by_test_id("activity-strip").locator("li").count() == 14)
            check("no pop-up for badges the seed already marked seen", page.get_by_test_id("badge-popup").count() == 0)
            card_shot(page, args.shots, "streak-done-today")

            page.goto(f"{APP}/profile")
            expect(page.get_by_test_id("badge-shelf")).to_be_visible()
            shelf = page.get_by_test_id("badge")
            earned = [shelf.nth(i).get_attribute("data-badge") for i in range(shelf.count())
                      if shelf.nth(i).get_attribute("data-earned") == "true"]
            check("badge shelf on the Profile page: all 9, earned ones dated", shelf.count() == 9 and len(earned) >= 3,
                  ", ".join(earned))
            if args.shots:
                page.add_style_tag(content="header { position: static !important; }")  # keep it off element shots
                page.get_by_test_id("badge-shelf").locator("xpath=..").screenshot(path=str(args.shots / "badge-shelf.png"))
            page.context.close()

            print("\n-- At risk")
            page = new_page()
            sign_in(page, at_risk, testkit.PASSWORD)
            check("yesterday's run still shows (not 0)", page.get_by_test_id("streak").inner_text() == "3")
            check("grey flame", page.get_by_test_id("streak-flame").get_attribute("data-lit") == "false")
            msg = page.get_by_test_id("streak-message").inner_text()
            check("'Do a quiz or log study today to keep your 3-day streak'",
                  msg == "Do a quiz or log study today to keep your 3-day streak", msg)
            page.get_by_role("button", name="Notifications", exact=False).first.click()
            expect(page.get_by_text("Keep your streak going").first).to_be_visible()
            check("streak-at-risk notification in the bell",
                  page.get_by_text("Do a quiz or log study today to keep your 3-day streak.").count() >= 1)
            page.keyboard.press("Escape")
            page.goto(f"{APP}/")
            expect(page.get_by_test_id("streak")).to_be_visible()
            card_shot(page, args.shots, "streak-at-risk")
            page.context.close()

            print("\n-- Freeze used")
            page = new_page()
            sign_in(page, frozen, testkit.PASSWORD)
            check("a missed day used a freeze and the streak survived", page.get_by_test_id("streak").inner_text() == "8")
            used = page.get_by_test_id("freeze-used").inner_text()
            check("the card says when the freeze was used", "streak freeze kept your streak alive on" in used, used)
            check("the frozen day is marked on the strip",
                  page.get_by_test_id("activity-strip").locator("[data-frozen=true]").count() == 1)
            check("freezes held: 0 of 2 (the one earned was used)", page.get_by_test_id("freezes").get_attribute("data-held") == "0")
            card_shot(page, args.shots, "streak-freeze-used")
            page.context.close()

            print("\n-- Celebrations")
            page = new_page()
            sign_in(page, fresh, testkit.PASSWORD)
            check("a new student starts at 0", page.get_by_test_id("streak").inner_text() == "0")
            page.goto(f"{APP}/log?topic={topic}")
            page.get_by_role("button", name="30 min").click()
            page.get_by_role("button", name="Save session").click()
            moment = page.get_by_test_id("streak-celebration")
            expect(moment).to_be_visible()
            check("'Streak started' moment after the first activity of the day", "Streak started" in moment.inner_text(),
                  moment.inner_text().split("\n")[0])
            if args.shots:
                page.wait_for_timeout(600)
                page.screenshot(path=str(args.shots / "celebration-streak.png"))
            expect(moment).to_be_hidden(timeout=8_000)
            check("the moment goes away by itself", True)

            page.goto(f"{APP}/topics/{topic}")
            page.get_by_role("link", name="Take topic quiz").first.click()
            page.get_by_role("button", name="Start quiz").click()
            expect(page.get_by_role("button", name="Next").or_(page.get_by_role("button", name="Submit"))).to_be_visible()
            while True:
                answer_current_question(page)
                if not page.get_by_role("button", name="Next").count():
                    break
                page.get_by_role("button", name="Next").click()
            page.once("dialog", lambda d: d.accept())
            page.get_by_role("button", name="Submit").click()
            page.wait_for_url(f"{APP}/attempts/**")
            popup = page.get_by_test_id("badge-popup")
            expect(popup).to_be_visible()
            check("badge pop-up on the results page after the first quiz", popup.get_attribute("data-badge") == "first_quiz",
                  popup.inner_text().replace("\n", " | "))
            check("no second streak moment for a later activity the same day", page.get_by_test_id("streak-celebration").count() == 0)
            if args.shots:
                page.wait_for_timeout(600)  # past the 400 ms entrance
                page.screenshot(path=str(args.shots / "celebration-badge.png"))
            expect(popup).to_be_hidden(timeout=10_000)
            page.goto(f"{APP}/")
            expect(page.get_by_test_id("streak")).to_be_visible(timeout=20_000)
            page.wait_for_load_state("networkidle")
            check("the pop-up shows once (badge marked seen)", page.get_by_test_id("badge-popup").count() == 0)
            check("XP today counts the quiz and the session",
                  int(page.get_by_test_id("xp-today").inner_text()) >= 10 + 6 + 10, page.get_by_test_id("xp-today").inner_text())
            check("goal ring ticked after 30 minutes", page.get_by_test_id("goal-tick").count() == 1)
            page.context.close()

            print("\n-- Reduced motion")
            context = browser.new_context(viewport=viewport, reduced_motion="reduce")
            page = context.new_page()
            page.goto(f"{APP}/login")
            animated = page.evaluate("""() => { const d = document.createElement('div');
                d.className = 'motion-safe:animate-[pop_400ms_ease-out]'; document.body.appendChild(d);
                return getComputedStyle(d).animationName; }""")
            check("celebrations do not animate when reduced motion is set", animated == "none", f"animation-name: {animated}")
            context.close()
            browser.close()
    finally:
        testkit.cleanup(db)

    print(f"\n{sum(results)}/{len(results)} checks passed")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
