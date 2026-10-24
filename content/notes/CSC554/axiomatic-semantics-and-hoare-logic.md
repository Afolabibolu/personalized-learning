# Axiomatic Semantics and Hoare Logic

## Why prove programs correct

Software failures come from poor design, human error, coding errors, inadequate testing and external factors. They cost money and disrupt operations, and they can cost lives. Examples in the course:

- **CrowdStrike, 2024:** a faulty update crashed more than 8.5 million Windows machines.
- **Knight Capital, 2012:** untested software lost $440 million in 45 minutes.

Edsger Dijkstra wrote that testing "can be a very effective way to show the presence of bugs, but it is hopelessly inadequate for showing their absence." Formal verification uses mathematics, through theorem proving or model checking, to prove correctness.

## Axiomatic program verification

Axiomatic program verification (APV) proves that a program meets its specification. Its key ideas:

- **Formal specifications** state what the program should do as logical assertions.
- **Assertions** are statements about the program state: **preconditions** hold before execution, **postconditions** after, and **invariants** at points such as inside loops.
- **Proof obligations** are formulas that must be proved. They show that if the preconditions hold, the postconditions follow.

## Hoare logic

Tony (C. A. R.) Hoare introduced Hoare logic in 1969. Its central idea is the **Hoare triple** {P} S {Q}: if precondition P is true before command S runs, then postcondition Q is true afterwards. In {x = 5} x := x + 1 {x = 6}, P is x = 5, S is x := x + 1 and Q is x = 6.

**Assignment rule.** Compute Q[x := E] by substituting the expression for the variable in the postcondition. The triple is valid if P implies the result.
- {x > 4} x := x + 3 {x > 5} gives x + 3 > 5, so x > 2. Since x > 4 implies x > 2, the triple is **valid**.
- {x ≥ 0} x := x − 1 {x > 0} gives x > 1. But x = 0 satisfies x ≥ 0 and not x > 1, so the triple is **not valid**.

**Sequence rule.** For S1; S2, the postcondition of S1 must be the precondition of S2. Swapping values with temp works backwards from {a = 20 ∧ b = 10} to recover the precondition {a = 10 ∧ b = 20}.

**Conditional rule.** From {B ∧ P} S1 {Q} and {¬B ∧ P} S2 {Q}, conclude {P} if B then S1 else S2 {Q}. Both branches must establish Q.

## Partial and total correctness

In Hoare logic, termination is handled separately from partial correctness. Partial correctness means that *if* the program terminates, Q holds. Total correctness also requires that it terminates. **Dynamic logic** expresses both directly: [P]φ is partial correctness, and ⟨P⟩true ∧ [P]φ is total correctness.

**Separation logic** extends Hoare logic to pointers and heap memory. It uses the separating conjunction P * Q, where P and Q hold for disjoint parts of memory, and the frame rule for local reasoning.

Source: CSC554 presentation-1.pdf (Axiomatic Program Verification and Hoare's Logic)
