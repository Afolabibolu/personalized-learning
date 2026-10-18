# Model comparison (simulated data)

All figures come from simulated students created by `scripts/seed_demo.py`, not from real students.

- Rows: 960 student-topic pairs from 80 simulated students
- Positive class (requires attention: next attempt below 50%): 38.8%
- Features: mean_score, last_score, attempt_count, session_count, total_minutes, days_since_last_studied
- Trained: 2026-10-18 14:15 UTC, model version v1

## Hold-out test set (25%, stratified, same split for both models) — simulated data

| model | accuracy | precision | recall | f1 |
| --- | --- | --- | --- | --- |
| Logistic Regression | 0.767 | 0.718 | 0.656 | 0.685 |
| Random Forest | 0.775 | 0.729 | 0.667 | 0.697 |
| Combined (average probability) | 0.779 | 0.733 | 0.677 | 0.704 |

## 5-fold stratified cross-validation (mean ± std) — simulated data

| model | accuracy | precision | recall | f1 |
| --- | --- | --- | --- | --- |
| Logistic Regression | 0.786 ± 0.029 | 0.748 ± 0.058 | 0.686 ± 0.018 | 0.714 ± 0.029 |
| Random Forest | 0.777 ± 0.036 | 0.737 ± 0.066 | 0.672 ± 0.043 | 0.701 ± 0.041 |
