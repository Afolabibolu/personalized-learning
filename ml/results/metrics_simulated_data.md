# Model comparison (simulated data)

All figures come from simulated students created by `scripts/seed_demo.py` (rules in `simulation_rules.md`), not from real students.

- Rows: 960 student-topic pairs from 80 simulated students
- Positive class (requires attention: next attempt below 50%): 30.6%
- Features: mean_score, last_score, attempt_count, session_count, total_minutes, days_since_last_studied
- The rule baseline uses only last_score; the models use all six features.
- Trained: 2026-10-19 21:39 UTC, model version v1

## 5-fold stratified cross-validation, mean ± standard deviation (simulated data)

| Model | Accuracy | Precision | Recall | F1 |
| --- | --- | --- | --- | --- |
| Rule baseline (last score < 50%) | 0.684 ± 0.023 | 0.488 ± 0.037 | 0.541 ± 0.047 | 0.512 ± 0.031 |
| Logistic Regression | 0.770 ± 0.009 | 0.678 ± 0.029 | 0.476 ± 0.029 | 0.559 ± 0.021 |
| Random Forest | 0.752 ± 0.011 | 0.633 ± 0.020 | 0.452 ± 0.035 | 0.527 ± 0.029 |

## Hold-out test set: 25%, stratified, the same rows for all three (simulated data)

| Model | Accuracy | Precision | Recall | F1 |
| --- | --- | --- | --- | --- |
| Rule baseline (last score < 50%) | 0.700 | 0.507 | 0.507 | 0.507 |
| Logistic Regression | 0.775 | 0.686 | 0.479 | 0.565 |
| Random Forest | 0.771 | 0.661 | 0.507 | 0.574 |
| System ranking (average of LR and RF probabilities) | 0.775 | 0.679 | 0.493 | 0.571 |

## What each model relies on (simulated data)

Logistic Regression coefficients are on standardised features: positive means a higher value makes "requires attention" more likely. Random Forest importances sum to 1.

| Feature | LR coefficient | RF importance |
| --- | --- | --- |
| mean_score | -1.332 | 0.426 |
| last_score | 0.225 | 0.118 |
| attempt_count | 0.001 | 0.037 |
| session_count | 0.013 | 0.073 |
| total_minutes | -0.16 | 0.151 |
| days_since_last_studied | 0.228 | 0.195 |
