# JavaScript

## What JavaScript is

**JavaScript** is a **client-side scripting language** that runs in the browser and makes pages interactive: responding to clicks, checking forms and changing content. Code goes in a `<script>` element in the head or body, or in an external .js file. `document.write()` writes to the page, `alert()` shows a message box, and `document.getElementById("demo").innerHTML` changes an element's content.

## Variables and scope

JavaScript is **untyped**: you do not declare a variable's type, as in `var a = 33;`. Its data types are numbers, strings and booleans, plus objects such as arrays. Variables have only **two scopes**:

- **Global** variables are defined anywhere in the code and are visible throughout.
- **Local** variables are visible **only inside the function** where they are defined, and function parameters are always local. A local variable **takes precedence over a global one with the same name**.

Variable names cannot be **reserved keywords**, must not start with a digit, and are **case-sensitive**.

## Operators

Arithmetic operators are `+ - * / %` and `++ --`. **Assignment operators** combine an operation with assignment: with a = 33 and b = 10, each starting again from a = 33, `a = b` gives 10; `a += b` gives 43; `a -= b` gives 23; `a *= b` gives 330; `a /= b` gives 3.3; and `a %= b` gives **3**, the remainder. Comparison operators are `== != > < >= <=`, and logical operators are `&&`, `||` and `!`.

## Control structures

```javascript
if (score >= 70) { grade = "A"; }
else if (score >= 60) { grade = "B"; }
else { grade = "C"; }

switch (grade) {
  case "A": document.write("Your grade is excellent"); break;
  default: document.write("Keep working");
}

for (var i = 1; i <= 5; i++) { document.write(i); }
```

A **while** loop checks its condition first, while a **do-while** loop runs at least once.

## Functions and events

A **function** is defined with `function name(parameters) { ... }` and can **return** a value. **Events** run code in response to the user:

- **onclick** triggers on a mouse click and is the **most frequently used** event;
- **onsubmit** occurs when a form is submitted, so it is used to **validate** the form first;
- **onmouseover** and **onmouseout** trigger when the pointer moves over or off an element; and
- **onload** runs when the page loads.

## Cookies, validation and arrays

A **cookie** stores small pieces of data in the browser through **document.cookie**, as `name=value` pairs with an optional **expires** date. **Form validation** checks that required fields are filled and correctly formatted before data is sent. An **array** stores several values in one variable, as in `var foods = ["Amala", "Eba"];`, indexed from 0.

Source: Akinola, Web Design with HTML, CSS, JavaScript and PHP, Chapters 10 to 19 (JavaScript)
