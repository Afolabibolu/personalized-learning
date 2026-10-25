# Algebraic Semantics and Unifying Theories of Programming

## Algebraic semantics

**Algebraic semantics** rests on abstract algebras, as denotational semantics rests on recursive function theory. The idea is to name the sorts of objects and the operations on them, and to use algebraic axioms to describe their properties. It is customarily used to specify **abstract data types**: a stack is specified by the properties of push and pop, not by how stacks are stored.

An algebraic specification has two parts:

- The **signature** Σ = <Sorts, Operations>. Sorts are names of types, such as Integer, Boolean and List. Operations are function symbols with their functionalities, such as cons ( _ , _ ) : Integer, List → List. An operation with no domain is a constant, such as emptyList or true.
- The **equations** (axioms), which constrain the operations. Their variables are implicitly universally quantified: head (cons (m, s)) = m holds for every m and s. An equation can be conditional: lhs = rhs when lhs1 = rhs1, ...

Specifications are written as **modules** that import other modules, export public sorts and operations and hide the rest, and can be parameterised to define generic types. In the Naturals module, 0 and **succ** are **constructors**: there are no equations for succ, so 0, succ(0), succ(succ(0)), ... are all different and stand for the natural numbers. Each sort has an error value, such as errorNatural from div(m, 0), and operations propagate errors.

The model of a specification is an algebra. The **initial algebra** is the finest-grained model: it equates only the terms the equations force to be equal. A model with values that no term denotes has **junk**; one that equates terms the equations do not has **confusion**.

**Equational reasoning** replaces equals by equals. In a **term rewriting system** the equations are used left to right as rewrite rules until no rule applies and the term is in **normal form**. If rewriting always terminates and is confluent, every term has exactly one normal form.

## Unifying Theories of Programming (UTP)

UTP, by C.A.R. Hoare and He Jifeng (1998), describes programs and specifications in one framework, as **predicates** relating initial observations (x) to final ones (x′). Extra variables such as ok and ok′ record that a program has started and terminated. A theory has an alphabet of variables, a signature of operators, and **healthiness conditions**: properties every predicate in the theory must satisfy, such as "nothing can be observed before the program starts". **Refinement** is reverse implication, so Q refines P when Q ⇒ P for every observation. Operational, denotational and algebraic semantics become views of the same theory.

**Predicate transformer semantics**, from Dijkstra, gives a command's meaning as its **weakest precondition**: wp(x := e, Q) = Q with e substituted for x.

Source: Slonneger and Kurtz, Formal Syntax and Semantics of Programming Languages, Chapter 12 (algebraic semantics); term rewriting, UTP and predicate transformers from general knowledge, following weeks 6 and 7 of CSC554 Course Outline.pdf
