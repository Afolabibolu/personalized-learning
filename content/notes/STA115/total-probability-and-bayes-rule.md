# The Law of Total Probability and Bayes' Rule

## The law of total probability

Let F₁, F₂, ..., Fₙ be a **partition** of Ω: mutually exclusive, together exhaustive, and each with P(Fᵢ) > 0. Then for any event E,

**P(E) = Σ P(E ∩ Fᵢ) = Σ P(E | Fᵢ)P(Fᵢ)**.

It is often easier to find each P(E | Fᵢ) than P(E) directly.

**Batteries**: supplier A provides 55% of a car maker's batteries with 5% defective, and B provides 45% with 4% defective. P(defective) = 0.05 × 0.55 + 0.04 × 0.45 = 0.0275 + 0.018 = **0.0455**, so P(works) = **0.9545**.

## Bayes' rule

**P(Fⱼ | E) = P(E | Fⱼ)P(Fⱼ) / Σ P(E | Fᵢ)P(Fᵢ)**

The terms:

- P(Fⱼ) is the **prior** probability;
- P(E | Fⱼ) is the **likelihood**;
- P(Fⱼ | E) is the **posterior**, what we believe after E is observed.

In general form, p(θ | y) = p(y | θ)p(θ)/p(y).

A table helps: list each case with its prior, likelihood and their product, then divide each product by the total.

**Baskets**: B₁ holds 1 white, 2 red and 3 black balls; B₂ holds 2 white, 3 red and 1 black; B₃ holds 3 white, 1 red and 2 black. A basket is chosen at random and two balls are drawn: one red and one white.

- The likelihoods are 2/15, 6/15 = 2/5, and 3/15 = 1/5.
- Each prior is 1/3, so the products total 11/45.
- P(B₂ | red and white) = (2/15)/(11/45) = **6/11**.

**Suppliers**: 2%, 1% and 3% of appliances from suppliers I, II and III are defective, and they supply 35%, 25% and 40%.

- P(defective) = 0.007 + 0.0025 + 0.012 = 0.0215.
- P(III | defective) = 0.012/0.0215 ≈ **0.558**.

## Monty Hall

A contestant picks door 1, and the host, who knows where the prize is, opens door 3 to show no prize.

- P(O₃ | D₁) = 1/2, P(O₃ | D₂) = 1 and P(O₃ | D₃) = 0.
- Bayes gives P(D₁ | O₃) = **1/3** and P(D₂ | O₃) = **2/3**.

So it is **better to switch**.

Bayes' rule also handles tests and detectors. For radar with a prior of 0.05, P(register | aircraft) = 0.99 and P(register | none) = 0.10, the posterior P(aircraft | register) = 0.0495/0.1445 ≈ 0.34. A false alarm happens more often than a real detection when the event is rare.

Source: STA 115 Lecture 3: The Law of Total Probability and Bayes' Rule (Shittu, 2021 and 2023); STA 115 tests (2016/17 to 2023) and STA 112 Probability I papers
