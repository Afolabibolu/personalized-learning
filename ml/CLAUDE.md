# ml/: recommendation service and training

Read the root CLAUDE.md first. This file adds the rules for the ML service only.

## What the models are for

For each student and topic, the models estimate the probability that the student's next attempt on that topic scores below 50% ("requires attention"). The service ranks topics by the average of the Logistic Regression and Random Forest probabilities and picks a resource for each of the top topics. This is FR4.

## `POST /recommend` output

Each recommendation row gets an `explanation` (JSON) so the frontend never computes reasons itself:

```json
{
  "reason": "Last score 40%. Not studied for 9 days. 20 minutes studied in total.",
  "probabilities": {"logistic_regression": 0.86, "random_forest": 0.92, "average": 0.89},
  "top_factors": [
    {"feature": "last_score", "value": 40, "direction": "raises risk"},
    {"feature": "days_since_last_studied", "value": 9, "direction": "raises risk"}
  ],
  "matched_preference": "note",
  "also": [
    {"resource_id": "…", "type": "video", "title": "Video: …", "url": "https://www.youtube.com/watch?v=…"},
    {"resource_id": "…", "type": "textbook", "title": "Textbook: …", "url": "https://…", "link_type": "buy"}
  ]
}
```

- `also` (25 Oct): the topic's first video and textbook that are not the main resource and not already accepted or dismissed. Cold-start rows get it too. A textbook carries its link and `link_type` (free, buy or preview, 4 Nov), or a null url when no link was confirmed; the app still opens its reading card in the app.

- `top_factors` for Logistic Regression comes from coefficient times the scaled feature value; take the two or three largest contributions. Do not add SHAP or other new libraries for this.
- Cold-start rows have `"reason": "Not enough quiz history yet for this course."`, no probabilities, and source `cold_start`.
- Diagnostic rows (Stage 2, 3 Nov) come from the SQL function `diagnostic_recommendations()`, not from Python: source `diagnostic`, no probabilities, `"reason": "You got 1 of 3 right on this topic in the diagnostic."`, plus `diagnostic` (correct, total, score), `threshold` and `completed_quizzes`. `/recommend` reads the threshold from `app_settings` each run (`cold_start_threshold()`); there is no copy of it in Python.
- "Keep it up" rows (low probability, used to fill the list when fewer than 3 topics need attention) say why, for example "Scoring 80%. Try the topic quiz: questions you haven't seen come first."

## Notifications written by the service

After each run, insert notifications for the student, once per kind per day:
- `new_recommendations` when the top-ranked topic changed since the last run
- `weak_topic_unstudied` when a topic above 0.7 average probability has no study log in 7 days

Other reminder kinds (streak at risk, inactivity, daily goal, score improved) come from the SQL function described in `supabase/CLAUDE.md`.

## Email reminders (4 Nov)

`app/emails.py` sends them; `main.py` runs `emails.run_once()` every 15 minutes in a background task (set `EMAIL_SCHEDULER=off` to stop it) and serves `GET /email/unsubscribe?token=`. Mail goes through Brevo's SMTP relay (9 Nov; it replaced Gmail). Settings in `ml/.env` only: `SMTP_HOST` (smtp-relay.brevo.com), `SMTP_PORT` (587 uses STARTTLS; 465 uses SSL), `SMTP_USER` and `SMTP_PASSWORD` (Brevo's SMTP login and key; the login is not an email address), `SMTP_FROM` (the sender students see, an address verified in Brevo), `TEST_EMAIL_TO` (the only address test sends go to), `APP_URL`, `EMAIL_DRY_RUN` (true unless set to false and the login, password and SMTP_FROM are all present). Kinds and triggers are in the module docstring; the due checks are pure functions tested in `tests/test_emails.py`. Never send real email to reserved test domains, and test real sends with `--send --to-test` only (to TEST_EMAIL_TO).

## Reliability (NFR4)

- If a model file is missing or fails to load, use the cold-start path and log a warning. Never return a 500 for a student who exists.
- Each run deletes that student's pending recommendations before inserting new ones.

## Training and results

- Keep the three-way comparison: rule baseline (last score below 50%), Logistic Regression, Random Forest. Same split, same folds.
- `ml/results/metrics.md` and `summary.md` say once, at the top, that the data comes from simulated students (rules in `simulation_rules.md`). File names and chart titles do not repeat it. Never present the numbers as results from real students.
- `python -m training.train` must finish in under two minutes on a laptop.
- Add `ml/results/summary.md`: one short paragraph per model in plain words, the results table, and which features mattered most. This feeds Chapter Four.
- `python -m training.export_dataset` (12 Nov) writes `results/training_data.csv` (the exact rows `train.py` uses, with student number, habit, course code and topic title) and `results/dataset_summary.md` (counts by study habit). Habits are not stored in the database; they are recovered by replaying the seeded simulation, which must reproduce every student's attempt, answer and log counts or the script stops. Rerun it after `seed_demo.py` (full).
