# Probability Spaces and Axioms

## Why probability matters

Probability theory, whose systematic foundation was laid in the seventeenth century by **Blaise Pascal** and **Pierre de Fermat** from games of chance, is used in medicine, engineering, quality control, meteorology, finance, insurance, genetics and demography.

## Experiments, sample spaces and events

A **random experiment** has outcomes that cannot be predicted with certainty, although all possible outcomes are known. Its **sample space** S (or Ω) is the set of all possible outcomes, and an **event** is a subset of S. Two events are **mutually exclusive** if they cannot occur together (A ∩ B = ∅).

**Example:** choosing four letters at random from the 26-letter alphabet, with repeats allowed, gives a sample space of 26⁴ = 456,976 equally likely codes. The probability that the code begins with a vowel is 5 ÷ 26.

## Approaches to probability

- **Classical:** if there are n equally likely outcomes and m favour A, then P(A) = m ÷ n.
- **Empirical (relative frequency):** P(A) is the limit of the proportion of times A occurs in many repeated trials.
- **Axiomatic:** probability is a function satisfying a set of axioms (Kolmogorov).

## Probability measure and axioms

A **probability measure** P assigns to each event A a number P(A) such that:

1. **non-negativity:** P(A) ≥ 0;
2. **certainty:** P(S) = 1;
3. **countable additivity:** for mutually exclusive events A₁, A₂, …, P(A₁ ∪ A₂ ∪ …) = P(A₁) + P(A₂) + ….

An assignment is not permissible if any probability is negative or the probabilities of the outcomes do not sum to 1.

## Theorems from the axioms

- **Complement:** P(Aᶜ) = 1 − P(A), so P(∅) = 0.
- **Monotonicity:** if A ⊆ B then P(A) ≤ P(B), and P(A) ≤ 1.
- **Difference:** P(A \ B) = P(A) − P(A ∩ B).
- **Addition theorem:** P(A ∪ B) = P(A) + P(B) − P(A ∩ B).
- **Inclusion-exclusion for three events:** P(A ∪ B ∪ C) = P(A) + P(B) + P(C) − P(A ∩ B) − P(A ∩ C) − P(B ∩ C) + P(A ∩ B ∩ C).

**Proof idea for complement:** S = A ∪ Aᶜ with A and Aᶜ disjoint, so 1 = P(A) + P(Aᶜ).

## Counting

Drawing two aces from 52 cards **with replacement** gives (4 ÷ 52)², and **without replacement** gives (4 ÷ 52) × (3 ÷ 51). Choosing 3 fuses from 20, of which 5 are defective, the chance that all three are defective without replacement is (5 × 4 × 3) ÷ (20 × 19 × 18) = 1 ÷ 114.

Source: Lanre_s 352 note.pdf (a student's handwritten MAT 352 lecture notes, used as secondary) (significance of probability, approaches, axioms, addition theorem); the counting examples are general knowledge, following the MAT 352 course outline and past papers (2020/21 Question 2a and the scanned CA)
