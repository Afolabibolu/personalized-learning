# Inheritance, Polymorphism and Special Methods

## Inheritance

**Inheritance** lets a class (the **child** or subclass) reuse attributes and methods from another class (the **parent** or superclass). It models an **"is-a" relationship**: a Dog is an Animal. It **avoids repeating code** (the **DRY** principle: don't repeat yourself), lets you build specialised versions of a general class, and organises code hierarchically.

```python
class Dog(Animal):     # Dog inherits from Animal
    pass
```

Dog automatically gets Animal's `__init__` and `speak()`. Usually a child adds its own attributes while keeping the parent's setup, using **`super()`** to call the parent's methods:

```python
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)     # calls Animal's __init__
        self.breed = breed
```

Types of inheritance are **single** (one parent, one child, the most common), **multilevel** (GoldenRetriever → Dog → Animal) and **multiple** (a class inherits from more than one parent, which **Python supports**).

## Polymorphism

**Polymorphism** ("poly", many, plus "morph", forms) is the ability of **different classes to be used through the same interface, each responding in its own way** to the same method call. Looping over `[Dog("Rex"), Cat("Whiskers"), Duck("Donald")]` and calling `a.speak()` gives a different result for each, and the loop does not need to know the kind of animal. It lets you write general code, such as functions that accept "any Animal", and add new classes later without changing existing code.

## Method overriding

**Method overriding** happens when a **child class defines a method with the same name** as one in its parent; the child's version replaces the parent's for objects of that child. To keep the parent's logic too, call `super().speak()` inside the overriding method. **Overloading** (the same name with different parameter lists) is **not supported in Python** the way it is in Java or C++: a later definition simply replaces the earlier one.

## Special methods

**Special (dunder or "magic") methods**, surrounded by double underscores, let objects work with Python's built-in syntax and functions. Without them, `print(p)` shows something unhelpful like `<__main__.Point object at 0x7f...>`.

| Method | Audience | Called by | Goal |
| --- | --- | --- | --- |
| `__str__` | end user | `print()`, `str()` | readable |
| `__repr__` | developer | `repr()`, the console, lists and dicts | unambiguous, ideally able to recreate the object |

Best practice: **always define `__repr__`**, because if `__str__` is missing, Python **falls back to `__repr__`** automatically.

Source: Advanced OOP Concepts_.docx (Week 4)
