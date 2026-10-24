# Graphs, Spanning Trees and NP-Completeness

## Graphs

A graph G = (V, E) is a set of vertices V and a set of edges E, written as pairs (u, v). Graphs model networks such as roads, circuits, web links and social networks.

**Terms:**
- **Adjacent vertices** share an edge.
- **Order** is the number of vertices; **size** is the number of edges.
- **Degree** is the number of edges at a vertex. An **isolated vertex** has none, and a **self-loop** joins a vertex to itself.
- A **path** is a sequence of edges from one vertex to another.

**Types of graph:**
- directed or undirected, weighted or unweighted
- **complete:** every vertex joined to every other
- **bipartite:** vertices split into two disjoint sets, with every edge crossing between them
- **tree:** connected, with no cycles

**Representations.** An **adjacency matrix** is an n × n matrix of 0s and 1s, where adjMat[i][j] = 1 if an edge joins i to j. An **adjacency list** is an array of n lists, each holding a vertex's neighbours.

## Traversal

**Breadth-first search (BFS)** visits every node at the current depth before moving deeper. It uses a **queue** and a visited array, because graphs, unlike trees, can contain cycles. **Depth-first search (DFS)** goes as deep as possible along each branch before backtracking. It uses a stack (or recursion) and a visited array. Both run in O(V + E) time.

## Spanning trees

A spanning tree is a subgraph of a connected undirected graph that includes every vertex, using the minimum number of edges. A complete graph with n vertices has n^(n−2) spanning trees, so 16 for n = 4. A **minimum spanning tree (MST)** is the spanning tree whose edge weights sum to the least.

**Kruskal's algorithm** is greedy:
1. Sort the edges from lowest to highest weight.
2. Add the lightest edge, rejecting it if it creates a cycle.
3. Repeat until every vertex is reached.

**Union-find** checks whether two vertices are already in the same cluster, which tells it whether an edge would form a cycle. Kruskal runs in O(E log E). **Prim's algorithm** starts from a vertex instead and keeps adding the lightest edge that leaves the tree. MSTs are used to design wiring, LANs and utility networks.

## NP-completeness

Tractable problems have polynomial-time algorithms, such as O(n) or O(n²); intractable ones need exponential time. A problem is in **NP** if a guessed solution can be verified in polynomial time. A problem is **NP-hard** if every NP problem reduces to it in polynomial time, and **NP-complete** if it is both in NP and NP-hard. If one NP-complete problem had a polynomial algorithm, every NP problem would.

Examples include SAT, knapsack, Hamiltonian path, the travelling salesman problem (decision version), subset sum, clique, vertex cover and graph colouring. In practice, NP-complete problems are attacked with approximation, randomization, restriction, parameterization or heuristics.

Source: CSC 551 Design and Analysis of Algorithms.pdf, Study Sessions 8, 9 and 10
