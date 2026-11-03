# The Operator D Method

## The operator D

Let **D = d/dx**, so Dy = y', D²y = y'' and so on. A linear equation with constant coefficients becomes **f(D)y = g(x)**, for example (D² + D − 2)y = 2x − 40 cos 2x. Operators with constant coefficients can be multiplied and factorised like polynomials, so (D + 1)(D − 3) = D² − 2D − 3. The **complementary function** comes from the roots of **f(m) = 0**, exactly as with the auxiliary equation.

## Inverse operators

The **particular integral** is **y_p = (1/f(D)) g(x)**, where 1/f(D) is the **inverse operator**: f(D) applied to (1/f(D))g gives g. In particular **1/D means integration**: (1/D)g = ∫ g dx, and 1/(D − a) g = e^(ax) ∫ e^(−ax) g dx.

## Standard rules

1. **Exponentials**: **(1/f(D)) e^(ax) = e^(ax)/f(a)**, provided f(a) ≠ 0. For example, (1/(D + 3)) e^(−2x) = e^(−2x)/1 = **e^(−2x)**, and (1/((D − 3)(D + 4))) e^(−x) = e^(−x)/((−4)(3)) = **−e^(−x)/12**. If f(a) = 0, multiply by x and differentiate the denominator: (1/f(D)) e^(ax) = x e^(ax)/f'(a).
2. **Sines and cosines**: **(1/f(D²)) sin ax = sin ax / f(−a²)**, and likewise for cos ax, provided f(−a²) ≠ 0 (replace D² by −a²). For example, (1/(D² + 4)) e^(−3x) is an exponential case giving e^(−3x)/13, while (1/(D² + 1)) cos 2x = cos 2x / (−4 + 1) = **−(1/3) cos 2x**.
3. **Polynomials**: expand 1/f(D) as a **power series in D** and apply it term by term, stopping at the degree of the polynomial. For 1/(1 − D), use 1 + D + D² + ...
4. **Exponential shift**: **(1/f(D)) [e^(ax) V(x)] = e^(ax) (1/f(D + a)) V(x)**. This handles e^x(sin x + cos x) and similar terms.

## Example

For y'' + y = 2e^x, that is (D² + 1)y = 2e^x, the particular integral is (1/(D² + 1)) 2e^x = 2e^x/(1 + 1) = **e^x**, and the CF is A cos x + B sin x. For y'' − y = 2e^x, f(1) = 0, so y_p = x · 2e^x / f'(1) = 2x e^x/2 = **x e^x**.

## Reduction of order

When f(D) factorises, the inverse operator can be split by **partial fractions** or applied one factor at a time, each 1/(D − a) acting as e^(ax) ∫ e^(−ax)(·) dx. This **reduction of order** turns the problem into successive first-order integrations and gives the general solution if the arbitrary constants are kept.

Source: MAT 241 Operator D technique slides; MAT 241 class slides (A. O. Akeju) (Chapter 4: the operator D method); MAT 241 past papers and the tutorial questions. The worked examples are solved here.
