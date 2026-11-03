# Differentiation

## First principles

For points P(x, f(x)) and Q(x + h, f(x + h)) on the curve, the gradient of the chord PQ is (f(x + h) − f(x))/h. As Q moves to P, this tends to the gradient of the curve at P:

**f'(x) = lim h→0 [f(x + h) − f(x)]/h**, written f'(x), dy/dx or (Df)(x).

From this: **D(c) = 0**, **D(x) = 1** and **D(xⁿ) = nxⁿ⁻¹**. Also **D(sin x) = cos x**, using sin(x + h) − sin x = 2 cos(x + h/2) sin(h/2) and sin θ/θ → 1, and **D(cos x) = −sin x**.

## Rules

- **Sum**: D(f + g) = Df + Dg.
- **Product**: **D(fg) = f Dg + g Df**. For y = x⁶ cos x, y' = 6x⁵ cos x − x⁶ sin x.
- **Quotient**: **D(f/g) = (g Df − f Dg)/g²**. So D(sec x) = D(1/cos x) = sin x/cos²x = **sec x tan x**.
- **Chain rule**: if h = f ∘ u, then **h'(x) = f'(u(x)) u'(x)**. For y = (x⁵ + 3x + 2)⁻¹, y' = −(x⁵ + 3x + 2)⁻²(5x⁴ + 3).

## Exponentials and logarithms

**D(eˣ) = eˣ**, **D(ln x) = 1/x** and **D(ln u) = u'/u**: d/dx ln(x³ + 4x) = (3x² + 4)/(x³ + 4x). With the chain rule, D(e^(ax)) = a e^(ax).

For y = f(x)^g(x), take logs: ln y = g ln f, so **y' = f^g [g' ln f + g f'/f]**.

## Implicit differentiation

Differentiate both sides, treating y as a function of x, and collect the dy/dx terms. For y³ − 2xy + x³ = 0, 3y²y' − 2y − 2xy' + 3x² = 0. At (1, 1) this gives y' = **−1**, so the tangent is y = −x + 2.

## Higher derivatives

D²f = D(Df), and so on. **D⁴(sin x) = sin x** (the cycle is cos, −sin, −cos, sin), and D³(sin x) = −cos x.

For y = e^(ax) sin x, y' = e^(ax)(a sin x + cos x), and one shows y'' − 2a y' + (a² + 1)y = 0.

Source: MAT 121 Lecture Notes; MAT 121 past papers; General knowledge of MTH 102 for the exponential and logarithmic rules, which the notes do not derive
