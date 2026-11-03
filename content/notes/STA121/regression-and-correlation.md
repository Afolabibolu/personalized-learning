# Regression and Correlation

## Scatter diagrams

A **scatter diagram** plots one variable against another. If the points lie close to a straight line, the association is **linear**; if they lie close to a curve, it is **non-linear**.

## Regression or correlation?

- If **Y depends on X**, we study **regression** ("Y is regressed on X"). Examples: blood pressure on age, a son's height on his father's, maize yield on the number of plants. Y is the **dependent** and X the **independent** variable.
- If **neither depends on the other**, we study **correlation**, their mutual linear association. Examples: plantain prices in Lagos and fuel prices in Onitsha, or left-arm and right-arm lengths.

## The least-squares line

**ŷ = α̂ + β̂x**, with

**β̂ = (nΣxy − ΣxΣy)/(nΣx² − (Σx)²)** and **α̂ = ȳ − β̂x̄**,

so the line passes through (x̄, ȳ). A rough line through (x̄, ȳ) with equal numbers of points on each side gives a quick impression but is not recommended.

β̂ is the **regression coefficient**:

- β = 0 means Y does not depend linearly on X;
- β > 0 means each unit increase in X raises Y by β;
- β < 0 means Y falls as X rises.

**Example (marks)**: for seven students' maths (x) and physics (y) marks, Σx = 304, Σy = 410, Σxy = 19,084 and Σx² = 14,536.

- β̂ = (7 × 19,084 − 304 × 410)/(7 × 14,536 − 304²) = 8948/9336 ≈ **0.958**.
- α̂ = 58.57 − 0.958 × 43.43 ≈ **16.9**.

## Correlation

Regressing Y on X and X on Y gives two coefficients, β and β′. **Pearson's r is their geometric mean, r = √(ββ′)**:

**r = (nΣxy − ΣxΣy)/√[(nΣx² − (Σx)²)(nΣy² − (Σy)²)]**, with **−1 ≤ r ≤ 1**.

- r > 0: X and Y rise together.
- r < 0: one rises as the other falls.
- r = ±1: perfect correlation.
- **r = 0: no *linear* relationship**, though a non-linear one may exist.

## Rank correlation

For ranked or qualitative data, rank each variable (1, 2, ..., n) and use **Spearman's rₛ = 1 − 6Σd²/(n(n² − 1))**, where d is the difference in ranks. **Tied** values each get the **mean** of the ranks they would occupy.

**Example**: two judges rank four GSM providers 2, 1, 3, 4 and 1, 2, 3, 4. Then Σd² = 2 and rₛ = 1 − 12/60 = **0.8**.

Source: STA 121 2018 Lecture 7: Regression and Correlation Analysis (Olubusoye)
