"""Phase 4 check: cold start for "New Student", ML recommendations for "Active Student".

Signs in as each demo account with the anon key, calls POST /recommend on the
ML service with the account's own token, then reads the recommendations back
as that student. Needs seed_demo.py, training.train and the ML service
(cd ml && uvicorn app.main:app) to have run.

    python scripts/phase4_check.py
"""

import os
import sys
from pathlib import Path

import httpx
from dotenv import load_dotenv
from supabase import create_client

load_dotenv(Path(__file__).parent / ".env")

ML_URL = os.getenv("ML_URL", "http://localhost:8000")
RESULTS = Path(__file__).resolve().parent.parent / "ml" / "results"
DEMO_PASSWORD = "DemoPass2026!"
WEAK = {"CSC 531": "Cognitive Psychology and Perception", "CSC 574": "Fuzzy Logic Systems"}

results: list[bool] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append(passed)
    print(f"{'PASS' if passed else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""))


def recommendations_for(email: str):
    client = create_client(os.environ["SUPABASE_URL"], os.environ["SUPABASE_ANON_KEY"])
    session = client.auth.sign_in_with_password({"email": email, "password": DEMO_PASSWORD}).session
    response = httpx.post(f"{ML_URL}/recommend", headers={"Authorization": f"Bearer {session.access_token}"}, timeout=60)
    response.raise_for_status()
    rows = client.table("recommendations").select(
        "rank, priority_score, source, model_version, status, topic:topics(title, course:courses(code)), "
        "resource:resources(title), quiz:quizzes(title)"
    ).execute().data
    rows.sort(key=lambda r: (r["topic"]["course"]["code"], r["rank"]))
    return response.json(), rows


def show(rows) -> None:
    for r in rows:
        target = (r["resource"] or r["quiz"] or {}).get("title")
        score = f"p={r['priority_score']:.2f}" if r["priority_score"] is not None else ""
        print(f"    {r['topic']['course']['code']}  #{r['rank']}  {r['source']:10} {score:7} "
              f"{r['topic']['title']}  ->  {target}")


def main() -> int:
    print("-- Service")
    health = httpx.get(f"{ML_URL}/health", timeout=10)
    check("GET /health returns ok", health.json() == {"status": "ok"})
    check("POST /recommend without a token is refused", httpx.post(f"{ML_URL}/recommend", timeout=10).status_code == 401)
    check("POST /recommend with a made-up token is refused",
          httpx.post(f"{ML_URL}/recommend", headers={"Authorization": "Bearer not-a-real-token"}, timeout=10).status_code == 401)

    print("\n-- New Student (no activity)")
    summary, rows = recommendations_for("new.student@demo.example.com")
    show(rows)
    check("every recommendation is cold start", rows and all(r["source"] == "cold_start" for r in rows),
          f"{len(rows)} recommendation(s)")
    check("one introductory list per course", {r["topic"]["course"]["code"] for r in rows} == {"CSC 531", "CSC 574"})

    print("\n-- Active Student (one weak topic per course)")
    summary, rows = recommendations_for("active.student@demo.example.com")
    show(rows)
    check("every recommendation comes from the models", rows and all(r["source"] == "ml" for r in rows),
          f"model {summary['model_version']}")
    for code, weak_title in WEAK.items():
        first = next(r for r in rows if r["topic"]["course"]["code"] == code and r["rank"] == 1)
        check(f"{code}: weakest topic ranked first", first["topic"]["title"] == weak_title,
              f"#1 is {first['topic']['title']}, p={first['priority_score']:.2f}")

    print("\n-- Running again does not duplicate pending recommendations")
    _, again = recommendations_for("active.student@demo.example.com")
    check("same number of pending recommendations after a second run", len(again) == len(rows), f"{len(again)}")

    print("\n-- Results (simulated data)")
    expected = [
        "metrics_simulated_data.md", "metrics_holdout_simulated_data.csv", "metrics_cv5_simulated_data.csv",
        "confusion_logistic_regression_simulated_data.png", "confusion_random_forest_simulated_data.png",
        "model_comparison_simulated_data.png", "rf_feature_importances_simulated_data.png",
    ]
    missing = [f for f in expected if not (RESULTS / f).exists()]
    check("ml/results holds the metrics table and charts", not missing, "missing: " + ", ".join(missing) if missing else f"{len(expected)} files")

    print(f"\n{sum(results)}/{len(results)} checks passed")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
