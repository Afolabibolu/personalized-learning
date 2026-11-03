# Differentiability and the Mean Value Theorems

## The derivative

For f : X → Y, the slope of the line through (x, f(x)) and (x0, f(x0)) is the **difference quotient** **(f(x) − f(x0))/(x − x0)**, defined for x ≠ x0. For f : [a, b] → R and x0 in [a, b], the **derivative** of f at x0 is

**f'(x0) = lim as x → x0 of (f(x) − f(x0))/(x − x0)**,

when the limit exists. It is the **slope of the tangent** to the graph at x0. f is **differentiable** if it is differentiable at every point of its domain.

**If f is differentiable at x0, it is continuous at x0**. **The converse is false**: f(x) = |x| is continuous at 0 but not differentiable there, because the one-sided difference quotients are 1 and −1.

For example, g(a) = a² for a ≥ 0 and −a² for a < 0 is **differentiable at 0**, because (g(a) − g(0))/a equals a for a > 0 and −a for a < 0, and both tend to **0**, so g'(0) = 0.

## Rolle's theorem

**If f is continuous on [a, b], differentiable on (a, b), and f(a) = f(b), then there is c in (a, b) with f'(c) = 0.** For f(x) = x³ − 4x on [−2, 2]: f(−2) = f(2) = 0, and f'(c) = 3c² − 4 = 0 gives **c = ±2/√3**, both inside (−2, 2).

## The mean value theorem

**If f is continuous on [a, b] and differentiable on (a, b), there is c in (a, b) with f(b) − f(a) = (b − a)f'(c).** Geometrically, some tangent is **parallel to the chord** joining the endpoints. For g(a) = 4a³ − 8a² + 7a − 2 on [2, 5]: solving 12c² − 16c + 7 = (g(5) − g(2))/3 gives c ≈ 2.24.

## Fermat and Darboux

- **Fermat's theorem**: if f has a **local maximum or minimum** at an interior point a and f'(a) exists, then **f'(a) = 0**.
- A **critical point** is where f'(x) = 0 (or does not exist). For g(x) = x³ − 3x² − 9x, g'(x) = 3(x − 3)(x + 1), so the critical points are x = 3 (a local minimum) and x = −1 (a local maximum).
- **Darboux's theorem**: if f is differentiable on [a, b] and f'(a) ≠ f'(b), then **f' takes every value between f'(a) and f'(b)**, even if f' is not continuous.

Source: MAT 223 lecture notes (scanned, Notes 1 to 9) (Differentiability of a Function; Application of Derivability to Investigate Behaviour of Functions); MAT 223 past papers. The worked mean value and critical point examples are calculated here from the past questions.
