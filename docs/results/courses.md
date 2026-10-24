# Courses in the knowledge base

CSC 531 and CSC 574 were built by hand and reviewed. Every other course was added in Phase 9 through the ingestion pipeline: `content/ingest/inventory.py`, then `extract.py`, then the course files written from the extracted text and the page images of scanned papers (default mode, no API key), then `validate.py` and `load.py`. These are sample courses (`is_reviewed = false`) and the app labels them "Sample content, pending lecturer review". They have no lecture links, because `content/sources/links.csv` has none for them yet.

Sample size per course: 4 or 5 topics, a study note of 300 to 500 words per topic, 8 practice questions per topic in at least three formats, and every past question found for the course.

| Code | Title | Semester | Topics | Notes | Questions | Past questions | Files used | Files skipped and why |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CSC 531 | Human-Computer Interaction | 1 | 6 | 6 | 60 | yes | Reviewed course (Phases 2 and 7) | — |
| CSC 574 | Intelligent Systems | 1 | 6 | 6 | 60 | yes | Reviewed course (Phases 2 and 7) | — |
| CSC 551 | Design and Analysis of Algorithms | 1 | 5 | 5 | 40 | 12 (2022/23, 2023/24, 2024/25) | CSC 551 Design and Analysis of Algorithms.pdf (lecture, Study Sessions 1–10); CSC 551(2023_2024).pdf and algorithm_pq_merge-all.pdf (scanned papers, read from the page images); the CSC 551 page of 500 LEVEL 1ST SEMESTER PAST QUESTIONS 20242025 SESSION .pdf | My CSC 551 Note (Algorithm): a student summary, the lecture was followed instead. CSC 551 Assessment.pdf: an online class quiz whose options came out of order in extraction, used only to judge question style. The 2024/25 paper is page 1 only; any later page is not in the file |
