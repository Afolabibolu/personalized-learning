"""Check of the three recommendation stages, against the database, the ML service and Chrome.

    Stage 1  Kemi Balogun  no diagnostic                      -> "Getting started" + "Take the diagnostic" cards
    Stage 2  Ngozi Eze     CSC 531 diagnostic only            -> weakest diagnostic topics, "Based on your diagnostic"
    Stage 3  Tolu Adeyemi  at or above the threshold          -> the models, unchanged

Also blocks the ML service in the browser and confirms Stage 2 still appears.
Needs the Vite dev server, the ML service, seed_demo.py and training.train.

    python scripts/stage_check.py [--shots DIR] [--mobile]
"""

import argparse
import sys
from pathlib import Path

import httpx
from playwright.sync_api import Page, expect, sync_playwright

import testkit

APP = "http://localhost:5173"
ML = "http://localhost:8000"
PASSWORD = "DemoPass2026!"
NEW = "new.student@demo.example.com"
DIAGNOSTIC = "diagnostic.student@demo.example.com"
ACTIVE = "active.student@demo.example.com"
# Ngozi's CSC 531 diagnostic (seed_demo.DIAGNOSTIC_RESULTS): right out of 3, in teaching order.
NGOZI_EXPECTED = [
    ("Cognitive Psychology and Perception", 0),
    ("Conceptual Models, Interaction Types and Ideation", 1),
    ("Understanding the Problem Space and User-Centred Design", 2),  # ties with Data Gathering (2 of 3); earlier in teaching order
]

