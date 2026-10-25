# From Algorithm to Program

## Implementation

In the implementation phase, the algorithm (the general solution) is translated into a programming language, giving a concrete solution. An algorithm must be written before any coding. The CCMAS lab work for COS 102 uses any language, such as Visual Basic, Python or C; the examples here use Python.

## Assignment, input and output

```python
name = input("Enter your name: ")   # input returns text
score = int(input("Enter your score: "))  # convert text to a whole number
print("Hello", name)
```

`=` is assignment: the value on the right is stored in the variable on the left. `total = total + score` reads the old value of total, adds score, and stores the result back.

## Condition statements

```python
if score >= 70:
    print("A")
elif score >= 50:
    print("Pass")
else:
    print("Fail")
```

Only one branch runs. The second test is reached only if the first is false, so the order of conditions matters. Python uses indentation to group statements.

## Loops

There are two basic types of loop.

- A **count-controlled loop** repeats a process a specified number of times. It has three parts: **initialise** the loop control variable, **test** it, and **increment** it. Starting at 0 and testing `count < limit`, the loop runs limit times.

```python
count = 0
while count < 5:
    print(count)
    count = count + 1
```

- An **event-controlled loop** repeats until an event inside the loop occurs, such as reading a negative value. The event must be initialised, tested and updated.

```python
total = 0
value = int(input())
while value >= 0:
    total = total + value
    value = int(input())
```

A while loop is a **pretest loop**: the test comes first, so if it is false at the start the body never runs. If the update is left out, the condition never changes and the loop runs forever: an **infinite loop**.

## Testing and debugging

Test the program with normal values, boundary values (exactly 50 for a pass mark) and invalid input, and compare the results with the answers worked out by hand. **Syntax errors** break the language's rules and stop the program running. **Runtime errors** happen while it runs, such as dividing by zero. **Logic errors** give wrong answers without any error message and are found only by testing.

Source: Computer Science Illuminated, 7th edition (2020), Chapters 7.1 and 7.2 (implementation phase, loops); Python statements, testing and error types from general knowledge, following the NUC CCMAS outline for COS 102
