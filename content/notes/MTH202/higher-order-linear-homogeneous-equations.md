# Higher-Order Linear Homogeneous Equations

## The auxiliary equation

For the nth-order homogeneous linear equation with constant coefficients

**a0 dⁿy/dxⁿ + a1 dⁿ⁻¹y/dxⁿ⁻¹ + ... + a(n−1) dy/dx + an y = 0**, a0 ≠ 0,

try y = e^(mx). Substituting gives the **auxiliary (characteristic) equation**

**a0 mⁿ + a1 mⁿ⁻¹ + ... + a(n−1) m + an = 0.**

Its roots decide the form of the solution. For a second-order equation a y'' + b y' + c y = 0, the auxiliary equation is am² + bm + c = 0.

## The three cases

1. **Distinct real roots** m1, m2: **y = c1 e^(m1 x) + c2 e^(m2 x)**. For y'' − y' − 6y = 0, m² − m − 6 = (m − 3)(m + 2) = 0, so **y = c1 e^(3x) + c2 e^(−2x)**.
2. **Repeated root** m (twice): **y = (c1 + c2 x) e^(mx)**. A root repeated k times contributes (c1 + c2 x + ... + ck x^(k−1)) e^(mx).
3. **Complex roots** a ± ib: **y = e^(ax)(A cos bx + B sin bx)**. For y'' + k²y = 0, m = ±ik, so y = A cos kx + B sin kx. If a ± ib are each **k-fold** roots, each of cos bx and sin bx is multiplied by (c1 + c2 x + ... + ck x^(k−1)).

For y'''' − 4y''' + 14y'' − 20y' + 25y = 0, the auxiliary equation is (m² − 2m + 5)² = 0, so m = 1 ± 2i twice and **y = e^x[(c1 + c2 x) cos 2x + (c3 + c4 x) sin 2x]**.

## Structure of solutions

For a linear homogeneous equation, **any linear combination of solutions is a solution** (superposition). If y1, ..., yn are **n linearly independent** solutions (their **Wronskian** is non-zero), the general solution is **y = c1 y1 + c2 y2 + ... + cn yn**. For a non-homogeneous equation with right-hand side f(x), the general solution is the **complementary function** (the general solution of the homogeneous part) **plus a particular integral**.

## Missing variables

Some non-linear second-order equations lack y or x. If y is missing, F(x, y', y'') = 0 is reduced to first order by **p = y'**, so y'' = dp/dx. If x is missing, use p = y' with y'' = p dp/dy.

Source: MAT 241 class slides (A. O. Akeju) (Chapter 4: second-order homogeneous linear equations); MAT 241 past papers. The repeated complex root example is solved here from the 2012/13 paper.
