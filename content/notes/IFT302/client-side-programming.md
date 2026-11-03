# Client-side Programming

## Client-side programming

**Client-side programming** is executed **on the user's device, usually in a web browser**. It includes the **user interface** (text, images, buttons, forms) and small changes on the page, such as opening a menu or showing an error. The main client-side languages are **HTML, CSS and JavaScript**.

## HTML

**HTML (HyperText Markup Language)** gives a page its **structure**. Its **tags** are written in **angle brackets**, as in `<head></head>`. A basic document is:

```html
<!DOCTYPE html>
<html>
<head><title>My First Web Page</title></head>
<body>
  <h1>Welcome</h1>
  <p>This is my first webpage.</p>
</body>
</html>
```

Common HTML5 elements are headings (`<h1>`, `<h2>`), paragraphs (`<p>`), links (`<a href="...">`), images (`<img src="..." alt="...">`), **ordered lists** (`<ol>`) and **unordered lists** (`<ul>`) with `<li>` items.

## CSS

**CSS (Cascading Style Sheets)** controls the **appearance and layout** of pages and **separates presentation from content**. The **CSS box model** surrounds each element's content with **padding**, a **border** and a **margin**.

## JavaScript

**JavaScript** adds **interactivity and dynamic functionality**: image sliders, form validation, pop-ups, menus, games and calculators.

- **Variables** store data: `let name = "John";` and `const age = 20;` (a const cannot be reassigned).
- **Data types**: string, number, boolean, array, object, **null** and **undefined**.
- **Operators**: arithmetic (+, -, \*, /, %), comparison (==, **===**, !=, >, <; === compares value **and type**) and logical (&&, ||, !).
- **Control flow**: `if (score >= 50) { ... } else { ... }` and loops such as `for (let i = 1; i <= 5; i++)`.
- **Functions** make code reusable: `function greet(name) { return "Welcome " + name; }`.

## The DOM and events

The **Document Object Model (DOM)** represents an HTML document as a **tree of objects**, letting JavaScript access and change elements. Elements are found with `document.getElementById("title")`, `getElementsByClassName()` or `querySelector(".menu")`; content changes with `.textContent = "Hello Students"` and style with `.style.color = "blue"`. Code responds to **events** such as **click**, mouseover, mouseout, keydown, keyup and **submit**, as in `<button onclick="greet()">`.

## Form validation

**Form validation** checks that **input is correct before it is submitted**. It ensures required fields are completed, reduces incorrect data, improves UX and **reduces unnecessary server processing**. **HTML5** offers `required`, `type="email"`, `minlength="8"` and `pattern="[A-Za-z]{3,}"`. In **JavaScript**, `<form onsubmit="return validateForm()">` calls a function that shows an alert and **returns false** if the input is invalid, which **stops the form from being submitted**. Best practice is to keep HTML, CSS and JavaScript in separate files, use **semantic HTML** and test on several browsers.

Source: Lesson 4 - Client-side Programming.pdf; IFT 302 Lesson 1-4.pdf (B. I. Dahunsi) (Lesson 4)
