# Sets

## Sets and notation

A **set** is a collection of objects, called **elements**. a ∈ A means "a is an element of A" and a ∉ A means it is not. A set can be written by **listing** its elements, A = {a₁, a₂, …, aₙ}, or by a **property**, as in {x ∈ N | x ≤ 200}. The **order of elements is meaningless**, and listing an element twice does not change the set: {dog, cat, horse} = {cat, horse, dog, dog}. Sets A and B are **equal** if and only if they contain exactly the same elements.

## Subsets and size

- A ⊆ B (A is a **subset** of B) means every element of A is in B; A ⊂ B (a **proper subset**) means A ⊆ B and A ≠ B. Every set is a subset of itself, and the **empty set** ∅ is a subset of every set.
- If S contains exactly n distinct elements, S is a **finite set** with **cardinality** n, |S| = n. Elements may themselves be sets: {5, {2, 3}, 6} has cardinality 3, and |∅| = 0.
- The **power set** P(A) is the set of all subsets of A. If |A| = n then |P(A)| = 2ⁿ; P({x, y}) = {∅, {x}, {y}, {x, y}}.
- The **Cartesian product** A × B is the set of all ordered pairs (a, b) with a ∈ A and b ∈ B, so |A × B| = |A| · |B|; the product of more than two sets is a set of ordered n-tuples.

## Set operations

With a **universal set** U containing everything under consideration:

- **Union** A ∪ B = {x | x ∈ A ∨ x ∈ B}.
- **Intersection** A ∩ B = {x | x ∈ A ∧ x ∈ B}; A and B are **disjoint** if A ∩ B = ∅.
- **Difference** A − B contains the elements of A that are not in B.
- **Complement** Aᶜ contains the elements of U that are not in A.

The operations mirror the logical connectives (OR, AND, NOT), which is why logic and set theory are closely related. **Venn diagrams** show sets as overlapping regions. To count a union of overlapping sets, add the sizes and subtract the overlap: |A ∪ B| = |A| + |B| − |A ∩ B|. If 40 students attend one workshop, 30 another and 15 both, then 55 attend at least one.

Source: 2. Sets.ppt (CSC 203 slides); CSC 242.pdf (Discrete Structures slides, filed in the CSC 203 folder), the set theory section
