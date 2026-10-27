# Dependability, Critical Systems and Formal Methods

## Critical systems

**Critical systems** are systems whose failure can cause serious loss, so users must be able to trust them.

- **Safety-critical** failure may cause injury, death or environmental damage: a car air-bag controller, or a blood-sugar monitor and insulin pump.
- **Mission-critical** failure stops an important goal: a spacecraft's navigation.
- **Business-critical** failure costs a lot of money: a bank's accounting system.

For such systems **dependability** matters more than any other property.

## Dimensions of dependability

**Dependability** reflects how far users trust a system. Its four principal dimensions are:

1. **availability:** the probability that the system is up and able to deliver services when requested;
2. **reliability:** the probability that it delivers services as specified over a given time;
3. **safety:** its ability to operate without catastrophic failure that threatens people or the environment;
4. **security:** its ability to protect itself against accidental or deliberate intrusion.

Further dependability properties include:

- **repairability:** how quickly it can be repaired after failure;
- **maintainability:** how easily it can be adapted to new requirements;
- **survivability:** its ability to keep delivering services under attack;
- **error tolerance:** how well it avoids and tolerates user input errors.

Dependability also covers **resilience**.

## Achieving dependability

- **Fault avoidance:** development techniques that reduce mistakes.
- **Fault detection and removal:** verification and validation to find faults before use.
- **Fault tolerance:** detecting faults at run time and recovering, using **redundancy** (spare capacity) and **diversity** (different implementations of the same function).

Higher dependability costs much more to achieve.

## Formal methods

**Formal methods** use mathematical notations (such as Z, B or VDM) to **specify** a system precisely, and mathematical reasoning to **verify** that a design or program meets its specification, sometimes by **proof** or **model checking**.

Developers choose formal methods because they:

1. remove **ambiguity**, since a mathematical specification has one meaning;
2. reveal errors and omissions in **requirements early**, when they are cheapest to fix;
3. allow **proof** that the program meets its specification, raising confidence;
4. help meet **certification** standards for safety- and security-critical systems (railways, avionics, medical devices);
5. support automated analysis and testing from the specification.

Their costs are specialist skills, effort and limited scalability, so they are used mainly for critical components.

**Choosing a process for critical systems:** a system that monitors a patient's blood sugar, or a car's air bag during an accident, is safety-critical. It suits a **formal method** or a disciplined model such as the **V model**, while an interactive system with unclear requirements suits **prototyping**.

Source: general knowledge, following the CSC 335 course and the 2021/22 paper (Questions 1b, 1c, 2b and 4b); the lecture file covers process models only
