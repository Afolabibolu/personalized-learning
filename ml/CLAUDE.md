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
    {"resource_id": "…", "type": "textbook", "title": "Textbook: …", "url": null}
  ]
}
```

- `also` (25 Oct): the topic's first video and textbook that are not the main resource and not already accepted or dismissed. Cold-start rows get it too.

- `top_factors` for Logistic Regression comes from coefficient times the scaled feature value; take the two or three largest contributions. Do not add SHAP or other new libraries for this.
- Cold-start rows have `"reason": "Not enough quiz history yet for this course."`, no probabilities, and source `cold_start`.
- "Keep it up" rows (low probability, used to fill the list when fewer than 3 topics need attention) say why, for example "Scoring 80%. Try the topic quiz: questions you haven't seen come first."

## Notifications written by the service

After each run, insert notifications for the student, once per kind per day:
- `new_recommendations` when the top-ranked topic changed since the last run
- `weak_topic_unstudied` when a topic above 0.7 average probability has no study log in 7 days

Other reminder kinds (streak at risk, inactivity, daily goal, score improved) come from the SQL function described in `supabase/CLAUDE.md`.

## Reliability (NFR4)

- If a model file is missing or fails to load, use the cold-start path and log a warning. Never return a 500 for a student who exists.
- Each run deletes that student's pending recommendations before inserting new ones.

## Training and results

- Keep the three-way comparison: rule baseline (last score below 50%), Logistic Regression, Random Forest. Same split, same folds.
- `ml/results/metrics.md` and `summary.md` say once, at the top, that the data comes from simulated students (rules in `simulation_rules.md`). File names and chart titles do not repeat it. Never present the numbers as results from real students.
- `python -m training.train` must finish in under two minutes on a laptop.
- Add `ml/results/summary.md`: one short paragraph per model in plain words, the results table, and which features mattered most. This feeds Chapter Four.
