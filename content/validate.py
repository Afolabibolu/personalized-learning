"""Checks every course and question file against the schema in CLAUDE.md.

    python content/validate.py

Prints errors, then question counts per topic and per format. Exits non-zero
on any error.

Course file, content/courses/<code>.json (code without spaces, e.g. CSC531.json):
    {"code": "CSC 531", "title": "...", "description": "...",
     "topics": [{"slug": "...", "title": "...", "subtopics": ["..."],
                 "resources": [{"title": "...", "type": "pdf|video|link", "url": "...",
                                "is_introductory": false, "intro_order": null}]}]}
Topics are listed in teaching order.

Question file, content/questions/<code>/<topic-slug>.json: a list of
    {"format": "...", "stem": "...", "options": [{"key": "a", "text": "..."}],
     "correct_answer": ["a"], "explanation": "...", "source": "..."}
"""

import json
import sys
from collections import Counter
from pathlib import Path

CONTENT = Path(__file__).parent
FORMATS = ("single_choice", "true_false", "multi_select", "odd_one_out")
RESOURCE_TYPES = ("pdf", "video", "link")
QUESTIONS_PER_TOPIC = 10


def load_courses(errors: list[str]) -> list[dict]:
    courses = []
    for path in sorted((CONTENT / "courses").glob("*.json")):
        try:
            course = json.loads(path.read_text())
        except json.JSONDecodeError as e:
            errors.append(f"{path.name}: invalid JSON ({e})")
            continue
        course["_file"] = path.stem
        courses.append(course)
    return courses


def check_course(course: dict, errors: list[str]) -> None:
    name = course["_file"]
    for key in ("code", "title", "topics"):
        if not course.get(key):
            errors.append(f"{name}: missing {key}")
    if course.get("code", "").replace(" ", "") != name:
        errors.append(f"{name}: file name should be the code without spaces ({course.get('code')!r})")
    topics = course.get("topics", [])
    if not 5 <= len(topics) <= 6:
        errors.append(f"{name}: has {len(topics)} topics, expected 5 or 6")
    slugs = [t.get("slug") for t in topics]
    for slug, n in Counter(slugs).items():
        if n > 1:
            errors.append(f"{name}: duplicate topic slug {slug!r}")

    intro_orders = []
    for topic in topics:
        where = f"{name}/{topic.get('slug')}"
        for key in ("slug", "title"):
            if not topic.get(key):
                errors.append(f"{where}: missing {key}")
        if not topic.get("subtopics"):
            errors.append(f"{where}: no subtopics")
        resources = topic.get("resources", [])
        if not resources:
            errors.append(f"{where}: no resource")
        for r in resources:
            if not r.get("title") or not r.get("url"):
                errors.append(f"{where}: resource needs title and url")
            if r.get("type") not in RESOURCE_TYPES:
                errors.append(f"{where}: resource type {r.get('type')!r} not in {RESOURCE_TYPES}")
            if r.get("is_introductory"):
                if r.get("intro_order") is None:
                    errors.append(f"{where}: introductory resource needs intro_order")
                intro_orders.append(r.get("intro_order"))
    if not intro_orders:
        errors.append(f"{name}: no introductory resource")
    elif len(set(intro_orders)) != len(intro_orders):
        errors.append(f"{name}: duplicate intro_order values")


