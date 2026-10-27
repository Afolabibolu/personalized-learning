# Deterministic Finite Automata

## How a finite automaton works

A **finite automaton** reads an input string one symbol at a time. It starts in the start state, follows the arrow labelled with each symbol in turn, and **accepts** the string if it ends in an **accept state**; otherwise it rejects it. In a **deterministic** finite automaton (DFA), every state has exactly one outgoing transition for each symbol of the alphabet.

## Formal definition

A DFA is a **5-tuple (Q, Σ, δ, q0, F)**:

1. Q, a finite set of **states**;
2. Σ, a finite **alphabet**;
3. δ: Q × Σ → Q, the **transition function**, so that δ(x, 1) = y means that in state x on reading 1 the machine moves to y;
4. q0 ∈ Q, the **start state**;
5. F ⊆ Q, the set of **accept states**.

A DFA may have zero accept states, and the language it accepts is the set of all strings it accepts.

## Designing a DFA

First decide what the machine must remember about the input read so far, and make each piece of information a state. Then draw the transitions for every symbol from every state, mark the start state and the accept states, and test the machine on strings that should and should not be accepted.

A **trap (dead) state** is a non-accepting state with all transitions looping back to itself. Once entered, the string can never be accepted, for example after a forbidden substring has been read.

## Equivalent states and minimisation

Two states p and q are **equivalent** if every string accepted from p is accepted from q, and every string rejected from p is rejected from q. States are **distinguishable** if some string leads one to an accepting state and the other to a non-accepting state. A DFA is minimal exactly when all its states are distinguishable.

**Table-filling (Myhill-Nerode) method:**

1. List all pairs of states.
2. Mark every pair where one state is final and the other is not.
3. Repeatedly mark an unmarked pair if, on some input, it leads to a marked pair.
4. Merge the pairs left unmarked.

**Partitioning (equivalence) method:**

1. Split the states into final and non-final (P0).
2. Split each group again if some input sends its members to different groups.
3. Stop when the partition no longer changes; each group becomes one state.

Before either method, remove states unreachable from the start state.

Source: CSC 351 Formal Languages and Automata Theory.pdf, Study Session 3 (finite automata and the formal definition), Study Session 4 (designing an automaton) and Study Session 7 (7.2, equivalence and minimisation)
