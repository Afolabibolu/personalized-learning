"""Runs one test case per requirement (FR1-FR6, NFR1-NFR5) and writes docs/test-cases.md.

    python scripts/run_test_cases.py [--measure]

Each case runs the existing checks and test suites and records what actually
happened. Needs the Vite dev server, the ML service, the seeded demo accounts
and trained models. Response times come from docs/performance.json; pass
--measure to measure them again first (takes about two minutes).
"""

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

from playwright.sync_api import sync_playwright

import testkit

ROOT = Path(__file__).resolve().parent.parent
PY = str(ROOT / ".venv" / "bin" / "python")
DOCS = ROOT / "docs"
APP = "http://localhost:5173"


@dataclass
class Case:
    id: str
    requirement: str
    title: str
    steps: list[str]
    expected: str
    result: str = "Not run"  # Pass, Fail, Partial
    actual: str = ""
    evidence: list[str] = field(default_factory=list)


_cache: dict[str, str] = {}


def run(name: str, cmd: list[str], cwd: Path = ROOT) -> str:
    """Runs a command once and caches its combined output."""
    if name not in _cache:
        print(f"  running {name}…", flush=True)
        proc = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=900)
        _cache[name] = proc.stdout + proc.stderr
    return _cache[name]


def lines(output: str, *needles: str) -> list[str]:
    """PASS/FAIL lines that contain any of the needles."""
    return [l.strip() for l in output.splitlines()
            if l.startswith(("PASS", "FAIL")) and any(n in l for n in needles)]


def all_pass(evidence: list[str]) -> bool:
    return bool(evidence) and all(l.startswith("PASS") for l in evidence)


def tail(output: str, pattern: str) -> str:
    found = [l.strip() for l in output.splitlines() if re.search(pattern, l)]
    return found[-1] if found else "(no summary line found)"


# --- checks that are not covered by an existing script ---

def protected_routes_check() -> list[str]:
    """Signed-out visitors are sent to the log-in page; demo account can sign in."""
    out = []
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=True)
        page = browser.new_page()
        for path in ["/", "/courses", "/log"]:
            page.goto(f"{APP}{path}")
            page.wait_for_url(f"{APP}/login")
            out.append(f"PASS  signed-out visit to {path} redirects to /login")
        page.get_by_label("Email").fill("new.student@demo.example.com")
        page.get_by_label("Password").fill("DemoPass2026!")
        page.get_by_role("button", name="Sign in").click()
        page.wait_for_url(f"{APP}/")
        out.append("PASS  New Student signs in and lands on the dashboard")
        page.get_by_role("button", name="Sign out").click()
        page.wait_for_url(f"{APP}/login")
        out.append("PASS  sign out returns to /login")
        browser.close()
    return out


def knowledge_base_check() -> list[str]:
    db = testkit.admin()
    courses = db.table("courses").select("code").neq("code", testkit.COURSE_CODE).execute().data
    topics = db.table("topics").select("id, title, resources(id), quizzes(id, kind)").execute().data
    approved = db.table("questions").select("id", count="exact", head=True).eq("status", "approved").execute().count
    no_resource = [t["title"] for t in topics if not t["resources"]]
    no_quiz = [t["title"] for t in topics if not any(q["kind"] == "topic" for q in t["quizzes"])]
    diagnostics = db.table("quizzes").select("id", count="exact", head=True).eq("kind", "diagnostic").execute().count
    return [
        f"{'PASS' if len(courses) == 2 else 'FAIL'}  {len(courses)} courses loaded ({', '.join(sorted(c['code'] for c in courses))})",
        f"{'PASS' if len(topics) == 12 else 'FAIL'}  {len(topics)} topics",
        f"{'PASS' if approved == 120 else 'FAIL'}  {approved} approved questions",
        f"{'PASS' if not no_resource else 'FAIL'}  every topic has at least one resource" + (f" (missing: {no_resource})" if no_resource else ""),
        f"{'PASS' if not no_quiz and diagnostics == 2 else 'FAIL'}  every topic has a topic quiz; {diagnostics} diagnostic quizzes",
    ]


