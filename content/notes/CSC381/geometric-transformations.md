# Geometric Transformations

Transformations change an object's position, size, orientation or shape.

## Basic 2D transformations

- **Translation** moves a point by (tx, ty): x′ = x + tx and y′ = y + ty.
- **Scaling** by factors (sx, sy) about the origin: x′ = sx·x and y′ = sy·y. Equal factors give uniform scaling; a factor above 1 enlarges.
- **Rotation** by angle θ about the origin, anticlockwise: x′ = x cos θ − y sin θ and y′ = x sin θ + y cos θ.
- **Reflection** mirrors an object, for example about the x-axis: (x, y) → (x, −y).
- **Shear** slants an object, for example x′ = x + shx·y.

## Homogeneous coordinates

Translation cannot be written as a 2 × 2 matrix product, so points are written in **homogeneous coordinates** (x, y, 1). Every transformation is then a 3 × 3 matrix:

- translation T = [[1, 0, tx], [0, 1, ty], [0, 0, 1]];
- scaling S = [[sx, 0, 0], [0, sy, 0], [0, 0, 1]];
- rotation R = [[cos θ, −sin θ, 0], [sin θ, cos θ, 0], [0, 0, 1]].

The transformed point is P′ = M · P.

## Composite transformations

A sequence of transformations is combined by **multiplying their matrices** into one composite matrix, applied right to left. Matrix multiplication is **not commutative**, so the order matters.

**Rotation about a fixed point (xr, yr):**

1. translate the point to the origin, T(−xr, −yr);
2. rotate, R(θ);
3. translate back, T(xr, yr).

The composite is M = T(xr, yr) · R(θ) · T(−xr, −yr). Scaling about a fixed point works the same way.

**Example:** rotating (1, 0) by 90° about the origin gives (cos 90°, sin 90°) = (0, 1).

## 3D transformations

In 3D, points are (x, y, z, 1) and matrices are 4 × 4.

- Translation and scaling extend directly.
- Rotation is about an axis. About the z-axis: x′ = x cos θ − y sin θ, y′ = x sin θ + y cos θ, z′ = z. Rotations about the x- and y-axes are similar.
- Rotation about an arbitrary axis combines translating, aligning the axis with a coordinate axis, rotating, and undoing the alignment.

## Window-to-viewport mapping

A **window** is the region of the world to display, and a **viewport** is where it appears on the screen. The mapping scales and translates window coordinates to viewport coordinates:

xv = xvmin + (xw − xwmin) × (xvmax − xvmin) ÷ (xwmax − xwmin),

and similarly for y.



Source: general knowledge, following the CSC 381 2023/24 paper; the CSC 381 folder has no lecture material
