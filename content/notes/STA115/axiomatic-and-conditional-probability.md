# Axiomatic and Conditional Probability

## Sample spaces and events

- A **random experiment** generates an outcome that cannot be known with certainty.
- Its **sample space** Ω is the set of all possible outcomes, finite or infinite.
- An **event** is any subset of Ω. A **simple** event has one outcome; a **compound** event has more; the **null event** ∅ has none.

For one die, Ω = {1, 2, 3, 4, 5, 6}. The event {2} is simple, and "even numbers" is compound.

Events obey the commutative, associative and distributive laws, and **De Morgan's laws**: (E ∪ F)ᶜ = Eᶜ ∩ Fᶜ and (E ∩ F)ᶜ = Eᶜ ∪ Fᶜ.

## Approaches to probability

- **Classical**: equally likely outcomes, so P(E) = n(E)/n(Ω).
- **Relative frequency**: P(E) = lim n(E)/n as the experiment is repeated.
- **Subjective**: personal degree of belief.
- **Axiomatic**: P is any rule that satisfies the three axioms:
  1. 0 ≤ P(E) ≤ 1;
  2. P(Ω) = 1;
  3. for mutually exclusive events, P(E₁ ∪ E₂ ∪ ...) = P(E₁) + P(E₂) + ....

From the axioms: **P(Eᶜ) = 1 − P(E)**, P(∅) = 0, **P(E ∪ F) = P(E) + P(F) − P(E ∩ F)**, and if E ⊂ F, then P(E) ≤ P(F).

**Example**: 30% of students take computer science (C), 45% mathematics (M), and 10% both. Then:

- P(C ∪ M) = 0.30 + 0.45 − 0.10 = **0.65**;
- C only = 0.30 − 0.10 = 0.20;
- M only = 0.35;
- neither = 1 − 0.65 = **0.35**.

(The slide labels the 10% as P(C ∪ M). It is P(C ∩ M).)

The complement rule makes the **birthday problem** easy: P(at least two of m share a birthday) = 1 − (365 × 364 × ... × (365 − m + 1))/365ᵐ.

## Independence and conditional probability

- **Conditional probability**: **P(F | E) = P(F ∩ E)/P(E)**, for P(E) > 0.
- **Independence**: E and F are independent if **P(E ∩ F) = P(E)P(F)**, or equivalently P(E | F) = P(E).

**Examples**:

- With two fair dice and a 4 on the first die, P(sum = 8) = (1/36)/(6/36) = **1/6**.
- A system works if components 1 and 2 (in series) work, or if component 3 works. With each working independently with probability 0.9, P(system works) = 0.81 + 0.9 − 0.729 = **0.981**.

Mutually exclusive events with positive probabilities are **never** independent, because P(E ∩ F) = 0 ≠ P(E)P(F).

Source: STA 115 Lecture 2: Axiomatic Probability (Shittu, 2023); STA 115 tests (2016/17 to 2023) and STA 112 Probability I papers; General knowledge of STA 115 for the classical and subjective approaches
