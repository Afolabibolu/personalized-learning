# Matrices, Determinants and Transformations

## Matrix algebra

An **m × n** matrix has m rows and n columns, with entries aᵢⱼ.

- Two matrices are **equal** if they have the same size and equal entries.
- Matrices of the **same order** are added entry by entry.
- **αA** multiplies every entry by α.
- **AB** is defined only if **the number of columns of A equals the number of rows of B**. An (m × n) times an (n × q) matrix is (m × q), with cᵢⱼ = Σ aᵢₖbₖⱼ.

In general **AB ≠ BA**. AB = AC does not imply B = C, and AB can be zero with A and B both non-zero.

The **transpose** Aᵀ swaps rows and columns, and **(A + B)ᵀ = Aᵀ + Bᵀ**. The special matrices are row, column, square, zero, **diagonal**, upper and lower **triangular** and **identity** (Iₙ, with **IA = AI = A**).

## Inverses and symmetry

A square matrix A is **invertible** if some B gives **AB = BA = I**; the inverse is unique. For A = (1 2; 4 3), **A² − 4A − 5I = 0**, so A⁻¹ = (1/5)(A − 4I). For a 2 × 2 matrix, A⁻¹ = (1/(ad − bc))(d −b; −c a), which exists only if **ad − bc ≠ 0**.

A is **symmetric** if **A = Aᵀ** and **skew-symmetric** if **Aᵀ = −A**. Every square matrix is the sum **A = ½(A + Aᵀ) + ½(A − Aᵀ)** of a symmetric and a skew-symmetric part.

**Elementary row operations** are: interchange rows (Rᵢⱼ), multiply a row by α ≠ 0 (Rᵢ(α)), and add α times one row to another (Rᵢⱼ(α)). They reduce a matrix to **echelon form**, which gives the **rank** and solves linear systems.

## Determinants

Expand a 3 × 3 determinant along any row or column with the sign pattern (+ − +; − + −; + − +), or use the **diagonal method**. For example |2 3 −4; 1 5 −2; 3 −1 6| = **84**. If the determinant is non-zero, the matrix is **non-singular**.

**Cramer's rule**: if |A| ≠ 0, the system has the unique solution **x = |B₁|/|A|, y = |B₂|/|A|, z = |B₃|/|A|**, where Bᵢ is A with column i replaced by the constants. For 3x − 2y + 3z = 8, x + y − 2z = −3 and 2x + y + 4z = 16, |A| = 31 and (x, y, z) = **(1, 2, 3)**.

## Transformations

A matrix maps points in the plane. Reflection in **y = x tan θ** has matrix **(cos 2θ sin 2θ; sin 2θ −cos 2θ)**. Graphs are translated as follows: y = f(x − a) + b moves the graph a units right and b units up.

Source: MAT 111 Module 3: Matrices and Determinants (Sangodapo, 2020/21); Ilori, MAT 111 (DLC) text (Lectures Twelve to Fourteen); MAT 111 past papers