def check_question(q: dict, where: str, errors: list[str]) -> None:
    fmt = q.get("format")
    if fmt not in FORMATS:
        errors.append(f"{where}: format {fmt!r} not in {FORMATS}")
        return
    for key in ("stem", "explanation", "source"):
        if not isinstance(q.get(key), str) or not q[key].strip():
            errors.append(f"{where}: missing {key}")

    options = q.get("options")
    correct = q.get("correct_answer")
    if not isinstance(options, list) or not all(isinstance(o, dict) and o.get("key") and o.get("text") for o in options):
        errors.append(f"{where}: options must be a list of {{key, text}}")
        return
    if not isinstance(correct, list) or not correct:
        errors.append(f"{where}: correct_answer must be a non-empty list of keys")
        return

    keys = [o["key"] for o in options]
    if len(set(keys)) != len(keys):
        errors.append(f"{where}: duplicate option keys")
    texts = [o["text"].strip().lower() for o in options]
    if len(set(texts)) != len(texts):
        errors.append(f"{where}: duplicate option texts")
    if unknown := [k for k in correct if k not in keys]:
        errors.append(f"{where}: correct_answer has unknown keys {unknown}")
    if len(set(correct)) != len(correct):
        errors.append(f"{where}: duplicate keys in correct_answer")

    if fmt == "true_false":
        if sorted(keys) != ["false", "true"]:
            errors.append(f"{where}: true_false needs exactly the options 'true' and 'false'")
        if len(correct) != 1:
            errors.append(f"{where}: true_false needs exactly one correct option")
    else:
        expected = [chr(ord("a") + i) for i in range(len(keys))]
        if keys != expected:
            errors.append(f"{where}: option keys should be {expected}")
        if len(keys) < 3:
            errors.append(f"{where}: {fmt} needs at least 3 options")
    if fmt == "single_choice" and len(correct) != 1:
        errors.append(f"{where}: single_choice needs exactly one correct option")
    if fmt == "multi_select":
        if len(correct) < 2:
            errors.append(f"{where}: multi_select needs at least two correct options")
        if len(correct) >= len(keys):
            errors.append(f"{where}: multi_select cannot have every option correct")
    if fmt == "odd_one_out":
        if len(correct) != 1:
            errors.append(f"{where}: odd_one_out needs exactly one odd option")
        if len(keys) < 4:
            errors.append(f"{where}: odd_one_out needs at least 4 options")


def main() -> int:
    errors: list[str] = []
    courses = load_courses(errors)
    if not courses:
        errors.append("no course files in content/courses/")

    per_topic: dict[str, Counter] = {}
    for course in courses:
        check_course(course, errors)
        stems: dict[str, str] = {}
        for topic in course.get("topics", []):
            slug = topic.get("slug")
            path = CONTENT / "questions" / course["_file"] / f"{slug}.json"
            label = f"{course['_file']}/{slug}"
            counts = per_topic.setdefault(label, Counter())
            if not path.exists():
                errors.append(f"{label}: missing {path.relative_to(CONTENT)}")
                continue
            try:
                questions = json.loads(path.read_text())
            except json.JSONDecodeError as e:
                errors.append(f"{label}: invalid JSON ({e})")
                continue
            if not isinstance(questions, list):
                errors.append(f"{label}: question file must be a list")
                continue
            for i, q in enumerate(questions, start=1):
                where = f"{label} #{i}"
                check_question(q, where, errors)
                counts[q.get("format")] += 1
                stem = " ".join(str(q.get("stem", "")).lower().split())
                if stem in stems:
                    errors.append(f"{where}: duplicate stem (also {stems[stem]})")
                stems[stem] = where

            total = sum(counts.values())
            if total != QUESTIONS_PER_TOPIC:
                errors.append(f"{label}: has {total} questions, expected {QUESTIONS_PER_TOPIC}")
            if len(counts) < 2:
                errors.append(f"{label}: uses fewer than two formats")
            for fmt, n in counts.items():
                if n > total / 2:
                    errors.append(f"{label}: {fmt} is {n} of {total}, more than half")

        known = {f"{t.get('slug')}.json" for t in course.get("topics", [])}
        for path in sorted((CONTENT / "questions" / course["_file"]).glob("*.json")):
            if path.name not in known:
                errors.append(f"{course['_file']}: {path.name} matches no topic in the course file")

    if per_topic:
        print(f"{'topic':40} {'total':>5} " + " ".join(f"{f:>13}" for f in FORMATS))
        totals = Counter()
        for label, counts in per_topic.items():
            totals.update(counts)
            print(f"{label:40} {sum(counts.values()):>5} " + " ".join(f"{counts[f]:>13}" for f in FORMATS))
        print(f"{'all':40} {sum(totals.values()):>5} " + " ".join(f"{totals[f]:>13}" for f in FORMATS))

    print()
    for error in errors:
        print(f"ERROR  {error}")
    print(f"{len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
