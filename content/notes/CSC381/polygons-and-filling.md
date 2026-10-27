# Shapes, Polygons and Polygon Filling

## Why shapes and polygons matter

Shapes and polygons are the **building blocks** of computer graphics:

1. **Modelling:** complex 2D and 3D objects are approximated by many simple polygons, usually triangles, which are easy to store and process.
2. **Simulating real-world objects:** polygon surfaces with physical properties let objects collide, bend and move realistically.
3. **Rendering:** GPUs are built to rasterise triangles quickly, so a polygon model can be lit, shaded and textured into an image.

## Polygons

A **polygon** is a closed shape made of straight edges joining vertices.

- In a **convex** polygon, every interior angle is less than 180°, and the line joining any two interior points stays inside.
- A **concave** polygon has at least one interior angle greater than 180°.
- A **regular** polygon has equal sides and angles.
- **Triangles** are always convex and planar, which is why they are preferred.

**Inside-outside tests** decide whether a point is inside a polygon:

- **Even-odd rule:** draw a ray from the point; an **odd** number of edge crossings means inside.
- **Non-zero winding-number rule:** count how many times the edges wind around the point; non-zero means inside.

## Filling areas

- **Scan-line fill:** for each scan line, find where it intersects the polygon's edges, sort the intersections, and fill the pixels between pairs. An **edge table** and **active edge list** make it efficient. It suits polygons given by vertices.
- **Boundary fill:** start from an interior **seed** point and spread to neighbouring pixels (4- or 8-connected) until the **boundary colour** is reached.
- **Flood fill:** start from a seed and recolour all connected pixels of the **same original colour**. It suits areas with no single boundary colour.

Recursive fills are simple but can overflow the stack on large areas, so stack- or span-based versions are used.

## Polygon meshes

A **polygon mesh** is a collection of vertices, edges and faces (usually triangles or quadrilaterals) that defines a 3D object's surface. Meshes can be refined by **subdivision** into more, smaller faces for smoothness. **Triangulation** splits any polygon into triangles; a polygon with n vertices gives n − 2 triangles.

## Clipping

**Clipping** removes the parts of a picture outside the viewing **window**.

- **Cohen-Sutherland** line clipping gives each endpoint a 4-bit **region code**: lines with both codes 0000 are accepted, and lines whose codes share a set bit are rejected.
- **Sutherland-Hodgman** polygon clipping clips the polygon against each window edge in turn.



Source: general knowledge, following the CSC 381 2023/24 paper; the CSC 381 folder has no lecture material
