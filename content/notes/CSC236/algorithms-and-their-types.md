# Algorithms: Meaning, Properties and Types

## What an algorithm is

Informally, an **algorithm** is any **well-defined computational procedure that takes some value, or set of values, as input and produces some value, or set of values, as output**: a sequence of computational steps that transform the input into the output. It is also described as a **finite set of instructions** that, if followed, accomplishes a particular task, or a **sequence of unambiguous instructions**: there is no room for subjective interpretation, so the same algorithm always behaves the same way on the same input. Everyday computing, from spell checks to web searches, is made of algorithms.

Algorithms are expected to have **zero or more inputs**, at least one **output**, **definiteness** (clear and unambiguous steps), **finiteness** (no infinite sequence of steps) and **effectiveness** (steps simple enough to be carried out). An algorithm is **correct** if, for every input instance, it **halts with the correct output**; an incorrect one may not halt on some inputs, or may halt with the wrong answer. Knowing an algorithm's behaviour also helps us use it effectively.

## Types of algorithm

- **Simple recursive** algorithms solve the base cases directly, recur with a simpler subproblem, and do some extra work to turn that solution into the answer.
- **Backtracking** algorithms are based on a **depth-first recursive search**: try a choice, and if it fails, back up and try another.
- **Divide and conquer** algorithms divide the problem into smaller subproblems of the same type, solve them recursively, and combine the results; traditionally they contain **two or more recursive calls**.
- **Dynamic programming** algorithms **remember past results** and use them to find new results; they are generally used for **optimization problems** whose subproblems overlap, unlike divide and conquer.
- **Greedy** algorithms take the best choice at each step, hoping for the best overall result. Counting out change with the largest note or coin first is always optimal for Naira and Kobo, but for some coin systems (the book's 15 krons example) greedy gives a solution that is not optimal.
- **Brute force** algorithms try all possibilities until a satisfactory solution is found; they often take exponential time and are improved with heuristics.
- **Randomized** algorithms use a random number at least once during the computation.

**Deterministic** algorithms give the same results by the same steps on a given input; **randomized** ones may vary from run to run. Their subclasses are **Monte Carlo** and **Las Vegas** algorithms; a Las Vegas algorithm always produces the same result on a given input.

Source: CSC_236_Introduction_to_Algorithm.pdf (CSC 236 course book), Unit 1 (Meaning, Importance and Types of Algorithms)
