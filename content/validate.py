"""Checks every course and question file against the schema in CLAUDE.md.

    python content/validate.py [--course "CSC 551"]

Prints errors, then question counts per topic and per format. Exits non-zero
on any error.

Course file, content/courses/<code>.json (code without spaces, e.g. CSC531.json):
    {"code": "CSC 531", "title": "...", "description": "...",
     "topics": [{"slug": "...", "title": "...", "summary": "two sentences",
                 "subtopics": ["..."], "lectures": [1, 2]}]}
Topics are listed in teaching order. A sample course built by the ingestion
pipeline (Phase 9) adds "is_reviewed": false; it then has 4 to 6 topics, 8
practice questions per topic in at least three formats, and needs no lecture
links (it has none unless one is added to content/sources/links.csv).

Study note, content/notes/<code>/<topic-slug>.md: 300 to 500 words, last line
"Source: Lecture N" or "Source: <file name>".

Links, content/resources/<code>.json (written by apply_links.py from
content/sources/links.csv): {"code": ..., "topics": {slug: [{"title", "type":
"lecture|past_questions|video", "url", "source"}]}}. Every topic needs a lecture.

Past questions, content/past_questions/<code>.json: {"code", "papers": [{"year",
"paper", "source"}], "questions": [{"year", "number", "marks", "topic", "text"}]}.
A topic with no past questions simply has none.

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
LINK_TYPES = ("lecture", "past_questions", "video")
NOTE_WORDS = (300, 500)
QUESTIONS_PER_TOPIC = 10
SAMPLE_QUESTIONS_PER_TOPIC = 8
SAMPLE_MIN_FORMATS = 3


def is_sample(course: dict) -> bool:
    return course.get("is_reviewed", True) is False


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
    low = 4 if is_sample(course) else 5
    if not low <= len(topics) <= 6:
        errors.append(f"{name}: has {len(topics)} topics, expected {low} to 6")
    if "is_reviewed" in course and not isinstance(course["is_reviewed"], bool):
        errors.append(f"{name}: is_reviewed must be true or false")
    slugs = [t.get("slug") for t in topics]
    for slug, n in Counter(slugs).items():
        if n > 1:
            errors.append(f"{name}: duplicate topic slug {slug!r}")

    for topic in topics:
        where = f"{name}/{topic.get('slug')}"
        for key in ("slug", "title", "summary"):
            if not topic.get(key):
                errors.append(f"{where}: missing {key}")
        if not topic.get("subtopics"):
            errors.append(f"{where}: no subtopics")
        if not isinstance(topic.get("lectures"), list):
            errors.append(f"{where}: lectures must be a list of lecture numbers (may be empty)")
        if "resources" in topic:
            errors.append(f"{where}: resources belong in content/resources/, not the course file")
        check_note(name, topic.get("slug"), where, errors)
    check_links(name, slugs, errors, lecture_required=not is_sample(course))
    check_past_questions(name, set(slugs), errors)


def check_note(course_file: str, slug: str, where: str, errors: list[str]) -> None:
    path = CONTENT / "notes" / course_file / f"{slug}.md"
    if not path.exists():
        errors.append(f"{where}: missing study note {path.relative_to(CONTENT)}")
        return
    text = path.read_text().strip()
    words = len(text.split())
    if not NOTE_WORDS[0] <= words <= NOTE_WORDS[1]:
        errors.append(f"{where}: study note has {words} words, expected {NOTE_WORDS[0]} to {NOTE_WORDS[1]}")
    last = text.splitlines()[-1].strip() if text else ""
    if not last.startswith("Source: "):
        errors.append(f"{where}: study note must end with a 'Source: ...' line")


def check_links(course_file: str, slugs: list[str], errors: list[str], lecture_required: bool = True) -> None:
    path = CONTENT / "resources" / f"{course_file}.json"
    if not path.exists() and not lecture_required:
        return  # a sample course with no links in links.csv yet
    if not path.exists():
        errors.append(f"{course_file}: missing {path.relative_to(CONTENT)} (run content/apply_links.py)")
        return
    topics = json.loads(path.read_text()).get("topics", {})
    for slug in slugs:
        where = f"{course_file}/{slug}"
        links = topics.get(slug, [])
        if lecture_required and not any(link.get("type") == "lecture" for link in links):
            errors.append(f"{where}: no lecture link (add it to content/sources/links.csv)")
        for link in links:
            url = str(link.get("url", ""))
            if link.get("type") not in LINK_TYPES:
                errors.append(f"{where}: link type {link.get('type')!r} not in {LINK_TYPES}")
            if not link.get("title"):
                errors.append(f"{where}: link needs a title")
            if not url.startswith("https://") or "todo" in url.lower():
                errors.append(f"{where}: link {url!r} is a placeholder or not https")
        if len({link.get("url") for link in links}) != len(links):
            errors.append(f"{where}: the same link appears twice")
    for slug in topics:
        if slug not in slugs:
            errors.append(f"{course_file}: resources file has unknown topic {slug!r}")


def check_past_questions(course_file: str, slugs: set[str], errors: list[str]) -> None:
    path = CONTENT / "past_questions" / f"{course_file}.json"
    if not path.exists():
        return  # optional: a course may have no past questions
    data = json.loads(path.read_text())
    years = {p.get("year") for p in data.get("papers", [])}
    for p in data.get("papers", []):
        if not p.get("year") or not p.get("paper") or not p.get("source"):
            errors.append(f"{course_file} past questions: each paper needs year, paper and source")
    for i, q in enumerate(data.get("questions", []), start=1):
        where = f"{course_file} past question #{i} ({q.get('year')} {q.get('number')})"
        if q.get("year") not in years:
            errors.append(f"{where}: year not listed under papers")
        if q.get("topic") not in slugs:
            errors.append(f"{where}: unknown topic {q.get('topic')!r}")
        if not str(q.get("text", "")).strip() or not q.get("number"):
            errors.append(f"{where}: needs number and text")


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
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--course", help='only this course, e.g. "CSC 551"')
    args = parser.parse_args()
    errors: list[str] = []
    courses = load_courses(errors)
    if args.course:
        courses = [c for c in courses if c.get("code") == args.course]
    if not courses:
        errors.append(f"no course files in content/courses/{' for ' + args.course if args.course else ''}")

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
            expected, min_formats = ((SAMPLE_QUESTIONS_PER_TOPIC, SAMPLE_MIN_FORMATS) if is_sample(course)
                                     else (QUESTIONS_PER_TOPIC, 2))
            if total != expected:
                errors.append(f"{label}: has {total} questions, expected {expected}")
            if len(counts) < min_formats:
                errors.append(f"{label}: uses fewer than {min_formats} formats")
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
