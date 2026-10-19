"""Phase 1 check: two students try to read and write each other's data.

Signs in as students A and B with the anon key, gives B some activity, then has
A try everything it should not be able to do (and a few things it should).
Prints one line per check and exits non-zero if any check fails. All test
users and the test course are removed at the end.

    python scripts/rls_check.py
"""

import sys
from datetime import datetime, timezone
from pathlib import Path

from postgrest.exceptions import APIError

import testkit

results: list[tuple[bool, str, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((passed, name, detail))
    print(f"{'PASS' if passed else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""))


def refused(name: str, action) -> None:
    """Passes when the request errors, or touches no rows."""
    try:
        rows = action().data
    except APIError as e:
        check(name, True, f"refused: {e.code} {e.message}")
        return
    check(name, not rows, "0 rows" if not rows else f"returned {len(rows)} rows")


def allowed(name: str, action) -> None:
    try:
        rows = action().data
    except APIError as e:
        check(name, False, f"{e.code} {e.message}")
        return
    check(name, bool(rows), f"{len(rows)} row(s)")


def main() -> int:
    db = testkit.admin()
    fx = testkit.setup(db)
    try:
        a_id, a_email = testkit.create_student(db, "RLS Student A")
        b_id, b_email = testkit.create_student(db, "RLS Student B")
        a = testkit.sign_in(a_email)
        b = testkit.sign_in(b_email)

        # B's activity: a graded quiz, a study log and a recommendation.
        started = b.rpc("start_quiz", {"p_quiz_id": fx.topic_quiz_id}).execute().data
        b_attempt = started["attempt_id"]
        answers = {q["id"]: fx.correct[q["id"]] for q in started["questions"]}
        b.rpc("submit_quiz", {"p_attempt_id": b_attempt, "p_responses": answers}).execute()
        b.table("study_logs").insert({
            "student_id": b_id, "topic_id": fx.topic_ids["alpha"],
            "duration_minutes": 30, "activity_type": "reading",
        }).execute()
        rec = {"topic_id": fx.topic_ids["alpha"], "resource_id": fx.resource_id, "rank": 1, "source": "cold_start"}
        b_rec = db.table("recommendations").insert({**rec, "student_id": b_id}).execute().data[0]["id"]
        a_rec = db.table("recommendations").insert({**rec, "student_id": a_id}).execute().data[0]["id"]

        print("\n-- Sign-up trigger")
        profiles = db.table("profiles").select("id, full_name, is_simulated").in_("id", [a_id, b_id]).execute().data
        check("profile row created for each new user", len(profiles) == 2,
              ", ".join(f"{p['full_name']} is_simulated={p['is_simulated']}" for p in profiles))

        print("\n-- Student B reading own data (control)")
        allowed("B reads own profile", lambda: b.table("profiles").select("*").eq("id", b_id).execute())
        allowed("B reads own study logs", lambda: b.table("study_logs").select("*").eq("student_id", b_id).execute())
        allowed("B reads own quiz attempts", lambda: b.table("quiz_attempts").select("*").eq("student_id", b_id).execute())
        allowed("B reads own attempt answers", lambda: b.table("attempt_answers").select("*").eq("attempt_id", b_attempt).execute())
        allowed("B reads own recommendations", lambda: b.table("recommendations").select("*").eq("student_id", b_id).execute())

        print("\n-- Student A reading student B's data")
        refused("A reads B's profile", lambda: a.table("profiles").select("*").eq("id", b_id).execute())
        refused("A reads B's study logs", lambda: a.table("study_logs").select("*").eq("student_id", b_id).execute())
        refused("A reads B's quiz attempts", lambda: a.table("quiz_attempts").select("*").eq("student_id", b_id).execute())
        refused("A reads B's attempt answers", lambda: a.table("attempt_answers").select("*").eq("attempt_id", b_attempt).execute())
        refused("A reads B's recommendations", lambda: a.table("recommendations").select("*").eq("student_id", b_id).execute())
        refused("A opens B's quiz review", lambda: a.rpc("get_attempt_review", {"p_attempt_id": b_attempt}).execute())

        print("\n-- Questions are hidden")
        refused("A selects from questions", lambda: a.table("questions").select("*").execute())
        refused("B selects from questions (after taking a quiz)", lambda: b.table("questions").select("*").execute())
        a_started = a.rpc("start_quiz", {"p_quiz_id": fx.topic_quiz_id}).execute().data
        leaked = [k for q in a_started["questions"] for k in ("correct_answer", "explanation") if k in q]
        check("start_quiz returns no correct_answer or explanation", not leaked,
              f"{len(a_started['questions'])} questions, keys: {sorted(a_started['questions'][0])}")

        print("\n-- Writing scores and answers directly")
        now = datetime.now(timezone.utc).isoformat()
        refused("A inserts a quiz attempt with a made-up score", lambda: a.table("quiz_attempts").insert({
            "student_id": a_id, "quiz_id": fx.topic_quiz_id, "question_ids": [],
            "score": 100, "completed_at": now,
        }).execute())
        refused("A sets the score on own open attempt", lambda: a.table("quiz_attempts").update(
            {"score": 100, "completed_at": now}).eq("id", a_started["attempt_id"]).execute())
        refused("A inserts an attempt answer", lambda: a.table("attempt_answers").insert({
            "attempt_id": a_started["attempt_id"], "question_id": a_started["questions"][0]["id"],
            "response": [], "is_correct": True,
        }).execute())
        refused("A submits B's attempt", lambda: a.rpc("submit_quiz", {"p_attempt_id": b_attempt, "p_responses": {}}).execute())
        refused("B submits own completed attempt again", lambda: b.rpc("submit_quiz", {"p_attempt_id": b_attempt, "p_responses": answers}).execute())

        print("\n-- Study logs")
        refused("A logs a study session as B", lambda: a.table("study_logs").insert({
            "student_id": b_id, "topic_id": fx.topic_ids["alpha"], "duration_minutes": 30, "activity_type": "reading",
        }).execute())
        allowed("A logs own study session", lambda: a.table("study_logs").insert({
            "student_id": a_id, "topic_id": fx.topic_ids["alpha"], "duration_minutes": 30, "activity_type": "video",
        }).execute())

        print("\n-- Recommendations: status column only")
        refused("A changes status of B's recommendation", lambda: a.table("recommendations").update(
            {"status": "dismissed"}).eq("id", b_rec).execute())
        b_status = db.table("recommendations").select("status").eq("id", b_rec).execute().data[0]["status"]
        check("B's recommendation still pending", b_status == "pending", b_status)
        refused("A changes priority_score of own recommendation", lambda: a.table("recommendations").update(
            {"priority_score": 0.99}).eq("id", a_rec).execute())
        refused("A inserts a recommendation", lambda: a.table("recommendations").insert(
            {**rec, "student_id": a_id}).execute())
        allowed("A accepts own recommendation", lambda: a.table("recommendations").update(
            {"status": "accepted"}).eq("id", a_rec).execute())

        print("\n-- Notifications")
        b.rpc("generate_reminders").execute()
        b_notes = b.table("notifications").select("id").execute().data
        check("B has notifications to protect", bool(b_notes), f"{len(b_notes)}")
        refused("A reads B's notifications", lambda: a.table("notifications").select("*").eq("student_id", b_id).execute())
        refused("A marks B's notification read", lambda: a.table("notifications").update(
            {"read_at": now}).eq("id", b_notes[0]["id"]).execute())
        refused("A inserts a notification", lambda: a.table("notifications").insert(
            {"student_id": a_id, "kind": "score_improved", "title": "x", "body": "x"}).execute())
        refused("B changes the text of own notification", lambda: b.table("notifications").update(
            {"title": "changed"}).eq("id", b_notes[0]["id"]).execute())
        allowed("B marks own notification read", lambda: b.table("notifications").update(
            {"read_at": now}).eq("id", b_notes[0]["id"]).execute())
        refused("A updates B's reminder settings", lambda: a.table("profiles").update(
            {"daily_goal_minutes": 5}).eq("id", b_id).execute())

        print("\n-- Profiles and content")
        refused("A sets is_simulated on own profile", lambda: a.table("profiles").update(
            {"is_simulated": True}).eq("id", a_id).execute())
        allowed("A updates own department and level", lambda: a.table("profiles").update(
            {"department": "Computer Science", "level": 500}).eq("id", a_id).execute())
        allowed("A reads courses", lambda: a.table("courses").select("id").eq("code", testkit.COURSE_CODE).execute())
        refused("A inserts a course", lambda: a.table("courses").insert({"code": "HACK 1", "title": "x"}).execute())
        refused("A edits a topic", lambda: a.table("topics").update({"title": "x"}).eq("id", fx.topic_ids["alpha"]).execute())
        refused("Signed-out visitor reads courses", lambda: testkit.anon().table("courses").select("*").execute())
    finally:
        testkit.cleanup(db)

    failed = [r for r in results if not r[0]]
    print(f"\n{len(results) - len(failed)}/{len(results)} checks passed")
    return 1 if failed else 0


def save_report(output: str, path: Path) -> None:
    """Writes the run to Markdown for the results chapter (NFR3)."""
    passed = sum(ok for ok, _, _ in results)
    sections: dict[str, list[tuple[bool, str, str]]] = {}
    current = "General"
    for line in output.splitlines():
        if line.startswith("-- "):
            current = line[3:].strip()
        elif line.startswith(("PASS", "FAIL")):
            ok, rest = line.startswith("PASS"), line[4:].strip()
            name, _, detail = rest.partition("  (")
            sections.setdefault(current, []).append((ok, name.strip(), detail.rstrip(")")))
    rows = []
    for section, checks in sections.items():
        rows.append(f"\n### {section}\n\n| Result | Check | Detail |\n| --- | --- | --- |")
        rows += [f"| {'Pass' if ok else '**Fail**'} | {name} | {detail} |" for ok, name, detail in checks]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "# Security: row-level security check (NFR3)\n\n"
        f"Run {datetime.now().strftime('%Y-%m-%d %H:%M')} with `python scripts/rls_check.py --out {path.as_posix()}` "
        "against the live Supabase project. Two test students (A and B) sign in with the public anon key, the same key the web app "
        "uses, and try to read and change each other's data. A signed-out visitor is also tried. The test accounts and test course "
        "are deleted at the end.\n\n"
        f"**Result: {passed} of {len(results)} checks passed.** \"Refused\" means the database rejected the request "
        "(42501 is Postgres' permission-denied code); \"0 rows\" means row-level security hid the other student's rows.\n"
        + "\n".join(rows) + "\n"
    )


if __name__ == "__main__":
    import argparse
    import contextlib
    import io

    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, help="also save the results as Markdown, e.g. docs/results/security.md")
    args = parser.parse_args()
    buffer = io.StringIO()

    class Tee(io.TextIOBase):
        def write(self, text):
            buffer.write(text)
            return sys.__stdout__.write(text)

    with contextlib.redirect_stdout(Tee()):
        code = main()
    if args.out:
        save_report(buffer.getvalue(), args.out)
        print(f"Saved {args.out}")
    sys.exit(code)
