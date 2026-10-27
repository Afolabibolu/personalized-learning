# Linguistic Analysis and Grammars

## Why study linguistic analysis

It explains the structure of programming languages and helps in designing new ones.

## Basic concepts

An **alphabet** (vocabulary) is a finite non-empty set of symbols. A **string** is a finite, possibly empty sequence of symbols, and a **sentence** is a finite string over the alphabet. If V is an alphabet, **V*** is the set of all strings over V, including the empty string, and **V+** is V* without the empty string. A language over V is usually a subset of V*.

**Recursion** lets a finite set of productions define an infinite language: A = "a" A | ∅ gives {∅, a, aa, ...}.

## The four tuples of a grammar

A grammar is **G = (VN, VT, P, S)**:

- **VN:** non-terminals, syntactic variables that can be replaced.
- **VT:** terminals, the basic symbols of the sentences.
- **P:** productions (re-writing rules) of the form α → β, where α is in V+ and β in V*.
- **S:** the start symbol, a member of VN.

VN and VT have nothing in common, and V = VN ∪ VT is the **total vocabulary**. The language is L(G) = {w | w in VT* and S ultimately derives w}. A **sentential form** may contain terminals and non-terminals; a **sentence** contains only terminals, so every sentence is a sentential form but not the reverse.

## Chomsky's hierarchy

- **Type 0 (unrestricted, phrase structure):** α → β with α not empty. All grammars are Type 0.
- **Type 1 (context sensitive):** γ1Aγ2 → γ1Bγ2, so A is replaced only in the context γ1 on its left and γ2 on its right; for example aBc → aBbc.
- **Type 2 (context free):** a single non-terminal on the left, A → B. Context-free grammars describe the syntax of programming languages.
- **Type 3 (regular, finite state):** the right side is a terminal, or a terminal with one non-terminal; for example S → aA, A → a.

Lower types are subsets of higher ones: every regular grammar is context free.

## Ambiguity and precedence grammars

A grammar is **ambiguous** if some sentence has more than one derivation tree; for example E → E + E | E − E | id gives two trees for id + id − id. Ambiguity cannot be removed automatically; the grammar must be rewritten or given associativity and precedence rules.

- A **precedence grammar** is context free with precedence relations between some pairs of symbols; it is **simple precedence** if no two productions have the same right side and at most one relation holds between any pair.
- An **operator grammar** has no two consecutive non-terminals on any right side.
- An **operator precedence grammar** is an operator grammar with at most one precedence relation between any pair of terminals.

Source: CSC 431 Compiler Construction.pdf (Ibadan Distance Learning course material), Study Sessions 2 and 3
