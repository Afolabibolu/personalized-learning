# Loops and Iteration

## Iteration

**Iteration (looping)** lets a block of code run **repeatedly** while a condition holds, or a fixed number of times. It is the **third fundamental control structure**, after sequence and selection. Loops avoid writing identical lines, process collections and arrays, and repeat a task until a condition changes.

## The for loop

Use a **for** loop when the **number of repetitions is known in advance**. Its syntax is `for (initialisation; condition; update) { body }`:

```java
int sum = 0;
for (int i = 1; i <= 10; i++) {
    sum += i;
}
// sum = 55
```

A loop can count down too: `for (int i = 5; i >= 1; i--)`. **Nested for loops**, a loop inside a loop, suit tables, grids and patterns, such as a 5 by 5 multiplication table where the inner loop prints a row and the outer loop moves to the next row.

## The while and do-while loops

Use a **while** loop when the number of repetitions is **not known in advance**. The condition is **checked before** each iteration, so the body may run **zero times**. For example, keep asking until a valid score (0 to 100) is entered:

```java
while (score < 0 || score > 100) {
    score = sc.nextInt();
}
```

Use a **do-while** loop when the body must run **at least once**, because the condition is **checked after** each iteration; a menu that always displays once and repeats until the user enters 0 is the classic example.

| Loop | When to use | Condition check | Minimum runs |
| --- | --- | --- | --- |
| for | Known number of repeats | Before body | 0 |
| while | Unknown repeats | Before body | 0 |
| do-while | Must run at least once | After body | 1 |

## Loop control

- **break** exits the loop **immediately**: a loop from 1 to 10 that breaks at 5 prints 1 2 3 4.
- **continue** **skips the rest of the current iteration** and jumps to the next: skipping even numbers prints 1 3 5 7 9.
- The **enhanced for (for-each)** loop cleanly iterates over arrays and lists: `for (int s : scores) System.out.println(s);`.

A loop whose condition never becomes false is an **infinite loop**; make sure the loop variable changes towards ending it.

A practical example is a score processor: a for loop reads five scores, adds each to a total, and tracks the highest and lowest, then computes the average with `(double) total / n`.

Source: cos201_weeks3to6.pdf (Week 6: Loops and Iteration); cos 201 L4.pdf (control statements) (looping and branching statements)
