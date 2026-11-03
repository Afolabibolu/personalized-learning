# Lists, Tuples, Sets and Dictionaries

## Lists

A **list** is a **mutable, ordered** collection in square brackets that allows duplicates and grows dynamically: animals = ['cat', 'dog', 'fish', 'lion'].

- **Indexing** starts at 0. animals[-1] is the last item, and animals[6] is an IndexError.
- **Slicing** includes the lower bound and excludes the upper: animals[1:3] gives ['dog', 'fish'], animals[::2] gives ['cat', 'fish'], and animals[:] makes a copy. For [1, 2, 3, 4, 5], [-2] is 4 and [::2] is [1, 3, 5].
- **Changing a list**: assign an element (my_list[1] = 10), append(), extend(), insert(i, x), pop(i), remove(x) (the first match), clear(), sort(), reverse(), index(x) and count(x). The functions len(), sum(), sorted() and reversed() return results without changing the list.
- pets = animals makes both names refer to the **same** list; pets = animals[:] copies it.
- **in** and **not in** test membership. **+** joins lists and ***** repeats them: [1, 2, 3] * 2 is [1, 2, 3, 1, 2, 3].
- **Iterating**: for fruit in fruits; for i in range(len(fruits)); **enumerate()**, which gives (index, value) pairs; **zip()**, which walks lists side by side; and **list comprehensions**. [x**2 for x in range(1, 6)] gives [1, 4, 9, 16, 25], and ["even" if x % 2 == 0 else "odd" for x in ...] labels the values.

## Tuples

A **tuple** is like a list but **immutable**: WEEKDAYS = ('Monday', ...). A single-element tuple needs a comma: (42,). Tuples support indexing, slicing, + and *, in, and the methods count() and index(). Calling append() or assigning an element fails; the workaround is to convert to a list and back. Use tuples for values that must not change.

## Sets

A **set** holds **unique**, **unordered** elements in braces: duplicates are dropped and there is no indexing. Create an empty set with **set()**, because {} is an empty dictionary. Use add(), remove() (KeyError if the item is missing), discard() (no error) and clear(). For even = {2, 4, 6, 8, 10} and big = {6, 7, 8, 9, 10}:

- big − even gives {7, 9};
- big | even is the union;
- big & even gives {6, 8, 10};
- big ^ even gives {2, 4, 7, 9}.


## Dictionaries

A **dict** holds **key-value pairs**: {"name": "Jane Doe", "age": 38}. Keys are **unique and immutable** (strings, numbers, tuples); values can be anything.

- d["name"] reads a value, and a missing key raises a **KeyError**. d.get("gender", "Not Found") gives a default instead.
- Assigning a new key adds it; repeating a key overwrites the old value.
- **del d["age"]** or **d.pop("age")** removes an entry, and clear() empties the dictionary.
- Loop over keys, **values()** or **items()**.

**Nested dictionaries** hold records: students["Alice"]["grade"].

Use **lists** when order matters or items change, **sets** for uniqueness, **tuples** for fixed data and **dictionaries** for lookup by key.

Source: CSC 103 Lecture 3 (2024): functions and lists; CSC 103 Lecture 4 (2024): tuples, sets, dictionaries, strings, regex and modules; CSC 103 2023/24 examination
