# Response times (NFR2)

Measured 2026-11-10 13:36 with `python scripts/timing.py --runs 20`, on the development laptop against the hosted Supabase project, with the Vite dev server and the ML service running locally. Times are in seconds. A case passes when its 95th percentile is within the target.

| Operation | Runs | Median | p95 | Slowest | Fastest | Target | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Quiz submit: Submit pressed → results on screen (browser) | 20 | 0.32 | 0.84 | 0.84 | 0.22 | ≤ 2.0 | Pass |
| Quiz submit: submit_quiz call only (API) | 20 | 0.19 | 0.21 | 0.21 | 0.17 | ≤ 1.0 | Pass |
| Dashboard load: page opened → recommendations and chart shown (browser) | 20 | 1.11 | 1.34 | 1.36 | 0.84 | ≤ 3.0 | Pass |
| Recommendation update: POST /recommend (runs in the background) | 20 | 4.20 | 4.40 | 5.32 | 3.98 | ≤ 5.0 | Pass |

Targets: a quiz result within 2 s of pressing Submit and a dashboard within 3 s keep the student's flow uninterrupted at single-institution usage. Recommendation updates run in the background after a quiz or a study log (the app does not wait for them), so their target is looser.

Caveats: one laptop, one user at a time, development build of the web app, network to the Supabase region included. Load with many concurrent users was not tested.