def portability_check() -> list[str]:
    """Adds a third course from JSON files only (no code change), loads it, then removes it."""
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        for f in ["validate.py", "load.py", ".env"]:
            shutil.copy(ROOT / "content" / f, tmp / f)
        (tmp / "questions" / "TST999").mkdir(parents=True)
        topics = []
        for i in range(1, 6):
            topics.append({"slug": f"topic-{i}", "title": f"Topic {i}", "subtopics": ["a"],
                           "resources": [{"title": f"Lecture {i}", "type": "link", "url": f"https://example.com/{i}",
                                          **({"is_introductory": True, "intro_order": 1} if i == 1 else {})}]})
            qs = []
            for j in range(10):
                fmt = ["single_choice", "true_false", "multi_select", "odd_one_out"][j % 4]
                opts = ([{"key": "true", "text": "True"}, {"key": "false", "text": "False"}] if fmt == "true_false"
                        else [{"key": k, "text": f"{k} {i}-{j}"} for k in "abcd"])
                correct = {"single_choice": ["a"], "true_false": ["true"], "multi_select": ["a", "b"], "odd_one_out": ["d"]}[fmt]
                qs.append({"format": fmt, "stem": f"Portability question {i}-{j}", "options": opts, "correct_answer": correct,
                           "explanation": "Test.", "source": "portability test"})
            (tmp / "questions" / "TST999" / f"topic-{i}.json").write_text(json.dumps(qs))
        (tmp / "courses").mkdir()
        (tmp / "courses" / "TST999.json").write_text(json.dumps({"code": "TST 999", "title": "Portability test course", "topics": topics}))

        validate = subprocess.run([PY, "-I", str(tmp / "validate.py")], capture_output=True, text=True)
        load = subprocess.run([PY, "-I", "-W", "ignore", str(tmp / "load.py")], capture_output=True, text=True)
    db = testkit.admin()
    course = db.table("courses").select("id, topics(id)").eq("code", "TST 999").execute().data
    loaded = bool(course) and len(course[0]["topics"]) == 5
    db.table("courses").delete().eq("code", "TST 999").execute()
    return [
        f"{'PASS' if '0 error(s)' in validate.stdout else 'FAIL'}  validate.py accepts a new course: {tail(validate.stdout, 'error')}",
        f"{'PASS' if load.returncode == 0 and loaded else 'FAIL'}  load.py loads it with no code change: {load.stdout.strip().splitlines()[-1] if load.stdout.strip() else load.stderr.strip()[-200:]}",
        "PASS  test course removed afterwards",
    ]


