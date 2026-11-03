# Probability Laws, Conditional Probability and Bayes' Rule

## Axioms

For a **sample space S** and events A ⊆ S:

1. **P(A) ≥ 0**;
2. **P(S) = 1**; and
3. for **mutually exclusive (disjoint)** events, **P(A ∪ B) = P(A) + P(B)**, and likewise for countably many.

From these: **P(A') = 1 − P(A)**, **P(∅) = 0**, and if A ⊆ B then P(A) ≤ P(B). The **relative frequency** definition sees P(A) as the long-run proportion of trials in which A occurs.

## Addition laws

**P(A ∪ B) = P(A) + P(B) − P(A ∩ B)**, and for three events

**P(A ∪ B ∪ C) = P(A) + P(B) + P(C) − P(A ∩ B) − P(A ∩ C) − P(B ∩ C) + P(A ∩ B ∩ C)**,

proved by applying the two-event law to (A ∪ B) ∪ C. Venn diagrams with these laws solve survey problems: of 500 students, if 186 take Algebra, 295 Physics and 329 Statistics, with given overlaps, the number taking all three is found by solving the three-event law with the total of 500.

## Conditional probability and independence

**P(B|A) = P(A ∩ B)/P(A)**, for P(A) > 0, so **P(A ∩ B) = P(A)P(B|A)** (the multiplication rule). A and B are **independent** if **P(A ∩ B) = P(A)P(B)**. For three events, **pairwise** independence is weaker than **mutual (complete)** independence, which also needs P(A ∩ B ∩ C) = P(A)P(B)P(C). Mutually exclusive events with positive probabilities are never independent.

## Total probability and Bayes' rule

If B1, ..., Bk **partition** S, then **P(A) = Σ P(A|Bi)P(Bi)** (the total probability rule) and

**P(Bi|A) = P(A|Bi)P(Bi) / Σ P(A|Bj)P(Bj)** (Bayes' rule).

**Example**: a fisherman fishes at the river, sea and lake with probabilities 0.25, 0.5 and 0.25, and catches fish with probabilities 0.45, 0.75 and 0.60. Then P(fish) = 0.25(0.45) + 0.5(0.75) + 0.25(0.60) = **0.6375**. Given that he caught fish, he was most likely at the **sea**: P(sea | fish) = 0.375/0.6375 ≈ **0.588**.

**Example**: a magician has 12 fair coins and 8 two-headed coins. P(head) = (12/20)(1/2) + (8/20)(1) = 0.7, so P(defective | head) = 0.4/0.7 = **4/7**.

**Example**: from 4 aspirin, 3 sedatives and 2 laxatives, selections follow the same rules with counting: P(two aspirin) = C(4, 2)/C(9, 2) = 6/36 = 1/6.

Source: Amahia, STA 211 Probability II (UI Distance Learning Centre) (Lectures Three and Four); STA 211 updated lecture slides (Basic Probability); STA 211 past papers (the fisherman, magician and survey problems)
