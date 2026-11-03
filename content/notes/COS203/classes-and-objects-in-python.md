# Classes and Objects in Python

## Why classes?

Simple data structures such as numbers, strings and lists represent simple pieces of information. To track employees with a name, age, position and start year, you could store each as a list, such as `["James Kirk", 34, "Captain", 2265]`. But this has problems: in a large file, it is hard to remember that index 0 is the name, and if one list leaves out the age, `mccoy[1]` returns the wrong value. **Classes** make such code more manageable and maintainable.

## Classes and instances

**Classes are used to create user-defined data structures.** They define functions called **methods**, which describe the behaviours an object created from the class can perform with its data. A **class is a blueprint**: it does not contain any data. A `Dog` class says a name and an age are needed, but contains no particular dog. An **instance** is an **object built from a class that contains real data**, such as a dog named Miles who is four years old. A class is like a form, and an instance is a form that has been filled in; many instances can be created from one class.

## Defining a class

All class definitions start with the **class** keyword, the class name and a colon; the indented code below is the class body. `pass` is a placeholder that lets an empty class run without an error. By convention, class names use **CapitalizedWords**, such as `JackRussellTerrier`.

The properties every object must have are set in the **`__init__()`** method, which runs each time a new object is created. Its first parameter is always **self**, the new instance:

```python
class Dog:
    species = "Canis familiaris"      # class attribute

    def __init__(self, name, age):
        self.name = name              # instance attributes
        self.age = age

    def description(self):            # instance method
        return f"{self.name} is {self.age} years old"

miles = Dog("Miles", 4)
print(miles.description())   # Miles is 4 years old
```

- **Instance attributes** are set in `__init__` through self, and each object has its own values.
- **Class attributes** are defined directly in the class body and have the **same value for every instance**.
- **Instance methods** are functions defined in the class, and their first parameter is also self.

You create an instance by calling the class like a function, passing the arguments for `__init__` except self, and reach its attributes and methods with **dot notation**, as in `miles.name`.

A class such as `Student` with a name, matric number and course code can then be saved to a file one record per line, and searched for by matric number.

Source: Python Basics (Real Python, 4th ed.), Chapter 10 (Object-Oriented Programming: Define a Class, Instantiate an Object)
