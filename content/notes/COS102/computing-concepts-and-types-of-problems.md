# Computing Concepts and Types of Problems

## What a computing system is

A **computing system** is computer hardware, software and data, which interact to solve problems. **Hardware** is the physical elements of the system. **Software** is the programs that provide the instructions a computer executes. **Data** are basic values or facts, and **information** is data that has been organised or processed in a useful manner.

A computing system is like an onion, made up of layers, each with its own role:

- **Information:** how data is represented, using binary digits 1 and 0.
- **Hardware:** gates, circuits, the CPU and memory.
- **Programming:** software, the instructions that accomplish computations and manage data. Its goal is always to solve problems.
- **Operating systems:** such as Windows, Mac OS or Linux, which manage the computer's resources.
- **Applications:** programs that solve specific real-world problems.
- **Communications:** networks that let computers share information and resources.

A computer does only very simple tasks, but it does them so fast that many simple tasks combine into complicated ones. **Abstraction**, a mental model that removes complex details, lets us study one layer at a time.

## Identifying a problem

A problem is a gap between the situation you have and the situation you want. Before solving it you must identify it: state what is given (the data), what is wanted (the result) and any conditions or limits. A vague problem statement leads to a solution for the wrong problem.

## Routine and non-routine problems

- A **routine problem** is one you have met before, with a known method: computing a student's average score, sorting a list, converting a number to another base. You recognise it and apply the method.
- A **non-routine problem** has no ready-made method. It needs analysis, creativity and often several attempts: designing a timetable with many constraints, or finding why a system fails only sometimes.

## Solvable and unsolvable problems

Some problems cannot be solved by any computer program. The **halting problem** asks: given a program and an input to it, determine whether the program will eventually stop with that input. Running the program is no answer, because if it does not stop you cannot tell how long to wait. Turing showed that no program can answer this for every program and input. Assuming such a program exists leads to a contradiction, so the problem is **unsolvable**. By the Church–Turing thesis, anything intuitively computable can be computed by a Turing machine, so a problem no Turing machine can solve is unsolvable.

Source: Computer Science Illuminated, 7th edition (2020), Chapters 1 and 18 (the reference textbook in the course folder); problem identification and routine and non-routine problems from general knowledge, following the NUC CCMAS outline for COS 102
