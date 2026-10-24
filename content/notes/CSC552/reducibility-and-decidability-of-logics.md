# Reducibility and Decidability of Logics

## Reducibility

A **reduction** converts problem A into problem B so that a solution to B can be used to solve A. Everyday examples:

- Finding your way around a new city reduces to getting a map.
- Travelling from Ibadan to Abuja reduces to buying a plane ticket, which reduces to earning the money.

When A reduces to B, A cannot be harder than B. If B is decidable, so is A. Equivalently, **if A is undecidable and reduces to B, then B is undecidable**.

## Undecidable problems

- **The halting problem, HALTTM:** does a TM halt on a given input? Suppose a TM R decides it. Then build S to decide ATM: ask R whether M halts on w, reject if not, and otherwise simulate safely. But ATM is undecidable, so R cannot exist.
- **ETM:** is a TM's language empty? Modify M to reject every input except w. Its language is non-empty exactly when M accepts w, so an ETM decider would decide ATM.

## Computation histories and LBAs

A **computation history** is the sequence of configurations C1, …, Cl a machine passes through. It is accepting if C1 is the start configuration, each Ci+1 legally follows Ci, and Cl contains qaccept.

A **linear bounded automaton (LBA)** is a TM whose head may not leave the part of the tape holding the input, so its memory is linear in n. An LBA with q states and g tape symbols has exactly q·n·gⁿ configurations on a tape of length n. That makes **ALBA decidable**: if it has not halted within q·n·gⁿ steps, it must be looping. **ELBA is undecidable**: build an LBA B that accepts only accepting computation histories of M on w. Then L(B) is empty exactly when M does not accept w.

## The Post Correspondence Problem

The PCP gives a collection of dominos, each with a string on top and a string below. A **match** is a list of dominos, with repetitions allowed, whose top string equals its bottom string. The PCP asks whether a collection has a match. It is **undecidable**, proved by reducing ATM through the modified PCP so that any match spells out an accepting computation history.

## Decidability of logics

A logic is decidable if an algorithm always terminates with "true" or "false" for any well-formed formula. **Propositional logic** (AND, OR, NOT) is decidable, because a truth table checks every assignment. More expressive logics, such as higher-order and some modal logics, may be undecidable.

## Non-monotonicity

In a **non-monotonic** logic, new information can retract an earlier conclusion. Classical logic never retracts. In **default logic**, from "if Bird(x), default to Fly(x)" and Bird(Tweety), we conclude Fly(Tweety). Learning ¬Fly(Tweety) later retracts it.

Decidability and non-monotonicity are largely orthogonal. Some decidable logics are monotonic, such as propositional logic. Some are non-monotonic, such as certain default logics. Some non-monotonic logics are undecidable.

Source: DLC CSC 552 Theory of Computation.pdf, Study Sessions 5 and 6
