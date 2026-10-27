# Words, Alphabets and Languages

## Why the theory matters

Formal language and automata theory studies mathematical models of computation. It gives practitioners conceptual tools, shows a simpler side of complicated machines, and trains clear, precise problem solving.

## Words

An **alphabet** Σ is a finite set of symbols, for example {0, 1} or the letters a to z. A **word** (string) is a finite sequence of symbols from the alphabet. The **empty word** ε has no symbols.

- The **length** |w| is the number of symbols; |ε| = 0. With k symbols there are k^n words of length n.
- **Concatenation** writes two words together: if w1 = xxzyyx and w2 = zxxz, then w1w2 = xxzyyxzxxz. Concatenating with ε changes nothing. Concatenation is **associative**, but usually not commutative.
- The **nth power** w^n is n copies of w, with w^0 = ε.
- The **reversal** (mirror image) of w = x1x2…xn is w^R = xn…x2x1, and (w1w2)^R = w2^R w1^R.
- u is a **prefix** of w if w = uv, and a **subword** (segment) if w = v1uv2.

## Languages

A **language** is a set of words over an alphabet. Kinds include:

- **finite** languages (finitely many words);
- **cofinite** languages (only finitely many words missing);
- the **empty language** ∅ (no words);
- a **singleton** language {w}.

Set notation applies: subset, union, intersection, difference and complement. Σ* is the set of **all words** over Σ, including ε, and Σ+ = Σ* − {ε} is the set of non-empty words. The complement of L is Σ* − L.

The **concatenation** of two languages is L1L2 = {w1w2 | w1 ∈ L1, w2 ∈ L2}, and the **power** L^n concatenates n words of L, with L^0 = {ε}.

## Kleene star and plus

The **Kleene star** L* joins words of L in every possible way, including ε: L* = L^0 ∪ L^1 ∪ L^2 ∪ …. **L+** is the same without the empty string: L+ = L^1 ∪ L^2 ∪ … = LL* = L*L. So ∅* = {ε} but ∅+ = ∅.

Example: for L = {1, 00}, L^2 = {11, 100, 001, 0000}.

Languages are defined by three kinds of tool: **grammars** generate their words, **automata** recognise them, and **regular expressions** describe them.

Source: CSC 351 Formal Languages and Automata Theory.pdf, Study Session 1 (formal language, words, languages and their operations)
