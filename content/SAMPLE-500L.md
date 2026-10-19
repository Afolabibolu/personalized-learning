# Sample: all 500-level courses

Goal: every 500-level Computer Science course appears in the app for the supervisor demo on Tuesday, with topics, study notes, past questions where they exist, and working quizzes. CSC 531 and CSC 574 are already done and reviewed. The rest are added as sample courses.

Read `content/CLAUDE.md` first for the content rules. This file sets the source folder, the size of each course and the order of work.

## Sources

All course files are already in the project, in the Drive layout:

```
content/sources/raw/500 LEVEL/
  1 semester/      one folder per course, plus a past question folder
  2 semester/      one folder per course, plus a past question folder
```

Note the spaces in the folder names; quote paths in commands.

Open the files directly with your file reader. It reads PDFs (including scanned pages), slides and documents. Do not build `inventory.py` or `extract.py` for this; they are not needed.

## Scope of this session

- Only touch `content/`, plus running `content/validate.py` and `content/load.py`. Another Claude Code session is working in `web/`, `ml/` and `supabase/` at the same time. Do not edit those folders and do not commit.

## Steps

1. List the folders in `1 semester` and `2 semester`. Show me a table: semester, course code, course title (from the folder name or the outline), number of files, and whether past questions exist for it. Mark CSC 531 and CSC 574 as already done. Stop and let me confirm the list.
2. Then, one course at a time, in the order I confirm:
   - Read the course outline first if there is one, then the lecture files, then the past questions.
   - Write the course files at sample size (below), mark the course as sample content (`is_reviewed = false`), run `validate.py`, then `load.py` for that course only.
   - Add a row to `docs/results/courses.md`: code, title, semester, topics, notes, questions, past questions, files used, files skipped and why.
   - Give me a three-line update, then continue with the next course without waiting.
3. When every course is loaded, show me the final table from `docs/results/courses.md`.

## Sample size per course

| Item | Size |
| --- | --- |
| Topics | 4 or 5, in teaching order |
| Study note per topic | about 300 words, ending with its source file |
| Practice questions per topic | 8, at least three formats |
| Past questions | every one found for the course, tagged by topic and year |
| Quizzes | one diagnostic per course, one quiz per topic (made by `load.py`) |

## Rules

- Every fact comes from the files in the course folder. Where a student's summary and a lecture slide disagree, follow the slide.
- Never invent URLs. Sample courses get no lecture links unless I add them to `content/sources/links.csv`; their content reaches students through the study notes and past questions.
- If a course folder has no usable files, skip it and list it in `docs/results/courses.md` with the reason. Never write a course from general knowledge.
- The app labels these courses "Sample content, pending lecturer review".
- If the session is running long, finish the course in progress, load it, and stop with the table. A smaller set of complete courses beats many half-built ones.
