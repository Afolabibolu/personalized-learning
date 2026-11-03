# Web Architecture and Development Tools

## Architecture

**Web development architecture** is the **structure and organisation of the components** that work together to deliver web applications, defining how clients, servers, databases and services communicate. A typical web application consists of a **client (web browser)**, a **web server**, **application logic** and a **database server**.

## Client-server architecture

**Client-server architecture** is a model in which **clients request services or resources and servers provide them** over a network, using **HTTP or HTTPS**.

- A **client** is any device or software that requests information, such as Chrome, Firefox, Edge or Safari. It sends requests, displays pages, collects input and runs client-side scripts.
- A **server** receives requests, processes them and sends responses: **Apache**, **Nginx** or Microsoft **IIS**. It hosts sites, runs application logic, manages authentication and accesses databases.
- A **database server** stores and retrieves data: **MySQL**, PostgreSQL, Oracle or SQL Server.

When a user visits a shop, the browser requests the homepage, the server receives it, the application retrieves products from MySQL, the server generates HTML and the browser displays it. **Advantages**: centralised management, security, easier maintenance, scalability and resource sharing. **Disadvantages**: **server failure affects all clients**, high load reduces performance, and network connectivity is required.

## Apache

**Apache HTTP Server** is one of the world's most widely used **open-source** web servers, maintained by the **Apache Software Foundation**. It is free, cross-platform, supports HTTP and HTTPS (SSL/TLS), is modular and works with PHP, Python and Perl. It receives requests, locates files, executes server-side scripts, returns pages, handles simultaneous connections and logs requests. Its configuration files are **httpd.conf** (main), **.htaccess** (directory level) and apache2.conf (Linux).

## Development environment

A **development environment** is the set of tools used to create, test, debug and deploy applications: a **code editor or IDE** (Visual Studio Code is preferred), browsers and **browser developer tools**, a **local server package** (**XAMPP**, WAMP, MAMP or Laragon, bundling **Apache, MySQL/MariaDB, PHP and phpMyAdmin**) and **package managers** (**npm**, **Composer**). XAMPP's web root is **htdocs** (WAMP's is www), and a page there is opened at `http://localhost/...`.

## Git

**Version control** records changes to files over time so developers can track changes, **revert** to earlier versions and collaborate. **Git** is a **distributed** version control system created by **Linus Torvalds in 2005**. A **repository** is a project folder managed by Git; a **commit** is a saved snapshot; a **branch** is an independent line of development; **merge** combines branches; **clone** copies a remote repository; **push** uploads changes and **pull** downloads them. Common commands are `git init`, `git status`, `git add .`, `git commit -m "message"`, `git log`, `git push origin main` and `git pull origin main`.

**MySQL** is an open-source **relational database management system** that uses **SQL**; with Apache and PHP it forms the classic stack for dynamic sites.

Source: IFT 302 Lesson 1-4.pdf (B. I. Dahunsi) (Lesson 3: Website Architecture and Tools); Web Application Development course content.docx (Week 1 practical)
