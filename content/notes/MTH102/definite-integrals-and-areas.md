# Definite Integrals and Areas

## Area and the definite integral

Let A(x) be the area under y = f(x) from a fixed point up to x. Then A(x + Δx) − A(x) ≈ f(x)Δx, so **dA/dx = f(x)**: the area function is an antiderivative of f. Hence the area from x = a to x = b is

**∫ₐᵇ f(x) dx = [F(x)]ₐᵇ = F(b) − F(a)**, where F is any antiderivative.

The constant of integration cancels. For example, ∫₁³ x² dx = 27/3 − 1/3 = **26/3**, and ∫₁² (x + 3) dx = (2 + 6) − (½ + 3) = **9/2**.

## Properties

1. **∫ₐᵇ f = ∫ₐᶜ f + ∫ᶜᵇ f**: the interval can be split.
2. **∫ₐᵇ f = −∫ᵇₐ f**: swapping the limits changes the sign, so ∫₂¹ (x + 3) dx = −9/2.
3. The sum and constant-multiple rules carry over from indefinite integrals.

## Areas

The area under y = x² between x = 0 and x = 2 is [x³/3]₀² = **8/3**.

The **area between two curves** is ∫ (upper − lower) dx between their intersections. For y = x and y = x², which meet at x = 0 and x = 1, the area is ∫₀¹ (x − x²) dx = ½ − ⅓ = **1/6**. For y = x² and y = x³ on [0, 1], it is ⅓ − ¼ = **1/12**.

Area below the x-axis gives a negative integral, so take the absolute value of each part.

## Motion

If acceleration a(t) is known, velocity is v = ∫a dt and displacement is s = ∫v dt, with constants fixed by the initial conditions.

For a particle with initial speed 20 m/s and acceleration 18 − 2t, v = 20 + 18t − t², so **v(3) = 65 m/s**. The distance in 3 s is ∫₀³ v dt = 60 + 81 − 9 = **132 m**.

## Trigonometric powers

Use identities or the reduction formula Iₙ = −(1/n) sinⁿ⁻¹x cos x + ((n − 1)/n) Iₙ₋₂. On [0, π/2] the boundary term vanishes, so

**∫₀^(π/2) sinⁿx dx = ((n − 1)/n) ∫₀^(π/2) sinⁿ⁻²x dx.**

Thus ∫₀^(π/2) sin⁸x dx = (7/8)(5/6)(3/4)(1/2)(π/2) = **35π/256**.

Source: MAT 121 Lecture Notes; MAT 121 past papers; General knowledge of MTH 102 for the motion and reduction-formula worked answers
