# Linear Systems, Eigenvalues and Vector Spaces

## Linear systems

A system of linear equations is AX = B, where A is the **matrix of coefficients** and [A | B] the **augmented matrix**. If B = 0 the system is **homogeneous**, otherwise **non-homogeneous**.

- A homogeneous system always has the **trivial solution** X = 0. If the row reduced form of A is **Iₙ, the only solution is X = 0**. If rank(A) is less than the number of equations, there are non-trivial solutions.
- For AX = B with B ≠ 0, let r = rank(A), k = rank([A | B]) and n the number of equations. If **r < k** the system is **inconsistent** (no solution); if **r = k < n** it has **infinitely many** solutions; if **r = k = n** it has a **unique** solution.

## Eigenvalues

For an n × n matrix A, **|A − λI| = 0** is the **characteristic polynomial**, and its roots λ₁, …, λₙ are the **eigenvalues**. For A with rows (3, 1) and (2, 2): (3 − λ)(2 − λ) − 2 = (λ − 4)(λ − 1), so λ = 4 and 1. An **eigenvector** for λ solves (A − λI)X = 0.

The **Cayley-Hamilton theorem**: **every square matrix is a root of its characteristic polynomial**, so if f(λ) = (λ − 4)(λ − 1) then f(A) = (A − 4I)(A − I) = 0. Matrices A and B are **similar** if B = P⁻¹AP for some invertible P. Taking the eigenvectors as the columns of P gives the diagonal matrix **D = P⁻¹AP** of eigenvalues. Similar matrices share their determinant, characteristic roots, rank and characteristic polynomial.

## Vector spaces

A **vector space** V over a field F is an additive abelian group with scalar multiplication satisfying α(u + v) = αu + αv, (α + μ)v = αv + μv, (αμ)v = α(μv) and 1v = v. Rⁿ, matrices and polynomials are vector spaces. v is a **linear combination** of v₁, …, vₙ if v = Σλᵢvᵢ. The vectors are **linearly independent** if Σλᵢvᵢ = 0 forces every λᵢ = 0, and dependent otherwise; non-zero vectors are dependent if one is a combination of the others. A set **spans** V if every vector is a combination of it; a linearly independent spanning set is a **basis**, such as e₁ = (1, 0, 0), e₂, e₃ for R³. The **dimension** is the number of basis elements.

## Linear transformations

T : Vₙ(F) → Vₘ(F) is a **linear transformation** if T(αu + βv) = αT(u) + βT(v). Its **kernel**, Ker(T) = {v : T(v) = 0}, is the **null space**; the dimension of Ker(T) is the **nullity**, and the dimension of Im(T) is the **rank**.

Source: MAT 213 Full.pdf (Algebra I lecture notes, B. O. Onasanya), Chapter 6 (systems of equations, characteristic polynomials, similar and triangular matrices) and Chapter 7 (Vector Spaces and Linear Transformations)
