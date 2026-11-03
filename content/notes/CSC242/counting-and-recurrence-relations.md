# Counting and Recurrence Relations

## Counting rules

- **Product rule**: if a task has two parts done in n₁ and n₂ ways, the task can be done in n₁ · n₂ ways. For sets, |A₁ × A₂ × … × Aₘ| = |A₁| · |A₂| · … · |Aₘ|.
- **Sum rule**: if A₁, …, Aₘ are **disjoint** sets, the number of elements in their union is |A₁| + |A₂| + … + |Aₘ|.
- When sets overlap, the **principle of inclusion-exclusion** corrects the double count: |A ∪ B| = |A| + |B| − |A ∩ B|. For three sets, add the three sizes, subtract the three pairwise intersections and add back the triple intersection.
- **Pigeonhole principle**: if k + 1 or more objects are placed into k boxes, at least one box has two or more objects. The **generalised** principle: N objects in k boxes put at least ⌈N/k⌉ objects in some box.

## Permutations and combinations

A **permutation** of a set of distinct objects is an **ordered** arrangement of them; an ordered arrangement of r of them is an **r-permutation**. For S = {1, 2, 3}, the arrangement 3, 1, 2 is a permutation and 3, 2 is a 2-permutation. By the product rule, the number of r-permutations of n elements is

P(n, r) = n · (n − 1) · (n − 2) · … · (n − r + 1) = n! / (n − r)!

An **r-combination** is an **unordered** selection of r elements, simply an r-element subset: {1, 3, 4} is a 3-combination of {1, 2, 3, 4}. Since every r-permutation is an r-combination put in order, P(n, r) = C(n, r) · P(r, r), so

C(n, r) = n! / (r! (n − r)!)

For example, choosing 3 males from 20 and 2 females from 12 can be done in C(20, 3) · C(12, 2) ways.

## Recurrence relations

A **recurrence relation** for a sequence {aₙ} expresses aₙ in terms of earlier terms. A sequence is a **solution** if its terms satisfy the relation; the same relation can have many solutions, and the **initial conditions** pick out one. Recurrences **model** problems such as compound interest, Pₙ = (1.05)Pₙ₋₁, and the Fibonacci numbers, fₙ = fₙ₋₁ + fₙ₋₂. A **linear homogeneous recurrence relation of degree k with constant coefficients** has the form aₙ = c₁aₙ₋₁ + … + cₖaₙ₋ₖ. A sequence satisfying it is uniquely determined by the relation and k initial conditions, and this class can be solved systematically.

Source: CSC 242.pdf (Discrete Structures lecture slides), the counting and recurrence relations sections
