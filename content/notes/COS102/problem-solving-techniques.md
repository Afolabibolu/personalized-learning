# Problem-Solving Techniques

The CCMAS outline for COS 102 lists techniques for finding a solution. None works for every problem; good problem solvers combine them.

## Simplifying the problem

- **Abstraction:** model the problem with only the details that matter and ignore the rest. A route-finding program needs roads and distances, not the colour of the buildings.
- **Analogy:** use the solution to a similar problem you have already solved. Finding the oldest person in a list is the same problem as finding the largest number.
- **Reduction:** transform the problem into one that already has a known solution, for example turning "is this name in the list?" into a search problem.
- **Divide and conquer:** break a large problem into smaller subproblems, solve each, and combine the results.

## Generating ideas

- **Brainstorming:** a group lists as many ideas as possible without judging them, then evaluates them afterwards.
- **Lateral thinking:** approach the problem from an unexpected angle instead of step-by-step logic, questioning assumptions about it. (The outline lists this as "literal thinking".)
- **Method of focal objects:** combine features of unrelated, randomly chosen objects with the object being improved, to produce new ideas.
- **Morphological analysis:** list the problem's main attributes and the options for each, then examine combinations systematically. A phone could be studied by screen, battery and material.

## Testing and searching

- **Trial and error:** try possible solutions one after another until one works. It suits problems with few options, but it is slow when there are many.
- **Hypothesis testing:** propose a likely explanation or solution, then test it and keep or reject it based on the result. This is common in debugging.
- **Means-end analysis:** compare the current state with the goal, pick an action that reduces the difference, and repeat. Large goals are split into subgoals.
- **Research:** study existing ideas, documentation and solutions before inventing your own.

## Finding causes and proving solutions

- **Root cause analysis:** look past the symptoms to the underlying cause, for example by asking "why?" repeatedly until the real cause appears. Fixing only a symptom lets the problem return.
- **Proof:** show by logical argument that a solution is correct for every case, not only for the cases tested.

## Choosing a technique

Routine problems usually need only analogy or a known method. Non-routine problems often start with brainstorming or lateral thinking to generate options, use abstraction and divide and conquer to make them manageable, and finish with testing or proof to confirm the answer.

Source: general knowledge, following the NUC CCMAS outline for COS 102 (the course folder's textbook does not cover these techniques)
