# Strings, Regular Expressions and Modules

## Strings

A **string** is a sequence of characters in single or double quotes. Text = "Python": text[0] is 'P', text[1:4] is **'yth'** and text[:3] is 'Pyt'. The common methods:

- lower() and upper() change case;
- strip() removes leading and trailing whitespace;
- "a,b,c".split(",") gives ['a', 'b', 'c'];
- ",".join(['a', 'b']) gives 'a,b';
- "cat".replace("c", "b") gives 'bat';
- "hello".find("e") gives 1.

"Python" in "I love Python" is True. Join pieces with + ("Hello" + " " + "World") or, for many strings, " ".join(words).

## Regular expressions

A **regular expression (regex)** is a pattern for matching text, used for searching, cleaning, validating and parsing, for example finding phone numbers or e-mail addresses. Python's **re** module provides it (import re). Write patterns as **raw strings**, r"\d{11}", so backslashes are not escapes.

| Symbol | Meaning |
| --- | --- |
| . | any character except newline ("c.t" matches cat and cot) |
| \d | a digit 0–9 |
| \w | a word character (letter, digit, underscore) |
| \s | whitespace |
| * | zero or more ("ca*t": ct, cat, caaat) |
| + | one or more |
| {n,m} | between n and m repetitions |

- **re.search()** returns the **first** match as a match object (or None): re.search(r"\d{11}", "Call me at 08103456789").group() gives 08103456789.
- **re.findall()** returns a **list of all** matches: \d+ in "The numbers are 123, 456, and 789." gives ['123', '456', '789'].
- **re.sub(pattern, repl, string)** replaces matches: "I like cats." becomes "I like dogs."

## Modules

A **module** is a Python file of functions, classes and variables that can be imported and reused. It promotes reuse and organises code. To make a **custom module**, write my_module.py (def add(a, b): return a + b), then in another file use:

- import my_module and then my_module.add(2, 3);
- from my_module import add;
- import my_module as mm.

**Built-in modules**:

- **math**: sqrt(16) = 4.0, pi, floor(4.7) = 4, ceil(4.3) = 5, pow(2, 3) = 8.0, fabs, sin and cos in radians, radians() and degrees(), factorial(5) = 120, gcd(48, 18) = 6, comb(5, 2) = 10 and perm(5, 2) = 20.
- **random**: random() gives a float from 0 to 1; randint(1, 6) simulates a die; uniform(), randrange(0, 10, 2) and choice(["Heads", "Tails"]).
- **datetime**: datetime.now(), date, time and **timedelta**, for example now + timedelta(days=10), or the days between two dates.

Source: CSC 103 Lecture 4 (2024): tuples, sets, dictionaries, strings, regex and modules; CSC 103 2023/24 examination
