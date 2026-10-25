# The Problem-Solving Process and Algorithms

## Polya's How to Solve It

In 1945 George Polya described the problem-solving process in *How to Solve It*. Written for mathematics, it applies to all problems if we read "unknown" as problem, "data" as information and "theorem" as solution:

1. **Understand the problem.** What is the unknown? What are the data? What is the condition?
2. **Devise a plan.** Find the connection between the data and the unknown. Have you seen it before? Do you know a related problem?
3. **Carry out the plan,** checking each step.
4. **Look back.** Examine the solution. Can you check the result? Can you use the method for another problem?

The second step, finding the connection between the information and the solution, is the heart of problem solving. Polya's list suggests strategies: **ask questions** (what do I know, what does the solution look like, what special cases exist, how will I recognise the solution?), **look for familiar things** (finding the highest and lowest temperatures is the same problem as finding the highest and lowest grades), and **divide and conquer** (break a large problem into smaller ones that can be solved individually).

## Algorithms

The plan in step two is, in computing, an **algorithm**: unambiguous instructions for solving a problem or subproblem in a finite amount of time using a finite amount of data. A good algorithm is commonly described as having inputs and outputs, steps that are definite (unambiguous) and effective (can actually be done), and finiteness (it ends).

A **heuristic** is a rule of thumb that usually finds a good answer quickly but does not guarantee the best or even a correct one, for example "always visit the nearest unvisited city next". Heuristics are used when an exact algorithm is unknown or too slow.

## The computer problem-solving process

The computer problem-solving process has four phases:

- **Analysis and specification:** understand the problem and produce a clear problem statement.
- **Algorithm development:** develop a logical sequence of steps, then test it by following the steps.
- **Implementation:** translate the algorithm into a programming language, run it and correct it.
- **Maintenance:** use the program and modify it for new requirements or errors.

An error found in one phase can send you back to an earlier one.

## Top-down design

The strategy that parallels Polya's outline is **top-down design**: analyse the problem, list the main tasks (the main module), write the remaining modules with successive refinement until each step is concrete, then re-sequence and revise. Algorithms must be tested before they are coded, because problems found early are cheaper to fix.

Source: Computer Science Illuminated, 7th edition (2020), Chapter 7.1; algorithm properties and heuristics from general knowledge, following the NUC CCMAS outline for COS 102
