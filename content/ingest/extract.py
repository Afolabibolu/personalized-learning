"""Extracts text from the files listed in inventory.csv.

    python content/ingest/extract.py --course "CSC 551"
    python content/ingest/extract.py --all

Writes one text file per source file to content/ingest/extracted/<code>/
(PDF pages and slides are marked "--- page N ---") and a manifest.csv with
file, kind, pages, characters and status. Status is "text", or "scanned" for
a PDF that yields under 200 characters per page and "image" for a photo:
those have no usable text, so whoever builds the course reads the original
file (the page images) instead. Exact duplicates and files of kind "other"
are skipped. No API key needed. Never reads outside content/sources/.
"""

import argparse
import csv
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RAW = HERE.parent / "sources" / "raw"
INVENTORY = HERE / "inventory.csv"
OUT = HERE / "extracted"
SCANNED_CHARS_PER_PAGE = 200


def pdf_pages(path: Path) -> list[str]:
    from pypdf import PdfReader
    return [page.extract_text() or "" for page in PdfReader(path).pages]


def pptx_pages(path: Path) -> list[str]:
    from pptx import Presentation
    slides = []
    for slide in Presentation(path).slides:
        parts = []
        for shape in slide.shapes:
            if shape.has_text_frame:
                parts.append(shape.text_frame.text)
            if getattr(shape, "has_table", False) and shape.has_table:
                parts += [" | ".join(c.text for c in row.cells) for row in shape.table.rows]
        if slide.has_notes_slide and slide.notes_slide.notes_text_frame.text.strip():
            parts.append("Notes: " + slide.notes_slide.notes_text_frame.text)
        slides.append("\n".join(p for p in parts if p.strip()))
    return slides


def docx_pages(path: Path) -> list[str]:
    from docx import Document
    doc = Document(path)
    parts = [p.text for p in doc.paragraphs]
    for table in doc.tables:
        parts += [" | ".join(c.text for c in row.cells) for row in table.rows]
    return ["\n".join(parts)]


READERS = {".pdf": pdf_pages, ".pptx": pptx_pages, ".docx": docx_pages}


def folder_name(code: str) -> str:
    return code.replace(" ", "")


def extract(row: dict) -> dict:
    path = RAW / row["file"]
    assert path.resolve().is_relative_to(RAW.resolve()), "outside content/sources/"
    out_dir = OUT / folder_name(row["code"])
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / (re.sub(r"[^\w.()-]+", "_", Path(row["file"]).stem).strip("_") + ".txt")
    info = {"file": row["file"], "kind": row["kind"], "text_file": target.name, "pages": 0, "characters": 0}
    reader = READERS.get(path.suffix.lower())
    if reader is None:
        return {**info, "status": "image", "text_file": ""}
    try:
        pages = reader(path)
    except Exception as e:  # a broken file is reported, not fatal
        return {**info, "status": f"error: {type(e).__name__}", "text_file": ""}
    chars = sum(len(p.strip()) for p in pages)
    scanned = path.suffix.lower() == ".pdf" and chars < SCANNED_CHARS_PER_PAGE * max(1, len(pages))
    body = "\n\n".join(f"--- page {i} ---\n{p.strip()}" for i, p in enumerate(pages, start=1))
    target.write_text(f"Source: {row['file']}\nKind: {row['kind']}\n\n{body}\n", errors="replace")  # PDFs can hold broken surrogates
    return {**info, "pages": len(pages), "characters": chars, "status": "scanned" if scanned else "text"}


def main() -> int:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--course", help='course code as in inventory.csv, e.g. "CSC 551"')
    group.add_argument("--all", action="store_true")
    args = parser.parse_args()
    if not INVENTORY.exists():
        print("Run content/ingest/inventory.py first.")
        return 1
    rows = [r for r in csv.DictReader(INVENTORY.open())
            if not r["duplicate_of"] and r["kind"] != "other" and (args.all or r["code"] == args.course)]
    if not rows:
        print(f"No files for {args.course!r} in inventory.csv.")
        return 1

    by_code: dict[str, list[dict]] = {}
    for row in rows:
        print(f"  {row['code']:<8} {row['file'][-70:]}", flush=True)
        by_code.setdefault(row["code"], []).append(extract(row))
    for code, results in sorted(by_code.items()):
        with (OUT / folder_name(code) / "manifest.csv").open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["file", "kind", "text_file", "pages", "characters", "status"])
            writer.writeheader()
            writer.writerows(results)
        statuses = [r["status"] for r in results]
        print(f"{code:<8} {len(results)} files: {statuses.count('text')} text, {statuses.count('scanned')} scanned, "
              f"{statuses.count('image')} image, {sum(s.startswith('error') for s in statuses)} error")
    return 0


if __name__ == "__main__":
    sys.exit(main())
