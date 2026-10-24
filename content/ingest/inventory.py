"""Finds courses in content/sources/raw/ and classifies every file.

    python content/ingest/inventory.py

Detects course codes from folder and file names (CSC 574, CSC574, csc-574),
classifies each file as outline, lecture, past_questions, notes or textbook
from its name, and writes content/ingest/inventory.csv (code, title, file,
kind, pages, duplicate_of). Files it cannot place get code UNKNOWN; correct
them in inventory_fixes.csv (file, code, kind, title; a row with no file sets
a course title), which is applied on every run; extract.py reads the result. Exact duplicates (same
bytes) are listed with duplicate_of set and are not extracted again.
No API key needed. Never reads outside content/sources/.
"""

import csv
import hashlib
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
RAW = HERE.parent / "sources" / "raw"
OUT = HERE / "inventory.csv"
FILE_TYPES = {".pdf", ".pptx", ".docx", ".jpeg", ".jpg", ".png"}

FIXES = HERE / "inventory_fixes.csv"
CODE = re.compile(r"\b([A-Z]{3})[\s_-]?(\d{3})(?!\d)", re.I)
TITLE_AFTER_CODE = re.compile(r"^[A-Z]{3}[\s_-]?\d{3}\s*(?:\(([^)]+)\)|[-–]\s*(.+)|\s([A-Za-z][A-Za-z ,&]+))", re.I)


def codes_in(name: str) -> list[str]:
    return [f"{m.group(1).upper()} {m.group(2)}" for m in CODE.finditer(name)]


def course_code(path: Path) -> str:
    """The code nearest the file: its own name, then each folder upwards. A
    folder with no code in its name takes the code that at least two thirds of
    the names inside it carry (so 'semantics/' becomes CSC 554)."""
    rel_parts = path.relative_to(RAW).parts
    for part in reversed(rel_parts):
        found = codes_in(part)
        if found:
            return found[0]
    for depth in range(len(rel_parts) - 1, 0, -1):
        folder = RAW.joinpath(*rel_parts[:depth])
        names = Counter(c for p in folder.rglob("*") for c in set(codes_in(p.name)))
        if names:
            code, n = names.most_common(1)[0]
            if n * 3 >= sum(names.values()) * 2:
                return code
            return "UNKNOWN"  # a folder that mixes courses, e.g. merged past papers
    return "UNKNOWN"


def title_from_names(rows: list[dict]) -> dict[str, str]:
    """A course title from names such as 'CSC 551 (Design and Analysis of Algorithms)' or 'CSC584 - ICT for Development'."""
    titles: dict[str, str] = {}
    for r in rows:
        for part in Path(r["file"]).parts:
            m = TITLE_AFTER_CODE.match(Path(part).stem.strip())
            if m and r["code"] in codes_in(part):
                title = next(g for g in m.groups() if g).strip(" -")
                if len(title.split()) >= 2 and not re.search(r"\d|note|outline|assessment|answer|group", title, re.I):
                    titles.setdefault(r["code"], title)
    return titles


def apply_fixes(rows: list[dict]) -> None:
    """Hand corrections from inventory_fixes.csv (file, code, kind, title); blank cells keep the detected value."""
    if not FIXES.exists():
        return
    fixes = list(csv.DictReader(FIXES.open()))
    by_file = {f["file"]: f for f in fixes if f.get("file")}
    titles = {f["code"]: f["title"] for f in fixes if not f.get("file") and f.get("title")}
    for r in rows:
        fix = by_file.get(r["file"], {})
        for key in ("code", "kind"):
            if fix.get(key):
                r[key] = fix[key]
        if r["code"] in titles:
            r["title"] = titles[r["code"]]


def kind(path: Path) -> str:
    name = path.name.lower()
    folders = " ".join(path.relative_to(RAW).parent.parts).lower()
    in_past_question_folder = any(f.strip().lower().startswith("past question") for f in path.relative_to(RAW).parent.parts)
    if "outline" in name or "teaching_plan" in name or "teaching plan" in name:
        return "outline"
    if re.search(r"\bpq\b|past q|question|\bq\b|assessment|\(20\d\d_20\d\d\)|20\d\d-\d\d", name) or in_past_question_folder:
        return "past_questions"
    if "note" in name or "term paper" in name or "presentation" in name:
        return "notes"
    if re.search(r"edition|pdfdrive|wiley|addison|independently published| - [a-z]+ [a-z]+\.pdf$|reference", name + folders):
        return "textbook"
    if re.search(r"lecture|lesson|week|slide|courseware|dlc|csc ?\d{3}|\.pptx$", name):
        return "lecture"
    return "lecture" if path.suffix.lower() == ".pdf" else "notes"


def pages(path: Path) -> int | str:
    try:
        if path.suffix.lower() == ".pdf":
            from pypdf import PdfReader
            return len(PdfReader(path).pages)
        if path.suffix.lower() == ".pptx":
            from pptx import Presentation
            return len(Presentation(path).slides)
    except Exception as e:  # a broken file still goes in the inventory
        return f"error: {type(e).__name__}"
    return 1 if path.suffix.lower() in {".jpeg", ".jpg", ".png"} else ""


def main() -> int:
    if not RAW.exists():
        print(f"No {RAW}; put the unzipped Drive folder there first.")
        return 1
    files = sorted(p for p in RAW.rglob("*") if p.is_file() and p.suffix.lower() in FILE_TYPES)
    first_by_hash: dict[str, str] = {}
    rows = []
    for path in files:
        rel = str(path.relative_to(RAW))
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        duplicate = first_by_hash.setdefault(digest, rel)
        rows.append({"code": course_code(path), "title": "", "file": rel, "kind": kind(path),
                     "pages": pages(path) if duplicate == rel else "", "duplicate_of": "" if duplicate == rel else duplicate})
    titles = title_from_names(rows)
    for r in rows:
        r["title"] = titles.get(r["code"], "")
    apply_fixes(rows)
    with OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["code", "title", "file", "kind", "pages", "duplicate_of"])
        writer.writeheader()
        writer.writerows(rows)

    kinds = ["outline", "lecture", "notes", "past_questions", "textbook"]
    counts: dict[str, Counter] = defaultdict(Counter)
    for r in rows:
        if not r["duplicate_of"]:
            counts[r["code"]][r["kind"]] += 1
    title_of = {r["code"]: r["title"] for r in rows}
    print(f"{'code':<8} {'title':<38} " + " ".join(f"{k[:9]:>9}" for k in kinds))
    for code in sorted(counts):
        print(f"{code:<8} {title_of.get(code, '')[:38]:<38} " + " ".join(f"{counts[code][k]:>9}" for k in kinds))
    dupes = sum(bool(r["duplicate_of"]) for r in rows)
    print(f"\n{len(rows)} files, {dupes} exact duplicates skipped -> {OUT.relative_to(HERE.parent.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
