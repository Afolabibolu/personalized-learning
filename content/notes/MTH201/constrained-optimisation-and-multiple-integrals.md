# Extrema of Several Variables, Lagrange Multipliers and Multiple Integrals

## Extrema of functions of two variables

At an interior local extremum where the partial derivatives exist, **f_x(a, b) = 0 and f_y(a, b) = 0**; such a point is a **critical point**.

**Second derivative test**: at a critical point, let **D = f_xx f_yy − (f_xy)²**.

- If **D > 0 and f_xx > 0**, it is a **local minimum**.
- If **D > 0 and f_xx < 0**, it is a **local maximum**.
- If **D < 0**, it is a **saddle point** (neither).

For f(x, y) = x² + y² − 2x − 6y + 14: f_x = 2x − 2 = 0 and f_y = 2y − 6 = 0 give the critical point (1, 3). D = (2)(2) − 0 = 4 > 0 and f_xx = 2 > 0, so it is a **local minimum f(1, 3) = 4**.

## Lagrange multipliers

To find the extreme values of **f(x, y) subject to a constraint g(x, y) = k**, solve

**∇f = λ∇g and g(x, y) = k**,

that is, f_x = λg_x, f_y = λg_y and g = k, for x, y and the **Lagrange multiplier λ**. For example, to maximise f = xy subject to x + y = 10: y = λ, x = λ and x + y = 10 give x = y = 5, so the maximum is **25**.

## Line integrals

A **line integral** integrates along a curve C. If C is given by x = x(t), y = y(t) for a ≤ t ≤ b, then

**∫_C f(x, y) ds = ∫ from a to b of f(x(t), y(t)) √((dx/dt)² + (dy/dt)²) dt.**

For a force field F, **∫_C F · dr** gives the **work done** moving along C.

## Multiple integrals

A **double integral** ∫∫_R f(x, y) dA over a region R is evaluated as an **iterated integral**, integrating with respect to one variable while holding the other constant. Over a rectangle, the order of integration can be swapped (Fubini's theorem). For example, ∫ from 0 to 2 ∫ from 0 to 1 of (x + y) dy dx = ∫ from 0 to 2 of (x + 1/2) dx = **3**.

- **∫∫_R 1 dA** is the **area** of R.
- **∫∫_R f(x, y) dA**, with f ≥ 0, is the **volume** under the surface z = f(x, y).
- A **triple integral** ∫∫∫_E f dV extends this to three dimensions; ∫∫∫_E 1 dV is the **volume** of E.

Source: MTH 201 Course Outline (2025/2026) (topics 7, 9 and 10); Function of Several Variables slides (Maximum and Minimum Values). The worked examples and the Lagrange, line and multiple integral sections are from general knowledge of MTH 201, following the outline, because the scanned slides on these topics were not read in full.
