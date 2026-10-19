# Problem Solving and Search

## What the topic is

Many intelligent-system problems can be stated as a **search problem**: find a sequence of actions that leads from where the agent starts to where it wants to be. Once the problem is stated precisely, search algorithms explore the possible states to find a solution.

## Subtopics

**Components of a search problem.**
- **Initial state:** the starting point in the problem space, the configuration the agent begins from. Example: a robot at (0,0) on a 2D grid.
- **Goal state:** the desired end condition. It can be a single state or a set of acceptable states. Example: the robot reaches (4,4).
- **State space:** the set of all states reachable from the initial state through actions, the "universe" in which search happens. Example: every (x, y) position on a 5×5 grid.
- **Successor function:** given a state, the actions available and the states they lead to. Example: move up, down, left or right while avoiding obstacles.
- **Path cost:** the cost of a sequence of actions. Example: each move costs 1 unit.

**Uninformed and informed search.** Uninformed search uses only the problem definition. Informed search also uses a **heuristic**, an estimate of how far a state is from the goal.

**Breadth-first search (BFS).** BFS explores all nodes at the current depth before going deeper. It is complete, and optimal when every step costs 1. Its time and space complexity is O(b^d), where b is the branching factor and d the depth.

**Depth-first search (DFS).** DFS goes as deep as possible along one branch before backtracking. In the lecture's example, a binary tree with the goal at depth 3, BFS finds the shortest path but uses more memory. DFS may reach the goal quickly but is not guaranteed to find the shortest path.

**Case study: warehouse robot navigation.** An autonomous robot must fetch items from shelves and deliver them to packing stations.
- **Initial state:** the charging station (0,0).
- **Goal state:** the target shelf (x, y).
- **State space:** the grid of navigable paths between shelves.
- **Successor function:** up, down, left or right, avoiding obstacles.
- **Path cost:** 1 unit per move.

**Designing a heuristic.** The class activity asks for a heuristic that estimates the distance from the robot's location to the goal and accounts for blocked paths or detours. Groups then compare it with straight-line distance on sample maps.

## Key terms

- **Branching factor (b):** the number of successors per state.
- **Heuristic:** an informed estimate of the remaining distance to the goal.

## Exam-style point

To formulate any search problem, name all five components. For the warehouse robot: start at (0,0), the goal is the shelf, the state space is the navigable grid, the moves avoid obstacles, and each step costs 1. Then choose BFS if the shortest path matters and memory allows.

Source: Lecture 2
