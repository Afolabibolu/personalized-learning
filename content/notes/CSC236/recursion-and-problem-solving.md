# Recursion and Problem-Solving Techniques

## Recursion

Algorithms are the first-step solutions to programming problems, and the commonest problem-solving techniques are **recursion, backtracking and divide and conquer**. **Recursion** allows something to be defined in terms of smaller instances of itself. A **recursive function** is a function that **calls itself**, directly or indirectly; each successive call works on a more refined set of inputs, bringing us closer to the solution. For example, addition can be written add(x, y) = 1 + add(x, y − 1) for y > 0, and add(x, y) = x for y = 0; the terminating condition is y = 0.

A recursive method can actually solve only the simplest case, the **base case**, and returns a result for it at once. For a complex problem it splits the problem into a piece it can solve and a piece that resembles the original problem but is slightly smaller. It then calls a fresh copy of itself on the smaller piece: the **recursive call** or **recursion step**, which must return a result to be combined with the known piece.

Examples:

- **Factorial**: n! = n × (n − 1) × … × 2, computed iteratively with a loop or recursively as fac(n) = n × fac(n − 1), with fac(1) = 1.
- **Fibonacci**: 0, 1, 1, 2, 3, 5, 8, 13, 21, …, where Fibonacci(n) = Fibonacci(n − 1) + Fibonacci(n − 2). The ratio of successive terms converges on about 1.618, the **golden ratio**.

## Recursion versus iteration

- Both are based on a control statement: iteration uses a **repetition** statement (for, while, do-while), recursion a **selection** statement (if, if-else, switch).
- Both involve repetition: iteration explicitly, recursion through repeated method calls.
- Both have a **termination test**: iteration ends when the loop condition fails, recursion when a **base case** is recognised.
- Both can occur **infinitely**: an infinite loop if the condition never becomes false, infinite recursion if the recursion step does not move towards the base case.

The **demerit of recursion** is that it repeatedly invokes the method-call mechanism, with its **overhead** of processor time and memory for each call.

## Divide and conquer

The **divide and conquer** technique has three steps: **divide** the problem into subproblems of the same type, **conquer** them by solving them recursively, and **combine** their solutions into a solution of the original problem. Merge sort and quicksort are the standard examples.

Source: CSC_236_Introduction_to_Algorithm.pdf (CSC 236 course book), Unit 2 (Problem Solving Techniques)
