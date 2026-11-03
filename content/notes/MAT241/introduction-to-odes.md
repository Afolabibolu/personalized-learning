# Introduction to Ordinary Differential Equations

## Definitions

An **ordinary differential equation (ODE)** is an equation involving an unknown dependent function of **one independent variable** and its derivatives. An equation with partial derivatives in several independent variables, such as ∂²v/∂x² + ∂²v/∂y² = 0, is a **partial differential equation (PDE)**. The general nth-order ODE is F(x, y, y', ..., y^(n)) = 0, or explicitly y^(n) = f(x, y, y', ..., y^(n−1)).

- The **order** is the **highest derivative** present.
- The **degree** is the **power of the highest-order derivative**, once the equation is free of radicals and fractions in the derivatives.
- An ODE is **linear** if the dependent variable and its derivatives appear only to the **first power** and there are **no products** of them; otherwise it is **non-linear**.

For example, dy/dx = cos x is first-order linear; d²y/dx² + k²y = 0 is second-order linear; and (d²w/dx²)³ − xy dw/dx + w = 0 is **second-order, degree 3, non-linear**.

## Solutions

A **solution** on an interval a ≤ x ≤ b is any function y(x) that satisfies the equation there. The **general solution** of an nth-order ODE contains **n arbitrary constants**; a **particular solution** fixes them. **Initial conditions** are values of the solution and its derivatives at given points, and their number depends on the order. An **initial value problem (IVP)** is an ODE together with enough initial conditions. For example, y = c1 e^(−2x) + c2 e^(3x) is the general solution of y'' − y' − 6y = 0, as substituting shows.

## Forming ODEs

An ODE is formed by **eliminating arbitrary constants**: differentiate as many times as there are constants and eliminate them. From y = −A sin ax + B cos ax, y'' = −a²y, so **y'' + a²y = 0**.

## Applications

When a quantity changes **at a rate proportional to its size**, dy/dt = ky, so **y = y0 e^(kt)**.

- **Population growth**: if a population doubles in 50 years, e^(50k) = 2, so k = (ln 2)/50. It triples when e^(kt) = 3, at **t = 50 ln 3 / ln 2 ≈ 79 years**.
- **Radioactive decay**: dQ/dt = −kQ gives Q = Q0 e^(−kt), and the **half-life** is (ln 2)/k.
- **Newton's law of cooling**: dT/dt = −k(T − T_s), so T − T_s = (T0 − T_s)e^(−kt), where T_s is the room temperature.

Source: MAT 241 class slides (A. O. Akeju) (Chapter 1, Introduction); MAT 241 past papers
