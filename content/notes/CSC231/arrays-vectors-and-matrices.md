# Arrays, Vectors and Matrices in MATLAB

## Vectors and matrices

Arrays are entered in square brackets. A **row vector** separates elements with spaces or commas, `B = [1 2 3]`; a **column vector** separates them with semicolons, `C = [1; 2; 3]`. A **matrix** separates rows with semicolons: `A = [1 2 3; 4 5 6; 7 8 9]` is a 3 × 3 matrix. The **colon operator** makes ranges, `t = 0:0.1:1` (start, step, end), and `linspace(a, b, n)` makes n equally spaced points from a to b, which gives smooth curves. `zeros(m, n)`, `ones(m, n)` and `eye(n)` create special matrices, and `size(A)` and `length(v)` give dimensions.

## Indexing

Indices start at **1**. `A(2, 3)` is the element in row 2, column 3 (6 in the matrix above). A colon selects a whole row or column: `A(1, :)` is the **first row** [1 2 3] and `A(:, 2)` is the **second column** [2; 5; 8]. `A(end, :)` is the last row, and `A'` is the **transpose**, which turns rows into columns.

## Operations

- `A * B` is **matrix multiplication**; the number of columns of A must equal the number of rows of B.
- `.*`, `./` and `.^` are **element-wise** operations, applied to each pair of elements. To evaluate a formula at many points, use element-wise operators: `y = t.^2`.
- Adding or subtracting arrays needs the same size: `E = B + C'` adds a row vector and a transposed column.
- `dot(B, C)` gives the **dot product**, a scalar: for [1 2 3] and [2 5 8] it is 2 + 10 + 24 = 36.
- `cross(B, C)` gives the **cross product**, a vector perpendicular to both; both vectors must have 3 elements.
- `inv(A)` and `det(A)` give the inverse and determinant, and `A \ b` solves the linear system A x = b.

These operations are what the course's tests ask for: pick off a row and a column of a matrix, then find their cross and dot products and multiply the matrix by a vector.

Source: Written from general knowledge of CSC 231; no course file covered this topic.
