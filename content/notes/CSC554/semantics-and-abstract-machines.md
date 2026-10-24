# Semantics and Abstract Machines

## Why formal semantics

Semantics is the study of meaning. Programming language semantics gives programs a precise mathematical meaning. Formal semantics rigorously specifies the meaning, or behaviour, of programs and hardware. That rigour matters for two reasons:

- It reveals ambiguities and subtle complexities in documents that look clear, such as programming language manuals.
- It is a basis for implementation, analysis and verification, especially proofs of correctness.

**Syntax versus semantics.** Syntax is the grammatical structure of a program. Syntactic analysis of z:=x; x:=y; y:=z finds three statements separated by ';', each a variable, ':=' and an expression. Semantics is the meaning of a grammatically correct program. This one swaps the values of x and y, and sets z to the final value of y.

## Abstract machines

Historically, the first rigorous operational semantics used an **abstract machine**: a transition system that specifies an interpreter for the language. The SMC machine is an example. Its configurations are triples of a Stack of results, a Memory and a Control stack of phrases to evaluate.

An abstract machine is a *machine* because it runs programs step by step. It is *abstract* because it leaves out the details of real hardware. It provides an intermediate stage for compilation. A generic abstract machine has a **memory**, which stores data and programs, and an **interpreter**, which executes instructions. The interpreter's operations cover primitive data, sequence control, data transfer and memory management.

Types of abstract machine include the WAM (Warren), SECD, RAM (Random Access Machine), LAM, IAM, TAM, CHAM (Chemical Abstract Machine), the von Neumann machine and the Turing machine.

## The SECD machine

Peter J. Landin described the SECD machine in "The Mechanical Evaluation of Expressions" (1964). It was the first machine designed specifically to evaluate **λ-calculus** expressions, and it gave semantics to the language ISWIM. It is named after its four registers:

- **S, the Stack:** temporary values, closures and arguments. Operands are pushed here.
- **E, the Environment:** variable bindings. It is a list of lists, one level per function scope, and the only register accessed by index.
- **C, the Control:** the instructions still to run, like a program counter.
- **D, the Dump:** saves the stack, environment and control when a function is called, and restores them when the call returns.

Lispkit Lisp was an influential compiler based on the SECD machine.

**λ-calculus.** An expression is a name, a function or an application:
- A function has the form λ name.expression.
- An application is one expression followed by another.
- Application associates from the left.

In the course's SECD rules, an operator expression op(e1, e2) is analysed into e1 :: e2 :: Prim(op) on the control. For an expression e:
- The **initial state** is (nil, empty, e :: nil) :: nil.
- A **final state** is (v :: nil, empty, nil) :: nil, where v is the result left on the stack.

Source: Semantic of Programming Language.pdf (CSC 554 lecture slides)
