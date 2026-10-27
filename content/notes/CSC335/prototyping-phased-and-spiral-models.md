# Prototyping, Phased and Spiral Models

## The prototype model

**Software prototyping** builds a **working model with limited functionality** that shows what the product will do, though it may not hold the real logic. It helps the team understand customer requirements early, get valuable feedback, and let users evaluate proposals before implementation. It allows repeated investigation of requirements or design, and reduces risk and uncertainty.

**Advantages:**

1. more user involvement before implementation;
2. users understand the system better from a working model;
3. less time and cost, since defects are found earlier;
4. quicker feedback and better solutions;
5. missing functionality is easy to identify;
6. confusing or difficult functions are identified.

**Disadvantages:**

1. risk of insufficient requirement analysis from relying too much on the prototype;
2. users may confuse the prototype with the real system;
3. scope may grow beyond the original plan;
4. developers may reuse prototypes that are not technically suitable;
5. prototyping effort may be too much if not monitored.

## Phased development: increments and iterations

**Phased development** gives a **shorter cycle time** by delivering the system in pieces, so customers have some functionality while the rest is built. Two systems run in parallel: the **production system** (release n, in use) and the **development system** (release n + 1).

- **Incremental development** starts with a small functional subsystem and adds functionality with each release.
- **Iterative development** starts with the full system and changes the functionality of each subsystem with each release.

It lets training and markets start early and lets frequent releases fix problems quickly.

## The spiral model

The **spiral model**, first described by **Barry Boehm in 1986**, is a **risk-driven** process model introduced to deal with the shortcomings of the waterfall. It combines iterative development with the controlled aspects of the waterfall, with a very high emphasis on **risk analysis**. Each loop of the spiral is a **phase**, and the number of loops varies with the project's risks, as decided by the project manager.

The four phases of each spiral are:

1. **Identification:** gathering business, then system, subsystem and unit requirements.
2. **Design:** conceptual, architectural, logical and physical design.
3. **Construct or build:** a proof of concept at first, then versioned builds sent for feedback.
4. **Evaluation and risk analysis:** identifying, estimating and monitoring technical and management risks, such as schedule slippage and cost overrun.

**When to use it:** budget constraints with important risk evaluation, medium- to high-risk projects, long-term commitments, unclear or complex requirements, a new product line released in phases, and significant expected changes.

- **Advantages:** changing requirements are accommodated, prototypes are used extensively, requirements are captured more accurately, users see the system early, and risky parts are developed first.
- **Disadvantages:** it needs very strict management, and there is a risk of running the spiral indefinitely.

Source: week 3 and 4 -Software Process.pdf (CSC 335 lecture slides, Software Process Models) (prototype model, phased development: increments and iterations, spiral model: design, application, advantages and disadvantages)
