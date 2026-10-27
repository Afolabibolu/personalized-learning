# Pushdown Automata

## What a PDA is

A **pushdown automaton (PDA)** is a finite automaton with extra memory in the form of a **stack**, which lets it recognise **context-free languages**. A DFA remembers only a finite amount of information, but a PDA's stack can hold an unbounded amount. PDAs are more capable than finite-state machines and less capable than Turing machines. Nondeterministic PDAs recognise all context-free languages; deterministic PDAs recognise the deterministic context-free languages and are used in parser design. "Pushdown" refers to the stack being pushed down like a tray dispenser in a cafeteria.

A PDA has three components:

1. an **input tape**,
2. a **control unit**, and
3. a **stack** of unlimited size.

The stack supports **push** (add a symbol at the top) and **pop** (read and remove the top symbol). A PDA may or may not read an input symbol in a move, but it must read the top of the stack.

## Formal definition

A PDA is a **7-tuple (Q, Σ, S, δ, q0, I, F)**:

- Q, the finite set of states;
- Σ, the input alphabet;
- S, the stack symbols;
- δ, the transition function, Q × (Σ ∪ {ε}) × S → Q × S*;
- q0, the initial state;
- I, the initial stack-top symbol;
- F, the set of accepting states.

A transition labelled **a, b → c** from q1 to q2 means: in state q1, on input a with b on top of the stack, pop b, push c and move to q2. An **instantaneous description** (q, w, s) records the state, the unread input and the stack contents. The turnstile ⊢ links one description to the next.

## Acceptance

- **By final state:** after reading the whole string the PDA is in a final state, whatever is left on the stack.
- **By empty stack:** after reading the whole string the stack is empty.

## Examples

**L = {0^n 1^n | n ≥ 0}:**

1. Push a marker $ onto the stack.
2. Push each 0 read.
3. Pop one 0 for each 1 read.
4. When $ is on top again, pop it and accept.

**L = {wcw^R}:** push the symbols of w, read the centre marker c, then pop and match each remaining symbol against the input. Accept when $ is reached.

## PDAs and grammars

For every context-free grammar there is an equivalent nondeterministic PDA, and for every PDA there is an equivalent CFG with L(G) = L(P). To build the PDA:

1. Put the grammar into Greibach normal form.
2. Use a single state, with the non-terminals as stack symbols and the terminals as input symbols.
3. Add one transition for each production.

Source: CSC 351 Formal Languages and Automata Theory.pdf, Study Session 11 (structure of a PDA, formal definition, acceptance, examples, PDA and CFG)
