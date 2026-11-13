"""Exports the exact training data the models use, and a summary of the simulated dataset.

    cd ml && python -m training.export_dataset

Writes ml/results/training_data.csv: one row per simulated student and topic, built by
the same function train.py trains on (train.load_training_data), with the student's
number (1 to 80, from sim-NNN), course code, topic title, the six features, the label
score and requires_attention. Also writes ml/results/dataset_summary.md: counts of
simulated students, quiz attempts, answers, study logs, rows and rows requiring
attention, overall and split by study habit.

The database does not store each simulated student's habit. It is recovered by
replaying the seeded simulation (scripts/seed_demo.py with the config in
synthetic.py), and accepted only if the replay reproduces every student's number of
quiz attempts, answers and study logs exactly; otherwise the script stops.
"""

import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from app import data
from app.config import RESULTS_DIR
from training.features import FEATURES
from training.synthetic import CONFIG, SimCourse, SimTopic, simulate_student, topic_difficulties
from training.train import load_training_data

ROOT = Path(__file__).resolve().parents[2]
SIM_SUFFIX = "@sim.example.com"
HABIT_LABELS = {"steady": "Steady (often, short sessions)", "crammer": "Crammer (little, then hard before quizzes)",
                "rare": "Rare (seldom)"}


def student_numbers(db) -> dict[str, int]:
    """student_id -> N, from the sim-NNN@sim.example.com sign-up address."""
    numbers, page = {}, 1
    while True:
        users = db.auth.admin.list_users(page=page, per_page=1000)
        for u in users:
            if u.email and u.email.endswith(SIM_SUFFIX) and u.email.startswith("sim-"):
                numbers[u.id] = int(u.email.split("@")[0].removeprefix("sim-"))
        if len(users) < 1000:
            return numbers
        page += 1


def replay_simulation(db) -> list:
    """The simulated students in creation order (1 to N), replayed from the seed, exactly as seed_demo.py builds them."""
    sys.path.insert(0, str(ROOT / "scripts"))
    from seed_demo import load_content  # the reviewed courses the simulation is built on

    courses, topics, quizzes, questions = load_content(db)
    np_rng = np.random.default_rng(CONFIG.seed)
    difficulties = topic_difficulties(np_rng, len(topics))
    topic_quiz = {q["topic_id"]: q["id"] for q in quizzes if q["kind"] == "topic"}
    diag = {q["course_id"]: q["id"] for q in quizzes if q["kind"] == "diagnostic"}
    sim_courses = [
        SimCourse(c["id"], diag[c["id"]], [
            SimTopic(t["id"], c["id"], topic_quiz[t["id"]],
                     [q for q in questions if questions[q]["topic_id"] == t["id"]], difficulties[i])
            for i, t in enumerate(topics) if t["course_id"] == c["id"]
        ])
        for c in courses
    ]
    now = datetime.now(timezone.utc)  # only shifts timestamps; the random draws do not depend on it
    return [simulate_student(np_rng, sim_courses, now) for _ in range(CONFIG.students)]