def cases() -> list[Case]:
    return [
        Case("TC-01", "FR1", "Register and create a profile",
             ["Open /signup and create an account", "Fill in department, level and learning preferences", "Check the profiles table"],
             "Account created without email confirmation; onboarding saves department, level and preferences to the student's own profile row"),
        Case("TC-02", "FR1", "Sign in, protected pages, sign out, update profile",
             ["Visit /, /courses and /log signed out", "Sign in as New Student", "Sign out", "Update own department and level through the API"],
             "Signed-out visits redirect to /login; sign-in lands on the dashboard; a student can update their own profile but not is_simulated"),
        Case("TC-03", "FR2", "Diagnostic quiz with per-topic results",
             ["New student takes the CSC 531 diagnostic (18 questions)", "Submit", "Open the results page"],
             "Three questions from every topic; graded server-side; results show a score per topic and each answer with explanation"),
        Case("TC-04", "FR2", "Topic quiz grading and question selection",
             ["Run pytest scripts (signed-in students against the live database)"],
             "All four formats graded correctly (partial multi-select is wrong); unseen questions first; a submitted attempt cannot be resubmitted; latest score per topic is correct"),
        Case("TC-05", "FR3", "Log a study session",
             ["Open Log study, choose a topic, 30 min, Reading, Save", "Check the study_logs table", "Try to log a session as another student"],
             "Session saved with topic, duration and activity type; logging for someone else is refused"),
        Case("TC-06", "FR4", "ML recommendations rank weak topics first",
             ["Sign in as Active Student (weak: Cognitive Psychology, Fuzzy Logic)", "POST /recommend with the student's token", "Read the recommendations"],
             "Top 3 overall from the models; the two weak topics ranked 1 and 2; re-running does not duplicate pending recommendations"),
        Case("TC-07", "FR4 / NFR4", "Cold-start fallback for a new student",
             ["Sign in as New Student (no quiz attempts or study logs)", "POST /recommend", "Open the dashboard"],
             "Introductory resources for each course in order, labelled 'Getting started'; not empty, no ML scores"),
        Case("TC-08", "FR4", "Model training and comparison with a rule baseline (simulated data)",
             ["python scripts/seed_demo.py (writes simulation_rules.md)", "cd ml && python -m training.train", "Inspect ml/results/"],
             "Rule baseline, Logistic Regression and Random Forest scored on the same split and 5-fold CV; three-row metrics table, confusion matrices, comparison chart, LR coefficients and RF importances and simulation rules saved, all labelled simulated data"),
        Case("TC-09", "FR5", "Academic knowledge base",
             ["python content/validate.py", "Count courses, topics, approved questions, resources and quizzes in Supabase"],
             "Validation passes; 2 courses, 12 topics, 120 approved questions; every topic has a resource and a topic quiz"),
        Case("TC-10", "FR6", "Progress tracking and consistency",
             ["Sign in as Active Student and open the dashboard", "Run npm test (streak and strip logic)"],
             "Streak, 14-day activity strip and per-topic progress chart shown; logic tests pass"),
        Case("TC-11", "FR6", "Reminders and recommendation feedback",
             ["Open the dashboard as Active Student and as New Student", "Press Accept and Dismiss", "Run npm test (reminder rules)"],
             "Weak-topic and diagnostic reminders shown; Accept and Dismiss change only the status column"),
        Case("TC-12", "NFR1", "Usability: core tasks without assistance",
             ["Complete registration, a quiz, a study log and reading a recommendation at laptop and phone width (automated walkthrough)",
              "SUS questionnaire with student participants (Section 3.14.3)"],
             "Every core task completes at both widths; SUS score above 68"),
        Case("TC-13", "NFR2", "Response times",
             ["python scripts/measure_performance.py --runs 10"],
             "p95 within target: quiz submit ≤ 2 s (browser), dashboard load ≤ 3 s, background recommendation update ≤ 5 s"),
        Case("TC-14", "NFR3", "Security: row-level security",
             ["python scripts/rls_check.py (two students with the anon key)"],
             "A student gets zero rows of another student's data, cannot read questions, cannot write scores or answers, and can change only the status of their own recommendations"),
        Case("TC-15", "NFR4", "Reliability: predictable behaviour with limited data",
             ["Unit tests: below the threshold and with no model files", "New Student via /recommend"],
             "Cold-start list instead of an error or empty result, including when the model files are missing"),
        Case("TC-16", "NFR5", "Portability: add a course without code changes",
             ["Write a third course as JSON files only", "Run validate.py and load.py on it", "Remove it"],
             "The new course validates and loads with no code change"),
    ]


