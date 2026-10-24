# Computational Complexity and NP-Completeness

## Computational complexity

Computational complexity classifies problems by how hard they inherently are and by the resources algorithms need to solve them.

- **Time complexity** measures how long an algorithm takes as a function of input size. **Space complexity** measures how much memory it uses. Both are usually written in Big O, an upper bound on growth such as O(n²).
- **P** is the class of problems a deterministic algorithm can solve in polynomial time, the efficiently solvable ones.
- **NP** is the class whose proposed solutions can be checked in polynomial time.
- **PSPACE** holds problems solvable in polynomial space, and **EXPTIME** those solvable in exponential time.
- **Polynomial-time reductions:** if A reduces to B in polynomial time and B is solvable in polynomial time, so is A.
- **Approximation algorithms** give solutions close to optimal when an exact answer is too hard.

## Open problems

- **P versus NP:** can every problem that is verifiable in polynomial time also be solved in polynomial time?
- The exact complexity of problems such as the travelling salesman problem, graph isomorphism and integer factoring.
- De-randomization: can every randomized algorithm be made equally efficient deterministically?

## NP-completeness

Stephen Cook introduced NP-completeness in 1971. A problem is in NP if its solution can be guessed and verified in polynomial time; "nondeterministic" means no particular rule guides the guess. A decision problem L is **NP-complete** if:

1. L is in NP, and
2. every problem in NP reduces to L in polynomial time.

A problem that satisfies only property 2 is **NP-hard**. So NP-complete means both NP and NP-hard. NP-complete problems are the hardest in NP: if any one can be solved in polynomial time, every NP problem can.

The **Cook–Levin theorem** is the foundation. It shows that the Boolean satisfiability problem **SAT** (is there a truth assignment that makes a formula true?) is NP-complete, the first such problem. It follows that SAT ∈ P if and only if P = NP.

Reducibility is transitive: if A reduces to B in polynomial time and B is NP-complete, then A is NP-complete, provided A is also in NP.

To prove a new problem NP-complete, show that it is in NP, then reduce a known NP-complete problem to it. Well-known NP-complete problems include SAT, Hamiltonian path, the travelling salesman problem (decision version) and subgraph isomorphism. **3SAT** restricts SAT to formulas whose clauses each have three literals, and 3SAT reduces in polynomial time to **CLIQUE**. Each clause becomes a triple of nodes, and a clique of size k corresponds to a satisfying assignment.

**Why it matters.** In theory, anyone trying to show P ≠ NP can focus on one NP-complete problem. In practice, proving a problem NP-complete is strong evidence that it has no polynomial-time algorithm, which saves time spent searching for one.

Source: DLC CSC 552 Theory of Computation.pdf, Study Sessions 7 and 8
