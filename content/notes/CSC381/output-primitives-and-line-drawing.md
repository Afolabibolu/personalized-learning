# Output Primitives and Line and Circle Drawing

## Output primitives

**Output primitives** are the basic geometric elements from which pictures are built:

- **points**;
- **straight-line segments**;
- **circles and ellipses**;
- **curves**;
- **polygons and filled areas**;
- **text (characters)**.

Each has **attributes** such as colour, line width, line style and fill pattern.

On a raster display, a primitive must be **scan-converted**: the continuous shape is approximated by choosing which pixels to light. Because pixels are discrete, slanted lines look stepped (**aliasing**, or "jaggies").

## The DDA line algorithm

The **digital differential analyser (DDA)** steps along the line in unit intervals of the axis with the larger change.

To draw from (x₁, y₁) to (x₂, y₂):

1. dx = x₂ − x₁ and dy = y₂ − y₁.
2. steps = max(|dx|, |dy|).
3. x_inc = dx ÷ steps and y_inc = dy ÷ steps.
4. Starting at (x₁, y₁), add the increments each step and plot the rounded point.

It is simple, but uses **floating-point** arithmetic and rounding, which is slow and accumulates error.

## Bresenham's line algorithm

**Bresenham's algorithm** uses only **integer** addition and subtraction. For a line with slope between 0 and 1, it steps x by one each time and decides whether y stays or rises by one, using a **decision parameter**:

- start with p₀ = 2dy − dx;
- if pₖ < 0, plot (xₖ + 1, yₖ) and set pₖ₊₁ = pₖ + 2dy;
- otherwise plot (xₖ + 1, yₖ + 1) and set pₖ₊₁ = pₖ + 2dy − 2dx.

Other slopes are handled by symmetry. It is faster and more accurate than DDA.

## The midpoint circle algorithm

A circle has **eight-way symmetry**: computing one octant gives the other seven by swapping and negating coordinates.

The **midpoint circle algorithm** starts at (0, r) with decision parameter p₀ = 1 − r. At each step x increases by 1:

- if p < 0, y stays and p = p + 2x + 1;
- otherwise y decreases by 1 and p = p + 2x + 1 − 2y.

It continues until x ≥ y. Like Bresenham, it uses only integer arithmetic.

## Antialiasing

**Antialiasing** reduces jaggies by shading pixels along an edge in intermediate intensities according to how much of the pixel the line covers. Techniques include **supersampling** (computing at higher resolution and averaging) and **area sampling**.

## Example

Drawing from (2, 3) to (10, 8) with DDA: dx = 8, dy = 5, steps = 8, x_inc = 1 and y_inc = 0.625. The points are (2, 3), (3, 3.625 → 4), (4, 4.25 → 4), and so on to (10, 8).



Source: general knowledge, following the CSC 381 2023/24 paper; the CSC 381 folder has no lecture material
