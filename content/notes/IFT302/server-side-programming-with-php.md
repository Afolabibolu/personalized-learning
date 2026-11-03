# Server-side Programming with PHP

## Server-side programming

A student portal must let users create accounts, log in, register courses and check results. That information lives on a **server**, usually in a **database**, and a language running on the server is needed to process it. **Server-side programming** is **executed on the web server** rather than in the browser. A server-side program can receive requests, process information, **apply business rules**, communicate with databases, **authenticate users**, create dynamic pages and send responses. Server-side technologies include **PHP, Python, Java, C#, Ruby and JavaScript with Node.js**.

In a login, the browser sends the username and password in an **HTTP request** to the web server; the **PHP application** queries the **MySQL database**; and the result returns as an **HTTP response** to the browser.

## PHP

**PHP** is a **server-side scripting language** for dynamic websites and web applications. It originally stood for **Personal Home Page**; it is now understood as **PHP: Hypertext Preprocessor**. **PHP code runs on the server, and only its result is sent to the browser**: for `<?php echo "Hello, Students!"; ?>` the browser receives just "Hello, Students!". This is a key difference from JavaScript, whose code the browser receives and runs.

PHP is popular because it is **easy to learn**, **open source**, cross-platform, **integrates well with HTML**, supports databases such as MySQL and has strong community support. It is used for login and registration systems, content management systems, e-commerce sites, student portals, blogs, online examination systems and inventory systems.

## Setting up

A PHP project needs a code editor, a browser, a web server, PHP and later a database. **XAMPP** provides Apache, PHP, MySQL/MariaDB and phpMyAdmin. Projects go in the server's document directory, **htdocs**, for example `htdocs/myphp/index.php`, opened at `http://localhost/myphp/` once **Apache is started**.

## PHP basics

- PHP code sits between `<?php` and `?>`; statements end with a **semicolon**; **echo** outputs text or HTML.
- **Variables** start with **$**, as in `$name = "Ada";`, and can be placed inside double-quoted strings: `echo "Name: $name";`.
- **Constants** are created with `define("SITE_NAME", "UI Portal");` and used without $.
- **var_dump()** shows a value's type and value, such as `bool(true)` for `$age >= 18`.
- PHP supports arithmetic, comparison and logical operators, **if/else**, **switch**, **for**, **while** and **foreach** loops, **functions**, **arrays** and string functions.

## Forms

HTML forms send data to PHP with **GET** or **POST**; PHP reads it from the **superglobals** `$_GET` and `$_POST`, for example `$_POST["username"]`. Input must be **validated** on the server too, because client-side checks can be bypassed.

Source: Lesson 5 - Server-Side Programming with PHP.pdf; Web Application Development course content.docx (Week 5)
