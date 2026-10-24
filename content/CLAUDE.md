# content/: knowledge base and course ingestion

Read the root CLAUDE.md first. This file covers the knowledge base content (FR5) and the pipeline that adds any course without code changes (NFR5).

## Two kinds of course

- Reviewed: CSC 531 and CSC 574. Built carefully and checked by me. Their questions load as `approved`.
- Sample (auto-generated): any other course added through the pipeline below, marked `"is_reviewed": false` in its course file, so `courses.is_reviewed = false`. The app shows these with a "Sample content, pending lecturer review" badge, and their questions still work in quizzes so the demo shows the pipeline end to end. Sample size: 4 to 6 topics, 8 practice questions per topic in at least three formats, no lecture link required. The list of courses built so far, with the files used and skipped, is in `docs/results/courses.md`.

## Content rules (both kinds)

- Each topic has: subtopics, a two-sentence summary, a study note (300 to 500 words, ending "Source: Lecture N" or "Source: <file name>"), past questions copied as written and tagged with year, and 10 practice questions in the four formats.
- Every fact comes from the files in `content/sources/`. Where a student's summary note and a lecture slide disagree, follow the slide.
- Never invent URLs. Lecture, past-question and video links come only from `content/sources/links.csv` (columns: course, lecture, kind, title, url).
- In `links.csv`, a row with lecture `all` is the fallback for that course: any lecture without its own row links to it. Some `all` rows point to a Drive folder, not a single file; label those "Open lecture folder" in the app.
- `validate.py` must pass before anything is loaded.

## Course ingestion pipeline (NFR5)

Goal: drop a course's files into a folder, run commands, and the course appears in the app with topics, notes, past questions and quizzes. No code changes.

```
content/
  sources/raw/                 the unzipped Drive folder, as downloaded
  ingest/
    inventory.py               finds courses and classifies files
    inventory.csv              output; I correct it by hand if needed
    extract.py                 pulls text out of PDF, PPTX and DOCX files
    extracted/<code>/          one text file per source file
    build_course.py            optional, API mode only
```

1. `inventory.py` walks `sources/raw/`, detects course codes from folder and file names (patterns like `CSC 574`, `CSC574`, `csc-574`), and classifies each file as outline, lecture, past_questions or notes from its name. It writes `inventory.csv` with columns: code, title, file, kind, pages. Files it cannot place go in with code `UNKNOWN`. It prints a table of courses with file counts per kind.
2. `extract.py --course <code>` (or `--all`) extracts text with pypdf, python-pptx and python-docx. A PDF that yields under 200 characters per page is marked `scanned`; it is later sent to the API as a PDF document instead of text.
3. Build the course files. Default mode, no API key needed: you (Claude Code) read `extracted/<code>/` and write the same files as the manual process (`courses/`, `notes/`, `past_questions/`, `resources/`, `questions/`), following the content rules above, and mark the course as auto-generated. One course per run.
4. Run `python content/ingest/publish.py --course <code>`: it rebuilds links, runs `validate.py --course`, and runs `load.py --course` only if there are 0 errors. The course appears in the app.

Corrections to the inventory go in `ingest/inventory_fixes.csv` (file, code, kind, title; a row with no file sets a course title), so they survive reruns. `ingest/extracted/` is not committed. Files marked `scanned` or `image` are read from their page images (render with `pdftoppm` from poppler) instead of their text.

Optional API mode, only if I later add `ANTHROPIC_API_KEY` to `content/.env`: `build_course.py --course <code>` does step 3 through the Claude API with structured outputs, and `--all` uses the Message Batches API for many courses at once. Do not build this unless I ask.

### Pipeline rules

- `inventory.py` and `extract.py` run without any API key.
- Never read or send files outside `content/sources/`.
- If a topic's files fail `validate.py`, fix them once; if they still fail, skip that topic and list it in the report.
- API mode rules, if it is ever built: key and model ID from `content/.env` (never hardcode a model name), print an estimate and require `--yes` before any call, `--max-courses` defaults to 3, and cache responses in `ingest/cache/`.

Check: one course that was not built by hand goes from `sources/raw/` to visible in the app (Knowledge Base, a topic quiz, a study note) using only these commands.
