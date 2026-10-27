# Context-Free Grammars and Normal Forms

## Context-free grammars

Regular languages cannot "count", so they cannot check matching parentheses. **Context-free grammars (CFGs)** can. A CFG is a set of recursive rules for generating strings, written G = (S, N, T, P):

- **T**, a set of **terminal** symbols, the characters of the strings generated;
- **N**, a set of **non-terminals** (variables), placeholders that always appear on the left of productions;
- **P**, a set of **productions** of the form variable → string of variables and terminals;
- **S**, the **start symbol**.

**Example:** A → 0A1 | B, B → # generates 000#111 by the derivation A ⇒ 0A1 ⇒ 00A11 ⇒ 000A111 ⇒ 000B111 ⇒ 000#111. Its language is {0^n#1^n | n ≥ 0}.

## Derivations and parse trees

- A **leftmost derivation** always replaces the leftmost variable; a **rightmost derivation** always replaces the rightmost one.
- A **parse (derivation) tree** has the start symbol at the root, non-terminals at internal vertices and terminals or ε at the leaves.
- The **yield** of a tree is its leaves read from left to right.

## Ambiguity

A grammar is **ambiguous** if some string has two or more different leftmost derivations, that is, two parse trees. For example, X → X+X | X*X | a gives two trees for a+a*a.

Ambiguity can sometimes be removed by rewriting the grammar with operator precedence and associativity, as in E → E + T | T, T → T * F | F. A language is **inherently ambiguous** if every grammar for it is ambiguous.

CFGs describe programming-language syntax and drive parser generators such as yacc and bison; for programming languages they are written in **Backus-Naur Form (BNF)**.

## Simplification

1. **Remove useless symbols:** first keep the symbols that derive a terminal string, then keep those reachable from the start symbol.
2. **Remove unit productions** A → B: add A → x for each B → x, then delete A → B.
3. **Remove null productions:** find the nullable variables, add every version of each rule with them left out, then drop the ε-rules.

## Normal forms

**Chomsky normal form (CNF):** every production is A → BC or A → a. To convert:

1. Add a new start symbol if S appears on a right-hand side.
2. Remove null and unit productions.
3. Break long right-hand sides into pairs.
4. Replace terminals in mixed rules by new variables (A → aB becomes A → XB, X → a).

**Greibach normal form (GNF):** every production is A → b or A → bD1…Dn (and possibly S → ε), where b is a terminal. Conversion also removes left recursion.

Source: CSC 351 Formal Languages and Automata Theory.pdf, Study Session 9 (CFGs, derivations, parse trees, ambiguity, applications, closure) and Study Session 10 (simplification, CNF and GNF). The book's line that the strings a CFG produces contain only non-terminal symbols is left out; they contain only terminals
