# Boolean Algebra and Standard Forms

## Boolean algebra

**Boolean algebra**, from George Boole's *An Investigation of the Laws of Thought*, deals with binary variables that take two discrete values (0 and 1) and with logic operations. It is "very nice machinery" for manipulating and simplifying Boolean functions. The three basic operations are AND, OR and NOT. For example, F(a, b) = a·b is 1 if and only if a = b = 1, and G(a, b) = a + b is 1 if either a = 1 or b = 1.

Terms:

- A **literal** is a variable or its complement.
- A **product term** is literals connected by · (AND).
- A **sum term** is literals connected by + (OR).

A function of **n variables has 2ⁿ rows** in its truth table, because there are 2ⁿ input combinations. The truth table is a **unique** representation: if two functions have identical truth tables, they are equivalent. Boolean expressions are **not unique**, so a cheaper expression with fewer components can implement the same function. To design a cost-effective, efficient circuit we must minimise its size. Truth tables can prove equality, but they grow exponentially with the number of variables, which is why algebra is used.

## Identities and duality

With X a Boolean variable and 0 and 1 constants, the basic identities come in pairs:

1. X + 0 = X and X · 1 = X
2. X + 1 = 1 and X · 0 = 0
3. X + X = X and X · X = X
4. X + X′ = 1 and X · X′ = 0

The **dual** of an expression is obtained by **exchanging · and +, and 1 and 0**, without changing the order of operations. Each identity's partner above is its dual. Identities are proved algebraically; for example x + x·y = x·1 + x·y = x·(1 + y) = x·1 = x.

## Canonical forms

A **minterm** is a product term containing every variable once, true or complemented; it is 1 in exactly one row of the truth table. A **maxterm** is a sum term containing every variable; it is 0 in exactly one row. A function written as an OR of its minterms is in **canonical sum-of-products** form, and as an AND of its maxterms it is in **canonical product-of-sums** form. Reading the 1-rows of a truth table gives the minterms directly.

Source: Standard forms of Expression.pptx (IFT 211 lecture 3); Minimisation Aids.pptx (IFT 211 lecture 4)
