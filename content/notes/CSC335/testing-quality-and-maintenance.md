# Software Testing, Quality and Maintenance

## The testing process

**Software testing** shows that a program does what it is meant to do and finds defects before it is used. A standard testing process runs:

1. design **test cases** (inputs and expected outputs);
2. prepare **test data**;
3. **run** the program with the test data;
4. compare the **test results** with the expected results;
5. write **test reports**.

**Testing levels:**

- **unit** testing of individual components;
- **integration** testing of components working together;
- **system** testing of the whole system.

**Three stages of system testing:**

1. **Development testing:** by the developers during development (unit, component and system testing).
2. **Release testing:** a separate team tests a complete version before it is released, checking it meets its requirements.
3. **User testing:** users test it in their own environment.
   - **Alpha testing:** with the developer.
   - **Beta testing:** a release given to a wider group.
   - **Acceptance testing:** the customer decides whether to accept the system.

**Verification** asks "are we building the product right?" (does it meet its specification?). **Validation** asks "are we building the right product?" (does it meet the user's needs?).

## Software quality assurance

**Quality assurance** defines the standards and processes that lead to quality software, and checks that they are followed through reviews, inspections and audits. Principles for achieving quality design include:

- **understand the requirements** fully before designing;
- **modularity** with high cohesion and low coupling;
- **abstraction and information hiding**;
- **simplicity**, keeping designs easy to understand;
- **reuse** of proven components;
- **review and verify** designs early;
- **design for change and testability**;
- follow **standards** and **document** decisions.

## Software maintenance

**Maintenance** covers the whole life of the system after delivery, and is often the largest share of its cost.

- **Corrective** maintenance fixes faults.
- **Adaptive** maintenance adapts the software to a new environment, such as an operating-system change.
- **Perfective** maintenance adds or improves functionality.
- **Preventive** maintenance restructures the code to prevent future problems.

**Lehman's laws** describe how systems evolve:

- a system in use must change continually or become less useful;
- its complexity grows unless work is done to reduce it.

**Factors affecting maintainability:**

1. **program structure and modularity** (cohesion and coupling);
2. **quality of documentation**;
3. **programming language and style**, including readable code and standards;
4. **age and size** of the system, with complexity growing over time;
5. **staff stability and skills**, since original developers may leave;
6. the **testing and configuration management** in place.

Source: general knowledge, following the CSC 335 course and the 2021/22 paper (Questions 1a, 3a, 4a and 5a); the lecture file lists testing and maintenance as life-cycle phases but does not detail them
