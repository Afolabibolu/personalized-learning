# Continuity, Differentiability and Differentiation Rules

## Continuity

f is **continuous at x = a** if three conditions hold:

1. **f(a) is defined**;
2. **lim as x → a of f(x) exists**; and
3. **the limit equals f(a)**.

f is continuous on an interval if it is continuous at every point of it. Polynomials, sin x, cos x and e^x are continuous everywhere; rational functions are continuous wherever the denominator is non-zero. A **jump** discontinuity occurs when the one-sided limits differ, a **removable** one when the limit exists but differs from f(a) or f(a) is undefined, and an **infinite** one when f is unbounded near a, as with 1/x at 0.

For a piecewise function, check that the pieces meet: f(x) = x² + 1 for x < 1 and 2x for x ≥ 1 is continuous at 1, because both sides give 2.

## Differentiability

The **derivative** of f at a is **f'(a) = lim as h → 0 of (f(a + h) − f(a))/h**, the slope of the tangent at a. **If f is differentiable at a, then f is continuous at a.** **The converse is false**: f(x) = |x| is continuous at 0 but not differentiable there, because the left-hand difference quotient is −1 and the right-hand one is 1. So continuity is necessary but not sufficient for differentiability.

For a piecewise function to be differentiable at a join, it must be continuous there and its one-sided derivatives must agree. In the example above, the left derivative at 1 is 2x = 2 and the right derivative is 2, so it is also differentiable at 1.

## Rules of differentiation

- **Power rule**: d/dx(xⁿ) = n xⁿ⁻¹.
- **Sum and constant multiple rules**: (f + g)' = f' + g' and (cf)' = cf'.
- **Product rule**: **(uv)' = u'v + uv'**. For example, d/dx(x² sin x) = 2x sin x + x² cos x.
- **Quotient rule**: **(u/v)' = (u'v − uv')/v²**. For example, d/dx(x/(x + 1)) = 1/(x + 1)².
- **Chain rule**: **d/dx f(g(x)) = f'(g(x))·g'(x)**. For example, d/dx (3x² + 1)⁵ = 5(3x² + 1)⁴ · 6x = 30x(3x² + 1)⁴, and d/dx sin(2x) = 2 cos(2x).

Standard derivatives: d/dx sin x = cos x, d/dx cos x = −sin x, d/dx eˣ = eˣ and d/dx ln x = 1/x.

## Increasing and decreasing

**If f'(x) > 0 on an interval, f is increasing there; if f'(x) < 0, f is decreasing.** For f(x) = x³ − 6x² + 9x, f'(x) = 3(x − 1)(x − 3), so f increases on (−∞, 1) and (3, ∞) and decreases on (1, 3).

Source: MTH 201 Course Outline (2025/2026) (topics 2 and 3); MTH201 slides 1 (real-valued functions of a real variable) (Differentiability and Continuity; Differentiation Rules; Increasing and Decreasing Functions); MTH201 Study Guide (integration applications, theorems, optimisation)
