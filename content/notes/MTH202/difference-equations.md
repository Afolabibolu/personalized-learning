# Difference Equations

## Finite differences

For values y0, y1, ..., yn at equally spaced points, the differences **y1 − y0, y2 − y1, ...** are the **first forward differences**, written **Δy0, Δy1, ...**, where **Δ is the forward difference operator**: **Δy_r = y_(r+1) − y_r**. Differences of differences are the second forward differences, Δ²y_r = Δy_(r+1) − Δy_r, and so on. **Backward differences** use **∇y_r = y_r − y_(r−1)**. The **shift operator E** moves one step: **E y_r = y_(r+1)**, so **Δ = E − 1** and ∇ = 1 − E⁻¹. For a polynomial of degree n, the nth differences are constant.

## Difference equations

A **difference equation** relates terms of a sequence, such as y_(n+2) − 5y_(n+1) + 6y_n = 0. Its **order** is the difference between the largest and smallest indices (here 2).

It is **formed by eliminating arbitrary constants**. From y_n = A + B·4ⁿ: y_(n+1) = A + 4B·4ⁿ and y_(n+2) = A + 16B·4ⁿ; eliminating gives **y_(n+2) − 5y_(n+1) + 4y_n = 0**. A solution y_n = C1 aⁿ + C2 bⁿ belongs to the equation with characteristic roots a and b: y_n = C1 (3)ⁿ + C2 (−4)ⁿ gives y_(n+2) + y_(n+1) − 12 y_n = 0.

## Solving linear equations

For **y_(n+2) + a y_(n+1) + b y_n = 0**, try y_n = mⁿ to get the **characteristic equation m² + am + b = 0**.

- **Distinct roots** m1, m2: **y_n = C1 m1ⁿ + C2 m2ⁿ**. For y_(n+2) − 5y_(n+1) + 6y_n = 0, m = 2, 3, so y_n = C1 2ⁿ + C2 3ⁿ.
- **Repeated root** m: **y_n = (C1 + C2 n) mⁿ**. For y_(n+2) − 4y_(n+1) + 4y_n = 0, m = 2 twice, so y_n = (C1 + nC2)2ⁿ; similarly y_(n+2) + 4y_(n+1) + 4y_n = 0 has y_n = (C1 + nC2)(−2)ⁿ.
- **Complex roots** r(cos θ ± i sin θ): **y_n = rⁿ(A cos nθ + B sin nθ)**.

## Particular solutions

For a non-homogeneous equation, add a **particular solution** of the same form as the right-hand side, using undetermined coefficients: try **K·aⁿ** for aⁿ (multiplied by n if a is a characteristic root) and a polynomial for a polynomial in n.

For y_(n+2) − 5y_(n+1) + 6y_n = 4·5ⁿ, try K·5ⁿ: K(25 − 25 + 6) = 4, so K = 2/3 and **y_n = C1 2ⁿ + C2 3ⁿ + (2/3)5ⁿ**. Initial conditions such as y0 = 1 and y1 = 3 then fix C1 and C2.

Difference equations also model growth step by step. If one amoeba in ten divides each hour, the population grows as **P_(n+1) = 1.1 P_n**, so P_n = 1500(1.1)ⁿ; adding 40 amoeba each hour gives **P_(n+1) = 1.1 P_n + 40**.

Source: MAT 241 Difference Equation slides; MAT 241 class slides (A. O. Akeju) (Chapter 6 in the outline); MAT 241 past papers. The worked examples are solved here from the past papers.
