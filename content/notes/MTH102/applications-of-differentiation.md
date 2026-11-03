# Applications of Differentiation

## Tangents and approximations

The tangent at (x₀, y₀) has slope f'(x₀), so **y − y₀ = f'(x₀)(x − x₀)**. This is the **linearisation** of the curve at that point.

For small Δx, **f(x + Δx) ≈ f(x) + f'(x)Δx**, and the **error** is **Δy ≈ f'(x)Δx**.

- (0.999)¹⁰: take f(x) = x¹⁰, x = 1 and Δx = −0.001. Then the value is ≈ 1 + 10(−0.001) = **0.99**.
- A sphere has V = (4/3)πr³. With r = 21 and an error of ±0.5, ΔV ≈ 4πr²Δr = 4π(21)²(0.5) ≈ **2772**.

## Rates and motion

The derivative is a rate. A car worth f(t) = 50 + 2000/(t + 1) naira after t years depreciates at f'(3) = −2000/16 = **−125 naira per year** at age three.

For motion, velocity is ds/dt and acceleration is dv/dt. A rocket at height y = 640t − 16t² has y' = 640 − 32t, which is zero at t = 20, giving the **maximum height 6400**.

## Extrema

f has an **absolute maximum** at x₀ if f(x₀) ≥ f(x) for all x, and a **relative (local) maximum** if this holds for all x near x₀. Minima are defined the same way. On a closed interval, the absolute extrema are among the **critical values**, where f'(x) = 0 or f' does not exist, and the **endpoints**.

**Second derivative test**: at a stationary point f'(x₀) = 0,

- **f''(x₀) > 0 gives a minimum**;
- **f''(x₀) < 0 gives a maximum**.

A **point of inflexion** is where the concavity changes. f is **increasing** where f' > 0 and decreasing where f' < 0.

For f(x) = 2x³ − 3x² − 12x + 8, f'(x) = 6(x − 2)(x + 1), and f''(x) = 12x − 6. So x = −1 is a **maximum** (f = 15) and x = 2 a **minimum** (f = −12).

## Curve sketching

1. Find where the curve crosses the x-axis (y = 0) and the y-axis (x = 0).
2. Find the behaviour for large |x| and where y becomes large (asymptotes).
3. Find the turning points and inflexions.
4. Remember that polynomials are smooth, and between two maxima there is a minimum.

y = (x² − 1)/(x² + 1) has intercepts (±1, 0) and (0, −1), a turning point at x = 0, and tends to 1 as x → ±∞. Its range is −1 ≤ y < 1.

Source: MAT 121 Lecture Notes; MAT 121 past papers
