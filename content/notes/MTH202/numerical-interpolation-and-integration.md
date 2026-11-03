# Numerical Interpolation and Integration

## Errors

If x* approximates x, the **absolute error** is |x − x*| and the **relative error** is |x − x*|/|x|. An approximation is correct to **d decimal places** if |x − x*| ≤ (1/2) × 10^(−d). When two approximations are added, **the error of the sum is the sum of the errors**: E_(x+y) = E_x + E_y.

## Interpolation

**Interpolation** estimates f(x) between tabulated points by a polynomial through them.

- **Lagrange interpolation**: the polynomial through (x0, f0), ..., (xn, fn) is **P(x) = Σ f_i L_i(x)**, where L_i(x) = Π over j ≠ i of (x − x_j)/(x_i − x_j). With three nodes, P is **quadratic**. For f(x) = x + 2/x at x = 1, 2, 2.5, P(1.5) approximates f(1.5).
- **Newton's forward difference formula**: with spacing h and p = (x − x0)/h, **f(x) ≈ y0 + pΔy0 + p(p − 1)/2! Δ²y0 + ...**. Newton's divided difference form, f0 + (x − x0)f[x0, x1] + (x − x0)(x − x1)f[x0, x1, x2], also builds the quadratic interpolant.

## Numerical differentiation

Derivatives are approximated from differences: the **forward difference** f'(x) ≈ (f(x + h) − f(x))/h, with an error proportional to h; the **central difference** (f(x + h) − f(x − h))/(2h) is more accurate, with an error proportional to h².

## Numerical integration

A **quadrature rule** approximates a definite integral from function values. Integrating Newton's forward interpolation gives the **Newton-Cotes quadrature formula**; taking n = 1 and n = 2 gives the two main rules. With h = (b − a)/n and y_i = f(a + ih):

- **Trapezoidal rule** (n = 1, straight lines): **∫ ≈ (h/2)[y0 + 2(y1 + y2 + ... + y_(n−1)) + yn]**. Geometrically it replaces the curve by **straight lines**, summing the areas of trapezia. Its error is of order **h²**: |E| ≤ (b − a)h² max|f''| / 12.
- **Simpson's 1/3 rule** (n = 2, parabolas; **n must be even**): **∫ ≈ (h/3)[y0 + 4(y1 + y3 + ...) + 2(y2 + y4 + ...) + yn]**. Its error is of order **h⁴**: |E| ≤ (b − a)h⁴ max|f⁽⁴⁾| / 180.

For ∫ from 0 to π/2 of (6 + 3 cos x) dx, the exact value is 3π + 3 ≈ 12.425. Simpson's rule with n = 4 is very close to this, and the relative error is |exact − approximate| / exact.

## MATLAB

MATLAB's **trapz(x, y)** applies the trapezoidal rule to vectors x and y: for example, x = 0:pi/100:pi; y = exp(sin(x)); trapz(x, y).

Source: MAT 241 Numerical Integration slides; MAT 241 class slides (A. O. Akeju) (Chapter 7 in the outline); MAT 241 past papers. The error bounds, central difference formula and MATLAB example are from general knowledge of MAT 241, because the papers set them but the slides do not show them.
