# Decidability

## Basic concepts

Decidability is the ability to determine, by an algorithm, whether a problem has a true or false answer.

- **Decision problem:** a question with a yes or no answer, such as "Is this number prime?"
- **Decidable problem:** some algorithm gives the right answer for every input in a finite number of steps. Equivalently, some Turing machine decides it.
- **Recursive language (REC):** a TM accepts every string in L and rejects every string not in L, always halting. Decidable and recursive mean the same thing.
- **Recursively enumerable language (RE):** a TM accepts every string in L but may loop on strings outside it. Every REC language is RE, but not every RE language is REC.
- **Semi-decidable (partially decidable):** RE but not REC.
- **Undecidable:** not decidable. A language that is not even partially decidable has no Turing machine at all.

## Decidable problems

Problems are expressed as languages of encodings. For example, ADFA contains the pairs ⟨B, w⟩ where the DFA B accepts w.

- **ADFA is decidable:** a TM simulates B on w and accepts if B ends in an accept state.
- **ANFA is decidable:** convert the NFA to a DFA and use the ADFA decider as a subroutine.
- **AREX is decidable:** convert the regular expression to an NFA.
- **EDFA (emptiness) is decidable:** mark the states reachable from the start state and check whether any accept state is marked.
- **EQDFA (equivalence) is decidable:** build a DFA C for the symmetric difference of L(A) and L(B). Then L(C) is empty if and only if L(A) = L(B).
- **ACFG is decidable:** convert G to Chomsky normal form, where any derivation of a string of length n has 2n − 1 steps, so only finitely many derivations need checking.
- **Every context-free language is decidable.**

So regular ⊂ context-free ⊂ decidable ⊂ Turing-recognisable.

## Undecidability of ATM

ATM = {⟨M, w⟩ | M is a TM and M accepts w} is **undecidable**, though it is Turing-recognisable. The universal machine U recognises it by simulating M on w, but U loops whenever M loops. So recognisers are more powerful than deciders.

## Diagonalization

Georg Cantor introduced diagonalization in 1873 to compare the sizes of infinite sets. Two sets have the same size if there is a one-to-one, onto correspondence (a bijection) between them. A set is **countable** if it is finite or the same size as N. The positive rationals Q are countable: list them diagonal by diagonal through an infinite matrix, skipping repeats. The real numbers are **uncountable**.

The ATM proof assumes a decider H and builds a machine D that does the opposite of what H says about a machine run on its own description. Running D on ⟨D⟩ forces D to do the opposite of itself, a contradiction. So neither H nor D exists.

Source: DLC CSC 552 Theory of Computation.pdf, Study Session 4
