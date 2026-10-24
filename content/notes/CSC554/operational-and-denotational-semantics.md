# Operational and Denotational Semantics

## Three ways to give meaning

The lecture distinguishes three ways of formalising what a program means:

- **Operational semantics:** a construct means the computation it induces when it runs on a machine. The interest is in *how* the effect is produced. The course covers structural operational semantics, which is small-step, and big-step, or natural, semantics, with transition rules and derivation trees.
- **Denotational semantics:** meanings are mathematical objects that represent the effect of the constructs. Only the effect matters, not how it is obtained.
- **Axiomatic semantics:** properties of the effect are stated as assertions, so some aspects of execution are ignored.

Algebraic semantics (Guttag's abstract data types) is a further method.

## Denotational semantics

Denotational semantics maps every syntactic entity to a suitable mathematical entity, its *denotation*:

meaning : Syntax → Semantics

For example, 28/2, (10+4), 014 and 14 all mean the number 14. Its features include mathematical formalism, domain theory, independence from implementation, compositionality, modularity and support for formal reasoning.

A denotational definition has **five parts**:

1. **Syntactic categories**, such as Command C, Expression E, Numeral N, Identifier I and Operator O.
2. **BNF** that defines their structure.
3. **Semantic (value) domains**: the mathematical sets. Boolean = {true, false}; Integer = {…, −1, 0, 1, …}; Store = (Variable → Integer).
4. **Semantic functions**: the signatures of the mappings, such as meaning : Program → Store and evaluate : Expression → (Store → Value).
5. **Semantic equations**: the rules for each production, such as evaluate [[E1 * E2]] sto = times(evaluate [[E1]] sto, evaluate [[E2]] sto).

There is generally one semantic function per syntactic category and one equation per grammar production. **Auxiliary functions** such as plus, minus and times describe operations in the domains.

**Compositionality.** The meaning of a phrase is built from the meanings of its parts, so E1 * E2 means the product of the meanings of E1 and E2.

**Worked example.** With environment ρ where x = 5 and y = 7:
- [[Var x + Num 2]]ρ = 5 + 2 = 7
- [[Var y * Num 3]]ρ = 7 × 3 = 21
- [[(Var x + Num 2) − (Var y * Num 3)]]ρ = 7 − 21 = −14

**Direct style** semantics gives meaning by how expressions are evaluated directly. **Fixed-point semantics** handles recursive or self-referential definitions. A fixed point of a function is a value the function leaves unchanged.

**Applications:**
- foundations for program logics such as Hoare logic
- modelling side effects, concurrency and parallelism
- formal verification of correctness, safety and termination

In the exam style, the denotational meaning of x := 2; y := x + 3 is found by applying each assignment's function to the state in turn: first x becomes 2, then y becomes x + 3 = 5.

Source: Semantic of Programming Language.pdf; CSC 554 Group 3 Term Paper.pdf (Denotational Semantics); CSC554 Course Outline.pdf
