# Integration and Its Applications

## The definite integral

**∫ from a to b of f(x) dx = F(b) − F(a)**, where F is any antiderivative of f (F' = f): this is the **fundamental theorem of calculus**. The integral gives **signed area**: where f is negative the area counts negatively, so use the absolute value for total area. The **power rule** is **∫ xⁿ dx = xⁿ⁺¹/(n + 1) + C** for n ≠ −1, and ∫ (1/x) dx = ln|x| + C.

For example, ∫ from 1 to 4 of (3x/2 + 1) dx = [3x²/4 + x] from 1 to 4 = 16 − 7/4 = **57/4**.

## Area between curves

If f(x) ≥ g(x) on [a, b], the area between them is **A = ∫ from a to b of [f(x) − g(x)] dx**: **upper minus lower**. Find the limits by solving f(x) = g(x), and if the curves cross, split the integral. For y = 4 − 2x and y = 2x², the curves meet where x² + x − 2 = 0, at x = −2 and 1, and **A = ∫ from −2 to 1 of (4 − 2x − 2x²) dx = 9**.

## Volumes of revolution

- **Disk method** about the x-axis: **V = π ∫ from a to b of [f(x)]² dx**. Rotating y = sin x on [0, π] gives V = π ∫ sin²x dx = π ∫ (1 − cos 2x)/2 dx = **π²/2**.
- About the y-axis, express x in terms of y: **V = π ∫ x² dy**. Rotating y = x³ between y = 1 and y = 8: x = y^(1/3), so V = π ∫ from 1 to 8 of y^(2/3) dy = (3π/5)(32 − 1) = **93π/5**.
- **Shell method** about the y-axis: **V = ∫ 2πx · (height) dx**. For y = sin x on [0, π], V = 2π ∫ x sin x dx = 2π[−x cos x + sin x] from 0 to π = **2π²**.

## Arc length

The length of a smooth curve y = f(x) from a to b is **L = ∫ from a to b of √(1 + [f'(x)]²) dx**, from ds² = dx² + dy². For y = (2/3)x^(3/2) on [0, 4], f' = √x, so L = ∫ √(1 + x) dx = **(2/3)(5√5 − 1)**.

## Average value

The **average value** of f on [a, b] is **f_avg = (1/(b − a)) ∫ from a to b of f(x) dx**: the height of the rectangle on [a, b] with the same area. The **mean value theorem for integrals** says a continuous f equals its average value at some c in (a, b).

Source: MTH201 Study Guide (integration applications, theorems, optimisation) (sections 1 to 5); MTH201 slides 2 (integration and optimisation) (integration rules and substitution); MTH 201 Course Outline (2025/2026) (topic 3)