results: list[bool] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append(passed)
    print(f"{'PASS' if passed else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""))


def user_id(db, email: str) -> str:
    return next(u.id for u in db.auth.admin.list_users(page=1, per_page=1000) if u.email == email)


def stages(db, student_id: str) -> dict[str, int]:
    codes = {c["id"]: c["code"] for c in db.table("courses").select("id, code").execute().data}
    return {codes[s["course_id"]]: s["stage"] for s in db.rpc("recommendation_stages", {"p_student": student_id}).execute().data}


def recommend(email: str) -> int:
    client = testkit.anon()
    client.auth.sign_in_with_password({"email": email, "password": PASSWORD})
    token = client.auth.get_session().access_token
    return httpx.post(f"{ML}/recommend", headers={"Authorization": f"Bearer {token}"}, timeout=120).status_code


def pending(db, student_id: str) -> list[dict]:
    rows = db.table("recommendations").select(
        "rank, source, priority_score, explanation, topic:topics(title, sequence_order, course:courses(code))").eq(
        "student_id", student_id).eq("status", "pending").execute().data
    return sorted(rows, key=lambda r: (r["topic"]["course"]["code"], r["rank"]))


def sign_in(page: Page, email: str) -> None:
    page.goto(f"{APP}/login")
    page.get_by_label("Email").fill(email)
    page.get_by_label("Password").fill(PASSWORD)
    page.get_by_role("button", name="Sign in").click()
    page.wait_for_url(f"{APP}/")
    expect(page.get_by_role("heading", name="Recommended for you")).to_be_visible()
    expect(page.get_by_test_id("recommendation").first).to_be_visible()
    page.wait_for_load_state("networkidle")


def rows_in(page: Page) -> list[dict]:
    items = page.get_by_test_id("recommendation")
    return [{"kind": items.nth(i).get_attribute("data-kind"),
             "topic": items.nth(i).get_by_test_id("recommendation-topic").inner_text(),
             "text": items.nth(i).inner_text()} for i in range(items.count())]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--shots", type=Path)
    parser.add_argument("--mobile", action="store_true")
    args = parser.parse_args()
    if args.shots:
        args.shots.mkdir(parents=True, exist_ok=True)
    db = testkit.admin()
    threshold = db.rpc("cold_start_threshold").execute().data
    check("one shared threshold (app_settings.cold_start_threshold)", threshold == 3, f"N = {threshold}")
    ids = {e: user_id(db, e) for e in (NEW, DIAGNOSTIC, ACTIVE)}

    print("\n-- Stages per course (database)")
    check("Kemi: Stage 1 in both courses", stages(db, ids[NEW]) == {"CSC 531": 1, "CSC 574": 1}, str(stages(db, ids[NEW])))
    check("Ngozi: Stage 2 in CSC 531, Stage 1 in CSC 574", stages(db, ids[DIAGNOSTIC]) == {"CSC 531": 2, "CSC 574": 1},
          str(stages(db, ids[DIAGNOSTIC])))
    check("Tolu: Stage 3 in both courses", stages(db, ids[ACTIVE]) == {"CSC 531": 3, "CSC 574": 3}, str(stages(db, ids[ACTIVE])))

    print("\n-- POST /recommend (ML service)")
    for email in ids:
        check(f"/recommend for {email.split('@')[0]}", recommend(email) == 200)
    kemi = pending(db, ids[NEW])
    check("Kemi: only 'Getting started' rows, no ML scores",
          kemi and all(r["source"] == "cold_start" and r["priority_score"] is None for r in kemi), f"{len(kemi)} rows")
    ngozi = pending(db, ids[DIAGNOSTIC])
    diag = [r for r in ngozi if r["source"] == "diagnostic"]
    got = [(r["topic"]["title"], r["explanation"]["diagnostic"]["correct"]) for r in diag]
    check("Ngozi: CSC 531 ranked by diagnostic score, lowest first, ties by teaching order", got == NGOZI_EXPECTED,
          "; ".join(f"{t} {c}/3" for t, c in got))
    check("Ngozi: fully right topics left out", all(c < 3 for _, c in got))
    check("Ngozi: reason says how many were right",
          diag and diag[0]["explanation"]["reason"] == "You got 0 of 3 right on this topic in the diagnostic.",
          diag[0]["explanation"]["reason"] if diag else "none")
    check("Ngozi: Stage 2 rows carry no ML probabilities, and say N",
          all(r["priority_score"] is None and r["explanation"]["probabilities"] is None and r["explanation"]["threshold"] == threshold
              for r in diag))
    check("Ngozi: CSC 574 still has its 'Getting started' list",
          [r["source"] for r in ngozi if r["topic"]["course"]["code"] == "CSC 574"] == ["cold_start"] * 3)
    tolu = pending(db, ids[ACTIVE])
    check("Tolu: ML rows with both models' probabilities (unchanged)",
          tolu and all(r["source"] == "ml" and r["explanation"]["probabilities"] for r in tolu), f"{len(tolu)} rows")

    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=True)
        viewport = {"width": 390, "height": 844} if args.mobile else {"width": 1280, "height": 900}

        print("\n-- Stage 1 dashboard (Kemi)")
        page = browser.new_page(viewport=viewport)
        page.set_default_timeout(20_000)
        sign_in(page, NEW)
        prompts = page.get_by_test_id("diagnostic-prompt").all_inner_texts()
        check("a 'Take the [CODE] diagnostic' card for each course, at the top",
              sorted(p.split("\n")[0] for p in prompts) == [
                  f"Take the {c} diagnostic so your recommendations can be personalised." for c in ("CSC 531", "CSC 574")],
              f"{len(prompts)} cards")
        check("the cards mention the real threshold", all(f"after {threshold} quizzes" in p for p in prompts))
        check("the list is 'Getting started'", all(r["kind"] == "getting-started" for r in rows_in(page)), f"{len(rows_in(page))} items")
        if args.shots:
            page.screenshot(path=str(args.shots / "stage1-dashboard.png"), full_page=True)
        page.close()

        print("\n-- Stage 2 dashboard (Ngozi)")
        page = browser.new_page(viewport=viewport)
        page.set_default_timeout(20_000)
        sign_in(page, DIAGNOSTIC)
        rows = rows_in(page)
        first = rows[0]
        check("weakest diagnostic topic first, labelled 'Based on your diagnostic'",
              first["kind"] == "diagnostic" and first["topic"] == NGOZI_EXPECTED[0][0] and "Based on your diagnostic" in first["text"],
              first["topic"])
        check("only the CSC 574 diagnostic card is shown",
              [p.split("\n")[0] for p in page.get_by_test_id("diagnostic-prompt").all_inner_texts()] == [
                  "Take the CSC 574 diagnostic so your recommendations can be personalised."])
        card = page.get_by_test_id("recommendation").first
        card.get_by_role("button", name="Why this?").click()
        why = card.get_by_test_id("why-panel").inner_text()
        check("'Why this?' says it comes from the diagnostic, not the models",
              "This comes from your diagnostic score, not from the machine learning models" in why)
        check("'Why this?' gives the real N", f"start after {threshold} quizzes on this course" in why,
              card.get_by_test_id("ml-starts-after").inner_text())
        check("'Focus next' names the weakest diagnostic topic",
              "Based on your diagnostic" in page.get_by_test_id("weekly-next").inner_text())
        if args.shots:
            page.evaluate("window.scrollTo(0, 0)")
            page.screenshot(path=str(args.shots / "stage2-dashboard.png"), full_page=True)
        page.close()

        print("\n-- Stage 2 with the ML service down")
        db.table("recommendations").delete().eq("student_id", ids[DIAGNOSTIC]).eq("status", "pending").execute()
        page = browser.new_page(viewport=viewport)
        page.set_default_timeout(20_000)
        page.route("**/recommend", lambda route: route.abort())
        sign_in(page, DIAGNOSTIC)
        diag_rows = [r for r in rows_in(page) if r["kind"] == "diagnostic"]
        check("with nothing saved and the service blocked, the dashboard still shows Stage 2",
              [r["topic"] for r in diag_rows] == [t for t, _ in NGOZI_EXPECTED], f"{len(diag_rows)} diagnostic items")
        with page.expect_response(lambda r: "refresh_fallback_recommendations" in r.url):
            page.get_by_role("button", name="Refresh").click()
        expect(page.get_by_test_id("ml-offline-notice")).to_be_visible()
        check("Refresh with the service down shows the quiet notice and keeps Stage 2",
              [r["topic"] for r in rows_in(page) if r["kind"] == "diagnostic"] == [t for t, _ in NGOZI_EXPECTED])
        page.close()
        recommend(DIAGNOSTIC)  # back to the service's own list

        print("\n-- Stage 3 dashboard (Tolu)")
        page = browser.new_page(viewport=viewport)
        page.set_default_timeout(20_000)
        sign_in(page, ACTIVE)
        rows = rows_in(page)
        check("ML items only ('Needs attention' or 'Keep it up'), no diagnostic cards",
              rows and all(r["kind"] in ("attention", "keep-it-up") for r in rows)
              and page.get_by_test_id("diagnostic-prompt").count() == 0, f"{len(rows)} items")
        card = page.get_by_test_id("recommendation").first
        card.get_by_role("button", name="Why this?").click()
        check("'Why this?' still shows both models", "Logistic Regression" in card.get_by_test_id("why-panel").inner_text())
        if args.shots:
            page.evaluate("window.scrollTo(0, 0)")
            page.screenshot(path=str(args.shots / "stage3-dashboard.png"), full_page=True)
        page.close()
        browser.close()

    print(f"\n{sum(results)}/{len(results)} checks passed")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
