# Stacks and Expression Conversion

## The stack

A **stack** is a linear data structure that follows **LIFO** (Last In, First Out). It has one open end, the **top**, and a single pointer to the topmost element. Insertion and deletion both happen at the top.

| Operation | Meaning |
| --- | --- |
| push() | insert at the top; if the stack is full, **overflow** occurs |
| pop() | delete from the top; if the stack is empty, **underflow** occurs |
| peek() | return the top element without removing it |
| isEmpty(), isFull() | test the state |

All of these take **O(1)** time. In C the top is initialised to **−1**, so the stack is empty when top is −1. Push increments top and stores the item; pop returns stack[top] and decrements top.

A stack can be built with an **array** (simple, no pointers, but fixed size) or a **linked list** (grows and shrinks at run time, but needs extra memory for pointers).

## Applications

Balancing of symbols (push each opening brace, pop on each closing one; anything left means an error), string reversal, undo and redo, recursion (the system stack keeps each call's state), depth-first search, backtracking (a maze), expression conversion, memory management and parsing.

## Infix, prefix and postfix

- **Infix:** operator between operands, a + b.
- **Prefix (Polish):** operator before operands, + a b.
- **Postfix (Reverse Polish):** operator after operands, a b +.

Prefix and postfix need no parentheses, because the position of each operator fixes the order of evaluation. Precedence (highest first): exponentiation ^ (right associative), then * and /, then + and − (left associative).

## Infix to postfix with a stack

Read the symbols from left to right:

1. An operand goes straight to the output.
2. A left parenthesis is pushed.
3. A right parenthesis pops operators to the output until the matching left parenthesis is removed.
4. An operator first pops any operators of higher or equal precedence to the output, then is pushed.
5. At the end, pop everything left on the stack.

Example: (A + B) * (C − D) becomes **A B + C D − \***.

## Postfix evaluation

Scan from left to right, pushing operands; on an operator, pop two operands (the first pop is the second operand), apply it and push the result. For 4 5 6 * +, 5 × 6 = 30 is pushed, then 4 + 30 = 34.

Source: CSC 341(Data structure).pdf, pages 3–31 (stack operations, implementations, applications, notations, conversion and evaluation)
