"""The system on courses below 500 level, with Bisi Adewale (200 level, seed_demo.LEVELS_*).

    COS 103 (100 level)  no diagnostic                    -> Stage 1, "Getting started"
    CSC 236 (200 level)  diagnostic + two topic quizzes    -> Stage 3, the models
    CSC 351 (300 level)  no diagnostic                    -> Stage 1, "Getting started"
    CSC 472 (400 level)  diagnostic only                  -> Stage 2, "Based on your diagnostic"

Checks the stages in the database, runs POST /recommend as Bisi, prints both models'
probabilities for every CSC 236 topic, then takes the screenshots in Chrome.
Needs seed_demo.py, the Vite dev server and the ML service (with trained models).

    python scripts/levels_check.py [--shots DIR]   (default docs/screenshots/levels)
"""

import argparse
import os
import sys
from pathlib import Path

import pandas as pd
from playwright.sync_api import Page, expect, sync_playwright

import testkit
from stage_check import APP, PASSWORD, pending, recommend, rows_in, sign_in, stages, user_id

ROOT = Path(__file__).resolve().parent.parent
BISI = "bisi.student@demo.example.com"
EXPECTED_STAGES = {"COS 103": 1, "CSC 236": 3, "CSC 351": 1, "CSC 472": 2}
DESKTOP = {"width": 1280, "height": 900}
PHONE = {"width": 390, "height": 844}