def main() -> int:
    db = data.service_client()
    rows = load_training_data()  # the rows train.py fits and scores
    numbers = student_numbers(db)

    topics = {t["id"]: t for t in data.fetch_all(lambda: db.table("topics").select("id, title, course_id, sequence_order").order("id"))}
    codes = {c["id"]: c["code"] for c in db.table("courses").select("id, code").execute().data}

    # Actual counts per simulated student, to check the replay against.
    sim_ids = set(numbers)
    attempts = [a for a in data.fetch_all(lambda: db.table("quiz_attempts").select("id, student_id").not_.is_("completed_at", "null")
                                          .order("id")) if a["student_id"] in sim_ids]
    attempt_owner = {a["id"]: a["student_id"] for a in attempts}
    answers = Counter()
    for chunk in range(0, len(attempts), 200):
        ids = [a["id"] for a in attempts[chunk:chunk + 200]]
        for r in data.fetch_all(lambda: db.table("attempt_answers").select("id, attempt_id").in_("attempt_id", ids).order("id")):
            answers[attempt_owner[r["attempt_id"]]] += 1
    logs = Counter(r["student_id"] for r in data.fetch_all(
        lambda: db.table("study_logs").select("id, student_id").order("id")) if r["student_id"] in sim_ids)
    actual = {sid: (Counter(a["student_id"] for a in attempts)[sid], answers[sid], logs[sid]) for sid in sim_ids}

    replay = replay_simulation(db)
    by_number = {n: sid for sid, n in numbers.items()}
    if sorted(by_number) != list(range(1, len(replay) + 1)):
        raise SystemExit(f"Expected simulated students 1 to {len(replay)}, found {len(by_number)}. Was seed_demo.py run with other settings?")
    habit = {}
    mismatched = []
    for n, student in enumerate(replay, start=1):
        sid = by_number[n]
        expected = (len(student.attempts), sum(len(a.answers) for a in student.attempts), len(student.logs))
        if expected != actual[sid]:
            mismatched.append(f"sim-{n:03d}: replay {expected}, database {actual[sid]}")
        habit[sid] = student.habit.split(":")[0]
    if mismatched:
        raise SystemExit("The replay does not reproduce the database, so habits cannot be recovered:\n  " + "\n  ".join(mismatched[:10]))
    print(f"Replay matches all {len(replay)} simulated students (attempts, answers and study logs per student)")

    out = pd.DataFrame({
        "student": rows["student_id"].map(numbers),
        "habit": rows["student_id"].map(habit),
        "course_code": rows["topic_id"].map(lambda t: codes[topics[t]["course_id"]]),
        "topic_order": rows["topic_id"].map(lambda t: topics[t]["sequence_order"]),
        "topic_title": rows["topic_id"].map(lambda t: topics[t]["title"]),
        **{f: rows[f] for f in FEATURES},
        "label_score": rows["label_score"],
        "requires_attention": rows["requires_attention"],
    }).sort_values(["student", "course_code", "topic_order"]).drop(columns="topic_order")
    for f in ("mean_score", "last_score", "label_score", "total_minutes", "days_since_last_studied"):
        out[f] = out[f].round(4)
    path = RESULTS_DIR / "training_data.csv"
    out.to_csv(path, index=False)
    print(f"Wrote {path.relative_to(ROOT)}: {len(out)} rows, {out['requires_attention'].sum()} requiring attention")

    # Summary, overall and per habit.
    table = []
    for key in [*HABIT_LABELS, None]:
        ids = [s for s in sim_ids if key is None or habit[s] == key]
        part = out[out["habit"] == key] if key else out
        n_rows, n_pos = len(part), int(part["requires_attention"].sum())
        table.append([HABIT_LABELS.get(key, "**All**"), len(ids), sum(actual[s][0] for s in ids), sum(actual[s][1] for s in ids),
                      sum(actual[s][2] for s in ids), n_rows, n_pos, f"{n_pos / n_rows:.1%}" if n_rows else "-"])
    head = ["Study habit", "Students", "Quiz attempts", "Answers", "Study logs", "Rows", "Rows requiring attention", "Share"]
    lines = ["| " + " | ".join(head) + " |", "| " + " | ".join("---" for _ in head) + " |",
             *("| " + " | ".join(str(v) for v in r) + " |" for r in table)]
    summary = f"""# Training dataset

All figures come from simulated students created by `scripts/seed_demo.py` (rules in `simulation_rules.md`), not from real students.

The models are trained on `training_data.csv`: one row per simulated student and topic, {len(out)} rows. Features come only from
attempts and study logs before the student's last attempt on the topic; that last attempt gives `label_score`, and
`requires_attention` is 1 when it is below 50%. Student-topic pairs with a single attempt have no next attempt and are left out
(none here: every student took a diagnostic and at least one later quiz on each topic). Courses: CSC 531 and CSC 574 (the reviewed
courses), {out['topic_title'].nunique()} topics.

Counts of quiz attempts (diagnostics included), answers and study logs are for the simulated students only.

{chr(10).join(lines)}

Each student's habit is not stored in the database; it was recovered by replaying the seeded simulation (seed {CONFIG.seed}),
which reproduced every student's number of quiz attempts, answers and study logs exactly.

Columns of `training_data.csv`: student (1 to {CONFIG.students}, from sim-NNN), habit, course_code, topic_title, {", ".join(FEATURES)},
label_score, requires_attention.
"""
    (RESULTS_DIR / "dataset_summary.md").write_text(summary)
    print(f"Wrote ml/results/dataset_summary.md")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
