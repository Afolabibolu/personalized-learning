# Techniques of Integration

## Indefinite integrals

An **antiderivative** of f is any F with F'(x) = f(x). The **indefinite integral** is **∫ f(x) dx = F(x) + C**, where C is the constant of integration. d/dx ∫ f dx = f and ∫ f' dx = f + C, so differentiation and integration are inverse processes. Geometrically, y = x² + C is a **family of parabolas** with parallel tangents at each x.

Properties: **∫(f + g) dx = ∫f dx + ∫g dx** and **∫kf dx = k∫f dx**.

Standard forms:

- ∫xⁿ dx = xⁿ⁺¹/(n + 1) + C, for n ≠ −1;
- ∫cos x dx = sin x + C and ∫sin x dx = −cos x + C;
- ∫1/x dx = ln|x| + C and ∫eˣ dx = eˣ + C.

## Substitution

Put u = g(x), so du = g'(x) dx.

- **∫(2x + 5)³ dx = (2x + 5)⁴/8 + C**.
- **∫cos(ax + b) dx = (1/a) sin(ax + b) + C**.
- **∫1/(at + b) dt = (1/a) ln|at + b| + C**.
- ∫x/√(x² + 1) dx = √(x² + 1) + C.

## Partial fractions

Rational functions are integrated by splitting them into partial fractions. The degree of the numerator must be **less than** that of the denominator; otherwise **long division** comes first. The cases are distinct linear factors, repeated linear factors and quadratic factors. For example, ∫(x + 8)/(x² + x − 2) dx = ∫[3/(x − 1) − 2/(x + 2)] dx = 3 ln|x − 1| − 2 ln|x + 2| + C.

## Trigonometric integrals

- Use **sin²x = ½(1 − cos 2x)**, **cos²x = ½(1 + cos 2x)**, sin³x = ¼(3 sin x − sin 3x) and **sec²x = 1 + tan²x**. So ∫sin²x dx = x/2 − sin 2x/4 + C, and ∫tan²x dx = tan x − x + C.
- **∫tan x dx = −ln|cos x| + C**, ∫cot x dx = ln|sin x| + C and **∫sec x dx = ln|sec x + tan x| + C**.
- For ∫tanᵐx secⁿx dx: if m is odd, put u = sec x; for even powers of sec x, put u = tan x.
- To remove radicals:
  - **√(a² − x²)**: put **x = a sin t**;
  - **√(a² + x²)**: put **x = a tan t**;
  - **√(x² − a²)**: put **x = a sec t**.

## By parts

**∫u dv = uv − ∫v du** (general knowledge; the scanned slides do not show it). ∫x eˣ dx = (x − 1)eˣ + C.

By parts gives **reduction formulae**: for Iₙ = ∫sinⁿx dx, **Iₙ = −(1/n) sinⁿ⁻¹x cos x + ((n − 1)/n) Iₙ₋₂**.

Source: MAT 121 Integration Lectures 1 and 2 (Adinya, 2021); MAT 121 Integration Lectures 3–4 (partial fractions) and 5–7 (trigonometric integrals) (Adinya, 2021); MAT 121 Lecture Notes; MAT 121 past papers; General knowledge of MTH 102 for integration by parts
