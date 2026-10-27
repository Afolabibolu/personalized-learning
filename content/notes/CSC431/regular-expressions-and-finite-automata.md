# Regular Expressions and Finite Automata

## Regular expressions

A **regular expression** specifies a pattern that matches a set of strings. The grammar it defines is a **regular grammar** and its language a **regular language**. Programming language tokens can be described by regular languages, which are easy to understand and efficient to implement.

## Operations

For languages L and M:

- **Union:** L ∪ M = {s | s is in L or s is in M}, written r | s.
- **Concatenation:** LM = {st | s is in L and t is in M}, written rs.
- **Kleene closure:** L*, zero or more occurrences of L, written r*.

**Precedence and associativity:** all three are left associative; * has the highest precedence, concatenation the second, and | the lowest.

## Notation for tokens

- **x*** means zero or more occurrences of x: {e, x, xx, ...}.
- **x+** means one or more occurrences: {x, xx, ...}, the same as x.x*.
- **x?** means at most one occurrence: {x} or {e}.
- **[a-z]**, **[A-Z]** and **[0-9]** are the lower-case letters, upper-case letters and digits.

With letter = [a-z] or [A-Z], digit = [0-9] and sign = [+ | -]:

- Decimal = (sign)?(digit)+
- Identifier = (letter)(letter | digit)*

## Regular expressions in Java

Java's String methods match regular expressions, used to validate program syntax and data inputs, such as a Nigerian plate number of three letters, up to four digits and two letters. Character classes include **\d** (a digit), **\w** (a word character), **\s** (white space) and their opposites **\D**, **\W** and **\S**. Square brackets match a set, such as [aeiou]; a dash gives a range, such as [A-Z]; a caret first, as in [^M], matches anything except the listed characters. The quantifiers *, +, ?, {n}, {n,} and {n,m} apply to the sub-expression just before them.

## Finite automata

A **finite automaton** is a state machine that recognises regular expressions: it changes state for each input symbol and **accepts** the string if it ends in a final state. Its model is:

- a finite set of **states** Q
- a finite set of **input symbols** Σ
- a **start state** q0
- a set of **final states** qf
- a **transition function** δ: Q × Σ → Q

In a diagram, states are circles, the start state has an arrow pointing to it, final states are double circles, and transitions are labelled arrows, including arrows from a state to itself.

## The longest match rule

The scanner reads letter by letter until a white space, operator or special symbol ends a word. In int intvalue; it cannot tell at "int" whether this is the keyword or the start of an identifier. The **longest match rule** chooses the longest matching token, and **rule priority** gives reserved words, such as keywords, priority over identifiers.

Source: CSC 431 Compiler Construction.pdf (Ibadan Distance Learning course material), Study Session 4
