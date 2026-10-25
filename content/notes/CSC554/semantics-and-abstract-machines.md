# Semantics and Abstract Machines

## Why formal semantics

Semantics is the study of meaning. Programming language semantics gives programs a precise mathematical meaning. Formal semantics rigorously specifies the meaning, or behaviour, of programs and hardware. That rigour matters for two reasons:

- It reveals ambiguities and subtle complexities in documents that look clear, such as programming language manuals.
- It is a basis for implementation, analysis and verification, especially proofs of correctness.

**Syntax versus semantics.** Syntax is the grammatical structure of a program: z:=x; x:=y; y:=z is three statements separated by ';'. Semantics is the meaning of a grammatically correct program: this one swaps x and y.

## Abstract machines

The first rigorous operational semantics used an **abstract machine**: a transition system that specifies an interpreter for the language, such as the SMC machine (Stack, Memory, Control).

An abstract machine runs programs step by step (a *machine*) but leaves out the details of real hardware (*abstract*), giving an intermediate stage for compilation. It has a **memory**, which stores data and programs, and an **interpreter**, whose operations cover primitive data, sequence control, data transfer and memory management.

Types include the WAM, SECD, RAM, LAM, CHAM, the von Neumann machine and the Turing machine.

## The RAM machine

The **Random Access Machine** has an unbounded set of registers r0, r1, r2, ..., each holding an integer, with r0 as the accumulator. A program is a numbered list of instructions, and a program counter selects the next one. Typical instructions are LOAD, STORE, ADD, SUB, JUMP, JZERO, READ, WRITE and HALT. An operand can be immediate (=k), direct (register k) or indirect (the register whose number is in register k). With x in r1 and y in r2, y := x + 3 for x = 2 is: LOAD =2; STORE 1; LOAD 1; ADD =3; STORE 2; HALT, leaving 5 in r2.

## The SECD machine

Peter J. Landin described the SECD machine in 1964, the first machine designed to evaluate **λ-calculus** expressions; it gave semantics to ISWIM. Its four registers:

- **S, the Stack:** temporary values, closures and arguments.
- **E, the Environment:** variable bindings, one level per function scope.
- **C, the Control:** the instructions still to run, like a program counter.
- **D, the Dump:** saves the stack, environment and control when a function is called, and restores them when the call returns.

**λ-calculus.** An expression is a name, a function (λ name.expression) or an application (one expression followed by another, associating from the left).

In the course's SECD rules, an operator expression op(e1, e2) is analysed into e1 :: e2 :: Prim(op) on the control. For an expression e:
- The **initial state** is (nil, empty, e :: nil) :: nil.
- A **final state** is (v :: nil, empty, nil) :: nil, where v is the result left on the stack.

Source: Semantic of Programming Language.pdf (CSC 554 lecture slides); the RAM machine section is from general knowledge, following week 2 of CSC554 Course Outline.pdf
