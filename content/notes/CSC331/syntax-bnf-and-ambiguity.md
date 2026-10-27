# Syntax, BNF and Ambiguity

## Syntax and semantics

**Syntax** is the set of rules for writing a language's symbols in a meaningful order: it decides which programs are grammatically valid. **Semantics** describes how such programs execute. A program can be **syntactically correct yet meaningless**: syntax is a prerequisite of meaning, not a guarantee of it.

Some semantic questions can be answered at compile time (**static semantics**, such as whether b and c in `a = b + c` allow +). Others only at run time (**dynamic semantics**). A **metalanguage** is used to describe another language.

## Backus-Naur Form

**BNF** is a metalanguage of rewriting rules P, terminal symbols Σ, non-terminals N and a start symbol S. Its symbols are:

- **→ or ::=** means "is defined as";
- **{ }** means zero or more repetitions;
- **[ ]** means zero or one occurrence (optional);
- **|** means "or".

Examples:

- `binaryDigit → 0 | 1`
- `Identifier → letter {letter | digit}`
- `Integer → [+ | −] Natural`

**EBNF** adds the repetition and option brackets, and **syntax diagrams** draw the same rules graphically.

The **lexicon** is the set of token categories:

1. **identifiers**;
2. **literals**;
3. **operators**;
4. **separators**;
5. **keywords**.

## Delimiters: reserved words and keywords

Words like BEGIN and END could clash with identifiers. There are three solutions:

- **Reserved words** are excluded from identifiers, which simplifies lexical analysis but takes useful names out of circulation (SUM in COBOL).
- **Keywords** are flagged by special delimiters, as in ALGOL.
- The words may be used as identifiers and resolved by **context**, as in PL/1 (`IF IF = 1 THEN IF = 0`), which burdens the compiler.

## The compiling process

Program → **lexical analysis** (a token stream) → **syntactic analysis** (a parse tree, detecting syntax errors) → **semantic analysis** (consistent use of operators and types) → **optimisation** → **code generation** (machine code).

## Ambiguity

A grammar is **ambiguous** if one expression has **two different parse trees**.

With `AmbExp → integer | AmbExp − AmbExp`, the expression 2 − 3 − 4 can mean 2 − (3 − 4) = 3 or (2 − 3) − 4 = −5. Likewise `expr → expr + expr | expr * expr` is ambiguous for 8 + 2 * 7, which can give 70 or 22.

The classic case is the **dangling else**: in `IF (x < 0) IF (y < 0) y = y − 1; ELSE y = 0;` the ELSE can attach to either IF. Rewriting the grammar with separate levels (expr, term, factor) or braces removes the ambiguity.

Source: CSC 331 Programming Principles and Paradigms.pdf (course book), Study Session 6 (syntax, BNF, delimiters, Pascal syntax, compiling process, syntactic ambiguity); EBNF and syntax diagrams are general knowledge, following the CSC 331 past papers (2024/25 paper, Questions 5 and 6)
