# Properties of Regular Languages and the Chomsky Hierarchy

## The pumping lemma

The **pumping lemma** is used to show that a language is **not** regular. For any regular language L there is an integer n such that every x ∈ L with |x| ≥ n can be split as x = uvw where:

1. |uv| ≤ n,
2. |v| ≥ 1, and
3. uv^i w ∈ L for all i ≥ 0.

The idea: a DFA for L has a limited number of states, so a long enough path through it must repeat a state, and the loop can be repeated or skipped.

**Example:** L = {a^i b^i | i ≥ 0} is not regular. Assume it is, and take w = a^n b^n. Since |xy| ≤ n, y is made only of a's. Pumping y once more gives a^(n+q) b^n, which is not in L, a contradiction.

Satisfying the lemma is **necessary** for a language to be regular, but **not sufficient**: some non-regular languages also satisfy it. It can therefore only prove that a language is not regular.

## Closure properties

Regular languages are **closed** under union, intersection, complement and difference, reversal, Kleene closure, concatenation, homomorphism and inverse homomorphism. Combining regular languages with any of these gives a regular language.

## Decision properties

These questions can be decided for regular languages given as DFAs:

- **Membership:** run w on a DFA for L; accept if it ends in an accepting state.
- **Emptiness:** L = ∅ if and only if no final state is reachable from the start state.
- **Finiteness:** remove unreachable states and states that cannot reach an accept state; L is finite if no cycle remains.
- **Equivalence:** whether two DFAs accept the same language.

## The Chomsky hierarchy

| Type | Languages | Grammars | Machines |
| --- | --- | --- | --- |
| 0 | Recursively enumerable | Unrestricted | Turing machines |
| 1 | Context-sensitive | Context-sensitive | Linear bounded automata |
| 2 | Context-free | Context-free | Pushdown automata |
| 3 | Regular | Right-linear | Finite automata |

Each class is contained in the one above: regular ⊂ context-free ⊂ context-sensitive ⊂ recursive ⊂ recursively enumerable.

| Class | Union | Intersection | Complement |
| --- | --- | --- | --- |
| Recursively enumerable | Yes | Yes | No |
| Recursive | Yes | Yes | Yes |
| Context-sensitive | Yes | Yes | Yes |
| Context-free | Yes | No | No |
| Regular | Yes | Yes | Yes |

Source: CSC 351 Formal Languages and Automata Theory.pdf, Study Session 6 (6.3–6.4, pumping lemma and closure properties), Study Session 7 (7.1, decision problems) and Study Session 8 (Chomsky hierarchy); the necessary-but-not-sufficient point is general knowledge, following the undated CSC 351 paper (Question 2(b))
