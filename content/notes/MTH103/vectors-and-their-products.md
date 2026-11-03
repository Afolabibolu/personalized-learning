# Vectors and Their Products

## Vectors

A **vector** has magnitude and direction: displacement, velocity, acceleration, force and momentum. A **scalar** has magnitude only: distance, time, mass, energy and power.

In space, r = xi + yj + zk, where i, j and k are mutually perpendicular unit vectors (a **unit triad**). Its magnitude is **|r| = √(x² + y² + z²)**, and the **unit vector** in its direction is **â = a/|a|**. The displacement **AB = b − a**.

For A(2, 1, 3) and B(6, 4, 3), AB = 4i + 3j, so |AB| = 5 and the unit vector is (4i + 3j)/5.

The **direction cosines** are cos α = x/|r|, cos β = y/|r| and cos γ = z/|r|, with **cos²α + cos²β + cos²γ = 1**.

Points are **collinear** if one displacement is a multiple of another: for A(1, 2, 3), B(3, 8, 1) and C(7, 20, −3), BC = 2AB.

## The scalar product

**a·b = |a||b| cos θ = a₁b₁ + a₂b₂ + a₃b₃**, so **cos θ = a·b/(|a||b|)**. Two vectors are **perpendicular if a·b = 0**.

- The **projection** of b on a is **b·â**.
- **Work done = F·d**. For F = 2i − 5j + 4k and AB = −i − 8j + 3k, the work is −2 + 40 + 12 = **50 J**.

## The vector product

**a × b = |a||b| sin θ n̂**, where n̂ is perpendicular to both vectors. It is the determinant

| i j k |
| a₁ a₂ a₃ |
| b₁ b₂ b₃ |

- a × b = 0 for parallel non-zero vectors.
- **|a × b|** is the **area of the parallelogram** on a and b, and the **area of a triangle** is **½|a × b|**.
- The **moment** of a force F about a point is **M = r × F** (the slides write F × r, which gives the same magnitude with the opposite sign). For F = 2i − j + k acting through (0, 3, 1), about (4, 0, −1), the magnitude is **√93 ≈ 9.64 N m**.
- A **unit vector perpendicular** to a and b is (a × b)/|a × b|.

## Triple products and the ratio theorem

The volume of the parallelepiped on a, b and c is **|a·(b × c)|**. The vectors are **coplanar** exactly when a·(b × c) = 0.

**Ratio theorem**: if P divides AB with AP : PB = m : n, then **r = (na + mb)/(m + n)**. For A(1, 1, 1), B(13, 4, 5) and the ratio 1 : 3, P = (4, 7/4, 2).

Source: MAT 141 Vectors in R3 slides, Part 2 (O. B. Ogunfolu, 2018); MAT 141 lecture note (University of Ibadan, 2016): vectors and motion, in Combined slides.pdf; MAT 141 / MTH 103 past papers
