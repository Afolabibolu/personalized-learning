# Data Visualisation, GUI Programming and Algorithms

## Data visualisation

Visualisation **simplifies complex data**, **reveals trends, patterns and outliers** and supports decisions. The libraries:

- **Matplotlib** is the foundation for static plots;
- **Seaborn**, built on it, gives statistical graphics;
- **Plotly** is interactive;
- **pandas** plots straight from DataFrames.

```python
import matplotlib.pyplot as plt
plt.plot(months, sales)
plt.title("Sales Trend"); plt.xlabel("Month"); plt.ylabel("Sales")
plt.grid(True)
plt.show()
```

The chart functions:

- plt.bar() for bar charts;
- plt.scatter() for scatter plots;
- plt.pie(sizes, labels=..., autopct='%1.1f%%', explode=...) for pie charts;
- label= with plt.legend() for several lines;
- **plt.subplots(2, 2)** for several charts in one figure.

**pandas**: import pandas as pd and df = pd.DataFrame(data). df.head() and df.tail() show rows; select with df['Category'] and filter with df[df['Sales'] > 1000]. Add a column with df['Bonus'] = df['Sales'] * 0.1, drop with drop(), and group with groupby(). Data comes in with **pd.read_excel()** and goes out with **df.to_excel()**; **pd.ExcelWriter** writes several sheets. df.plot(kind='bar') plots.

## GUI programming with Tkinter

A **GUI** lets users interact visually, through buttons and windows. **Tkinter** is **built into Python**, beginner-friendly and cross-platform; PyQt and Kivy are third-party alternatives.

```python
import tkinter as tk
root = tk.Tk()
root.title("Hello World")
root.geometry("400x300")
tk.Label(root, text="Hello, World!").pack()
tk.Button(root, text="Close", command=root.destroy).pack()
root.mainloop()
```

- tk.Tk() creates the main window, title() sets its title and geometry() its size.
- **mainloop()** starts the event loop.
- **Widgets**: Label, Button, Entry (one-line input) and Text (multi-line).
- **Event handling** links actions to functions through **command=**, and label.config(text=...) updates a widget.
- **Layout**: **pack()** stacks widgets, **grid(row, column)** places them in a grid and **place()** uses coordinates.
- Using root.destroy as the Close button's command is from general knowledge; the slides' Close button only prints "Bye!".

## Sorting and searching

**Algorithm analysis** judges efficiency in **time and space**.

- **Selection sort** repeatedly finds the smallest element of the unsorted part and swaps it to the front.
- **Merge sort** merges sorted partitions of sizes 1, 2, 4, 8 and so on until one partition covers the list.
- Others are insertion, bubble, heap, quick and shell sort.

**Linear search** checks each element in turn and works on any list. **Binary search** needs a **sorted** list: it checks the middle element and halves the search area each time, so it is much faster on large data.

Source: CSC 103 Lecture 7: data visualisation; CSC 103 Lecture 8: GUI programming; sorting, searching and algorithm analysis; CSC 103 2023/24 examination; General knowledge of COS 103 for root.destroy
