# Probability, Conditional Probability and Bayes' Theorem

## Random phenomena

**Deterministic** phenomena have a model that predicts outcomes perfectly. **Non-deterministic** ones are either **haphazard** (no long-run regularity) or **random**: each outcome is unpredictable, but **in the long run the outcomes show statistical regularity**. Tossing a coin, S = {Head, Tail}, gives heads about 50% of the time.

## Events and the addition rule

The **sample space** S is the set of all outcomes; an **event** is a subset of S. Probability satisfies **0 ≤ P(A) ≤ 1**, **P(S) = 1** and, for **mutually exclusive** events, P(A ∪ B) = P(A) + P(B). In general,

**P(A ∪ B) = P(A) + P(B) − P(A ∩ B)**, and

**P(A ∪ B ∪ C) = P(A) + P(B) + P(C) − P(A ∩ B) − P(A ∩ C) − P(B ∩ C) + P(A ∩ B ∩ C)**.

Also P(A') = 1 − P(A), and if A implies B (A ⊂ B), then **P(A) ≤ P(B)**.

## Conditional probability

The **conditional probability of B given A** is **P(B|A) = P(A ∩ B)/P(A)**, for P(A) > 0. From S = {2, 3, ..., 9}, with A = odd and B = multiple of 3: P(A) = 4/8, P(A ∩ B) = P({3, 9}) = 1/4, so **P(B|A) = 1/2**. For a family of two children, the probability that both are boys given at least one is a boy is (1/4)/(3/4) = **1/3**.

## Independence

A and B are **independent** if **P(A ∩ B) = P(A)P(B)**, equivalently P(B|A) = P(B). The **multiplication rule** is P(A ∩ B) = P(A)P(B|A). If P(A) = 1/5, P(A ∪ B) = 1/2 and A, B are independent, then 1/2 = 1/5 + p − p/5, so **P(B) = 3/8**.

**Mutually exclusive events with non-zero probabilities are not independent**, because P(A ∩ B) = 0 ≠ P(A)P(B). Events can be **pairwise** independent without being **mutually (completely)** independent, which also needs P(A ∩ B ∩ C) = P(A)P(B)P(C).

## Bayes' theorem

If B1, ..., Bk partition S, the **total probability rule** is **P(A) = Σ P(A|Bi)P(Bi)**, and **Bayes' theorem** reverses the conditioning:

**P(Bi|A) = P(A|Bi)P(Bi) / Σ P(A|Bj)P(Bj).**

For two bags (one with 4 red and 5 black balls, the other with 5 red and 4 black), choosing a bag at random and drawing one ball, the probability of black is (1/2)(5/9) + (1/2)(4/9) = **1/2**.

Source: STA 204 Lecture 3 (Elements of Probability); STA 204 Lecture 3b (Conditional Probability, Bayes Theorem and Independent Events); STA 201/202/204 quiz (2024/2025 session) (probability items)
