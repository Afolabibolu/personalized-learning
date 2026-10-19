# Response times (NFR2)

Measured 2026-10-19 17:11 with `python scripts/measure_performance.py --runs 10`, on the development laptop against the hosted Supabase project, with the Vite dev server and the ML service running locally. Times are in seconds. A case passes when its 95th percentile is within the target.

| Operation | Runs | Median | p95 | Range | Target | Result |
| --- | --- | --- | --- | --- | --- | --- |
| Quiz submit: Submit pressed → results on screen (browser) | 10 | 0.33 | 0.83 | 0.32–0.83 | ≤ 2.0 | Pass |
| Quiz submit: submit_quiz call only (API) | 10 | 0.22 | 0.27 | 0.19–0.27 | ≤ 1.0 | Pass |
| Dashboard load: page opened → recommendations and chart shown (browser) | 10 | 1.35 | 1.38 | 1.34–1.38 | ≤ 3.0 | Pass |
| Recommendation update: POST /recommend (runs in the background) | 10 | 2.28 | 4.49 | 2.07–4.49 | ≤ 5.0 | Pass |

Targets: a quiz result within 2 s of pressing Submit and a dashboard within 3 s keep the student's flow uninterrupted at single-institution usage. Recommendation updates run in the background after a quiz or a study log (the app does not wait for them), so their target is looser.

Caveats: one laptop, one user at a time, development build of the web app, network to the Supabase region included. Load with many concurrent users was not tested.
