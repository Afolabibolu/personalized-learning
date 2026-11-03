# Rolle's Theorem, the Mean Value Theorem and Taylor Series

## Rolle's theorem

If **f is continuous on [a, b], differentiable on (a, b), and f(a) = f(b)**, then there is **at least one c in (a, b) with f'(c) = 0**: a smooth curve that starts and ends at the same height has a horizontal tangent somewhere between.

**Every condition is necessary.** f(x) = 1/x on [−1, 1] is not continuous at 0, and f'(x) = −1/x² is never 0; f(x) = |x| − 1 on [−1, 1] has f(−1) = f(1) = 0 but is not differentiable at 0, so no horizontal tangent exists.

For f(x) = x² + 2x on [−2, 0]: f(−2) = f(0) = 0 and f'(x) = 2x + 2 = 0 at **c = −1**. For f(x) = x³ − 4x on [−2, 2]: f'(x) = 3x² − 4 = 0 at **c = ±2/√3**.

## The mean value theorem

If **f is continuous on [a, b] and differentiable on (a, b)**, there is c in (a, b) with **f'(c) = (f(b) − f(a))/(b − a)**: the instantaneous rate of change equals the average rate, so the tangent at c is **parallel to the secant**.

For f(x) = x³ − x on [1, 3]: (24 − 0)/2 = 12 and 3c² − 1 = 12, so **c = √(13/3) ≈ 2.08**.

**Consequences**: if f' = 0 on (a, b), f is **constant**; if f' > 0, f is **strictly increasing**; if f' < 0, **strictly decreasing**; and if f' = g', then **f = g + C**.

## Power series

A **power series** about a is **Σ cₙ(x − a)ⁿ**. It converges for |x − a| < R, where R is the **radius of convergence**, found with the ratio test.

## Taylor and Maclaurin series

The **Taylor series** of f about x = a is

**f(x) = f(a) + f'(a)(x − a) + f''(a)(x − a)²/2! + ... + f⁽ⁿ⁾(a)(x − a)ⁿ/n! + ...**

The **Maclaurin series** is the case **a = 0**. Standard Maclaurin series are:

- **eˣ = 1 + x + x²/2! + x³/3! + ...** (for all x);
- **sin x = x − x³/3! + x⁵/5! − ...**;
- **cos x = 1 − x²/2! + x⁴/4! − ...**; and
- **ln(1 + x) = x − x²/2 + x³/3 − ...** (for −1 < x ≤ 1).

Truncating the series gives a **Taylor polynomial**, used to approximate values: e^0.1 ≈ 1 + 0.1 + 0.005 = 1.105.

Source: MTH201 Study Guide (integration applications, theorems, optimisation) (sections 7 and 8); MTH 201 Course Outline (2025/2026) (topics 4 and 5). The power and Taylor series section is from general knowledge of MTH 201, following the outline, as the study guide in the folder covers the theorems but not the series.
