# Python: Decisions and Loops

## Decisions

Sequencing alone cannot solve every problem, so **control structures** let a program choose and repeat. A **condition** evaluates to **True or False**, using relational operators (<, <=, ==, !=, >, >=) and the logical operators **and** (both true), **or** (at least one true) and **not**.

- **if**: the **if** keyword, a condition, a **colon**, then an **indented block** on a new line. The block runs only if the condition is true.
- **if...else**: else runs when the condition is false; the else is optional.
- **elif** (multiple decision): checks conditions in order and runs the **first** that is true.
- **nested if**: an if inside another. Avoid too many layers.

```python
score = int(input("Enter score: "))
if score >= 70:
    print("Grade point is 4")
elif score >= 60:
    print("Grade point is 3")
else:
    print("Grade point is 2 or below")
```

**Indentation groups code** in Python, so bad indentation gives wrong output or errors. if (y = 5) is wrong, because = assigns while == compares, and =< is not an operator. Code with braces, such as if (age = 16) Ellipsis, is not Python.

## Loops

A loop repeats a body. Its parts are: initialise the control, test it, execute the body and update the control.

- A **for** loop is a **definite (counting)** loop: for i in [0, 1, 2, 3]:, or with **range(start, stop, step)**. range(5) gives 0 to 4, range(1, 8) gives 1 to 7, range(0, 14, 3) gives 0, 3, 6, 9, 12 and range(8, 1, −1) counts down 8 to 2. The stop value is never reached.
- A **while** loop is **indefinite**: it runs while the condition is true, and the programmer must initialise and update the variable (i = 1; while i <= 5: print(i); i += 1). Python loops are **pre-test** loops: the body may run zero times.
- If the tested value never changes, the result is an **infinite loop**. A computer cannot detect every infinite loop; this is the **halting problem**.
- **break** leaves the loop at once. **continue** skips to the next iteration: for i in range(1, 6), skipping 3, prints 1, 2, 4, 5.
- Loops can be **nested**, for example for a multiplication table.

## Usability

Software that users cannot understand is useless. From **Jakob Nielsen**'s heuristics:

- keep users informed (**visibility**);
- **minimise memory load** (recognition rather than recall: show the valid input, e.g. "Enter age (0 – 114)");
- be **consistent**;
- give **feedback**;
- provide clearly marked exits;
- handle errors helpfully;
- **match the real world**;
- keep the design minimal.

Source: COS 102 Lecture 9 (control structures); COS 102 Lecture 10 (loops and usability)
