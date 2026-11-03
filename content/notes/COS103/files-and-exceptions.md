# Files and Exception Handling

## File handling

File handling stores and retrieves data, logs activity and processes large data sets. File types include text (.txt), Excel (.xls, .xlsx, .csv) and binary files such as images.

- **open()** opens a file and **close()** closes it.
- **read()** reads the whole file, **readline()** one line, and **readlines()** gives a list of lines.
- **write()** and **writelines()** write.

**Modes**:

- **"r"**: read, the default;
- **"w"**: write, which creates or **overwrites** the file;
- **"a"**: **append** to the end;
- **"x"**: exclusive creation;
- **"r+"**: read and write.

The **with** statement is recommended because it **closes the file automatically**:

```python
with open("example.txt", "r") as file:
    content = file.read()
```

For **Excel**, **openpyxl** reads and writes .xlsx (load_workbook, Workbook, sheet["A1"].value, sheet.append(row), workbook.save()), and pandas, xlrd and xlsxwriter also help. For **images**, **Pillow** opens images (Image.open), and can resize((150, 150)), crop((left, top, right, bottom)), rotate(45) and convert("L") to greyscale. OpenCV is for advanced work.

## Errors

- **Syntax errors** break Python's rules, such as print "Hello World" without brackets in Python 3. Python detects them before running.
- **Runtime errors (exceptions)** happen during execution and can crash the program, as with division by zero or a missing file.
- **Logical errors** run but give wrong results. product = 0 then product *= i always stays 0.

**Common exceptions**: ZeroDivisionError, FileNotFoundError, IndexError, KeyError, ValueError, TypeError, AttributeError (e.g. calling append on an int) and ImportError/ModuleNotFoundError.

## Handling exceptions

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(result)
finally:
    print("Goodbye!")
```

- One except can catch several types: except (ValueError, ZeroDivisionError).
- Multiple except clauses are checked **top down**; if none matches, the exception is unhandled and the program crashes.
- **else** runs only if no exception occurred; **finally** always runs and is used for clean-up.
- **raise** creates your own exception: raise ValueError("Age cannot be negative!"), caught with except ValueError as err.
- Wrap each input in its own try block to tell the user which input was wrong.

Source: CSC 103 Lecture 5 (2024): file handling; CSC 103 Lecture 6 (2024): error and exception handling; CSC 103 2023/24 examination
