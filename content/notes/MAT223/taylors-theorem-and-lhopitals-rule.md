# Taylor's Theorem and L'Hopital's Rule

## Higher derivatives

If f is differentiable on [a, b] and f' is differentiable at x0, the **second derivative** is f''(x0) = lim (f'(x) − f'(x0))/(x − x0). Inductively, the nth derivative f^(n) exists when f^(n−1) is differentiable. For f(x) = x sin x, f'(x) = sin x + x cos x and **f''(x) = 2 cos x − x sin x**. For g(x) = 1/(x + 1), g'(x) = −1/(x + 1)², g''(x) = 2/(x + 1)³, **g'''(x) = −6/(x + 1)⁴** and g'''(0) = −6.

## Taylor's theorem

If f has n continuous derivatives near x0, then

**f(x) = f(x0) + f'(x0)(x − x0) + f''(x0)(x − x0)²/2! + ... + f^(n)(x0)(x − x0)^n/n! + R_n**,

where the **remainder** R_n is small for x near x0; in Lagrange's form, R_n = f^(n+1)(c)(x − x0)^(n+1)/(n + 1)! for some c between x0 and x.

**Example (n = 2)**: for g(a) = (1 + a)^(1/2) about 0, g(0) = 1, g'(0) = 1/2 and g''(0) = −1/4, so **(1 + a)^(1/2) ≈ 1 + a/2 − a²/8**. Then **√1.2 = (1 + 0.2)^(1/2) ≈ 1 + 0.1 − 0.005 = 1.095**. The same idea with (1 + a)^(1/3) ≈ 1 + a/3 − a²/9 gives **(1.6)^(1/3) ≈ 1 + 0.2 − 0.04 = 1.16**.

## L'Hopital's rule

The **Cauchy mean value theorem** states that if f and g are continuous on [a, b] and differentiable on (a, b), there is x0 in (a, b) with f'(x0)/g'(x0) = (f(b) − f(a))/(g(b) − g(a)), provided the denominators are non-zero.

From it comes **L'Hopital's rule**: suppose f(x) and g(x) both tend to **zero (or both to infinity)** as x → x0, are differentiable near x0 and g'(x) ≠ 0 there. Then

**lim f(x)/g(x) = lim f'(x)/g'(x)**,

provided the right-hand limit exists. Some limits are easy by factorising, such as lim as x → 3 of (x² − 9)/(x − 3) = 6, but others, such as **(1 − cos x)/x**, need the rule: the derivatives give sin x / 1 → **0**.

Examples from the papers:

- lim as x → 2 of (x³ − x² − x − 2)/(x³ − 3x² + 3x − 2): both are 0 at 2, and the derivatives give (12 − 4 − 1)/(12 − 12 + 3) = **7/3**.
- lim as x → 0 of (e^(x²) − 1)/sin x²: the rule gives 2x e^(x²) / (2x cos x²) → **1**.

Other indeterminate forms, such as ∞ − ∞ in 1/x − 1/sin x, or 1^∞, are rewritten as 0/0 or ∞/∞ first. For example, 1/x − 1/sin x = (sin x − x)/(x sin x) → **0** as x → 0. The limit lim (1 + 2/n)^(3n) = **e⁶**.

Source: MAT 223 lecture notes (scanned, Notes 1 to 9) (Taylor's Theorem; Indeterminate Forms and L'Hopital Rules); MAT 223 past papers. The worked numerical examples are calculated here from the past questions.
