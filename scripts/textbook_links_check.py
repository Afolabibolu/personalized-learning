"""Check of the textbook links (Prompt 5).

    1. Every book link in content/textbooks/*.json still loads (HTTP 200 after redirects, not a
       search page), from a plain request or, for sites that block scripts, headless Chrome.
    2. The database: every textbook card carries its book's link and type, and none has a type
       without a link.
    3. Chrome: the "Read free online" / "Buy or preview" button on a recommendation card's
       "Also recommended", in the Knowledge Base and on the reading card, opening in a new tab,
       while the card itself still opens in the app.

    python scripts/textbook_links_check.py [--links-only] [--shots DIR] [--mobile]
"""

import argparse
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import httpx
from playwright.sync_api import Page, expect, sync_playwright

import testkit

ROOT = Path(__file__).resolve().parent.parent
APP = "http://localhost:5173"
ACTIVE = "active.student@demo.example.com"
DEMO_PASSWORD = "DemoPass2026!"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
SEARCH_PAGE = re.compile(r"/search|[?&](q|aq|query|keywords?)=")
CHALLENGE = re.compile(r"(?i)<title>\s*(client challenge|just a moment|attention required)")

results: list[bool] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append(passed)
    print(f"{'PASS' if passed else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""))


def book_links() -> dict[str, dict]:
    """url -> one book that uses it, from the committed textbook files."""
    links = {}
    for path in sorted((ROOT / "content" / "textbooks").glob("*.json")):
        for book in json.loads(path.read_text())["books"].values():
            if book.get("url"):
                links.setdefault(book["url"], {"title": book["title"], "link_type": book["link_type"], "code": path.stem})
    return links


def plain(url: str) -> tuple[int, str, str]:
    try:
        r = httpx.get(url, headers={"User-Agent": UA, "Accept-Language": "en"}, follow_redirects=True, timeout=30)
        return r.status_code, str(r.url), r.text
    except httpx.HTTPError as e:
        return 0, url, str(e)


def loads(url: str, browser) -> tuple[bool, str]:
    status, final, doc = plain(url)
    how = "http"
    if status != 200 or len(doc) < 2000 or CHALLENGE.search(doc):
        page = browser.new_page(user_agent=UA)
        try:
            resp = page.goto(url, wait_until="domcontentloaded", timeout=45_000)
            status, final, how = (resp.status if resp else 0), page.url, "chrome"
        except Exception as e:  # a timeout or a network error is a failed link
            status, final, how = 0, url, f"chrome ({e.__class__.__name__})"
        finally:
            page.close()
    if status != 200:
        return False, f"HTTP {status} via {how}"
    if SEARCH_PAGE.search(final.lower()) and not SEARCH_PAGE.search(url.lower()):
        return False, f"redirected to a search page ({final})"
    return True, how


def check_links(browser) -> None:
    links = book_links()
    print(f"-- {len(links)} distinct book links")
    with ThreadPoolExecutor(8) as pool:
        first = dict(zip(links, pool.map(plain, links)))
    failed = []
    for url, book in links.items():
        status, final, doc = first[url]
        if status == 200 and len(doc) >= 2000 and not CHALLENGE.search(doc) and not SEARCH_PAGE.search(final.lower()):
            continue
        ok, how = loads(url, browser)
        if not ok:
            failed.append(f"{book['code']} {book['title']}: {how}")
    check("every textbook link still loads", not failed, f"{len(links) - len(failed)} of {len(links)} load"
          + ("; " + "; ".join(failed) if failed else ""))
    kinds = {k: sum(1 for b in links.values() if b["link_type"] == k) for k in ("free", "buy", "preview")}
    check("every link is free, buy or preview", sum(kinds.values()) == len(links), str(kinds))


def check_database(db) -> None:
    print("\n-- Database")
    rows = all_textbooks(db)
    with_link = [r for r in rows if r["url"]]
    check("textbook cards carry their book's link and type", with_link and all(r["link_type"] for r in with_link),
          f"{len(with_link)} of {len(rows)} cards linked")
    check("no textbook card has a link type without a link", all(r["url"] for r in rows if r["link_type"]))
    known = set(book_links())
    check("every card's link comes from content/textbooks/", all(r["url"] in known for r in with_link))


def all_textbooks(db) -> list[dict]:
    rows, start = [], 0
    while True:
        page = db.table("resources").select("id, title, url, link_type").eq("type", "textbook").order("id") \
            .range(start, start + 999).execute().data
        rows += page
        if len(page) < 1000:
            return rows
        start += 1000


def sign_in(page: Page) -> None:
    page.goto(f"{APP}/login")
    page.get_by_label("Email").fill(ACTIVE)
    page.get_by_label("Password").fill(DEMO_PASSWORD)
    page.get_by_role("button", name="Sign in").click()
    page.wait_for_url(f"{APP}/")
    expect(page.get_by_test_id("recommendation").first).to_be_visible(timeout=20_000)
    page.wait_for_load_state("networkidle")


def check_app(browser, shots: Path | None, mobile: bool) -> None:
    viewport = {"width": 390, "height": 844} if mobile else {"width": 1280, "height": 900}
    page = browser.new_context(viewport=viewport).new_page()
    page.set_default_timeout(20_000)

    print("\n-- Recommendation card (Tolu)")
    sign_in(page)
    buttons = page.get_by_test_id("recommendation").get_by_test_id("book-link")
    check("'Also recommended' textbooks carry a link button", buttons.count() >= 1, f"{buttons.count()} buttons")
    if buttons.count():
        b = buttons.first
        label, kind = b.inner_text().split("\n")[0], b.get_attribute("data-link-type")
        check("the label matches the link type",
              label == ("Read free online" if kind == "free" else "Buy or preview"), f"{label!r} for {kind}")
        check("it opens in a new tab", b.get_attribute("target") == "_blank" and "noopener" in (b.get_attribute("rel") or ""))
        card = b.locator("xpath=ancestor::li[@data-testid='recommendation']")
        textbook = card.get_by_test_id("also-link").filter(has_text="Textbook:")
        check("the textbook itself still opens its reading card in the app",
              (textbook.get_attribute("href") or "").startswith("/resources/"), textbook.get_attribute("href"))
        if shots:
            page.add_style_tag(content="header { position: static !important; }")
            card.scroll_into_view_if_needed()
            card.screenshot(path=str(shots / "recommendation-card-book-link.png"))
        reading = textbook.get_attribute("href")
    else:
        reading = None

    print("\n-- Knowledge Base")
    page.goto(f"{APP}/knowledge")
    page.wait_for_load_state("networkidle")
    page.get_by_placeholder(re.compile("Search", re.I)).fill("Interaction Design")
    kb = page.get_by_test_id("book-link")
    expect(kb.first).to_be_visible()
    check("the Knowledge Base shows the button beside textbooks", kb.count() >= 1, f"{kb.count()} buttons")
    if shots and kb.count():
        kb.first.scroll_into_view_if_needed()
        page.wait_for_timeout(300)
        page.screenshot(path=str(shots / "knowledge-base-book-link.png"))

    print("\n-- Reading card")
    if reading:
        page.goto(f"{APP}{reading}")
        row = page.get_by_test_id("book-link-row")
        expect(row).to_be_visible()
        check("the reading card shows the button under the card", row.get_by_test_id("book-link").count() == 1,
              row.inner_text().replace("\n", " | "))
        if shots:
            page.evaluate("window.scrollTo(0, 0)")
            page.screenshot(path=str(shots / "reading-card-book-link.png"), full_page=True)
    page.context.close()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--links-only", action="store_true", help="only check that every link loads")
    parser.add_argument("--shots", type=Path)
    parser.add_argument("--mobile", action="store_true")
    args = parser.parse_args()
    if args.shots:
        args.shots.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=True)
        if not args.mobile:
            check_links(browser)
        if not args.links_only:
            check_database(testkit.admin())
            check_app(browser, args.shots, args.mobile)
        browser.close()
    print(f"\n{sum(results)}/{len(results)} checks passed")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
