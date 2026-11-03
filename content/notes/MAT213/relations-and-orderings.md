# Relations, Equivalence and Orderings

## Relations

A relation R from X to Y is a set of ordered pairs (x, y); its **inverse** is R⁻¹ = {(y, x)}. A relation between a set A and itself is a **relation on A**. The diagonal {(x, x)} is the **identity relation**, and X × X is the **universal relation**. A relation R on A is:

- **reflexive** if aRa for every a: the identity relation, the universal relation, ⊆, ≤ and = are reflexive;
- **symmetric** if aRb implies bRa: ⊆ and ≤ are not symmetric;
- **antisymmetric** if aRb and bRa imply a = b: ⊆ and ≤ are antisymmetric, the universal relation is not;
- **transitive** if aRb and bRc imply aRc.

## Equivalence relations

A relation that is **reflexive, symmetric and transitive** is an **equivalence relation**. The key example is **congruence modulo m**: a ≡ b (mod m) when m divides a − b. It is reflexive (m | 0), symmetric (m | (x − y) gives m | (y − x)) and transitive (m | (x − y) and m | (y − z) give m | (x − z)). **An equivalence relation induces a partition, and a partition induces an equivalence relation.** The **R-equivalence class** of a is [a] = {x : x R a}, and the collection of all equivalence classes is the **quotient set** X/R.

## Orderings

A relation that is **reflexive, antisymmetric and transitive** is a **partial order**, and (X, ≼) is a **partially ordered set (POSET)**. (R, ≤), (R, ≥) and (P(X), ⊆) are POSETs, but (Z, |) is not, because a | −a and −a | a with a ≠ −a, so it is not antisymmetric.

- a and b are **comparable** if a ≼ b or b ≼ a. A POSET in which every pair is comparable is **totally (linearly) ordered**, a **chain**. (N, |) is not a chain, since 3 and 5 are incomparable, but ({2, 6, 12, 36}, |) is.
- The **first (least)** element precedes every element and the **last (greatest)** follows every element. A **minimal** element has nothing properly preceding it and a **maximal** element nothing properly following it. In (P(X), ⊆), ∅ is first and minimal and X is last and maximal. (Z, ≤) has no minimal or maximal element.
- A totally ordered set is **well ordered** if every non-empty subset has a first element: (N, ≤) is, but (Z, ≤) is not, because the negative integers have no first element.
- Upper and lower bounds, the **least upper bound** and the **greatest lower bound** are defined for subsets: in (R, ≤), (0, 1) has least upper bound 1 and greatest lower bound 0.

Source: MAT 213 Full.pdf (Algebra I lecture notes, B. O. Onasanya), Chapter 2 (Relations) and Chapter 3 (Orderings)
