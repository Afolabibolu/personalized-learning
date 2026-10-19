"""Exports real students' training rows to CSV, for train.py --real-test.

    python scripts/export_real_rows.py real_rows.csv

Real students are everyone except simulated students, the two demo accounts
and test accounts. Builds the same one-row-per-student-per-topic table as
training (features before the last attempt, label from the last attempt).
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ml"))
from app import data  # noqa: E402
from training.features import to_frames, training_rows  # noqa: E402

EXCLUDED_DOMAINS = ("@sim.example.com", "@demo.example.com", "@rls-check.example.com")


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 1
    db = data.service_client()
    users, page = [], 1
    while True:
        batch = db.auth.admin.list_users(page=page, per_page=1000)
        users += batch
        if len(batch) < 1000:
            break
        page += 1
    real = {u.id for u in users if u.email and not u.email.endswith(EXCLUDED_DOMAINS)}
    simulated = {r["id"] for r in data.fetch_all(lambda: db.table("profiles").select("id").eq("is_simulated", True).order("id"))}
    real -= simulated

    scores = [r for r in data.fetch_all(lambda: db.table("ml_attempt_topic_scores").select(
        "student_id, topic_id, attempt_id, completed_at, score").order("attempt_id").order("topic_id")) if r["student_id"] in real]
    logs = [r for r in data.fetch_all(lambda: db.table("study_logs").select(
        "student_id, topic_id, logged_at, duration_minutes").order("id")) if r["student_id"] in real]
    rows = training_rows(*to_frames(scores, logs))
    rows.to_csv(sys.argv[1], index=False)
    print(f"{len(rows)} rows from {rows['student_id'].nunique() if len(rows) else 0} real students -> {sys.argv[1]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
