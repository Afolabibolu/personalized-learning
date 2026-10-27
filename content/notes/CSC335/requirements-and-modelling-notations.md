# Requirements Engineering and Modelling Notations

## Requirements engineering

**Requirements engineering** is the process of finding out what a system must do and the constraints on it. Its activities are:

1. **feasibility study:** whether the system is worth building;
2. **elicitation and analysis:** discovering requirements from stakeholders through interviews, observation, scenarios and prototypes;
3. **specification:** writing the requirements down;
4. **validation:** checking that they are complete, consistent, realistic and what the customer wants.

Requirements change over time, so they are also **managed**.

## Functional and non-functional requirements

- **Functional requirements** state what the system should do: the services it provides and how it reacts to inputs. For example, "a member can search the library catalogue by title".
- **Non-functional requirements** are constraints on the system as a whole:
  - performance (response time);
  - reliability and availability;
  - security;
  - usability;
  - portability;
  - legal or organisational constraints.

  They are often more critical, since failing one can make the whole system unusable.

The **software requirements specification (SRS)** documents both, for customers, managers and developers. User requirements are written in natural language and diagrams, and system requirements are more detailed.

## Modelling notations

Models represent a system from different perspectives:

- **use case diagrams:** actors and the things the system does for them;
- **class diagrams:** classes, attributes, operations and relationships;
- **sequence diagrams:** objects exchanging messages over time;
- **activity diagrams:** the flow of activities in a process;
- **state (state machine) diagrams:** how an object responds to events;
- **data flow diagrams:** processes, data flows, data stores and external entities.

Most of these belong to the **UML (Unified Modeling Language)**. **Formal notations** (such as Z) are used for precise specifications.

## Use case diagrams

A **use case diagram** shows **actors** (stick figures for users or other systems) and **use cases** (ovals for system functions) within a system boundary.

- An **include** relationship means one use case always uses another.
- An **extend** relationship means a use case optionally adds behaviour to another.

**A simple library system:**

- A **patron** searches for items, borrows items and returns items.
- Borrowing **includes** checking membership.
- Paying a fine **extends** returning an item when it is overdue.
- A **librarian** manages the catalogue and registers members.

Each use case can then be described as a scenario: the normal flow, alternatives and exceptions. Sequence diagrams show the messages between the patron, the catalogue and the loan records.

Source: general knowledge, following the CSC 335 course and the 2021/22 paper (Questions 5b and 5c); the course's lecture file covers process models only
