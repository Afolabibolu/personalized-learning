# Training dataset

All figures come from simulated students created by `scripts/seed_demo.py` (rules in `simulation_rules.md`), not from real students.

The models are trained on `training_data.csv`: one row per simulated student and topic, 960 rows. Features come only from
attempts and study logs before the student's last attempt on the topic; that last attempt gives `label_score`, and
`requires_attention` is 1 when it is below 50%. Student-topic pairs with a single attempt have no next attempt and are left out
(none here: every student took a diagnostic and at least one later quiz on each topic). Courses: CSC 531 and CSC 574 (the reviewed
courses), 12 topics.

Counts of quiz attempts (diagnostics included), answers and study logs are for the simulated students only.

| Study habit | Students | Quiz attempts | Answers | Study logs | Rows | Rows requiring attention | Share |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Steady (often, short sessions) | 38 | 2073 | 11353 | 3728 | 456 | 138 | 30.3% |
| Crammer (little, then hard before quizzes) | 26 | 1441 | 7881 | 2677 | 312 | 71 | 22.8% |
| Rare (seldom) | 16 | 872 | 4776 | 532 | 192 | 85 | 44.3% |
| **All** | 80 | 4386 | 24010 | 6937 | 960 | 294 | 30.6% |

Each student's habit is not stored in the database; it was recovered by replaying the seeded simulation (seed 2026),
which reproduced every student's number of quiz attempts, answers and study logs exactly.

Columns of `training_data.csv`: student (1 to 80, from sim-NNN), habit, course_code, topic_title, mean_score, last_score, attempt_count, session_count, total_minutes, days_since_last_studied,
label_score, requires_attention.
