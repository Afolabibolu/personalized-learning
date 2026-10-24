# Turing Machines

## Why the theory of computation

The theory of computation studies algorithms, computation and the limits of what can be computed.

## Finite automata versus Turing machines

- **Power:** finite automata recognise only regular languages, the simplest class in the Chomsky hierarchy. Turing machines recognise far more, up to the recursively enumerable languages.
- **Memory:** finite automata have a fixed number of states. A Turing machine has an infinite tape.
- **Processing:** finite automata read the input once, left to right. A Turing machine moves back and forth and can read, write and erase.
- **Acceptance:** finite automata accept if they end in a final state. A Turing machine accepts by halting in an accept state, rejects by halting in a reject state, or loops forever.

## The machine

Alan Turing proposed the model in 1936. Its infinite tape first holds only the input, with blanks everywhere else. A head reads and writes symbols and moves left or right. The accept and reject states take effect immediately. If neither is reached, the machine never halts.

Formally, a Turing machine is a **7-tuple** (Q, Σ, Γ, δ, q0, qaccept, qreject):

- Q is the set of states, and q0 is the start state.
- Σ is the input alphabet, which does not contain the blank.
- Γ is the tape alphabet, which includes the blank and Σ.
- δ: Q × Γ → Q × Γ × {L, R} is the transition function, the heart of the machine.
- qaccept and qreject are the accept and reject states.

A **configuration** records the current state, the tape contents and the head position, written uqv: the machine is in state q, the tape holds uv, and the head is on the first symbol of v. For example, if δ(q1, b) = (q2, c, L), then aaq1bb yields aq2acb.

## Languages

- A TM **recognises** L if it accepts exactly the strings in L. Such L is Turing-recognisable, or **recursively enumerable**.
- A TM that halts on every input is a **decider**. A language decided by one is **decidable**, or **recursive**.
- Every recursive language is recursively enumerable, but not the reverse.

**Examples.** For B = {w#w}, M1 zig-zags across the #, crossing off matching symbols, and rejects on a mismatch. For strings of 0s whose length is a power of 2, M2 crosses off every other 0 on each sweep. It accepts if a single 0 is left and rejects if an odd number greater than 1 remain.

## Variants

All reasonable variants have the same power, which is called **robustness**:

- **Multitape TMs:** simulated on one tape with # delimiters and dotted symbols marking the heads.
- **Nondeterministic TMs:** simulated deterministically by a breadth-first search of the computation tree. Depth-first search could run down an infinite branch.
- **Enumerators:** TMs with a printer. A language is Turing-recognisable if and only if some enumerator enumerates it.

Source: DLC CSC 552 Theory of Computation.pdf, Study Sessions 1 and 2
