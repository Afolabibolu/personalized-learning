# Problems and Computational Problems

## Problems

A **problem** is a perceived **gap between the existing state and a desired state**: a puzzle, a task or a challenge, not necessarily something negative. Einstein said that with one hour to save the planet he would spend **59 minutes defining the problem** and one minute solving it. **Problem solving** is the act of finding a solution to a perplexing or unsettled question. In computing it is the sequential process of analysing information about a situation and generating appropriate responses.

A computer **cannot solve every problem**:

- it does nothing without being told what to do;
- it is not intelligent on its own and relies on human solutions;
- it has limitations;
- but it frees people from repetitive, voluminous and boring tasks.

**Six steps to solve a computer problem**:

1. understand the problem;
2. formulate a model;
3. develop an algorithm;
4. write the program;
5. test the program;
6. evaluate the solution.

## Computational problems

A **computational problem** is a task a computer can solve by following an algorithm. It defines **what** is to be computed, not how: given the input, produce the correct output.

- **Decision**: the answer is yes or no ("Is this number prime?").
- **Search**: find a solution that meets conditions ("the shortest path between two cities").
- **Optimisation**: find the **best** solution ("the cheapest way to travel across 5 cities").
- **Function**: output a specific value (the GCD of two numbers).
- **Classification**: assign inputs to categories ("is this email spam?").
- **Sorting**: arrange items in order.
- **Counting**: count the solutions ("how many ways to arrange 5 books?").

## Pólya's method

**George Pólya**'s *How to Solve It* (1945) gives four steps:

1. **Understand the problem.** What is the unknown? What are the data and the condition? Is the condition sufficient, redundant or contradictory? Draw a figure and choose notation. The output is a clear problem statement.
2. **Devise a plan.** Don't reinvent the wheel: have you seen a related problem? Use **divide and conquer**, breaking a large task into smaller ones, as with cleaning a house room by room.
3. **Carry out the plan**, checking each step.
4. **Look back.** Check the result, try deriving it differently, and reuse the method.

**Example**: two numbers with sum 15 and product 50. Then x(15 − x) = 50 gives x² − 15x + 50 = 0, so **5 and 10**; checking, 5 + 10 = 15 and 5 × 10 = 50. To test whether n is even, check n % 2 == 0.

## Solvable or not

A **solvable** problem has an algorithm that always gives the correct answer in finite time, such as the fastest route from hostel to cafeteria. An **unsolvable** problem has no such algorithm for all cases. Questions too vague or unpredictable, like predicting exact global weather for 50 years, have no step-by-step method.

Source: COS 102 Problem Solving (Lecture 4); COS 102 Lecture 6 (identification of problems) (class quizzes)
