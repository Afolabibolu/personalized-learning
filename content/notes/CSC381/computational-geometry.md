# Computational Geometry

## What it is

**Computational geometry** is the study of efficient algorithms for solving geometric problems, involving points, lines, polygons and shapes. Real-life applications include:

1. **Computer graphics:** visibility, hidden-surface removal and collision detection in games.
2. **Robotics:** motion planning, obstacle avoidance and localisation.
3. **Geographic information systems:** map overlay, finding the nearest hospital, route planning.
4. **Computer-aided design and manufacturing:** modelling parts and planning tool paths.
5. **Computer vision and medical imaging:** shape reconstruction and mesh generation.
6. **Wireless networks:** coverage areas and cell placement using Voronoi diagrams.

## Convex hulls

The **convex hull** of a set of points is the smallest convex polygon containing them, like a rubber band stretched around nails.

- **Gift wrapping (Jarvis march)** starts at the leftmost point and repeatedly picks the point making the widest turn, in O(nh) time, where h is the number of hull points.
- **Graham scan** sorts the points by angle around the lowest point and keeps only left turns, in O(n log n) time.

## Basic tests

- **Orientation test:** the sign of the cross product (q − p) × (r − p) tells whether p, q, r turn left, turn right or are collinear. Most algorithms are built on it.
- **Segment intersection:** two segments intersect if each straddles the line through the other, checked with orientation tests. The **sweep-line** algorithm finds all intersections among n segments efficiently.
- **Point in polygon:** the ray-casting (even-odd) or winding-number test.

## Triangulation and Voronoi diagrams

- **Triangulation** divides a polygon or point set into triangles. The **Delaunay triangulation** maximises the smallest angles, avoiding thin triangles, which suits terrain and finite-element meshes.
- A **Voronoi diagram** divides the plane into regions, each containing the points closest to one site. It is the dual of the Delaunay triangulation, and answers nearest-neighbour questions.

## Robot navigation in a crowded warehouse

- **Configuration space:** the robot is shrunk to a point and each obstacle grown by the robot's size, so planning becomes finding a path for a point.
- **Motion planning:** a **visibility graph** joins mutually visible obstacle corners, giving shortest paths. **Voronoi-based roadmaps** keep the robot as far as possible from obstacles, and grid or sampling methods (probabilistic roadmaps, RRT) handle complex spaces. Paths are searched with **Dijkstra's** or the **A*** algorithm.
- **Obstacle avoidance:** collision detection with bounding boxes and spatial partitioning (quadtrees, k-d trees), with fast replanning as people and forklifts move.
- **Localisation:** matching sensor data to a map, for example by triangulation from known beacons or SLAM, to estimate the robot's position.



Source: general knowledge, following the CSC 381 2023/24 paper; the CSC 381 folder has no lecture material
