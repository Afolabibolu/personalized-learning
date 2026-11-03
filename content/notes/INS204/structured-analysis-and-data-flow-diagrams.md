# Structured Analysis and Data Flow Diagrams

## Structured analysis

Every information system is a network of processes that **receive data (input), transform it (processing) and produce information (output)**. **Structured system analysis** is a systematic approach that describes this network with **standard graphical notation** rather than free-form narrative, so that clients, sponsors and programmers interpret it the same way. It sits inside the **analysis phase**, after requirements are gathered. It was developed from the late 1970s by **Tom DeMarco, Chris Gane, Trish Sarson and Edward Yourdon**, and its ideas reappear in UML and BPMN. Its principles include **graphical modelling**, **decomposition** and **redundancy elimination** (each fact captured once).

## Design approaches

- **Top-down** design starts with the whole system and breaks it into smaller parts.
- **Bottom-up** design builds small components first and combines them.
- **Modular** design divides a system into independent modules with clear interfaces.

**Decomposition** breaks a complex process into simpler sub-processes level by level. **Documentation** records processes (workflows, DFDs, rules), data (the **data dictionary**, entities and fields) and more, for analysts, developers and users. **CASE tools** draw diagrams, maintain the data dictionary and **automatically check balancing**.

## The four DFD symbols

A **data flow diagram (DFD)** models how data moves through a system. Every DFD uses exactly four symbols:

1. **External entity**: a person, organisation or external system that exchanges data with the system, such as a student or a bank.
2. **Process**: transforms input data into output data, named with an **action**, such as "Validate Registration".
3. **Data flow**: the movement of data, labelled with a meaningful name such as "Registration Form".
4. **Data store**: a logical repository of data, with a unique reference and name, such as "D1 Loan Records".

## Levels

The **context diagram** shows the **whole system as a single process** with its external entities and data flows. The next level decomposes that process into its **major functions**, and lower levels decompose each process further. Each child diagram must be **balanced** against its parent: **the inputs and outputs of a parent process must match those of its child diagram**.

## Rules

1. Every process needs **at least one input and one output**. A process with inputs but no output is a **black hole**; one with outputs but no input is a **miracle**.
2. Every data flow needs a clear **source and destination**.
3. **Do not connect an external entity directly to another external entity**,
4. **an external entity directly to a data store**,
5. **or one data store directly to another**: each needs a process between them.
6. Label data flows and data stores meaningfully.
7. Use action names for processes.
8. Maintain **balance** between parent and child diagrams.

Common errors are black holes, miracles, unlabelled flows, direct entity-to-store links and unbalanced levels.

Source: INS 204 Lecture 4 & 5 (Structured Analysis and DFDs)
