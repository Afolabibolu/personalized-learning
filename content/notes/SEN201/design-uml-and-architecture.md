# Software Design, UML and Architectural Design

## Design and implementation

A **software design** is a description of the **structure** of the software, the **data models** and structures, the **interfaces** between components and sometimes the **algorithms**. Design is a **creative activity**: identifying components and their relationships from the customer's requirements. **Implementation** converts a specification into an executable system; it always involves design and programming, which are interleaved in incremental development. The design activities are:

- **Architectural design**: the overall structure, principal components (sub-systems or modules), their relationships and distribution.
- **Interface design**: unambiguous interfaces between components, so a component can be used without knowing how it is implemented.
- **Component design**: how each component will operate.
- **Database design**: the system's data structures and their representation in a database.

## Object-oriented design and UML

An object-oriented system is made of **interacting objects** that keep their own **private local state** and provide operations on it. Such systems are **easier to change** than functional designs, because objects combine data and operations and can be understood and modified as stand-alone entities. Design proceeds by identifying the **object classes**. When using the **Unified Modelling Language (UML)**, you develop two kinds of design model:

1. **Structural models**, describing the **static structure** using object classes and their relationships, such as generalisation (inheritance), uses and composition.
2. **Dynamic models**, describing the **dynamic structure** and interactions between objects, such as sequences of service requests and state changes.

Interfaces must be specified so that objects and subsystems can be designed in parallel. The first stage of design is understanding the system's **context**: a **system context model** is a **structural** model of the other systems in the environment, and an **interaction model** is a **dynamic** model of how the system interacts with its environment as it is used.

## Architectural design

**Architectural design** is concerned with how a system should be organised and its overall structure; it is the first stage of design and links design with requirements engineering. Architecture matters because it affects **performance, robustness, distributability and maintainability**. Four fundamental architectural views, related through use cases or scenarios, are:

1. **Logical view**: the key abstractions as objects or classes.
2. **Process view**: the interacting processes at run time, useful for judging performance and availability.
3. **Development view**: how the software is broken into components for development teams.
4. **Physical view**: the hardware and how components are distributed across processors.

An ATM system is the notes' example of a simple architecture.

Source: SEN 201 Lecture Notes.docx, Software Design and Implementation; Object-Oriented Design using UML; Architectural Design
