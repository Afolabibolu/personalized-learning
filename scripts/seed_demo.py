"""Creates the simulated students and the two demo accounts.

    python scripts/seed_demo.py [--students N] [--seed N]   (defaults from the simulation config)
    python scripts/seed_demo.py --demo-only    # reset just the two demo accounts

Run after content/load.py (simulated answers point to real questions). Uses
the service role key from scripts/.env. Every user is created through the
Supabase admin API, so each has a real auth user and profile row.

  - About 80 simulated students (is_simulated = true) with six weeks of quiz
    attempts and study logs from ml/training/synthetic.py, whose config block
    holds every rule and parameter. Training data only. Also writes
    ml/results/simulation_rules.md describing those rules for Chapter Four.
  - "New Student": no activity, to show cold start.
  - "Active Student": a history where one topic per course is clearly weak,
    to show ML recommendations.

Running it again deletes everything it created before and starts over.
--demo-only resets only the two demo accounts (for example after trying them
out before a presentation) and leaves the simulated students alone.
"""

import argparse
import dataclasses
import os
import random
import sys
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path

import numpy as np
from dotenv import load_dotenv
from supabase import Client, create_client

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ml"))
from training.synthetic import (  # noqa: E402
    CONFIG,
    SimAttempt,
    SimCourse,
    SimStudent,
    SimStudyLog,
    SimTopic,
    describe_rules,
    simulate_student,
    topic_difficulties,
)

load_dotenv(Path(__file__).parent / ".env")

SIM_DOMAIN = "sim.example.com"
DEMO_DOMAIN = "demo.example.com"
SIM_PASSWORD = "Simulated-2026!"
DEMO_PASSWORD = "DemoPass2026!"
NEW_STUDENT = ("Kemi Balogun", f"new.student@{DEMO_DOMAIN}")
ACTIVE_STUDENT = ("Tolu Adeyemi", f"active.student@{DEMO_DOMAIN}")
# Preferred ways to study (FR1); the engine prefers these resource types.
NEW_PREFERENCES = ["lecture", "video"]
ACTIVE_PREFERENCES = ["note", "past_questions"]
STUDY_TYPES = ["note", "lecture", "past_questions", "video"]
# The Active Student's clearly weak topic in each course (by slug).
WEAK_TOPICS = {"CSC 531": "cognitive-psychology", "CSC 574": "fuzzy-logic"}
BATCH = 500


def admin() -> Client:
    return create_client(os.environ["SUPABASE_URL"], os.environ["SUPABASE_SERVICE_ROLE_KEY"])


def reset(db: Client, domains: tuple[str, ...] = (SIM_DOMAIN, DEMO_DOMAIN)) -> int:
    """Deletes every user on the given email domains; their data cascades with them."""
    suffixes = tuple(f"@{d}" for d in domains)
    removed, page = 0, 1
    while True:
        users = db.auth.admin.list_users(page=page, per_page=1000)
        for user in users:
            if user.email and user.email.endswith(suffixes):
                db.auth.admin.delete_user(user.id)
                removed += 1
        if len(users) < 1000:
            return removed
        page += 1


def load_content(db: Client):
    """The reviewed courses (CSC 531, CSC 574) only: the simulation and the demo accounts are built on them,
    so sample courses added later through the pipeline change neither the training data nor the demo."""
    courses = db.table("courses").select("id, code").eq("is_reviewed", True).order("code").execute().data
    ids = {c["id"] for c in courses}
    topics = [t for t in db.table("topics").select("id, course_id, slug, sequence_order").order("sequence_order").execute().data
              if t["course_id"] in ids]
    topic_ids = {t["id"] for t in topics}
    quizzes = [q for q in db.table("quizzes").select("id, course_id, topic_id, kind").execute().data if q["course_id"] in ids]
    questions = [q for q in db.table("questions").select("id, topic_id, options, correct_answer").eq("status", "approved")
                 .in_("topic_id", list(topic_ids)).execute().data]
    if not questions:
        raise SystemExit("No approved questions. Run python content/load.py first.")
    return courses, topics, quizzes, {q["id"]: q for q in questions}


def create_user(db: Client, name: str, email: str, password: str, simulated: bool, rng: random.Random,
                preferences: list[str] | None = None) -> str:
    user = db.auth.admin.create_user({
        "email": email,
        "password": password,
        "email_confirm": True,
        "user_metadata": {"full_name": name},
        "app_metadata": {"is_simulated": simulated},
    }).user
    # Set is_simulated here too: the admin API writes app_metadata after the
    # auth user row is inserted, so the sign-up trigger does not see it.
    db.table("profiles").update({
        "is_simulated": simulated,
        "department": "Computer Science",
        "level": 500,
        "learning_preferences": preferences or rng.sample(STUDY_TYPES, k=rng.randint(1, 3)),
    }).eq("id", user.id).execute()
    return user.id


