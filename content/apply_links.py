"""Rebuilds each topic's lecture resources from content/sources/links.csv.

    python content/apply_links.py && python content/validate.py && python content/load.py

Each topic in content/courses/<code>.json lists the lectures it covers
("lectures": [4, 5]). For every lecture with its own row in links.csv the
topic gets that link. Lectures without a row share the course's fallback row
(lecture "all"), as one resource per topic. A topic that covers no lecture
gets the fallback too. Links never come from anywhere else, so resources not
in links.csv (for example supplementary readings) are dropped and listed.

The first three topics keep their place in the introductory sequence.
"""

import csv
import json
import sys
from pathlib import Path

CONTENT = Path(__file__).parent
LINKS = CONTENT / "sources" / "links.csv"
INTRO_TOPICS = 3


def load_links() -> dict[str, dict]:
    links: dict[str, dict] = {}
    with open(LINKS, newline="") as f:
        for row in csv.DictReader(f):
            if row["kind"] != "lecture":
                continue
            links.setdefault(row["course"].strip(), {})[row["lecture"].strip()] = row
    return links


def resource_type(url: str) -> str:
    return "link" if "/folders/" in url else "pdf"


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
    links = load_links()
    dropped: list[str] = []
    for path in sorted((CONTENT / "courses").glob("*.json")):
        course = json.loads(path.read_text())
        code = course["code"]
        rows = links.get(code, {})
        fallback = rows.get("all")
        for order, topic in enumerate(course["topics"], start=1):
            dropped += [f"{code} / {topic['title']}: {r['title']}" for r in topic.get("resources", [])
                        if not any(r["url"] == row["url"] for row in rows.values())]
            lectures: list[int] = topic.get("lectures", [])
            own = [n for n in lectures if str(n) in rows]
            shared = [n for n in lectures if str(n) not in rows]
            resources = [{"title": rows[str(n)]["title"], "type": resource_type(rows[str(n)]["url"]),
                          "url": rows[str(n)]["url"]} for n in own]
            if (shared or not lectures) and fallback:
                title = f"{lecture_label(shared)}, in {fallback['title']}" if shared else fallback["title"]
                resources.append({"title": title, "type": resource_type(fallback["url"]), "url": fallback["url"]})
            if not resources:
                print(f"WARNING {code} / {topic['title']}: no link in links.csv for lectures {lectures}")
            if order <= INTRO_TOPICS and resources:
                resources[0] |= {"is_introductory": True, "intro_order": order}
            topic["resources"] = resources
        path.write_text(json.dumps(course, indent=2, ensure_ascii=False) + "\n")
        print(f"{code}: " + "; ".join(f"{t['slug']} -> {len(t['resources'])} link(s)" for t in course["topics"]))
    if dropped:
        print("\nNot in links.csv, so left out:")
        for d in sorted(set(dropped)):
            print(f"  - {d}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
