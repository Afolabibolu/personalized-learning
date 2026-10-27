# Semantic Analysis and Intermediate Code

## What semantic analysis does

**Semantic analysis** (context-sensitive analysis) follows parsing and checks that declarations and statements are meaningful: identifiers declared before use and only once, **type checking**, procedures called with the right number and type of arguments, labels, flow of control (no break outside a loop) and scope. It is a separate phase because these rules are not context free. For example, int a = 2.3; passes lexical and syntax analysis but is a semantic error.

Semantic errors include type mismatch, undeclared variables, misused reserved identifiers, multiple declarations in one scope, out-of-scope variables and parameter mismatch. **Static** semantics are checked at compile time; **dynamic** semantics at run time, such as an array index out of range or division by zero.

## Attribute grammars

An **attribute grammar** attaches attributes to the non-terminals of a context-free grammar to carry semantic information. **Synthesized** attributes take their values from child nodes, as E gets its value in E → E + T; **inherited** attributes take values from the parent or siblings. An **S-attributed** syntax-directed translation uses only synthesized attributes and is evaluated bottom-up; an **L-attributed** one uses both, but never values from right siblings.

## Intermediate languages

The semantic analyser rewrites accepted code in an internal form: **Polish notation**, **quadruples** or **triples**.

**Polish (postfix) notation**, from the logician Łukasiewicz, puts operators immediately after their operands, so no parentheses are needed: A * B + C becomes AB*C+, and A * (B + C / D) becomes ABCD/+*. Identifiers keep their order, and operators appear in the order they are evaluated. A postfix expression is evaluated in one left-to-right scan with a **stack**: push each operand; for a binary operator, apply it to the top two operands and replace them with the result. The notation extends to assignment, jumps (BRL), conditional branches (BZ, BP, BM), array declarations (ADEC) and blocks (BLOCKBEGIN, BLOCKEND).

A **quadruple** is (operator, operand1, operand2, result). A * B + C * D becomes:

- *, A, B, T1
- *, C, D, T2
- +, T1, T2, T3

A **triple** has three fields (op, arg1, arg2), and results are referred to by position, such as (0). Triples are hard to reorder during optimization; **indirect triples** use pointers instead, so sub-expressions can be moved.

## Semantic routines

Routines needed to implement a semantic analyser include:

- **LOOK_UP(name, p):** finds a name in the symbol table and returns its address p.
- **LOOK_UP_DEC():** checks whether a name is declared.
- **INSERT(name, p):** inserts a name at entry p.
- **ENTER(operator, operand1, operand2, operand3):** enters a quadruple.
- **CHECK_TYPE(p, n):** checks that entry p is of type n.

Source: CSC 431 Compiler Construction.pdf (Ibadan Distance Learning course material), Study Session 9
