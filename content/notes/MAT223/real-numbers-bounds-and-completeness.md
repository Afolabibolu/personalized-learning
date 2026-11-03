# The Real Numbers: Bounds, Supremum and Completeness

## Bounded sets

Let P be a non-empty subset of R, the set of real numbers.

- P is **bounded above** if there is a real number M with **x ≤ M for every x in P**; M is an **upper bound**.
- P is **bounded below** if there is a real number m with **x ≥ m for every x in P**; m is a **lower bound**.
- P is **bounded** if it is bounded above and below, that is, |x| ≤ K for some K and every x in P.

## Supremum and infimum

The **supremum** sup P (least upper bound) is a real number β such that:

1. β is an upper bound of P; and
2. **no smaller number is an upper bound**: for every ε > 0 there is some x in P with x > β − ε.

The **infimum** inf P (greatest lower bound) is defined the same way from below. The supremum and infimum of a set are **unique** when they exist, and they need not belong to the set. For A = {n/(n+1) : n in N}, inf A = 1/2 (attained at n = 1) and sup A = 1 (never attained).

Useful properties, which appear often in the examinations:

- **sup(P + k) = k + sup P**, where P + k = {p + k : p in P};
- **sup(−A) = −inf A**;
- if A ⊆ B, then **inf B ≤ inf A ≤ sup A ≤ sup B**; and
- inf{u_i + v_i} ≥ inf{u_i} + inf{v_i}.

## The rationals

The rational numbers Q are **dense**: if x and y are rational with x < y, there is a third rational between them, for example **(x + y)/2**. Yet **Q is not complete**. There is **no rational x with x² = 2**: if x = p/q in lowest terms, then p² = 2q², so p is even; writing p = 2r gives q² = 2r², so q is even too, contradicting lowest terms. The set {x in Q : x² < 2} is bounded above in Q but has **no supremum in Q**.

## Completeness

The real numbers satisfy the **completeness axiom (least upper bound property)**: **every non-empty subset of R that is bounded above has a supremum in R**. This is what distinguishes R from Q, and it underlies the convergence theorems for sequences: a bounded monotone sequence converges, and every Cauchy sequence converges. R is a **complete ordered field**: it satisfies the field axioms for addition and multiplication, the order axioms, and completeness.

Source: MAT 223 lecture notes (scanned, Notes 1 to 9); MAT 223 past papers (definitions as examined). The worked proofs are from general knowledge of MAT 223, since the scanned notes on real numbers are only partly legible.
