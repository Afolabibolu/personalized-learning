# Algorithms and Heuristics

## Solving computing problems

A **computing problem** is a task a computer can solve, such as sorting, finding routes or scheduling. It goes through these stages:

- **problem definition**;
- **analysis** of inputs, outputs, constraints and relationships;
- **design** of a step-by-step plan;
- **implementation** in code;
- **testing and debugging**;
- **evaluation** of efficiency and effectiveness.

## Algorithms

An **algorithm** is a **finite set of step-by-step instructions** that solves a problem and produces output after a finite number of steps. A good algorithm has:

- **finiteness**: it terminates;
- **definiteness**: each step is precise and unambiguous;
- **input**: zero or more well-defined inputs;
- **output**: at least one;
- **effectiveness**: each step is simple enough to do exactly.

It must be repeatable and predictable, and executable by different "computers", people or machines. One algorithm can be written in several ways, and several algorithms may solve the same problem. It is represented as **pseudocode** or a **flowchart**.

## Heuristics

A **heuristic** is a **rule of thumb or shortcut**: often good enough, but not guaranteed. Choosing the restaurant with the most cars outside usually works, but not always. Heuristics:

- come from experience and intuition;
- suit complex or ill-defined problems;
- give approximate answers;
- cut computation time or the search space.

The methods:

- **Greedy approach**: take the best immediate option at each step, hoping local choices give a global optimum. To buy as many snacks as possible with ₦1000, keep picking the cheapest: Sweet ₦100, Biscuit ₦200, Bread ₦300, Cake ₦400. That is **4 snacks**, with no money left for Juice. For a 6 kg bag with fractions allowed, take the highest value per kilogram first: Bronze (3.5 per kg), Silver (3), then 1 kg of Gold. That gives a **total value of 18**.
- **Trial and error**: try options and use failures as feedback, "keep what works". Examples are adjusting a jollof rice recipe, or restoring a lost Internet connection by checking the signal, data, bundle, airplane mode and so on.
- **Rule-based systems**: decisions from predefined **IF–THEN** rules drawn from human expertise, as in expert systems. IF temperature > 37.5°C THEN show "You may have a fever"; IF score ≥ 70 THEN grade "A".
- **Means–ends analysis**: compare the current state with the goal and take actions that **reduce the gap**, for example moving from a 45% average to the 60% goal by attending classes and practising. (One slide's list wrongly describes it as applying expert knowledge; that describes rule-based systems.)
- **Analogy-based reasoning**: solve a new problem like a similar solved one, such as learning Google Docs after Word, or building an e-learning app by studying existing ones.

Source: COS 102 Lecture 7 (algorithms and heuristics)
