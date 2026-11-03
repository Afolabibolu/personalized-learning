# PHP and MySQL

## What PHP is

**PHP (Hypertext Preprocessor)** is a **server-side scripting language**: the server runs the code and sends plain HTML to the browser. PHP code goes between `<?php` and `?>`. Comments have **three styles**: `//` and `#` for single lines, and `/* ... */` for several lines.

## Variables and loose typing

**PHP variables begin with a $ sign** and are **case-sensitive**. A variable's value is its **most recent assignment**; variables **need not be declared** before use and have **no intrinsic type** other than that of their current value. **PHP is loosely typed**, so the same variable can hold different types in one program:

```php
$a = 5;          // integer
$a = 3.7;        // double
$a = "I am a boy"; // string
```

This makes coding quicker and more flexible, but type mistakes are found only when the program runs, so values should be checked carefully (PHP 7 added optional type declarations).

## Scope and constants

PHP has three variable scopes:

- **Global**: a variable outside any function, which keeps its meaning through the rest of the file (but not inside function bodies unless declared global).
- **Local**: a variable restricted to a function or class.
- **Static**: a local variable that **keeps its value between calls** of the function, for example to count how many times a function is called.

**Constants** are created with `define()`, have **no $**, are usually written in **uppercase**, hold one value for their lifetime and have **global scope**.

PHP has **eight data types**, including integers, doubles, booleans, strings, arrays and objects. Its control structures (if, else, elseif, switch, for, while, do-while and **foreach** for arrays), functions, arrays, string functions and file functions work much like those of other languages.

## Connecting to MySQL

PHP connects to **MySQL** with the **MySQLi** extension ("i" for **improved**) or **PDO** (PHP Data Objects), which also works with other databases:

```php
$conn = mysqli_connect("localhost", "username", "password", "mydb");
if (!$conn) { die("Connection failed: " . mysqli_connect_error()); }
// ... queries ...
mysqli_close($conn);
```

## SQL statements

- **CREATE TABLE** defines a table: `CREATE TABLE countries (country_id INT, country_name VARCHAR(40), region_id INT);`
- **INSERT** adds rows; one statement can insert several: `INSERT INTO countries VALUES (1, 'Nigeria', 1), (2, 'Ghana', 1);`
- **SELECT** retrieves data, and **AS** renames columns: `SELECT first_name AS "First Name", last_name AS "Last Name" FROM employees;`

Source: Akinola, Web Design with HTML, CSS, JavaScript and PHP, Chapters 20 to 26 (PHP Basics to PHP MySQL Database Handling)
