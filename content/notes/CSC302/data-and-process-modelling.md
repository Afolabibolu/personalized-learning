# Data and Process Modelling

## Data flow diagrams

A **data flow diagram (DFD)** shows how data moves through an information system. It does not show program logic or processing steps. In the Gane and Sarson notation it uses four symbols:

- **Process** (a rounded rectangle): receives input data and produces output that has a different content, form or both. It is named with a verb and noun, such as "Assign advisor".
- **Data flow** (an arrow): a path for data moving between processes, stores and entities, named with a noun.
- **Data store** (a flat, open-ended rectangle): data kept for later use, such as a class roster.
- **External entity** (a square): a person, department or system outside the system that supplies or receives data, also called a source or sink.

## Levels of DFD

- The **context diagram** is the top level. It shows the entire system as a single process (numbered 0) with its external entities and the data flows between them; it has no data stores.
- The **level 0 diagram** expands process 0 into the major processes, data flows and data stores, showing the system in more detail. Creating it is called **decomposing** or **exploding** the context diagram.
- Lower levels expand each process further, producing **leveled** DFDs. A diagram must be **balanced**: the inputs and outputs of a parent process match those of its child diagram.

## DFD rules and common errors

- A process must have at least one input and one output.
- A **black hole** is a process with inputs but no outputs; a **gray hole** is a process whose outputs cannot be produced from its inputs; **spontaneous generation** (a miracle) is a process with outputs but no inputs.
- Data cannot flow directly between two entities, between two data stores, or between an entity and a data store. It must pass through a process.
- Every data store needs at least one data flow in and one out.

## Data dictionary

The **data dictionary** (data repository) is a central store of facts about the system's data. It documents:

- each **data element** (name, type, length, values);
- **data flows**;
- **data stores**;
- **processes**;
- **external entities**;
- **records** (groups of data elements).

## Process descriptions

A process at its lowest level, a **functional primitive**, is documented with:

- **structured English**: plain sentences using a limited vocabulary of sequence, selection (IF … THEN … ELSE) and repetition;
- **decision tables**: all combinations of conditions with the action for each;
- **decision trees**: the same logic drawn as branching lines.

## Logical and physical models

A **logical model** shows what the system must do; a **physical model** shows how it will be built. The logical model usually comes first.

Source: general knowledge, following the CSC 302 past papers (2020/21 Question 1(e), the 2020/21 test and the 2021/22 and 2024/25 papers); the lecture slides cover requirements modelling up to Chapter 4 and preview logical modelling only
