# Fuzzy Logic Systems

## What the topic is

Fuzzy logic mimics human reasoning by handling partial truth. Computers normally need precise values, but people reason well with vague, linguistic terms such as "hot" or "young". Fuzzy logic bridges the two by letting a statement be true to a degree between 0 and 1, so systems can handle uncertainty and vagueness.

## Subtopics

**Classical versus fuzzy logic.** In classical logic a truth value is 0 or 1 ("water is hot" = true), giving binary decisions. In fuzzy logic it can be any value between 0 and 1 ("water is 0.7 hot"), which handles uncertainty and vagueness.

**Fuzzy sets and membership.** In a fuzzy set, an element with membership 1 belongs unconditionally and an element with membership 0 is outside it. Everything in between belongs partially. Experts define the shape of the membership function, usually triangular or trapezoidal. The lecture's example: cold = max(1 − x/20, 0) and hot = max((x − 20)/20, 0), for temperature x from 0 to 40.

**Fuzzy system architecture.** Fuzzification turns crisp inputs into membership degrees. A rule base and inference engine apply IF-THEN rules. Defuzzification turns the fuzzy result back into a crisp output.

**Mamdani inference.** For an air conditioner, with rules IF temperature is cold THEN fan speed is low and IF temperature is hot THEN fan speed is high:
1. Apply the rules.
2. Combine the outputs with min/max operators.
3. Defuzzify with the centroid method.

In the lecture's simplified code, a crisp 25°C gives hot_degree = min((25 − 20)/20, 1) = 0.25, and the output speed is a weighted combination of the low and high speeds.

**Case studies.**
- **Intelligent washing machine:** inputs are dirtiness and load size; outputs are wash time and water level. Example rule: IF dirtiness is high AND load is large THEN long wash.
- **Smart office air conditioning:** inputs are temperature, time and occupancy; the output is fan speed; the goal is energy efficiency.
- **Autonomous vehicle speed:** inputs are traffic density and road condition; the output is speed. Example rule: IF traffic is heavy OR road is slippery THEN slow speed.
- **Car braking (class activity):** IF speed is high AND obstacle is near THEN brake hard.

**Uses.** Search engines, chip design and databases; dryers, refrigerators, shower systems, TVs and camcorders. Fuzzy logic is flexible with uncertainty and ideal for modelling human decisions. A practical challenge is defining good rules.

## Key terms

- **Membership function:** maps an input to a degree of membership in [0, 1].
- **Defuzzification:** turns a fuzzy output into one crisp value (centroid method).

## Exam-style point

For a calculation, substitute the crisp input into each membership function and clamp the result to [0, 1]. With cold = max(1 − x/20, 0), 10°C is cold to degree 1 − 10/20 = 0.5.

Source: Lecture 5
