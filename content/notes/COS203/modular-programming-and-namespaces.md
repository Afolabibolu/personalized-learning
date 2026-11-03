# Modular Programming, Modules and Namespaces

## Modular programming

**Modular programming** is a software design technique that **breaks a program into smaller, manageable, reusable components called modules**. Real programs grow to thousands or millions of lines; one file becomes impossible to manage, and teams need to work on different parts at the same time. Modular programming solves this by **improving readability**, **enabling code reuse**, **making debugging easier** and **supporting team collaboration**.

## Modules

A **module** is a **file containing Python code that can be reused in other Python files**. Breaking a program into modules has **four main advantages**:

1. **Simplicity**: each module focuses on one part of the problem.
2. **Maintainability**: a change in one module rarely affects the others.
3. **Reusability**: code in one module can be used by many programs.
4. **Scoping**: each module has its own namespace, which avoids name clashes.

## Importing a module

When you import one module into another, the content of the imported module becomes available in the other. The module containing the import statement is the **calling module**. For example, if `code_1.py` defines

```python
def add(x, y):
    return x + y
```

then another file can use it:

```python
import code_1
value = code_1.add(2, 2)
print(value)   # 4
```

## Namespaces

A **namespace** is a **collection of names**, such as variable, function and class names. **Every Python module has its own namespace**. Names in the same module are used just by typing them, but this does not work for imported modules: to access a name in an imported module, type the **module's name, a dot (.) and the name**, as in `code_1.add`. With `import code_1`, the module's whole namespace is imported.

Namespaces work like international ID numbers: two people in different countries can share an ID number but are told apart by their country codes. Namespaces **group names into logical containers**, **prevent clashes between duplicate names** and **provide context** for names.

## Variations of import

- `import <module> as <other name>` renames the import, so the module's namespace is reached through the new name: `import pandas as pd`.
- `from <module> import <name>` imports **a single name** instead of the whole namespace, so it can be used without the module prefix: `from code_1 import add`, then `add(2, 2)`.

A typical modular program has an input module, a logic module, an output module and a `main.py` that imports them all and runs the program.

Source: COS 203(Practical Lab).pdf (Modular Programming); Python Basics (Real Python, 4th ed.), Chapter 11 (Modules and Packages)
