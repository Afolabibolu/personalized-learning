"""NFR2: measures response times and writes docs/results/performance.md (+ .json).

    python scripts/timing.py [--runs 20]

Needs the Vite dev server and the ML service running, and the demo accounts
from seed_demo.py. Measures, from this laptop against the hosted Supabase:
  - quiz submit: Submit pressed -> results page shown (browser), and the
    submit_quiz call on its own (API)
  - dashboard load: page opened -> recommendations and progress chart shown
    (browser, Active Student)
  - POST /recommend for the Active Student (runs in the background in the app)
A temporary student takes the topic quizzes and is deleted at the end.
"""

import argparse
import json
import os
import statistics
import sys
import time
from datetime import datetime
from pathlib import Path

import httpx
from playwright.sync_api import expect, sync_playwright

import testkit

APP = "http://localhost:5173"
ML_URL = os.getenv("ML_URL", "http://localhost:8000")
DOCS = Path(__file__).resolve().parent.parent / "docs" / "results"
ACTIVE = ("active.student@demo.example.com", "DemoPass2026!")

# Targets for "does not disrupt a student's use" (NFR2), set for this test.
TARGETS = {
    "quiz_submit_ui": 2.0,
    "quiz_submit_api": 1.0,
    "dashboard_load_ui": 3.0,
    "recommend_api": 5.0,
}
LABELS = {
    "quiz_submit_ui": "Quiz submit: Submit pressed → results on screen (browser)",
    "quiz_submit_api": "Quiz submit: submit_quiz call only (API)",
    "dashboard_load_ui": "Dashboard load: page opened → recommendations and chart shown (browser)",
    "recommend_api": "Recommendation update: POST /recommend (runs in the background)",
}


def summarise(samples: list[float]) -> dict:
    ordered = sorted(samples)
    p95 = ordered[min(len(ordered) - 1, round(0.95 * (len(ordered) - 1)))]
    return {
        "runs": len(samples),
        "median": round(statistics.median(samples), 3),
        "p95": round(p95, 3),
        "min": round(min(samples), 3),
        "max": round(max(samples), 3),
    }


def topic_quiz_ids(db) -> list[str]:
    return [q["id"] for q in db.table("quizzes").select("id").eq("kind", "topic").execute().data]


def measure_api_submit(email: str, quiz_ids: list[str], runs: int) -> list[float]:
    client = testkit.sign_in(email)
    samples = []
    for i in range(runs):
        started = client.rpc("start_quiz", {"p_quiz_id": quiz_ids[i % len(quiz_ids)]}).execute().data
        responses = {q["id"]: [q["options"][0]["key"]] for q in started["questions"]}
        t0 = time.perf_counter()
        client.rpc("submit_quiz", {"p_attempt_id": started["attempt_id"], "p_responses": responses}).execute()
        samples.append(time.perf_counter() - t0)
    return samples


def measure_ui(email: str, quiz_ids: list[str], runs: int) -> tuple[list[float], list[float]]:
    submit, dashboard = [], []
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=True)

        page = browser.new_page(viewport={"width": 1280, "height": 900})
        page.set_default_timeout(30_000)
        sign_in(page, email, testkit.PASSWORD)
        for i in range(runs):
            page.goto(f"{APP}/quiz/{quiz_ids[i % len(quiz_ids)]}")
            page.get_by_role("button", name="Start quiz").click()
            expect(page.get_by_text("/ 5", exact=False).first).to_be_visible()
            for q in range(5):
                page.get_by_role("radio").first.click() if page.get_by_role("checkbox").count() == 0 else page.get_by_role("checkbox").first.click()
                if q < 4:
                    page.get_by_role("button", name="Next").click()
            page.once("dialog", lambda d: d.accept())
            t0 = time.perf_counter()
            page.get_by_role("button", name="Submit").click()
            expect(page.get_by_text("Score per topic")).to_be_visible()
            submit.append(time.perf_counter() - t0)
        page.close()

        page = browser.new_page(viewport={"width": 1280, "height": 900})
        page.set_default_timeout(30_000)
        sign_in(page, *ACTIVE)
        # seed_demo.py --demo-only leaves no saved recommendations; compute them once, outside the timed runs.
        with page.expect_response(lambda r: "/recommend" in r.url and r.request.method == "POST", timeout=30_000):
            page.get_by_role("button", name="Refresh").click()
        for _ in range(runs):
            page.goto("about:blank")
            t0 = time.perf_counter()
            page.goto(f"{APP}/")
            expect(page.get_by_test_id("recommendation").first).to_be_visible()
            expect(page.get_by_test_id("progress-chart").locator(".recharts-bar-rectangle").first).to_be_visible()
            dashboard.append(time.perf_counter() - t0)
        browser.close()
    return submit, dashboard


