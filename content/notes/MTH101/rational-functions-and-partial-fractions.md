# Rational Functions and Partial Fractions

## Rational functions

A **rational function** is f(x)/g(x), where f and g are polynomials and g(x) ≠ 0. It is **proper** if deg f < deg g and **improper** otherwise. Rational functions are added, subtracted, multiplied and divided like fractions.

- The **domain** of a polynomial is all of ℝ. For y = f(x)/g(x), **Dom(y) = ℝ \ {x : g(x) = 0}**. For example, y = (x² + 4)/(x² − 1) has domain ℝ \ {1, −1}.
- The **zeros** come from setting the **numerator** f(x) = 0: (x² − 5x + 4)/(x − 5) has zeros 1 and 4.
- The **range**: make x the subject. For y = (2x + 1)/(3 − 4x), x = (3y − 1)/(4y + 2), so the range is ℝ \ {−½}. If x satisfies a quadratic in x, the range is where its **discriminant is ≥ 0**. For y = (x² − 5x + 4)/(x − 5) this gives (y − 1)(y − 9) ≥ 0, so **y ≤ 1 or y ≥ 9**.
- A **vertical asymptote** is where the denominator is zero: y = 6/(3 − x) has x = 3, with horizontal asymptote y = 0. To sketch the graph, combine the intercepts, asymptotes, turning points and sign.

## Partial fractions

**Resolution into partial fractions** splits a proper rational function into simpler ones.

- **Type I, distinct linear factors**: (px + q)/((x − a)(x − b)) ≡ A/(x − a) + B/(x − b). For (7x + 23)/((x + 2)(x + 5)), put x = −5 to get B = 4 and x = −2 to get A = 3. That is the **cover-up rule**; **comparing coefficients** gives the same answer.
- **Type II, repeated linear factors**: (px + q)/(x − a)² ≡ A/(x − a) + B/(x − a)², and generally up to Aₖ/(x − a)ᵏ. (x² + 1)/((x − 1)(x + 3)²) = 1/(8(x − 1)) + 7/(8(x + 3)) − 5/(2(x + 3)²).
- **Type III, non-factorisable quadratic factors**: each quadratic gets **(Bx + C)** on top. x²/((x + 1)(x² + x + 1)) = 1/(x + 1) − 1/(x² + x + 1).

If the fraction is **improper**, divide first to get a polynomial plus a proper fraction.

Partial fractions also make sums **telescope**: 1/(k(k + 1)) = 1/k − 1/(k + 1).

Source: MAT 111 Lecture 5: Rational Functions (Sangodapo); MAT 111 past papers; General knowledge of MTH 101 for asymptotes, which the slides do not treat
