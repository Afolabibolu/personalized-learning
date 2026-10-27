# Regular Expressions and Regular Languages

## Regular expressions

A **regular expression** (RE) is a formula that defines a language using three operations: **union** (written +), **concatenation** and the **Kleene star** (*). Its atoms are the symbols of the alphabet, the empty language ∅ and the empty word ε, with parentheses where needed.

The order of precedence is: **star** first, then **concatenation**, then **union**.

## Regular languages

Languages defined by regular expressions are the **regular languages**. The family R is built by these rules:

1. ∅ is in R, with regular expression ∅.
2. {ε} is in R, with regular expression ε.
3. For each symbol x, {x} is in R, with regular expression x.
4. If L1 and L2 are in R with expressions r1 and r2, then L1 ∪ L2 (r1 + r2) and L1L2 (r1r2) are in R.
5. If L is in R with expression r, then L* (r*) is in R.
6. Nothing else is in R.

Common abbreviations: rr = r², and r r* = r+.

## Building expressions

- L(E + F) = L(E) ∪ L(F)
- L(EF) = L(E)L(F)
- L(E*) = (L(E))*

## Algebraic laws

- **Commutative:** E + F = F + E.
- **Associative:** (E + F) + G = E + (F + G), and (EF)G = E(FG).
- **Identity:** E + ∅ = E, and εE = Eε = E.
- **Annihilator:** ∅E = E∅ = ∅.
- **Distributive:** E(F + G) = EF + EG, and (F + G)E = FE + GE.
- **Idempotent:** E + E = E.
- **Kleene closure:** (E*)* = E*; ∅* = ε; ε* = ε; E+ = EE*; E? = ε + E; E+ + ε = E*.

## Regular expressions and finite automata

A language is regular if and only if a regular expression describes it, or equivalently if a DFA, NFA or ε-NFA can be built for it.

- **For every DFA A** there is a regular expression R with L(R) = L(A). Informally, trace the distinct paths from the start state to each final state and combine the expressions along them.
- **For every regular expression R** there is an ε-NFA accepting L(R). It is built from the smallest sub-expressions upwards; for example, (ab ∪ a)* is built from NFAs for a and b.

Regular expressions are declarative and program-like, while automata are machine-like (input a string, output accept or reject). Unix tools such as grep, the bash shell and vi rely heavily on regular expressions.

Source: CSC 351 Formal Languages and Automata Theory.pdf, Study Session 2 (regular expressions, regular languages and their laws) and Study Session 6 (6.1–6.2, REs versus finite automata). The book's example law (R + S)* = R* + S* is left out, because it does not hold in general
