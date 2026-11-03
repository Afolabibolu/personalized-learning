# Reading and Writing Files

## Opening a file

To work with a file, a program first **opens** it, which creates a **file object**. You can use the built-in `open()` or the `open()` method of a `pathlib.Path` object, giving a **mode** and an **encoding**:

```python
file = open("hello.txt", mode="r", encoding="utf-8")
```

The main **modes** are:

| Mode | Meaning |
| --- | --- |
| "r" | read; raises an error if the file cannot be opened |
| "w" | write; **overwrites all existing data** in the file |
| "a" | append; adds data **to the end** of the file |
| "rb", "wb", "ab" | the same three for **binary** files |

## The with statement

If a program crashes between opening and closing a file, the system resources used by the file can stay in use. To make sure they are cleaned up, open the file in a **with statement**:

```python
with open("hello.txt", mode="r", encoding="utf-8") as file:
    text = file.read()
```

The header starts with `with` and ends with a colon, and the file object is assigned to the name after `as`. When execution leaves the indented block, **the file is closed automatically, even if an exception is raised**.

## Reading

- `.read()` reads the whole file and returns it as **one string**; lines are separated by the newline character `\n`.
- `.readlines()` returns the lines one at a time, so a for loop can process **each line as a record**. Because `print()` adds its own newline, use `print(line, end="")` to avoid blank lines between them.

## Writing and appending

Opening a file in **"w"** mode and calling `.write()` replaces the file's contents. Opening it in **"a"** mode writes new data **to the end, leaving old data intact**; put `\n` at the start of the string so the text goes on a new line. `.writelines()` writes a **list of strings** at once, so each string should end with `\n`.

Each record in a simple data file, such as a book title, borrower name and date borrowed, is often written as **one line**, so the program can later read the lines back to display and count the records.

## Missing files

Reading a file that does not exist raises **FileNotFoundError**, from both `Path.open()` and the built-in `open()`. Opening a missing file in **write mode creates it**, as long as all the parent folders exist; if a parent folder is missing, `.open()` raises FileNotFoundError too. A program that stores records should handle the case where the file does not yet exist, for example by checking `path.exists()` first.

Source: Python Basics (Real Python, 4th ed.), Chapter 12 (File Input and Output: Reading and Writing Files)