def sign_in(page, email: str, password: str) -> None:
    page.goto(f"{APP}/login")
    page.get_by_label("Email").fill(email)
    page.get_by_label("Password").fill(password)
    page.get_by_role("button", name="Sign in").click()
    page.wait_for_url(lambda url: "/login" not in url)
    page.wait_for_load_state("networkidle")


def measure_recommend(runs: int) -> list[float]:
    client = testkit.anon()
    token = client.auth.sign_in_with_password({"email": ACTIVE[0], "password": ACTIVE[1]}).session.access_token
    samples = []
    for _ in range(runs):
        t0 = time.perf_counter()
        httpx.post(f"{ML_URL}/recommend", headers={"Authorization": f"Bearer {token}"}, timeout=60).raise_for_status()
        samples.append(time.perf_counter() - t0)
    return samples


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--runs", type=int, default=20)
    args = parser.parse_args()

    db = testkit.admin()
    quiz_ids = topic_quiz_ids(db)
    _, email = testkit.create_student(db, f"Performance {int(time.time())}")
    db.table("profiles").update({"department": "Computer Science", "level": 500}).eq(
        "id", next(u.id for u in db.auth.admin.list_users(page=1, per_page=1000) if u.email == email)).execute()
    try:
        print(f"Measuring {args.runs} runs each…")
        samples = {"quiz_submit_api": measure_api_submit(email, quiz_ids, args.runs)}
        samples["quiz_submit_ui"], samples["dashboard_load_ui"] = measure_ui(email, quiz_ids, args.runs)
        samples["recommend_api"] = measure_recommend(args.runs)
    finally:
        uid = next((u.id for u in db.auth.admin.list_users(page=1, per_page=1000) if u.email == email), None)
        if uid:
            db.auth.admin.delete_user(uid)

    results = {k: {**summarise(v), "target": TARGETS[k], "pass": summarise(v)["p95"] <= TARGETS[k],
                   "samples": [round(s, 3) for s in v]} for k, v in samples.items()}
    measured_at = datetime.now().strftime("%Y-%m-%d %H:%M")
    DOCS.mkdir(exist_ok=True)
    (DOCS / "performance.json").write_text(json.dumps({"measured_at": measured_at, "results": results}, indent=2))

    order = ["quiz_submit_ui", "quiz_submit_api", "dashboard_load_ui", "recommend_api"]
    rows = "\n".join(
        f"| {LABELS[k]} | {results[k]['runs']} | {results[k]['median']:.2f} | {results[k]['p95']:.2f} | "
        f"{results[k]['max']:.2f} | {results[k]['min']:.2f} | ≤ {results[k]['target']:.1f} | {'Pass' if results[k]['pass'] else 'Fail'} |"
        for k in order
    )
    (DOCS / "performance.md").write_text(
        "# Response times (NFR2)\n\n"
        f"Measured {measured_at} with `python scripts/timing.py --runs {args.runs}`, on the development laptop "
        "against the hosted Supabase project, with the Vite dev server and the ML service running locally. "
        "Times are in seconds. A case passes when its 95th percentile is within the target.\n\n"
        "| Operation | Runs | Median | p95 | Slowest | Fastest | Target | Result |\n| --- | --- | --- | --- | --- | --- | --- | --- |\n"
        f"{rows}\n\n"
        "Targets: a quiz result within 2 s of pressing Submit and a dashboard within 3 s keep the student's flow "
        "uninterrupted at single-institution usage. Recommendation updates run in the background after a quiz or a study "
        "log (the app does not wait for them), so their target is looser.\n\n"
        "Caveats: one laptop, one user at a time, development build of the web app, network to the Supabase region "
        "included. Load with many concurrent users was not tested.\n"
    )
    for k in order:
        r = results[k]
        print(f"{'PASS' if r['pass'] else 'FAIL'}  {LABELS[k]}: median {r['median']:.2f}s, p95 {r['p95']:.2f}s, slowest {r['max']:.2f}s (target {r['target']}s)")
    return 0 if all(r["pass"] for r in results.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
