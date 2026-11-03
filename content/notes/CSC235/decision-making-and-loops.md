# Decision Making and Loops

## Decision making

Decision-making structures need the programmer to specify **one or more conditions** to be evaluated, a statement to run if a condition is true, and optionally another if it is false.

1. **if statement**: a Boolean expression followed by one or more statements.
2. **if...else statement**: an if followed by an optional else, which runs when the expression is false.
3. **Nested if**: an if or else if inside another.
4. **switch statement**: tests a variable for equality against a list of values.
5. **Nested switch**: a switch inside another switch.

The **conditional operator ? :** can replace if...else: `Exp1 ? Exp2 : Exp3`. Exp1 is evaluated; if it is true, Exp2 is evaluated and becomes the value of the whole expression, otherwise Exp3. So with x = 20 and y = 10, `x > y ? "yes" : "no"` gives "yes".

## Loops

Statements normally run in sequence, but a **loop** executes a statement or group of statements several times.

- **while loop**: repeats while a condition is true; it **tests the condition before** running the body.
- **for loop**: runs a sequence of statements many times and abbreviates the code that manages the loop variable.
- **do...while loop**: like while, but it **tests the condition at the end** of the body, so the body runs at least once.
- **Nested loops**: one loop inside another.

A **for loop** has three parts, `for (initialization; condition; iterator)`:

1. The **initialization** runs first and **only once**; the loop variable is usually declared and initialised here.
2. The **condition**, a Boolean expression, is evaluated.
3. If it is true, the body runs, then the **iterator** (which usually changes the loop variable) runs, and the condition is tested again.
4. When the condition is false, the loop ends.

`for (int i = 0; i <= 10; i = i + 2)` prints the even numbers from 0 to 10.

## Loop control

- **break** ends the loop or switch and moves execution to the statement just after it.
- **continue** skips the rest of the body and retests the condition.

A loop whose condition never becomes false is an **infinite loop**. Since none of the three parts of a for loop is required, `for (;;)` is commonly used to signify one; a missing condition is assumed to be true.

Source: Introduction to C# Programming Language, weeks 10-12 slides, Decision Making and Loops
