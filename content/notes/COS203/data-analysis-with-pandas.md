# Data Analysis with Pandas

## What is Pandas?

**Pandas** is the standard Python library for **tabular data**: rows and columns, like a spreadsheet or database table. The name comes from **panel data**, and it was created by **Wes McKinney in 2008**. It is imported as `import pandas as pd`.

Its two core structures are:

- a **Series**, a **single labelled column (1-D)**, such as scores indexed by name; and
- a **DataFrame**, a **full table (2-D)**: a collection of Series sharing the same index, like one spreadsheet sheet. Pandas adds the leftmost **index** (0, 1, 2, ...) automatically.

## Loading and inspecting

Most work starts with a file: `pd.read_csv("results.csv")`, `pd.read_excel()` (needs openpyxl) or `pd.read_json()`. Options include `sep=";"`, `index_col` and `na_values=["NIL", "-"]`. **Never analyse before you look**: `df.head()` shows the first 5 rows, `df.tail()` the last, `df.shape` gives (rows, columns), `df.dtypes` the column types, `df.info()` the types and non-null counts, and `df.describe()` summary statistics. A column you expect to be numeric that shows **object** contains text somewhere and needs cleaning.

## Selecting and filtering

`df["Name"]` gives one column (a Series); `df[["Name", "Exam"]]` gives several (note the double brackets). Rows are selected with **`.loc[]` by label** and **`.iloc[]` by integer position**. A common exam point: **`df.loc[0:2]` returns three rows** (it includes the end label), while **`df.iloc[0:2]` returns two** (normal Python slicing).

**Boolean indexing** is the most-used skill: `df[df["Exam"] >= 50]`. Combine conditions with **`&`, `|` and `~`, not and, or, not**, and **wrap each condition in parentheses**: `df[(df["Level"] == 200) & (df["Exam"] >= 50)]`.

## Columns and missing data

New columns are computed directly, as in `df["Total"] = df["CA"] + df["Exam"]`, or with `.apply(grade)`. Most methods **return a new DataFrame** rather than changing the original, so reassign the result. Missing values appear as **NaN**: `df.isnull().sum()` counts them, `dropna()` drops rows with them and `fillna(0)` or `fillna(mean)` fills them. Each choice has a cost (filling with the mean silently invents data), so always state your assumption. `drop_duplicates()` removes duplicate rows.

## Sorting, grouping and merging

`df.sort_values("Total", ascending=False)` sorts highest first, and `nlargest(3, "Total")` gives the top three. **`groupby()`** follows a **split → apply → combine** pattern: `df.groupby("Level")["Total"].mean()` gives the average per level, and `value_counts()` counts each grade. **`pd.merge(ca_df, exam_df, on="Matric", how="inner")`** joins two tables on a common key, like a SQL join; "inner" keeps only keys present in both.

Source: Working with External Libraries.pdf (lesson note) (Parts 3 and 4: Introduction to Pandas; Data Manipulation with DataFrames)
