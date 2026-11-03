# Lines and Planes in Space

## Lines

A line through the point A (position vector a), parallel to the direction vector d, is

**r = a + αd**, for α ∈ ℝ.

Through two points A and B, take d = b − a, so **r = a + α(b − a)**. Any non-zero multiple of d works as the direction.

Writing r = (x, y, z) gives the **parametric equations** x = a₁ + αd₁, y = a₂ + αd₂, z = a₃ + αd₃. Eliminating α gives the **standard Cartesian form**

**(x − a₁)/d₁ = (y − a₂)/d₂ = (z − a₃)/d₃**.

**Example**: the line through A(5, 2, 6) and B(−3, 6, 2) has AB = 4(−2i + j − k), so r = **(5 − 2α, 2 + α, 6 − α)**, or (x − 5)/(−2) = y − 2 = (z − 6)/(−1).

**Example**: through (−1, 2, 3) parallel to (3, 0, −1): x = −1 + 3α, y = 2, z = 3 − α. Conversely, (−x + 2)/7 = (3y − 1)/5 = (2z + 1)/3 becomes r = (2, ⅓, −½) + α(−7, 5/3, 3/2).

Two lines **intersect** if their equations are equal for some parameters: set r₁ = r₂ and solve component by component (general knowledge).

## Planes

A plane through r₀ = (x₀, y₀, z₀) with **normal vector n = (a, b, c)** is

**n·(r − r₀) = 0**, that is, **a(x − x₀) + b(y − y₀) + c(z − z₀) = 0**.

- Through (2, 4, −1) with normal (3, 5, −2): **3x + 5y − 2z = 28**.
- Through a = i + 5j + 3k, perpendicular to 2i + 3j + 6k: **2x + 3y + 6z = 35**.

**Through three points P, Q and R**, take n = PQ × QR, then use any one of the points. For P(1, −1, 3), Q(4, 1, −2) and R(−1, −1, 1), n = (−4, 16, 4) and the plane is **−x + 4y + z = −2**. (The slides end with −4x + 16y + 4z = −8, the same plane.)

**A line meeting a plane**: substitute the line's parametric form into the plane's equation and solve for the parameter. For r = (1, 0, 1) + s(2, 1, −3) and 3x + 2y + 4z = 11, this gives 3 + 6s + 2s + 4 − 12s = 11, so s = −1 and the point is **(−1, −1, 4)**.

Source: MAT 141 Vectors in R3 slides, Part 2 (O. B. Ogunfolu, 2018); MAT 141 / MTH 103 past papers; General knowledge of MTH 103 for intersections
