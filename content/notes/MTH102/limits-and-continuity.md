# Limits and Continuity

## Limits

**lim x→a f(x)** is the value f(x) approaches as x gets indefinitely close to a, but **not equal** to it. That is why a factor x − a can be cancelled.

- **Factorise and cancel**: (x² − a²)/(x − a) = x + a for x ≠ a, so the limit is **2a**. Similarly (x³ − a³)/(x − a) → **3a²**, and in general **(xⁿ − aⁿ)/(x − a) → naⁿ⁻¹**.
- **Rationalise**: multiply by the conjugate surd. For [√(3a − x) − √(x + a)]/(4(x − a)), the numerator becomes 2a − 2x, so the limit is −1/(2(√(2a) + √(2a))) = **−1/(4√(2a))**. (The notes write √3a + √2a in the last step; at x = a both surds equal √(2a).)
- **Direct substitution** works when the function is defined and continuous there: lim x→1 (2x² − 1) = 1.
- **Limits at infinity**: divide the top and bottom by the highest power. (Ax² + Bx + C)/(ax² + bx + c) → **A/a** as x → ∞, because B/x, C/x² and so on → 0.

## The basic trigonometric limit

Comparing areas in the unit circle gives ½ sin θ ≤ θ/2 ≤ ½ tan θ, so 1 ≤ θ/sin θ ≤ 1/cos θ. Since cos θ → 1,

**lim θ→0 (sin θ)/θ = 1.**

Consequences:

- lim x→0 tan 2x/(2x) = 1.
- lim x→1 sin 2(x − 1)/(x³ − 1) = 2 × 1 × ⅓ = **⅔**, by writing it as [sin 2(x − 1)/(2(x − 1))] × 2/(x² + x + 1).
- **lim θ→0 (1 − cos θ)/θ = 0**, using 1 − cos θ = 2sin²(θ/2).
- **lim x→0 (1 − cos x)/x² = ½**.

## Continuity

f is **continuous at a** if f(a) is defined, the limit exists, and **lim x→a f(x) = f(a)**. Polynomials, sin and cos are continuous everywhere. A rational function is continuous wherever the denominator is non-zero: (x + 1)(x − 3)/((x − 2)(x + 4)) is continuous for all x except **2 and −4**.

Source: MAT 121 Lecture Notes; MAT 121 past papers; General knowledge of MTH 102 for the definition of continuity
