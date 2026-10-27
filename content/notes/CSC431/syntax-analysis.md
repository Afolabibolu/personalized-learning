# Syntax Analysis (Parsing)

## What the parser does

Syntax analysis, the second phase after lexical analysis, checks that the tokens form a valid program under the language's **context-free grammar** and builds a **parse tree** (syntax tree), or reports errors. A parser detects and locates syntax errors, describes them clearly and recovers to find further errors.

## Derivation and parse trees

A **derivation** is a sequence of production rules that produces the input string.

- In a **leftmost derivation**, the leftmost non-terminal is replaced first.
- In a **rightmost derivation**, the rightmost non-terminal is replaced first.

For E → E + E | E * E | id and the input id + id * id, the leftmost derivation is E ⇒ E * E ⇒ E + E * E ⇒ id + E * E ⇒ id + id * E ⇒ id + id * id. In a parse tree, all leaves are terminals, all interior nodes are non-terminals, and an in-order traversal gives the input. The deepest sub-tree is evaluated first, so a parse tree shows **precedence**. **Associativity** decides which operator takes an operand that has operators on both sides; +, −, * and / are left associative: (id op id) op id.

## Preparing the grammar

- **Left recursion** (A ⇒ Aα | β) can send a top-down parser into an endless loop. It is removed by rewriting as A ⇒ βA′ and A′ ⇒ αA′ | ε; an algorithm removes indirect left recursion too.
- **Left factoring** removes a common prefix shared by several productions, so the parser can choose between them.
- **FIRST(α)** is the set of terminals that can begin strings derived from α. **FOLLOW(α)** is the set of terminals that can come immediately after α; FOLLOW of the start symbol contains $.

## Types of parsing

- **Top-down:** builds the tree from the root to the leaves. **Predictive (LL(1))** parsers use a look-ahead symbol and need no backtracking; **recursive descent** parsers have one small function per non-terminal.
- **Bottom-up (shift-reduce):** builds from the leaves to the root. **LR** parsers scan left to right and construct a rightmost derivation in reverse.

## The operator precedence algorithm

1. Find the **FIRST** and **LAST** terminals of each non-terminal.
2. Define the relations: r = s if r and s occur together or separated by one non-terminal; r < s if r comes before a non-terminal V and s is in FIRST(V); r > s if a non-terminal V comes before s and r is in LAST(V).
3. Build a **precedence matrix** of all terminals and use it to parse.

Its disadvantages: the minus sign has two precedences (unary and binary), and only a small class of grammars can be parsed. Whether a token is declared, initialised or used validly is left to the semantic analyser.

Source: CSC 431 Compiler Construction.pdf (Ibadan Distance Learning course material), Study Session 8
