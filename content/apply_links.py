"""Writes content/resources/<code>.json: each topic's links, from content/sources/links.csv.

    python content/apply_links.py && python content/validate.py && python content/load.py

Each topic in content/courses/<code>.json lists the lectures it covers
("lectures": [4, 5]). For every lecture with its own row in links.csv the
topic gets that link. Lectures without a row share the course's fallback row
(lecture "all"), as one resource per topic. A topic that covers no lecture
gets the fallback too. Past-question and video links work the same way (a
course-wide "all" row goes on every topic), and a row whose lecture column is a
topic slug goes on that topic only (used for the one video per topic, each
checked to exist through YouTube's oEmbed endpoint before it was added).
Links never come from anywhere else.

Study notes and transcribed past questions are not links: load.py reads them
from content/notes/ and content/past_questions/.
"""

import csv
import json
import sys
from pathlib import Path

CONTENT = Path(__file__).parent
LINKS = CONTENT / "sources" / "links.csv"


def load_links(kind: str) -> dict[str, dict]:
    links: dict[str, dict] = {}
    with open(LINKS, newline="") as f:
        for row in csv.DictReader(f):
            if row["kind"].strip() == kind:
                links.setdefault(row["course"].strip(), {})[row["lecture"].strip()] = row
    return links


def lecture_label(numbers: list[int]) -> str:
    if len(numbers) == 1:
        return f"Lecture {numbers[0]}"
    if numbers == list(range(numbers[0], numbers[-1] + 1)):
        return f"Lectures {numbers[0]}–{numbers[-1]}"
    return "Lectures " + ", ".join(map(str, numbers))


def main() -> int:
    if not LINKS.exists():
        print(f"missing {LINKS}")
        return 1
    lectures_by_course = load_links("lecture")
    past_by_course = load_links("past_questions")
    videos_by_course = load_links("video")
    (CONTENT / "resources").mkdir(exist_ok=True)
    for path in sorted((CONTENT / "courses").glob("*.json")):
        course = json.loads(path.read_text())
        code = course["code"]
        rows = lectures_by_course.get(code, {})
        fallback = rows.get("all")
        out: dict[str, list[dict]] = {}
        for topic in course["topics"]:
            lectures: list[int] = topic.get("lectures", [])
            own = [n for n in lectures if str(n) in rows]
            shared = [n for n in lectures if str(n) not in rows]
            links = [{"title": rows[str(n)]["title"], "type": "lecture", "url": rows[str(n)]["url"],
                      "source": f"Lecture {n}"} for n in own]
            if (shared or not lectures) and fallback:
                title = f"{lecture_label(shared)}, in {fallback['title']}" if shared else fallback["title"]
                links.append({"title": title, "type": "lecture", "url": fallback["url"],
                              "source": lecture_label(shared) if shared else "Lecture folder"})
            for kind, by_course in (("past_questions", past_by_course), ("video", videos_by_course)):
                course_rows = by_course.get(code, {})
                for key, row in course_rows.items():
                    if key == "all" or key == topic["slug"] or (key.isdigit() and int(key) in lectures):
                        links.append({"title": row["title"], "type": kind, "url": row["url"], "source": "links.csv"})
            if not links:
                print(f"WARNING {code} / {topic['title']}: no link in links.csv for lectures {lectures}")
            out[topic["slug"]] = links
        target = CONTENT / "resources" / f"{path.stem}.json"
        target.write_text(json.dumps({"code": code, "topics": out}, indent=2, ensure_ascii=False) + "\n")
        print(f"{code}: " + "; ".join(f"{slug} -> {len(v)} link(s)" for slug, v in out.items()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
