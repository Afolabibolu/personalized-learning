# External Libraries and pip

## Why external libraries?

Python ships with a **Standard Library** of modules such as `math`, `random`, `datetime`, `os` and `json`, which are already installed and only need importing. But the standard library cannot read an Excel file, train a machine learning model, build a website or plot a chart. For those you need **third-party libraries**: code written by other developers and published for reuse. "A library is somebody else's solved problem"; reusing it is professional practice.

**PyPI (the Python Package Index)** is the official public repository of these libraries, with over 500,000 packages. **pip** ("Pip Installs Packages") downloads a package from PyPI and installs it; it comes with Python 3.4 and later. `python -m pip` is the safest form, because it installs into the same Python you are running.

## Core pip commands

| Task | Command |
| --- | --- |
| Install a package | `pip install pandas` |
| Install a specific version | `pip install pandas==2.1.4` |
| Upgrade | `pip install --upgrade pandas` |
| Uninstall | `pip uninstall pandas` |
| List installed packages | `pip list` |
| Details of one package | `pip show pandas` |
| Save the environment | `pip freeze > requirements.txt` |
| Install from a file | `pip install -r requirements.txt` |

Installing pandas also pulls in its **dependencies** (numpy and others), which pip resolves automatically. The install name and import name are not always the same: `pip install scikit-learn` gives `import sklearn`, and `beautifulsoup4` gives `from bs4 import BeautifulSoup`.

## requirements.txt and virtual environments

A **requirements.txt** file records exactly what a project needs, such as `pandas==2.2.2`, so anyone can reproduce the environment with one command. If Project A needs pandas 1.5 and Project B needs 2.2, a **virtual environment**, an **isolated Python installation per project**, solves the conflict: `python -m venv myenv` creates it, `source myenv/bin/activate` (macOS/Linux) or `myenv\Scripts\activate` (Windows) activates it, and `deactivate` exits. Rule of thumb: **one project, one virtual environment**.

## Popular libraries

**NumPy** (fast arrays and maths), **Pandas** (tables, cleaning, aggregation), **Matplotlib** and **Seaborn** (charts), **Requests** (fetching data from web services), **BeautifulSoup** (extracting data from HTML), **Flask** and **Django** (web development), **scikit-learn** (machine learning), **TensorFlow/PyTorch** (deep learning) and **pytest** (testing). NumPy operates on whole arrays at once: `scores * 1.1` scales every score, whereas a plain list times 1.1 raises a TypeError.

**Safety**: anyone can publish to PyPI, and attackers upload look-alike names (**typosquatting**, such as "panadas"). Confirm the exact name on pypi.org and prefer well-known, maintained packages.

Source: Working with External Libraries.pdf (lesson note) (Parts 1 and 2)
