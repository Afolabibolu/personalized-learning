# Nondeterministic Finite Automata

## Nondeterminism

In a DFA each state has exactly one exiting arrow per symbol. In a **nondeterministic finite automaton (NFA)** a state may have **zero, one or many** exiting arrows for a symbol, and arrows labelled **ε** that are followed without reading any input.

When an NFA has several ways to proceed, it splits into copies that follow every possibility in parallel. A copy dies if no arrow matches the next symbol, and an ε-arrow splits the machine again. The computation is a tree of possibilities, and the NFA **accepts if at least one branch ends in an accept state**. The book's example NFA R1 accepts every string containing 101 or 11 as a substring.

NFAs are useful because they are often easier to build and smaller than the equivalent DFA.

## Formal definition

An NFA is a 5-tuple (Q, Σ, δ, q0, F) like a DFA, except for the transition function. For a state and an input symbol or ε, it gives a **set** of possible next states:

**δ: Q × Σε → P(Q)**

Here Σε = Σ ∪ {ε} and P(Q) is the power set of Q.

## ε-NFA and ε-closure

An **ε-NFA** allows transitions on the empty string. It makes it easy to show that DFAs, NFAs and regular expressions are equivalent. The **ε-closure** of a state is the set of states reachable from it by ε-transitions alone, including the state itself.

**Converting an ε-NFA to an NFA:**

1. Find the ε-closure of each state.
2. For each state and symbol, take the states reachable from its ε-closure on that symbol, followed by ε-moves.
3. Write the result as a transition table and draw the new diagram.
4. A state becomes accepting if its ε-closure contains an accept state.

## Converting an NFA to a DFA (subset construction)

1. Write the NFA's state table.
2. Start the DFA at the NFA's start state.
3. For each input symbol, find the set (combination) of NFA states reachable. Each new combination becomes a new DFA state.
4. Repeat for every new state until no new combinations appear.
5. Any DFA state containing an NFA final state is final.

**Every DFA has an equivalent NFA, and every NFA has an equivalent ε-NFA**, so all three accept exactly the regular languages.

Source: CSC 351 Formal Languages and Automata Theory.pdf, Study Session 5 (NFA, computation, formal definition, ε-NFA and the equivalence of DFA and NFA); ε-closure steps follow the 2021/22 and 2024/25 papers
