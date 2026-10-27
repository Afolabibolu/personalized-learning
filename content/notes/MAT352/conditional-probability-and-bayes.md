# Conditional Probability, Independence and Bayes' Theorem

## Conditional probability

The probability of A **given** that B has occurred is

**P(A | B) = P(A ∩ B) ÷ P(B)**, for P(B) > 0.

It behaves as a probability measure on the reduced sample space B: 0 ≤ P(A | B) ≤ 1, and P(B | B) = 1. Rearranging gives the **multiplication rule**:

P(A ∩ B) = P(B) P(A | B) = P(A) P(B | A),

and in general P(A₁ ∩ A₂ ∩ A₃) = P(A₁) P(A₂ | A₁) P(A₃ | A₁ ∩ A₂).

## Independence

Events A and B are **independent** if P(A ∩ B) = P(A) P(B), equivalently P(A | B) = P(A).

- Events A, B and C are **pairwise independent** if each pair is independent.
- They are **mutually independent** if, in addition, P(A ∩ B ∩ C) = P(A) P(B) P(C).
- Pairwise independence does not imply mutual independence.

**Example:** throw two dice. Let A be "the sum is 7", B be "die 1 shows 3" and C be "die 2 shows 4". Each has probability 1/6 and every pair is independent (for example P(A ∩ B) = 1/36). But P(A ∩ B ∩ C) = 1/36, not 1/216, so they are **pairwise but not mutually independent**.

## The law of total probability

Events E₁, E₂, …, Eₙ form a **partition** of S if they are mutually exclusive and their union is S. For any event A:

**P(A) = Σ P(A | Eᵢ) P(Eᵢ)**.

## Bayes' theorem

Reversing the conditioning gives **Bayes' theorem** (Thomas Bayes):

**P(Eᵢ | A) = P(A | Eᵢ) P(Eᵢ) ÷ Σₖ P(A | Eₖ) P(Eₖ)**.

**Medical test example:** 0.1 percent of a population has a disease. A test detects 99 percent of infected people but gives a false positive in 0.5 percent of healthy people. Then

P(disease | positive) = (0.99 × 0.001) ÷ (0.99 × 0.001 + 0.005 × 0.999) ≈ **0.165**.

So most positives are false, because the disease is rare.

**Rental car example:** a firm rents 60 percent of its cars from agency 1, 30 percent from agency 2 and 10 percent from agency 3. 9, 20 and 6 percent of their cars respectively need an oil change. The chance a delivered car needs one is 0.6 × 0.09 + 0.3 × 0.20 + 0.1 × 0.06 = **0.12**.

## Conditional probability properties

- If E₂ has positive probability, 0 ≤ P(E₁ | E₂) ≤ 1 and P(E₂ | E₂) = 1.
- If A and B are independent, so are A and Bᶜ, Aᶜ and B, and Aᶜ and Bᶜ.

Source: Lanre_s 352 note.pdf (a student's handwritten MAT 352 lecture notes, used as secondary) (conditional probability, its theorems and proofs, Bayes' theorem); the worked examples are general knowledge, following the MAT 352 course outline and past papers (2020/21 Question 5a, 2021/22 Questions 2b and 3a, and the scanned CA)
