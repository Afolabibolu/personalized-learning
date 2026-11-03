# Functions of Several Variables and Partial Derivatives

## Functions of several variables

A **function of two variables** assigns to each ordered pair (x, y) in a set D a unique real number **f(x, y)**; D is the **domain** and the set of values taken is the **range**.

- For f(x, y) = √(x + y + 1)/(x − 1), f(3, 2) = √6/2, and the domain is **{(x, y) : x + y + 1 ≥ 0, x ≠ 1}**: the points on or above the line y = −x − 1, excluding the line x = 1.
- For g(x, y) = √(9 − x² − y²), the domain is the **disk x² + y² ≤ 9** and the range is **[0, 3]**, since a square root is never negative.

The **graph** of f is the surface z = f(x, y) in three dimensions. z = 6 − 3x − 2y is a **plane** with intercepts 2, 3 and 6; z = √(9 − x² − y²) is the **upper half of the sphere** of radius 3; and z = 4x² + y² is an **elliptic paraboloid**.

## Level curves

The **level curves** of f are the curves **f(x, y) = k** for constants k: where the surface has height k. For f(x, y) = 6 − 3x − 2y, the level curves 3x + 2y + (k − 6) = 0 are **parallel lines**, equally spaced because the graph is a plane.

## Partial derivatives

The **partial derivative with respect to x**, **∂f/∂x** or f_x, differentiates f with respect to x **while holding y constant**; ∂f/∂y holds x constant. For f(x, y) = x³ + x²y³ − 2y²:

- f_x = 3x² + 2xy³ and f_y = 3x²y² − 4y;
- the second-order partials are f_xx = 6x + 2y³, f_yy = 6x²y − 4 and **f_xy = f_yx = 6xy²** (the mixed partials agree when they are continuous).

## The chain rule

If z = f(x, y) with x = x(t) and y = y(t), then **dz/dt = (∂f/∂x)(dx/dt) + (∂f/∂y)(dy/dt)**. This chaining of derivatives is the foundation of **backpropagation** in neural networks.

## Differentials and linear approximation

The **total differential** of z = f(x, y) is **dz = f_x dx + f_y dy**, which estimates the change Δz caused by small changes dx and dy. The **linearisation** of f at (a, b) is **L(x, y) = f(a, b) + f_x(a, b)(x − a) + f_y(a, b)(y − b)**, used to approximate values and estimate errors. For a cylinder's volume V = πr²h, dV = 2πrh dr + πr² dh estimates the error in V from errors in r and h.

Source: Function of Several Variables slides (Function of several variables; Partial Derivatives); MTH 201 Course Outline (2025/2026) (topics 6, 7 and 8). The chain rule and differentials are from general knowledge of MTH 201, following the outline. The slide's range of [−3, 3] for √(9 − x² − y²) is corrected to [0, 3].
