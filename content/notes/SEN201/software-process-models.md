# Software Processes and Process Models

## Software processes

A **software process** is a sequence of activities that leads to a software product. Four activities are common to all processes:

1. **Software specification**: defining the software and the constraints on its operation.
2. **Software development**: designing and programming it.
3. **Software validation**: checking that it does what the customer requires.
4. **Software evolution**: modifying it as requirements change.

A **software process model** is a simplified representation of a process from a particular perspective. Models are not mutually exclusive and are often combined for large systems.

## The waterfall model

The **waterfall model**, the first published model, is **plan-driven**: its phases follow in sequence, and **each phase must finish (be "signed off") before the next starts**:

1. Requirements analysis and definition
2. System and software design
3. Implementation and unit testing
4. Integration and system testing
5. Operation and maintenance, often the longest phase

It is simple, structured and visible to managers, but **inflexible to requirement changes**, so it suits systems whose requirements are well understood and stable. **Formal system development**, which refines a mathematical specification into a program, is a variant.

## Incremental and reuse-oriented approaches

**Incremental development** builds an initial implementation, shows it to users and evolves it through versions; it is a fundamental part of agile approaches and is better than waterfall for most business, e-commerce and personal systems. Early increments carry the most important functions, and changes cost less.

**Reuse-oriented software engineering** integrates existing components. Its stages are **component analysis, requirements modification, system design with reuse, and development and integration**. Components may be **web services**, **object collections** integrated with a framework such as .NET or J2EE, or **stand-alone systems** configured for use. It reduces cost and risk and speeds delivery, but requirements may be compromised.

## Coping with change

- A **prototype** is an initial version used to demonstrate concepts and try out designs, helping requirements elicitation and validation and user interface design. Its stages are: **establish objectives, define functionality, develop, evaluate**.
- **Incremental delivery** deploys some increments for real use: customers gain value early and the most important services get the most testing, though common facilities are hard to identify and it can conflict with procurement models.
- **Boehm's spiral model** (1988) is **risk-driven**: the process is a spiral, and each loop has four sectors: **objective setting, risk assessment and reduction, development and validation, and planning**. Its main difference from other models is its **explicit recognition of risk**.

Source: SEN 201 Lecture Notes.docx, Software Lifecycle and Process Models
