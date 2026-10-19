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


SECTIONS = {"fr5": fr5}


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