results: list[bool] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append(bool(passed))
    print(f"{'PASS' if passed else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""))


def all_probabilities(student_id: str, course_id: str) -> pd.DataFrame:
    """Both models' probabilities for every topic in the course, computed exactly as POST /recommend does."""
    sys.path.insert(0, str(ROOT / "ml"))
    cwd = os.getcwd()
    os.chdir(ROOT / "ml")
    try:
        from app import data
        from app.recommender import model_probabilities
        from training.features import prediction_rows, to_frames
        db = data.service_client()
        course = next(c for c in data.load_courses(db) if c.course_id == course_id)
        scores, logs = to_frames(*data.student_history(db, student_id))
        features = prediction_rows(scores, logs, course.topic_ids, pd.Timestamp.now(tz="UTC"))
        probs = model_probabilities(data.load_models(), features)
        titles = data.topic_titles(db)
        probs["topic"] = [titles[t] for t in probs.index]
        probs["last_score"] = features.set_index("topic_id")["last_score"].reindex(probs.index).values
        return probs.sort_values("average", ascending=False)
    finally:
        os.chdir(cwd)


def ids(db) -> dict:
    courses = {c["code"]: c["id"] for c in db.table("courses").select("id, code").in_("code", list(EXPECTED_STAGES)).execute().data}
    topics = db.table("topics").select("id, course_id, slug, sequence_order").in_("course_id", list(courses.values())).execute().data
    topic = {(code, t["slug"]): t["id"] for code, cid in courses.items() for t in topics if t["course_id"] == cid}
    return {"course": courses, "topic": topic}


def resource_id(db, topic_id: str, kind: str) -> str:
    rows = db.table("resources").select("id, body").eq("topic_id", topic_id).eq("type", kind).execute().data
    return next(r["id"] for r in rows if r["body"])  # the in-app one, not a folder link


def top(page: Page) -> None:
    page.evaluate("window.scrollTo(0, 0)")
    page.wait_for_timeout(300)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--shots", type=Path, default=ROOT / "docs" / "screenshots" / "levels")
    args = parser.parse_args()
    args.shots.mkdir(parents=True, exist_ok=True)
    db = testkit.admin()
    bisi = user_id(db, BISI)
    known = ids(db)

    print("-- Bisi's profile and courses (database)")
    profile = db.table("profiles").select("full_name, level").eq("id", bisi).execute().data[0]
    check("Bisi Adewale, 200 level", profile == {"full_name": "Bisi Adewale", "level": 200}, str(profile))
    codes = {v: k for k, v in known["course"].items()}
    enrolled = sorted(codes.get(e["course_id"], e["course_id"]) for e in
                      db.table("enrollments").select("course_id").eq("student_id", bisi).execute().data)
    check("enrolled in exactly COS 103, CSC 236, CSC 351 and CSC 472", enrolled == sorted(EXPECTED_STAGES), ", ".join(enrolled))
    got = stages(db, bisi)
    check("stages: CSC 236 Stage 3, CSC 472 Stage 2, COS 103 and CSC 351 Stage 1", got == EXPECTED_STAGES, str(got))
    logs = db.table("study_logs").select("duration_minutes").eq("student_id", bisi).execute().data
    check("three or four study sessions of 20 to 60 minutes",
          3 <= len(logs) <= 4 and all(20 <= l["duration_minutes"] <= 60 for l in logs), str([l["duration_minutes"] for l in logs]))

    print("\n-- POST /recommend as Bisi (ML service)")
    check("/recommend returns 200", recommend(BISI) == 200)
    rows = pending(db, bisi)
    by_course: dict[str, list[dict]] = {}
    for r in rows:
        by_course.setdefault(r["topic"]["course"]["code"], []).append(r)
    ml = by_course.get("CSC 236", [])
    check("CSC 236: ML recommendations with both models' probabilities",
          ml and all(r["source"] == "ml" and r["explanation"]["probabilities"] for r in ml), f"{len(ml)} rows")
    check("CSC 236: the weak, never-studied topic first",
          ml and ml[0]["topic"]["title"] == "Recurrences and the Master Theorem", ml[0]["topic"]["title"] if ml else "none")
    diag = by_course.get("CSC 472", [])
    check("CSC 472: 'Based on your diagnostic' items, lowest diagnostic score first",
          diag and all(r["source"] == "diagnostic" for r in diag)
          and [r["explanation"]["diagnostic"]["correct"] for r in diag] == sorted(r["explanation"]["diagnostic"]["correct"] for r in diag),
          "; ".join(f"{r['topic']['title']} {r['explanation']['diagnostic']['correct']}/3" for r in diag))
    for code in ("COS 103", "CSC 351"):
        rs = by_course.get(code, [])
        check(f"{code}: a 'Getting started' list", rs and all(r["source"] == "cold_start" for r in rs), f"{len(rs)} rows")

    probs = all_probabilities(bisi, known["course"]["CSC 236"])
    print("\n   CSC 236, every topic (probability it needs attention):")
    print("   " + f"{'Topic':52} {'Last':>5} {'LR':>6} {'RF':>6} {'Avg':>6}")
    for _, p in probs.iterrows():
        print("   " + f"{p['topic'][:52]:52} {p['last_score']:5.0f} {p['lr']:6.3f} {p['rf']:6.3f} {p['average']:6.3f}")
    saved = {r["topic"]["title"]: r["priority_score"] for r in ml}
    check("the saved CSC 236 scores match the models' top three",
          list(saved) == list(probs["topic"][:3]) and all(abs(saved[t] - a) < 0.001 for t, a in zip(probs["topic"], probs["average"]) if t in saved))

    t = known["topic"]
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=True)
        page = browser.new_page(viewport=DESKTOP)
        page.set_default_timeout(20_000)
        sign_in(page, BISI)

        print("\n-- Dashboard: all three stages")
        kinds = {r["kind"] for r in rows_in(page)}
        check("dashboard shows ML, diagnostic and getting-started cards",
              {"diagnostic", "getting-started"} <= kinds and kinds & {"attention", "keep-it-up"}, ", ".join(sorted(kinds)))
        prompts = sorted(x.split("\n")[0] for x in page.get_by_test_id("diagnostic-prompt").all_inner_texts())
        check("'Take the diagnostic' cards for COS 103 and CSC 351 only",
              prompts == [f"Take the {c} diagnostic so your recommendations can be personalised." for c in ("COS 103", "CSC 351")],
              f"{len(prompts)} cards")
        top(page)
        page.screenshot(path=str(args.shots / "dashboard-bisi.png"), full_page=True)

        card = page.get_by_test_id("recommendation").filter(has_text="Recurrences and the Master Theorem").first
        card.get_by_role("button", name="Why this?").click()
        why = card.get_by_test_id("why-panel")
        check("'Why this?' on the CSC 236 card shows both models", "Logistic Regression" in why.inner_text())
        card.evaluate("el => window.scrollTo(0, el.getBoundingClientRect().top + window.scrollY - 76)")
        page.wait_for_timeout(300)
        page.screenshot(path=str(args.shots / "why-this-csc236.png"))

        page.get_by_label("Course").select_option(label="CSC 236 · Introduction to Algorithms")
        chart = page.get_by_test_id("progress-chart")
        page.wait_for_function("() => document.querySelector('[data-testid=progress-chart]').textContent.includes('Master Theorem')")
        check("progress chart with CSC 236 selected", "Master Theorem" in chart.text_content())
        chart.evaluate("el => window.scrollTo(0, el.getBoundingClientRect().top + window.scrollY - 180)")
        page.wait_for_timeout(500)
        page.screenshot(path=str(args.shots / "progress-csc236.png"))

        print("\n-- Knowledge Base and resources on lower levels")
        page.goto(f"{APP}/knowledge")
        page.get_by_role("button", name="100 level").click()
        header = page.get_by_role("button", name="COS 103 · Introduction to Programming")
        page.wait_for_load_state("networkidle")
        if header.get_attribute("aria-expanded") != "true":  # her own courses already open
            header.click()
        expect(header).to_have_attribute("aria-expanded", "true")
        check("Knowledge Base: 100 level picked, COS 103 expanded", page.get_by_test_id("kb-topic").count() == 7,
              f"{page.get_by_test_id('kb-topic').count()} topics open")
        top(page)
        page.screenshot(path=str(args.shots / "kb-100-level.png"))

        page.goto(f"{APP}/topics/{t[('COS 103', 'loops')]}")
        expect(page.get_by_role("heading", name="Loops", exact=True)).to_be_visible()
        page.wait_for_load_state("networkidle")
        check("COS 103 topic page with its resources", page.get_by_text("Study note: Loops").first.is_visible())
        top(page)
        page.screenshot(path=str(args.shots / "topic-cos103.png"), full_page=True)

        page.goto(f"{APP}/resources/{resource_id(db, t[('CSC 351', 'deterministic-finite-automata')], 'note')}")
        expect(page.locator("article .prose h1")).to_be_visible()
        check("CSC 351 study note in the resource viewer", "Deterministic" in page.locator("article .prose h1").inner_text())
        top(page)
        page.screenshot(path=str(args.shots / "note-csc351.png"), full_page=True)

        page.goto(f"{APP}/resources/{resource_id(db, t[('CSC 472', 'sql')], 'past_questions')}")
        expect(page.locator("article .prose")).to_be_visible()
        check("CSC 472 past questions in the resource viewer", "SQL" in page.locator("article").inner_text())
        top(page)
        page.screenshot(path=str(args.shots / "pastq-csc472.png"), full_page=True)

        print("\n-- Quizzes")
        diag_quiz = db.table("quizzes").select("id").eq("course_id", known["course"]["CSC 236"]).eq("kind", "diagnostic").execute().data[0]["id"]
        attempt = db.table("quiz_attempts").select("id").eq("student_id", bisi).eq("quiz_id", diag_quiz).execute().data[0]["id"]
        page.goto(f"{APP}/attempts/{attempt}")
        expect(page.get_by_role("heading", name="Score per topic")).to_be_visible()
        page.wait_for_load_state("networkidle")
        check("CSC 236 diagnostic results with a score per topic", "Recurrences and the Master Theorem" in page.inner_text("main"))
        top(page)
        page.screenshot(path=str(args.shots / "diagnostic-csc236.png"))

        sql_quiz = db.table("quizzes").select("id").eq("topic_id", t[("CSC 472", "sql")]).eq("kind", "topic").execute().data[0]["id"]
        page.goto(f"{APP}/quiz/{sql_quiz}")
        page.get_by_role("button", name="Start quiz").click()
        stem = page.locator("main h1").first
        expect(stem).to_be_visible()
        page.wait_for_load_state("networkidle")
        check("a CSC 472 topic quiz question", bool(stem.inner_text().strip()), stem.inner_text()[:70])
        top(page)
        page.screenshot(path=str(args.shots / "quiz-csc472.png"))
        page.close()
        # The quiz above was only opened for the screenshot: remove the unfinished attempt.
        db.table("quiz_attempts").delete().eq("student_id", bisi).is_("completed_at", "null").execute()

        print("\n-- Phone width")
        page = browser.new_page(viewport=PHONE)
        page.set_default_timeout(20_000)
        sign_in(page, BISI)
        overflow = page.evaluate("document.documentElement.scrollWidth > window.innerWidth")
        check("phone dashboard (390 px) fits, no sideways scroll", not overflow)
        top(page)
        page.screenshot(path=str(args.shots / "phone-dashboard-bisi.png"), full_page=True)
        browser.close()

    print(f"\n{sum(results)}/{len(results)} checks passed")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
