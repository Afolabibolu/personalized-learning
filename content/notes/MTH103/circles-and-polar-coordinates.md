# Circles and Polar Coordinates

## Equations of a circle

A circle with centre (a, b) and radius r has equation **(x − a)² + (y − b)² = r²**. Expanding gives the **general form**

**x² + y² + 2gx + 2fy + c = 0**,

with **centre (−g, −f)** and **radius √(g² + f² − c)**.

**Example**: x² + y² − 8x − 10y + 32 = 0 has centre (4, 5) and r² = 16 + 25 − 32 = 9, so its area is **9π**.

## Tangent and normal

Differentiating x² + y² + 2gx + 2fy + c = 0 implicitly gives the slope of the **tangent** at (x₁, y₁):

**dy/dx = −(x₁ + g)/(y₁ + f)**.

The **normal** is perpendicular to the tangent, with slope **(y₁ + f)/(x₁ + g)**. It passes through the centre.

A circle **touches a line** when the perpendicular distance from the centre to the line equals the radius. The circle with centre (7, −6) touching 3x − 4y + 5 = 0 has r = |21 + 24 + 5|/5 = 10, so it is **(x − 7)² + (y + 6)² = 10²**.

The **length of the tangent** from an outside point (x₁, y₁) is **√(x₁² + y₁² + 2gx₁ + 2fy₁ + c)**. From (8, 10) to x² + y² − 2x − 4y = 4, it is √(64 + 100 − 16 − 40 − 4) = **√104** (general knowledge; the slide only poses the question).

A circle through three given points comes from substituting each point into the general form and solving for g, f and c.

## Polar coordinates

A point can be given by its **Cartesian** coordinates (x, y) or its **polar** coordinates (r, θ), where r is the distance from the origin and θ the angle from the positive x-axis. They are related by

**x = r cos θ, y = r sin θ, r² = x² + y², tan θ = y/x**.

To convert an equation, substitute. x² + y² = 4y becomes r² = 4r sin θ, so **r = 4 sin θ**: a circle of radius 2 centred at (0, 2).

Source: MAT 141 lecture note on Analytic Geometry and Mechanics (B. O. Onasanya), in Combined slides.pdf; MAT 141 / MTH 103 past papers; General knowledge of MTH 103 for tangent lengths and polar conversion, which appear only as outline headings and test questions
