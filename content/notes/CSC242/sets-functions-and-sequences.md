# Sets, Functions and Sequences

## Sets

A **set** is a collection of objects (**elements**): a ∈ A means "a is an element of A". The **order of elements is meaningless** and repetition does not matter, so {9, 2, 7, −3} = {7, 9, −3, 2} and {cat, horse, dog, dog} = {dog, cat, horse}. Two sets are **equal** if and only if they contain exactly the same elements. Logic and set theory are closely related.

- A ⊆ B: A is a **subset** of B; A ⊂ B: a **proper subset**.
- A finite set S with n distinct elements has **cardinality** n, written |S| = n.
- The **power set** P(A) contains all subsets of A; a set with n elements has 2ⁿ subsets.
- The **Cartesian product** A × B is the set of ordered pairs (a, b) with a ∈ A and b ∈ B, so |A × B| = |A| · |B|.
- **Union** A ∪ B = {x | x ∈ A ∨ x ∈ B}, **intersection** A ∩ B = {x | x ∈ A ∧ x ∈ B}, the **difference** A − B, and the **complement** of A (everything in the universe not in A). Sets are **disjoint** when their intersection is empty.

## Functions

A **function** f from A to B assigns to each element a of A **exactly one** element f(a) of B; A is the **domain** and B the **codomain**, and the set of values actually taken is the **range**.

- f is **one-to-one (injective)** if it never maps two distinct elements of A to the same element: f(x) = f(y) → x = y. f(x) = x² on the integers is not, because f(3) = f(−3). A strictly increasing or decreasing function is one-to-one.
- f is **onto (surjective)** if its range is all of B.
- f is a **bijection (one-to-one correspondence)** if it is both. A bijection has an **inverse function** f⁻¹: B → A.
- The **composition** (f ∘ g)(a) = f(g(a)) applies g first, then f. A function composed with its inverse is the identity i(x) = x.

The **floor** ⌊x⌋ assigns to a real number the largest integer less than or equal to it, and the **ceiling** ⌈x⌉ the smallest integer greater than or equal to it.

## Sequences

A **sequence** {aₙ} is a function from a subset of the natural numbers to a set, representing an **ordered list**. Finite sequences are also called **strings**. A formula such as aₙ = 2n − 1 describes 1, 3, 5, 7, …, and summation notation Σ adds the terms between an upper and lower index of summation.

Source: CSC 242.pdf (Discrete Structures lecture slides), the sets, functions and sequences sections
