# Sets and Functions

## Sets

A set is a collection of elements; an element can itself be a set, so {b, c} can be an element of C. The **cardinality** |A| or n(A) is the number of elements, finite or infinite. A set with no elements is the **empty set**, such as the set of all living humans who do not breathe.

If every element of A is in B, A is a **subset** of B (A ⊆ B); the empty set is a subset of every set. If A ⊆ B and B ⊆ A, then **A = B**. A ⊂ B means A ⊆ B and A ≠ B: A is a **proper subset**. For A = {1, …, 10}, the odd numbers B and the even numbers C are proper subsets.

The **universal set** E contains all objects under discussion, and the **complement** of A is Ā = {x | x ∈ E but x ∉ A}. With E = {0, 1, 2, …} and A = {1, …, 5}, Ā = {0, 6, 7, 8, …}. Union, intersection and difference A − B = {x : x ∈ A, x ∉ B} combine sets, and identities such as A − (B ∪ C) = (A − B) − C are proved by showing each side is contained in the other. The **symmetric difference** is

A Δ B = (A ∪ B) − (A ∩ B) = (A − B) ∪ (B − A).

## Products and partitions

The **Cartesian product** A₁ × A₂ × … × Aₙ is the set of all n-tuples (a₁, …, aₙ) with aᵢ ∈ Aᵢ. A collection {Aᵢ} of non-empty subsets of X is a **partition** of X if every element of X lies in some Aᵢ and distinct blocks are disjoint. The blocks are also called parts or cells; the odd and even integers partition Z.

## Functions

A **function (mapping)** f : A → B is a rule that assigns to each element a of A a **unique** element f(a) of B, its **image**. A is the **domain** and B the **codomain**.

- f is **injective (one-one)** if f(a) = f(b) always implies a = b.
- f is **surjective (onto)** if every element of B is an image, so Im(f) = B.
- f is **bijective (a one-one correspondence)** if it is both.

On the real numbers, eˣ is injective but not surjective; x(x − 1)(x − 2) is surjective but not injective, since f(0) = f(1) = f(2) = 0; the identity f(x) = x is bijective; and x² is neither. The **composition** g ∘ f : A → C applies f, then g; if f and g are injective, so is g ∘ f. Every function is a relation, but not every relation is a function.

Source: MAT 213 Full.pdf (Algebra I lecture notes, B. O. Onasanya), Chapter 1 (Sets and Functions)
