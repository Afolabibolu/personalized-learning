"""Copies each book's link from content/sources/textbook_links.csv into content/textbooks/<code>.json.

    python content/apply_textbook_links.py && python content/validate.py && python content/load.py

textbook_links.csv has one row per book (title, authors, edition, url, link_type,
source, date_checked). A link is a legal free copy (link_type "free": the author's
or publisher's own free edition, an open textbook, or a university repository) or,
failing that, where the book can be bought or previewed ("buy": the publisher's
page; "preview": Google Books). Every link was opened and matched to the book's
title, author and edition before it was added; a book with no confirmed link has
an empty url and keeps its reading card without a button. Shadow libraries and
unofficial PDF copies are never used. Links never come from anywhere else.

A book matches its row on title, authors and edition, so two editions of the same
book (Sipser 2nd and 3rd) get their own links.
"""

import csv
import json
import sys
from pathlib import Path

CONTENT = Path(__file__).parent
LINKS = CONTENT / "sources" / "textbook_links.csv"
LINK_TYPES = {"free", "buy", "preview"}


def key(title: str, authors: str, edition: str | None) -> tuple[str, str, str]:
    return title.strip(), authors.strip(), (edition or "").strip()


def load_links() -> dict[tuple[str, str, str], dict]:
    with open(LINKS, newline="") as f:
        return {key(r["title"], r["authors"], r["edition"]): r for r in csv.DictReader(f)}


def main() -> int:
    links = load_links()
    missing, linked, unlinked = [], 0, 0
    for path in sorted((CONTENT / "textbooks").glob("*.json")):
        data = json.loads(path.read_text())
        for book in data["books"].values():
            row = links.get(key(book["title"], book["authors"], book.get("edition")))
            if row is None:
                missing.append(f"{data['code']}: {book['title']}")
                continue
            url, link_type = row["url"].strip(), row["link_type"].strip()
            if url and link_type not in LINK_TYPES:
                raise SystemExit(f"{book['title']}: link_type must be one of {sorted(LINK_TYPES)}, not {link_type!r}")
            book.pop("url", None)
            book.pop("link_type", None)
            if url:
                book["url"], book["link_type"] = url, link_type
                linked += 1
            else:
                unlinked += 1
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    if missing:
        print("Books with no row in textbook_links.csv:\n  " + "\n  ".join(missing))
        return 1
    print(f"{linked} book entries linked, {unlinked} without a confirmed link")
    return 0


if __name__ == "__main__":
    sys.exit(main())
