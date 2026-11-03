# Rings, Integral Domains and Fields

## Rings

A non-empty set R with two binary operations + and × is a **ring** if

1. **(R, +) is an abelian group**,
2. **(R, ×) is a semigroup** (multiplication is associative), and
3. multiplication **distributes** over addition on both sides: a × (b + c) = (a × b) + (a × c) and (a + b) × c = (a × c) + (b × c).

A ring is **commutative** if a × b = b × a, and has an **identity (is unital)** if some e satisfies a × e = a = e × a. When R is commutative, left and right distributivity coincide.

Examples:

- Z, Q, R and C are **commutative rings with identity**.
- mZ = {mn : n ∈ Z}, such as 2Z = {0, ±2, ±4, …}, is a commutative ring.
- **Zₘ** with addition and multiplication modulo m is a commutative ring with identity.
- R[x], the polynomials with real coefficients, is a commutative ring with identity.
- Mₙ(R), the n × n real matrices, is a **non-commutative ring with identity**.

## Zero divisors and integral domains

A non-zero a is a **zero divisor** if a × s = 0 or s × a = 0 for some non-zero s. In Z₈, 2, 4 and 6 are zero divisors, since 2 ×₈ 4 = 0 and 4 ×₈ 6 = 0; generally Zₘ has zero divisors when m is not prime, while Zₚ for a prime p has none. A commutative ring with identity and **no zero divisors** is an **integral domain**: Z, Zₚ, R, Q, C, R[x] and Z[i] are integral domains. So **Zₙ is not an integral domain when n is not prime**.

## Characteristic and subrings

R has **characteristic n** if n is the least positive integer with na = 0 for all a, and characteristic 0 if there is none: Zₙ has characteristic n, while Z, Q, R and C have characteristic 0. A non-empty S ⊆ R is a **subring** if it is a ring under the same operations; it suffices that a − b ∈ S and ab ∈ S for all a, b ∈ S. nZ is a subring of Z.

## Fields

R is a **division ring (skew field)** if (R − {0}, ×) is a group. A **field** F satisfies: (F, +) is an abelian group, (F − {0}, ×) is an abelian group, and multiplication distributes over addition; equivalently, a field is a commutative division ring. **Zₚ for prime p**, Q, R and C are fields. Z is **not** a field, because (Z − {0}, ×) is not a group, and Mₙ(R) is not a field.

Source: MAT 213 Full.pdf (Algebra I lecture notes, B. O. Onasanya), Chapter 5 (Ring, Some Properties of Rings, Subrings, Fields)
