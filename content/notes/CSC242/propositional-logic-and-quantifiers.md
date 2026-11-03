# Propositional Logic, Quantifiers and Inference

## Propositions

Logic is crucial for mathematical reasoning and for designing electronic circuitry. It is built on **propositions**: a proposition is a statement that is **either true or false, not both**. Its **truth value** is T or F, which corresponds to 1 and 0 in digital circuits. "Elephants are bigger than mice" is a proposition (true). "Please do not fall asleep" is not a statement, so it is not a proposition; only statements can be propositions. "x < y" is not a proposition because its truth value depends on unspecified variables; it is a **propositional function** (open sentence).

## Logical operators

Propositions p, q, r, … combine into **compound propositions** with logical operators (connectives):

- **Negation** ¬ (NOT), the only unary operator.
- **Conjunction** ∧ (AND): true only when both are true.
- **Disjunction** ∨ (OR): true when at least one is true.
- **Exclusive or** ⊕ (XOR): true when exactly one is true.
- **Implication** → (if … then): false only when the hypothesis is true and the conclusion false.
- **Biconditional** ↔ (if and only if): true when both have the same truth value.

**Truth tables** show how operators combine propositions. A **tautology** is a statement that is always true; a **contradiction** is always false; the negation of a tautology is a contradiction and vice versa. If S → T is a tautology we write S ⇒ T, and if S ↔ T is a tautology we write S ⇔ T: the statements are **logically equivalent**. **De Morgan's laws** are two such tautologies: ¬(P ∧ Q) ⇔ (¬P) ∨ (¬Q) and ¬(P ∨ Q) ⇔ (¬P) ∧ (¬Q).

## Predicates and quantifiers

In a propositional function P(x), P is the **predicate** and x the **variable**; it becomes a proposition when x takes a value or is quantified.

- **Universal quantifier**: ∀x P(x), "for all x, P(x)", true when P(x) holds for every x in the universe of discourse.
- **Existential quantifier**: ∃x P(x), "there is at least one x such that P(x)".

For example, ∀x (S(x) → G(x)) reads "all UMBC students are geniuses", while ∃x (P(x) ∧ G(x)) reads "at least one UMBC professor is a genius". A statement of the form ∀x P(x) is disproved by one **counterexample**: "All birds can fly" is false because of the penguin. Negation swaps the quantifiers: ¬∀x P(x) ⇔ ∃x ¬P(x) and ¬∃x P(x) ⇔ ∀x ¬P(x).

Source: CSC 242.pdf (Discrete Structures lecture slides), the logic section; LOGIC CLASS ONE.pdf
