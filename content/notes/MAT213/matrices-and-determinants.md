# Matrices and Determinants

## Matrices

A **matrix** is a rectangular array of numbers from a field; an m × n matrix A = (aᵢⱼ) is **square** if m = n, a **row matrix** if m = 1, and a **column matrix** if n = 1. Its **transpose** is Aᵀ = (aⱼᵢ). A square matrix is

- **symmetric** if Aᵀ = A and **skew-symmetric** if Aᵀ = −A,
- **normal** if AAᵀ = AᵀA, and
- **orthogonal** if AAᵀ = I = AᵀA.

Matrices of the same dimension add and subtract entry by entry, A ± B = (aᵢⱼ ± bᵢⱼ). AB is defined when the number of columns of A equals the number of rows of B.

## Elementary operations

Elementary row operations turn a matrix into an **equivalent** one: **Rᵢⱼ** interchanges rows i and j, **Rᵢ(a)** multiplies row i by a, and **Rᵢⱼ(α)** multiplies row j by α and adds it to row i. Performing one on an identity matrix gives an **elementary matrix**. If B is produced from A by a sequence of elementary row operations, A and B are **equivalent**.

A matrix is in **row reduced echelon form** if (1) the leading entry of every non-zero row is 1 and all other entries in its column are 0, (2) zero rows are below the non-zero rows, and (3) each leading entry is to the left of the one in the next row. Its **canonical (normal) form** also has the first leading entry in the first column. The number of non-zero rows in the row reduced echelon form is the **rank**.

## Determinants

For a 2 × 2 matrix, det(A) = a₁₁a₂₂ − a₁₂a₂₁; for example, the matrix with rows (4, 3) and (−2, 1) has determinant 4 + 6 = 10. A 3 × 3 determinant uses the **Laplace (cofactor) expansion** along a row with minors Mᵢⱼ and signs (−1)ⁱ⁺ʲ. Properties:

1. Interchanging two rows changes the sign.
2. Adding a multiple of one row to another leaves it unchanged.
3. Multiplying a row by α multiplies it by α.
4. The determinant of a triangular matrix is the product of its diagonal entries, so det(Iₙ) = 1.

## The inverse

The **cofactor matrix** C(A) holds the signed minors, and the **adjoint** is A* = C(A)ᵀ. Then **A⁻¹ = A*/|A|**. If |A| = 0 the inverse does not exist and A is **singular**. The inverse can also be found by applying elementary operations to [A | I] until A becomes I; I then becomes A⁻¹.

Source: MAT 213 Full.pdf (Algebra I lecture notes, B. O. Onasanya), Chapter 6 (Matrices and Other Concepts)
