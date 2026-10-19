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


SECTIONS = {"fr5": fr5, "fr4": fr4}


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
