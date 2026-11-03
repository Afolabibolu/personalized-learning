# Real-Valued Functions and Limits

## Functions

A **function** f from X to Y, written **f : X → Y**, is a rule that assigns to **each element x of X exactly one element f(x) of Y**. A correspondence that can give one input several outputs, such as associating a person with "a parent", is **not a function**. A **real-valued function of a real variable** has X and Y as subsets of R.

- The **domain** is the set of all real inputs for which the function is defined.
- The **codomain** is the set of possible outputs declared for the function.
- The **range** is the set of outputs **actually taken**, a subset of the codomain.

## Finding the domain

Domains come from restrictions on the input:

- a **square root** needs a non-negative radicand: √(x − 2) needs x ≥ 2;
- a **denominator** cannot be zero: 1/(x − 3) needs x ≠ 3; and
- a **logarithm** needs a positive argument: ln(x + 1) needs x > −1.

For f(x) = √(x + 4)/(x − 1), the domain is x ≥ −4 with x ≠ 1.

## Types of functions

The course lists **algebraic** (polynomial and rational), **trigonometric**, **logarithmic**, **exponential** and **modulus** functions. The modulus function |x| equals x for x ≥ 0 and −x for x < 0, so it is naturally **piecewise**.

## Limits

**lim as x → a of f(x) = L** means f(x) can be made arbitrarily close to L by taking x close enough to a (but not equal to a). The **left-hand limit** lim as x → a⁻ looks at values below a; the **right-hand limit** lim as x → a⁺ at values above. **The limit exists if and only if both one-sided limits exist and are equal.**

For f(x) = x² for x < 2 and 3x − 2 for x ≥ 2, the left limit at 2 is 4 and the right limit is 3(2) − 2 = 4, so **lim f(x) = 4**. For g(x) = |x|/x, the left limit at 0 is −1 and the right limit is 1, so **the limit does not exist**.

## Properties of limits

If lim f = L and lim g = M, then lim (f ± g) = L ± M, lim (fg) = LM, lim (f/g) = L/M if M ≠ 0, and lim (cf) = cL. For polynomials, the limit is found by **substitution**. A 0/0 form needs simplifying first: lim as x → 3 of (x² − 9)/(x − 3) = lim (x + 3) = **6**. The standard limit **lim as x → 0 of (sin x)/x = 1**.

Source: MTH 201 Course Outline (2025/2026) (topics 1 and 2); 201 slides (real-valued functions); MTH201 slides 1 (real-valued functions of a real variable) (limits and piecewise examples)