def response_for(question: dict, correct: bool, rng: random.Random) -> list[str]:
    if correct:
        return list(question["correct_answer"])
    wrong = [o["key"] for o in question["options"] if o["key"] not in question["correct_answer"]]
    return [rng.choice(wrong)]


def rows_for(student_id: str, student: SimStudent, questions: dict, rng: random.Random):
    attempts, answers, logs = [], [], []
    for a in student.attempts:
        attempts.append({
            "id": a.id,
            "student_id": student_id,
            "quiz_id": a.quiz_id,
            "question_ids": [q for q, _ in a.answers],
            "score": a.score,
            "started_at": a.started_at.isoformat(),
            "completed_at": a.completed_at.isoformat(),
        })
        for question_id, ok in a.answers:
            answers.append({
                "attempt_id": a.id,
                "question_id": question_id,
                "response": response_for(questions[question_id], ok, rng),
                "is_correct": ok,
            })
    for log in student.logs:
        logs.append({
            "student_id": student_id,
            "topic_id": log.topic_id,
            "duration_minutes": log.duration_minutes,
            "activity_type": log.activity_type,
            "logged_at": log.logged_at.isoformat(),
        })
    return attempts, answers, logs


def insert(db: Client, table: str, rows: list[dict]) -> None:
    for i in range(0, len(rows), BATCH):
        db.table(table).insert(rows[i:i + BATCH]).execute()


def active_student_history(courses, topics, quizzes, questions, now: datetime, rng: random.Random) -> SimStudent:
    """Three weeks of steady work, except one weak, never-studied topic per course."""
    student = SimStudent()
    by_topic: dict[str, list[str]] = {}
    for q in questions.values():
        by_topic.setdefault(q["topic_id"], []).append(q["id"])
    diag = {q["course_id"]: q["id"] for q in quizzes if q["kind"] == "diagnostic"}
    topic_quiz = {q["topic_id"]: q["id"] for q in quizzes if q["kind"] == "topic"}
    code = {c["id"]: c["code"] for c in courses}

    def attempt(quiz_id: str, picks: list[tuple[str, int, int]], days_ago: float) -> None:
        """picks: (topic_id, questions, correct)."""
        started = now - timedelta(days=days_ago)
        answers = []
        for topic_id, n, correct in picks:
            for i, q in enumerate(rng.sample(by_topic[topic_id], n)):
                answers.append((q, i < correct))
        student.attempts.append(SimAttempt(str(uuid.uuid4()), quiz_id, started, started + timedelta(minutes=8), answers))

    for course in courses:
        course_topics = [t for t in topics if t["course_id"] == course["id"]]
        weak = {t["id"] for t in course_topics if t["slug"] == WEAK_TOPICS.get(code[course["id"]])}
        attempt(diag[course["id"]], [(t["id"], 3, 0 if t["id"] in weak else rng.choice([2, 3])) for t in course_topics], 21)
        for t in course_topics:
            if t["id"] in weak:
                attempt(topic_quiz[t["id"]], [(t["id"], 5, 1)], 12)
                attempt(topic_quiz[t["id"]], [(t["id"], 5, 2)], 4)
            else:
                attempt(topic_quiz[t["id"]], [(t["id"], 5, rng.choice([4, 5]))], 14)
                attempt(topic_quiz[t["id"]], [(t["id"], 5, rng.choice([4, 5]))], 5)
                for days_ago in (18, 11, 6, rng.choice([1, 2])):
                    student.logs.append(SimStudyLog(
                        t["id"], rng.choice([30, 45, 60]), rng.choice(["reading", "video", "practice"]),
                        now - timedelta(days=days_ago, hours=rng.uniform(0, 8))))
    student.attempts.sort(key=lambda a: a.started_at)
    return student