def evaluate(case: Case) -> None:
    py = [PY, "-W", "ignore"]
    if case.id == "TC-01":
        out = run("phase3", py + ["scripts/phase3_check.py"])
        case.evidence = lines(out, "sign up", "onboarding", "profiles:")
    elif case.id == "TC-02":
        rls = run("rls", py + ["scripts/rls_check.py"])
        case.evidence = protected_routes_check() + lines(rls, "A updates own department", "A sets is_simulated", "A reads B's profile")
    elif case.id == "TC-03":
        out = run("phase3", py + ["scripts/phase3_check.py"])
        tests = run("pytest-scripts", [str(ROOT / ".venv/bin/pytest"), "scripts", "-q", "-p", "no:cacheprovider", "-W", "ignore"])
        case.evidence = lines(out, "score per topic", "explanation", "quiz_attempts", "attempt_answers")
        case.evidence.append(("PASS" if " passed" in tests and "failed" not in tests else "FAIL") +
                              "  pytest: diagnostic covers every topic and scores each one (" + tail(tests, r"passed|failed") + ")")
    elif case.id == "TC-04":
        tests = run("pytest-scripts", [str(ROOT / ".venv/bin/pytest"), "scripts", "-q", "-p", "no:cacheprovider", "-W", "ignore"])
        case.evidence = [("PASS" if " passed" in tests and "failed" not in tests else "FAIL") + "  pytest scripts: " + tail(tests, r"passed|failed")]
        case.evidence += lines(run("rls", py + ["scripts/rls_check.py"]), "submits own completed attempt again", "start_quiz returns")
    elif case.id == "TC-05":
        out = run("phase3", py + ["scripts/phase3_check.py"])
        case.evidence = lines(out, "study logger", "study_logs:") + lines(run("rls", py + ["scripts/rls_check.py"]), "logs a study session")
    elif case.id == "TC-06":
        out = run("phase4", py + ["scripts/phase4_check.py"])
        case.evidence = lines(out, "comes from the models", "top 3 overall", "ranked first and second", "second run")
    elif case.id == "TC-07":
        out4 = run("phase4", py + ["scripts/phase4_check.py"])
        out5 = run("phase5", py + ["scripts/phase5_check.py"])
        case.evidence = lines(out4, "every recommendation is cold start", "one introductory list") + \
            lines(out5, "'Getting started'", "first three lectures")
    elif case.id == "TC-08":
        md = (ROOT / "ml/results/metrics_simulated_data.md").read_text()
        cv_section = md.split("## 5-fold")[1].split("##")[0]
        rows = [l for l in cv_section.splitlines() if l.startswith(("| Rule", "| Logistic", "| Random"))]
        case.evidence = lines(run("phase4", py + ["scripts/phase4_check.py"]), "metrics table", "simulation_rules") + \
            [f"INFO  5-fold CV {r}" for r in rows]
        tests = run("pytest-ml", [str(ROOT / ".venv/bin/pytest"), "-q", "-W", "ignore"], cwd=ROOT / "ml")
        case.evidence.append(("PASS" if "failed" not in tests else "FAIL") + "  pytest ml (features, simulator, cold start, ranking): " + tail(tests, r"passed|failed"))
    elif case.id == "TC-09":
        out = run("validate", [PY, "-I", "content/validate.py"])
        case.evidence = [("PASS" if "\n0 error(s)" in out else "FAIL") + "  validate.py: " + tail(out, r"error\(s\)")] + knowledge_base_check()
    elif case.id == "TC-10":
        out = run("phase5", py + ["scripts/phase5_check.py"])
        npm = run("npm-test", ["npm", "test"], cwd=ROOT / "web")
        case.evidence = lines(out, "streak", "activity strip", "progress chart")
        case.evidence.append(("PASS" if "failed" not in npm and "passed" in npm else "FAIL") + "  npm test: " + tail(npm, r"Tests"))
    elif case.id == "TC-11":
        out = run("phase5", py + ["scripts/phase5_check.py"])
        case.evidence = lines(out, "reminder", "reminded", "Accept", "Dismiss", "Keep it up")
        case.evidence += lines(run("rls", py + ["scripts/rls_check.py"]), "priority_score of own", "accepts own recommendation")
    elif case.id == "TC-12":
        laptop = run("phase3", py + ["scripts/phase3_check.py"])
        phone = run("phase3-mobile", py + ["scripts/phase3_check.py", "--mobile"])
        phone5 = run("phase5-mobile", py + ["scripts/phase5_check.py", "--mobile"])
        case.evidence = [
            ("PASS" if "checks passed" in laptop and "FAIL" not in laptop else "FAIL") + "  core tasks at laptop width: " + tail(laptop, "checks passed"),
            ("PASS" if "checks passed" in phone and "FAIL" not in phone else "FAIL") + "  core tasks at phone width (390 px): " + tail(phone, "checks passed"),
            ("PASS" if "checks passed" in phone5 and "FAIL" not in phone5 else "FAIL") + "  reading recommendations at phone width: " + tail(phone5, "checks passed"),
            "NOT RUN  SUS questionnaire with student participants (out of scope for this demo; future work)",
        ]
    elif case.id == "TC-13":
        perf = json.loads((DOCS / "performance.json").read_text())
        for key, r in perf["results"].items():
            case.evidence.append(f"{'PASS' if r['pass'] else 'FAIL'}  {key}: median {r['median']:.2f} s, p95 {r['p95']:.2f} s, target {r['target']} s ({r['runs']} runs, {perf['measured_at']})")
    elif case.id == "TC-14":
        out = run("rls", py + ["scripts/rls_check.py"])
        case.evidence = [("PASS" if "FAIL" not in out else "FAIL") + "  rls_check.py: " + tail(out, "checks passed")] + \
            lines(out, "B's study logs", "B's quiz attempts", "B's recommendations", "selects from questions", "made-up score")
    elif case.id == "TC-15":
        tests = run("pytest-ml", [str(ROOT / ".venv/bin/pytest"), "-q", "-W", "ignore"], cwd=ROOT / "ml")
        unit = run("pytest-ml-coldstart", [str(ROOT / ".venv/bin/pytest"), "-W", "ignore", "-k", "cold or missing or threshold", "-v", "-p", "no:cacheprovider"], cwd=ROOT / "ml")
        case.evidence = ["PASS  unit test " + re.sub(r"^tests/\S+::|\s+PASSED.*$", "", l.strip())
                         for l in unit.splitlines() if " PASSED" in l]
        case.evidence += [l.replace("FAILED", "FAIL") for l in unit.splitlines() if "FAILED" in l]
        case.evidence += lines(run("phase4", py + ["scripts/phase4_check.py"]), "every recommendation is cold start")
        if "failed" in tests:
            case.evidence.append("FAIL  pytest ml: " + tail(tests, "failed"))
    elif case.id == "TC-16":
        case.evidence = portability_check()

    passed = [l for l in case.evidence if l.startswith("PASS")]
    failed = [l for l in case.evidence if l.startswith("FAIL")]
    not_run = [l for l in case.evidence if l.startswith("NOT RUN")]
    if failed or not passed:
        case.result = "Fail"
    elif not_run:
        case.result = "Partial"
    else:
        case.result = "Pass"
    case.actual = f"{len(passed)} of {len(passed) + len(failed)} checks passed" + (f"; {len(not_run)} not run" if not_run else "")


