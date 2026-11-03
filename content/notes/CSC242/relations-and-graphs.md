# Relations and Graphs

## Relations

A **binary relation R from A to B** is a **subset of the Cartesian product A × B**; we write x R y when (x, y) ∈ R. A relation on A is a relation from A to itself. The **inverse relation** R⁻¹ from B to A contains (y, x) whenever (x, y) ∈ R; its arrow diagram reverses the arrows of R. For relations R and S, their **composition** pairs x with z when x R y and y S z for some y.

A relation R on a set A is:

1. **Reflexive** if x R x for every x in A: in its directed graph there is a loop at every point.
2. **Symmetric** if whenever x R y, then y R x: every arrow has a reverse arrow.
3. **Transitive** if whenever x R y and y R z, then x R z.

To show a property fails, give a counterexample, for example elements x and y with x R y but not y R x.

A relation that is reflexive, symmetric and transitive is an **equivalence relation**. The **equivalence class** [a] of an element a is the set of all elements related to a. The equivalence classes form a **partition** of A: a collection of nonempty, mutually disjoint subsets whose union is A. "Being in the same project group" is an equivalence relation whose classes are the groups.

## Graphs

A **graph** G consists of two finite sets: a nonempty set V(G) of **vertices** and a set E(G) of **edges**, each with one or two vertices as its **endpoints**. An edge with a single endpoint is a **loop**; two or more distinct edges with the same endpoints are **parallel**. Two vertices joined by an edge are **adjacent**, an edge is **incident** on its endpoints, and a vertex with no incident edges is **isolated**. A **directed graph (digraph)** gives each edge an ordered pair of vertices, drawn as an arrow; the directed graph of a relation is an example.

A **simple graph** has no loops or parallel edges. The **complete graph** Kₙ is the simple graph on n vertices with exactly one edge between each pair, so it has n(n − 1)/2 edges; K₅ has 10. The **degree** of a vertex is the number of edges incident on it, with a loop counted twice. By the **handshake theorem**, the total degree of a graph equals twice its number of edges. Graphs can be stored as an **adjacency matrix**, with entry (i, j) giving the number of edges from vertex i to vertex j.

Source: discrete mathematics ( PDFDrive ).pdf (Epp, Discrete Mathematics with Applications, 4th edition), Sections 8.1 to 8.3 (relations) and 10.1 (graphs)
