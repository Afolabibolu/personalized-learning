# 3D Modelling, Viewing and Rendering

## Building 3D models

A special-effects company modelling a fantasy creature for a film would:

1. **Block out** the creature with simple shapes (boxes, spheres, cylinders).
2. Build a **polygon mesh**, a surface of connected vertices, edges and faces, usually quads and triangles.
3. Refine it with **subdivision surfaces**, which split faces repeatedly to make smooth curved surfaces from a coarse "cage".
4. Use **digital sculpting**, pushing and pulling millions of polygons for skin, scales and wrinkles, then **retopology** to make an efficient animation mesh.
5. **UV-unwrap** the mesh and apply **textures** and materials.
6. Add **rigging** (a skeleton and controls) so animators can move it, with **skinning** to deform the mesh.
7. **Light and render** it, often with ray tracing, and composite it into live footage.

## Curves and surfaces

**Bézier curves** are defined by control points; the curve starts at the first point and ends at the last, pulled towards the others. **B-splines** and **NURBS** give smooth, locally controllable curves and surfaces, widely used in CAD.

## Viewing and projection

A 3D scene is viewed through a **camera**, defined by its position, direction and view volume, then **projected** onto a 2D plane.

- **Parallel (orthographic) projection:** projection lines are parallel, so sizes are preserved. It is used in engineering drawings.
- **Perspective projection:** projection lines meet at a centre of projection, so distant objects look smaller. It gives realistic views, with **vanishing points**.

## Hidden-surface removal

- **Back-face culling** discards polygons facing away from the viewer, those whose normal points away.
- The **z-buffer (depth buffer)** stores the depth of the nearest surface at each pixel. A new fragment is drawn only if it is closer. It is simple and handled in hardware.
- The **painter's algorithm** draws polygons from back to front.

## Lighting and shading

Lighting models combine **ambient**, **diffuse** (Lambertian, depending on the angle to the light) and **specular** (shiny highlight) reflection, as in the **Phong reflection model**.

- **Flat shading** gives each polygon one colour, so faces show.
- **Gouraud shading** computes colour at vertices and interpolates it across faces.
- **Phong shading** interpolates normals and computes colour per pixel, giving smooth highlights.

**Ray tracing** follows rays of light for accurate shadows, reflections and refraction, at a higher cost.

## Texture mapping and animation

**Texture mapping** wraps 2D images onto a surface for colour and detail, and **bump** or **normal maps** fake fine surface relief. **Animation** uses keyframes, interpolation, physical simulation (hair, cloth, muscle) and motion capture.



Source: general knowledge, following the CSC 381 2023/24 paper; the CSC 381 folder has no lecture material