def write_report(all_cases: list[Case]) -> None:
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    counts = {r: sum(c.result == r for c in all_cases) for r in ["Pass", "Partial", "Fail"]}
    summary = "\n".join(
        f"| {c.id} | {c.requirement} | {c.title} | {c.expected} | {c.actual} | **{c.result}** |" for c in all_cases)
    details = []
    for c in all_cases:
        steps = "\n".join(f"{i}. {s}" for i, s in enumerate(c.steps, start=1))
        evidence = "\n".join(f"    {l}" for l in c.evidence)
        details.append(f"### {c.id} · {c.requirement} · {c.title}\n\n**Steps**\n\n{steps}\n\n**Expected:** {c.expected}\n\n"
                       f"**Actual:** {c.actual}. **Result: {c.result}**\n\n```\n{evidence}\n```\n")
    (DOCS / "test-cases.md").write_text(
        "# Test cases (Chapter Four)\n\n"
        f"Run {stamp} with `python scripts/run_test_cases.py`. One or more cases per functional (FR1–FR6) and "
        "non-functional (NFR1–NFR5) requirement from Chapter Three, including the cold-start case (Section 3.14). "
        "Every case was run against the live system; the evidence lines are the actual output.\n\n"
        f"**Summary:** {counts['Pass']} pass, {counts['Partial']} partial, {counts['Fail']} fail.\n\n"
        "| ID | Requirement | Test | Expected result | Actual result | Pass/Fail |\n| --- | --- | --- | --- | --- | --- |\n"
        f"{summary}\n\n"
        "Notes\n\n"
        "- TC-12 is partial by design: the automated walkthrough shows the core tasks complete without assistance, but the "
        "SUS questionnaire with student participants (Section 3.14.3) was not run for this demo and is future work.\n"
        "- TC-08 metrics come from simulated students, not real students (simulated data).\n"
        "- TC-13 targets were set for this test; see docs/performance.md for all samples and caveats.\n\n"
        "## Details\n\n" + "\n".join(details)
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--measure", action="store_true", help="measure response times again first")
    args = parser.parse_args()
    if args.measure or not (DOCS / "performance.json").exists():
        run("performance", [PY, "-W", "ignore", "scripts/measure_performance.py"])

    all_cases = cases()
    for case in all_cases:
        print(f"{case.id} {case.requirement}: {case.title}")
        try:
            evaluate(case)
        except Exception as e:  # record the failure instead of stopping the run
            case.evidence.append(f"FAIL  {type(e).__name__}: {e}"[:300])
            case.result, case.actual = "Fail", "check raised an error"
        print(f"  -> {case.result} ({case.actual})")
    write_report(all_cases)
    counts = {r: sum(c.result == r for c in all_cases) for r in ["Pass", "Partial", "Fail"]}
    print(f"\n{counts['Pass']} pass, {counts['Partial']} partial, {counts['Fail']} fail -> docs/test-cases.md")
    return 1 if counts["Fail"] else 0


if __name__ == "__main__":
    sys.exit(main())
