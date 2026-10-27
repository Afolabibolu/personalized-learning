# Graphs and Spanning Trees

## Terms

A **graph** G = (V, E) is a set of **vertices** (nodes) and **edges**, each edge joining two vertices. A **path** is a sequence of edges between two vertices, and two vertices joined by an edge are **adjacent**. In a **directed** graph each edge has a direction; in an **undirected** graph it does not. Graphs are **sparse** (few edges) or **dense** (many edges).

## Representation

**Adjacency matrix:** a |V| × |V| matrix of 0s and 1s, where entry (i, j) is 1 if edge (i, j) exists; for a weighted graph the weight is stored instead.

- The matrix of an undirected graph is always **symmetric**; that of a directed graph is not.
- It is simple to program, and adding, removing or checking an edge takes **O(1)** time.
- It uses a lot of memory for big graphs, and adding or removing a vertex is costly. It is best for dense graphs.

**Adjacency list:** an array of linked lists, one per vertex, each listing that vertex's neighbours.

- It needs less memory and stores the graph more compactly.
- Adding or removing an edge is less easy, and it copes badly with a changing number of vertices.

## Traversal

Graph traversal visits each vertex exactly once; tree traversal is a special case.

**Depth-first search (DFS)** goes deep along one path before exploring breadth, using a **stack**:

1. Visit an adjacent unvisited vertex, mark it, display it and push it.
2. If no adjacent unvisited vertex is left, pop a vertex from the stack.
3. Repeat until the stack is empty.

A disconnected graph cannot be fully visited from one start.

**Breadth-first search (BFS)** visits all neighbours before going deeper, using a **queue**:

1. Visit an adjacent unvisited vertex, mark it, display it and enqueue it.
2. If none is left, dequeue the first vertex.
3. Repeat until the queue is empty.

BFS finds the shortest path between two vertices in an unweighted graph, so it can check whether two servers in a network are connected.

## Spanning trees

A **spanning tree** of a connected undirected graph is a subgraph that connects all the vertices with the fewest possible edges.

- It has **n − 1 edges** and no cycles.
- Removing an edge disconnects it, and adding one creates a loop.
- A disconnected graph has no spanning tree.
- A complete graph has at most **n^(n−2)** spanning trees.

A **minimum spanning tree** has the least total edge weight, and is found by the greedy algorithms of **Kruskal** and **Prim**. Uses include network planning, routing protocols and cluster analysis.

Source: Graph Adj List.pdf, pages 1–22 (representation, DFS, BFS and spanning trees)
