# Loops

## for loops

A **for** loop runs its block once for each item in a sequence, such as a list, tuple, string or **range**.

```python
total = 0
for num in range(1, 6):
    total += num        # total is 15
```

**range(start, stop, step)** stops before stop: range(3) gives 0, 1, 2 and range(1, 10, 3) gives **1, 4, 7**. range(1, 2, 3) gives just 1. for loops suit cases where the **number of iterations is known**. A pattern loop: for i in range(1, 5): print("*" * i).

## while loops

A **while** loop repeats **as long as a condition is True**, so it suits indefinite repetition: waiting for valid input, reading to the end of a file, or a game loop that runs until the player enters "quit". The loop variable must be initialised and updated:

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

If the condition never becomes False (while True:), the result is an **infinite loop**. Avoid it by making the condition eventually False or by using break.

## Controlling loops

- **break** ends the loop at once. In for attempt in range(3): with a correct password, break stops asking.
- **continue** skips the rest of this iteration and moves on: for num in range(5), skipping 2, prints 0, 1, 3, 4.
- A loop's **else** block runs after the loop finishes **unless a break occurred**:

```python
i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print(0)
```

This prints 0, 1, 2. Because break ran, the else is skipped.

## Nested loops

In a **nested loop** the inner loop runs completely for each iteration of the outer loop. Nested loops are used for tables, grids and patterns. for i in range(1, 4): for j in range(1, 4): print(f"{i} * {j} = {i * j}") prints a 3 × 3 multiplication table, and three nested loops over 2, 2 and 2 values run the innermost body 2 × 2 × 2 = 8 times.

**Combining loops and conditions**: sum only positive inputs with for i in range(3), using continue when not user_input.isdigit() or int(user_input) <= 0.

**Pitfalls**: deep nesting (break logic into functions) and infinite loops. Use meaningful names and comments.

Source: CSC 103 Lecture 2 (2024): elements of Python, selection and iteration; CSC 103 2023/24 examination
