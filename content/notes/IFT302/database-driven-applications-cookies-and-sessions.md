# Database-Driven Applications, Cookies and Sessions

## Database-driven applications

In a **database-driven** application, a page receives a request, **PHP runs the logic and sends SQL to MySQL**, MySQL returns data or makes a change, and PHP builds the response for the browser: **Browser → PHP → MySQL → PHP → Browser**. The course's case study is a **Student Record Management System (SRMS)** that adds, views, searches, edits and deletes student records.

Designing the table means identifying the **entity** (STUDENT), its attributes, data types and a **primary key**: `id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY`, `matric_no VARCHAR(30) NOT NULL UNIQUE`, `gender ENUM('Male','Female')` and `created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP`. A **primary key** uniquely identifies each row, and a table has **one**; **UNIQUE** prevents duplicate values in a column, such as matric numbers.

## CRUD

**CRUD** is **Create (INSERT), Read (SELECT), Update (UPDATE) and Delete (DELETE)**, the operations of almost every data application. Connection code is kept in **db.php** and included with `require_once 'db.php';`, which centralises settings and keeps credentials out of the HTML.

**Prepared statements** write the SQL structure **separately from user values**, using **? placeholders** and **binding** values with their types: **s** (string), **i** (integer), **d** (double) and **b** (binary). They **protect against SQL injection** and should be used whenever external input enters SQL. **htmlspecialchars()** converts special HTML characters when data is displayed, **protecting HTML output** from injected script (XSS). The two solve different problems. Searches use **LIKE** with wildcards, as in `%john%`. Deletion should be confirmed, and an ID should never simply be trusted.

## State: cookies and sessions

**HTTP is stateless**: each request is independent, so an application needs a way to recognise the same user across login, dashboard and results pages.

- A **cookie** is a **small piece of information stored by the browser** at a site's request and sent back on later requests. It is created with `setcookie("username", "Evans", time() + 3600)`, read with `$_COOKIE["username"]` (check with **isset()** first) and deleted with a **past expiry time**. Cookie values are **client-controlled**, so **never trust them alone for authorisation**.
- A **session** keeps **state on the server**, identified by a session ID usually carried in a cookie called **PHPSESSID**. Call `session_start()` first; store values in **$_SESSION**, such as `$_SESSION["user_id"] = 25;`. Protect a page by checking `isset($_SESSION["logged_in"])` and otherwise using `header("Location: login.php"); exit();`. **Logout** clears `$_SESSION`, calls **session_destroy()** and redirects.

## Security

**Session fixation** tricks a victim into using a session ID the attacker knows; prevent it with **session_regenerate_id(true)** after login. **Session hijacking** steals a valid session ID; defend with HTTPS and cookie flags. **HttpOnly** stops JavaScript reading the cookie, **Secure** sends it only over **HTTPS**, and **SameSite** (Strict, **Lax** or None) limits cross-site sending and reduces **CSRF**. **Authentication and authorisation must remain server-side.**

Source: Database Driven Web Applications_.pptx; PHP Cookies and Session Management_.pptx