def history_notifications(student_id: str, history: SimStudent, questions: dict, topic_titles: dict) -> list[dict]:
    """A few already-read notifications for the Active Student, computed from its own history
    (so the numbers are real): its biggest score improvement and a day it met its 30-minute goal."""
    topic_of = {qid: q["topic_id"] for qid, q in questions.items()}
    per_topic: dict[str, list[tuple[datetime, float]]] = {}
    for a in history.attempts:
        by_topic: dict[str, list[bool]] = {}
        for qid, ok in a.answers:
            by_topic.setdefault(topic_of[qid], []).append(ok)
        for topic_id, oks in by_topic.items():
            per_topic.setdefault(topic_id, []).append((a.completed_at, 100.0 * sum(oks) / len(oks)))
    notes = []
    best = max(
        ((t, s[-2][1], s[-1][1], s[-1][0]) for t, s in ((t, sorted(v)) for t, v in per_topic.items()) if len(s) >= 2),
        key=lambda x: x[2] - x[1], default=None)
    if best and best[2] - best[1] >= 20:
        topic_id, before, after, when = best
        notes.append({"kind": "score_improved", "title": "Score improved",
                      "body": f"{topic_titles[topic_id]}: {round(before)}% to {round(after)}%, up {round(after - before)} points.",
                      "link": f"/topics/{topic_id}", "created_at": (when + timedelta(minutes=1)).isoformat()})
    minutes_by_day: dict = {}
    for log in history.logs:
        minutes_by_day[log.logged_at.date()] = minutes_by_day.get(log.logged_at.date(), 0) + log.duration_minutes
    goal_days = sorted(d for d, m in minutes_by_day.items() if m >= 30)
    if goal_days:
        day = goal_days[-1]
        last = max(log.logged_at for log in history.logs if log.logged_at.date() == day)
        notes.append({"kind": "daily_goal_reached", "title": "Daily goal reached",
                      "body": f"You studied {minutes_by_day[day]} minutes today (goal: 30). Nice work.",
                      "link": "/", "created_at": (last + timedelta(minutes=1)).isoformat()})
    return [{**n, "student_id": student_id, "read_at": n["created_at"]} for n in notes]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--students", type=int, default=CONFIG.students)
    parser.add_argument("--seed", type=int, default=CONFIG.seed)
    parser.add_argument("--demo-only", action="store_true", help="reset only the two demo accounts")
    args = parser.parse_args()

    db = admin()
    if args.demo_only:
        print(f"Removed {reset(db, (DEMO_DOMAIN,))} demo users")
    else:
        print(f"Removed {reset(db)} existing simulated and demo users")

    courses, topics, quizzes, questions = load_content(db)
    np_rng = np.random.default_rng(args.seed)
    rng = random.Random(args.seed)
    now = datetime.now(timezone.utc)

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

    all_attempts, all_answers, all_logs = [], [], []
    for n in range(1, 0 if args.demo_only else args.students + 1):
        student_id = create_user(db, f"Simulated Student {n:03d}", f"sim-{n:03d}@{SIM_DOMAIN}", SIM_PASSWORD, True, rng)
        a, ans, logs = rows_for(student_id, simulate_student(np_rng, sim_courses, now), questions, rng)
        all_attempts += a
        all_answers += ans
        all_logs += logs
        if n % 20 == 0:
            print(f"  created {n} simulated students")

    create_user(db, *NEW_STUDENT, DEMO_PASSWORD, False, rng, NEW_PREFERENCES)
    active_id = create_user(db, *ACTIVE_STUDENT, DEMO_PASSWORD, False, rng, ACTIVE_PREFERENCES)
    active_history = active_student_history(courses, topics, quizzes, questions, now, rng)
    a, ans, logs = rows_for(active_id, active_history, questions, rng)
    all_attempts += a
    all_answers += ans
    all_logs += logs

    insert(db, "quiz_attempts", all_attempts)
    insert(db, "attempt_answers", all_answers)
    insert(db, "study_logs", all_logs)
    titles = {t["id"]: t["title"] for t in db.table("topics").select("id, title").execute().data}
    seeded = history_notifications(active_id, active_history, questions, titles)
    if seeded:
        insert(db, "notifications", seeded)

    simulated = "no simulated students (--demo-only)" if args.demo_only else f"{args.students} simulated students"
    print(f"\nInserted {len(all_attempts)} quiz attempts, {len(all_answers)} answers and {len(all_logs)} study logs "
          f"for {simulated} and the Active Student.")
    if not args.demo_only:
        rules = Path(__file__).resolve().parent.parent / "ml" / "results" / "simulation_rules.md"
        rules.parent.mkdir(exist_ok=True)
        rules.write_text(describe_rules(dataclasses.replace(CONFIG, students=args.students, seed=args.seed)))
        print(f"Wrote {rules.relative_to(rules.parents[2])}")
    print("Weak topics for the Active Student: " + ", ".join(f"{c} {s}" for c, s in WEAK_TOPICS.items()))
    print("\nDemo logins (password for both: " + DEMO_PASSWORD + ")")
    print(f"  {NEW_STUDENT[0]:15} {NEW_STUDENT[1]}    no activity -> cold start (prefers lecture slides, videos)")
    print(f"  {ACTIVE_STUDENT[0]:15} {ACTIVE_STUDENT[1]} weak topics -> ML recommendations (prefers notes, practice questions)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
