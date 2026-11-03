# Logic and Quantified Statements

## Propositions

Logic is a system based on **propositions**. A proposition is a statement that is **either true or false**, which correlates to 1 and 0 (on or off) in digital circuits.

- "y > 5" is **not** a proposition: its truth value depends on y, which is not specified. Such a statement is a **propositional function** or **open statement**.
- "Please do not fall asleep" is not a statement but a **request**, and only statements can be propositions.
- "x < y if and only if y > x" **is** a proposition, because its truth value does not depend on x and y; it is true.

One or more propositions combine into a **compound proposition** using **logical operators**, also called **connectives**, and truth tables show how they combine:

1. **Negation** (NOT), ¬
2. **Conjunction** (AND), ∧
3. **Disjunction** (OR), ∨
4. **Exclusive OR** (XOR), ⊕
5. **Implication** (if … then), →
6. **Biconditional** (if and only if), ↔

A **tautology** is a statement that is always true and a **contradiction** is a statement that is always false; the negation of any contradiction is a tautology and vice versa. For example, p ∨ ¬p is a tautology and p ∧ ¬p a contradiction.

## Quantified statements

**Quantified statements** tell us "how many" elements in a domain satisfy a property. The **universal quantifier** ∀x P(x) says P(x) holds for every x; the **existential quantifier** ∃x P(x) says it holds for at least one. Four rules connect quantified and specific statements:

- **Universal instantiation (UI)**: if a statement is true for every member of a domain, it is true for any specific individual in that domain. From "every UI student is a genius" and "George is a UI student" we conclude "George is a genius".
- **Universal generalisation (UG)**: if a statement is true for an arbitrary, representative individual, it is true for every member of the domain.
- **Existential instantiation (EI)**: if some individual satisfies a property, we may introduce a new, unnamed constant to stand for that individual while reasoning.
- **Existential generalisation (EG)**: if a statement is true of a specific individual, then there exists at least one individual in the domain for which it is true.

Negating a quantified statement swaps the quantifier: ¬∀x P(x) is equivalent to ∃x ¬P(x), and ¬∃x P(x) to ∀x ¬P(x).

Source: CSC 203.pdf (CSC 203 topics and logic note); CSC 203 NOTE.pdf, Quantified Statements; 7. MathReasoning.ppt (CSC 203 slides)
