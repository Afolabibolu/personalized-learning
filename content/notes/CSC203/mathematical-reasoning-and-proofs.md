# Mathematical Reasoning, Proofs and Induction

## Mathematical reasoning

We need mathematical reasoning to **decide whether an argument is correct** and to **construct arguments**; it matters for proofs, program verification and artificial intelligence. An **axiom** is a basic assumption that needs no proof. A **theorem** is a statement that can be shown to be true; a **lemma** is a simple theorem used on the way to another; a **corollary** follows directly from a proved theorem; a **conjecture** is a statement whose truth is unknown until it is proved. A **proof** is a sequence of statements forming an argument, and the steps connecting them are the **rules of inference**. Incorrect reasoning is a **fallacy**.

## Rules of inference

The general form: if hypotheses p₁, p₂, …, pₙ are all true, then the conclusion q is true. Key rules:

- **Modus ponens** (law of detachment): p and p → q give q.
- **Modus tollens**: ¬q and p → q give ¬p.
- **Hypothetical syllogism**: p → q and q → r give p → r ("if it rains we will not barbecue today; if not today, then tomorrow; so if it rains we barbecue tomorrow").
- **Disjunctive syllogism**: p ∨ q and ¬p give q ("Gary is intelligent or a good actor; he is not intelligent; so he is a good actor").

An argument is **valid** if its conclusion is true whenever its hypotheses are; a valid argument can still reach a false conclusion if a hypothesis is false. "If you listen to me you will pass; you passed; so you listened" is **not valid**: it assumes ((p → q) ∧ q) → p, which is false when p is false and q is true.

## Proofs

A proof gives **absolute certainty** under its axioms, uses **deductive reasoning** in every step, has **no hidden assumptions**, and may be formal or informal. Even numbers are written 2k and odd numbers 2k + 1.

- A **direct proof** of p → q assumes p and derives q: if n = 2k + 1 then n² = 2(2k² + 2k) + 1, so n² is odd.
- An **indirect proof (by contraposition)** proves the equivalent ¬q → ¬p: to show "if 3n + 2 is odd then n is odd", assume n = 2k is even, so 3n + 2 = 2(3k + 1) is even.
- **Mathematical induction** proves P(n) for all positive integers: the **basis step** proves P(1), and the **inductive step** proves P(n) → P(n + 1).

Source: 7. MathReasoning.ppt (CSC 203 slides); CSC 203 NOTE.pdf, Proof and Types of Proofs; Induction.ppt (CSC 203 slides)
