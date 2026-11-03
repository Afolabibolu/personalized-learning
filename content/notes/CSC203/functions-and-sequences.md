# Functions and Sequences

## Functions

A **function** f from A to B, written f: A → B, assigns to each element of A **exactly one** element of B. A is the **domain**, B the **codomain**, f(a) the **image** of a, and the set of all images the **range**.

- f is **one-to-one (injective)** if distinct elements have distinct images: f(x) = f(y) implies x = y. A function that is strictly increasing or strictly decreasing is one-to-one.
- f is **onto (surjective)** if every element of B is the image of some element of A, so the range equals the codomain.
- f is a **bijection (one-to-one correspondence)** if it is both. Only bijections have an **inverse function** f⁻¹: B → A, with f⁻¹(b) = a exactly when f(a) = b.
- The **composition** f ∘ g applies g first and then f: (f ∘ g)(x) = f(g(x)). With g(x) = 3ˣ + 7x and f(x) = x³, (f ∘ g)(2) = f(23) = 12167. A function composed with its inverse gives the identity function.

The **floor** function ⌊x⌋ gives the largest integer ≤ x, and the **ceiling** function ⌈x⌉ the smallest integer ≥ x, so ⌊3.7⌋ = 3 and ⌈3.2⌉ = 4. Both map the real numbers onto the integers.

## Sequences

A **sequence** is a function from a subset of the natural numbers to a set: an **ordered list** a₁, a₂, a₃, …, written {aₙ}. Finite sequences are also called **strings**. A sequence is described by a **formula** for its general term or by a **recurrence** that gives each term from earlier ones:

- 1, 3, 5, 7, 9, … is aₙ = 2n − 1 (odd numbers).
- −1, 1, −1, 1, … is aₙ = (−1)ⁿ.
- 2, 5, 10, 17, 26, … is aₙ = n² + 1.
- 1, 7, 25, 79, 241, … is aₙ = 3ⁿ − 2.

To find a formula, look at the differences or ratios between terms and compare with squares, powers and known sequences.

**Summation notation** Σⱼ₌ₘⁿ aⱼ adds aₘ + aₘ₊₁ + … + aₙ; j is the **index of summation**, m the lower limit and n the upper limit. Useful results include 1 + 2 + … + n = n(n + 1)/2. Double summations add over two indices.

Source: 4. Sequences.ppt (CSC 203 slides); CSC 242.pdf (Discrete Structures slides, filed in the CSC 203 folder), the functions and sequences sections
