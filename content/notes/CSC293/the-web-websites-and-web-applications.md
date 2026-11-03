# The Web, Websites and Web Applications

## Internet and Web

The **Internet** is a series of huge computer networks that lets computers worldwide connect and communicate. Languages that move information between computers are **protocols**; email, for example, uses IMAP, POP3 and SMTP. The **World Wide Web** is another layer on the Internet: an information system where documents are identified by **Uniform Resource Locators (URLs)**, interlinked by hypertext. The Web uses three technologies: **HTML** (the language pages are written in), **HTTP** (which requests the HTML document from the server and serves it to the browser) and **URLs** (the address of a document, `<protocol>://<node>/<location>`).

In **1989** **Sir Tim Berners-Lee**, a British computer scientist at **CERN**, created the Web; by 1990 he had also created HTML, the URL, HTTP and the first browser, called **WorldWideWeb** (later Nexus). The first website, explaining the Web project, became public in **1991** and was **static**: users could only browse it. The need for interaction led to **dynamic** websites, such as pages with forms.

## Pages, sites and applications

- A **web page** holds text, images, audio and video that users see, hear or interact with.
- A **website** is a **set of related web pages** with a common domain name, hosted on at least one web server and reached by a URL. It provides **static documents**; **no user input affects business functionality**.
- The **home page (index page)** is the first page of a site.
- A **web application builds on a website**: it **takes user input that affects back-end business logic**.

A web application's components are the **client tier** (the browser, with HTML and scripts such as JavaScript), the **Internet**, a **firewall**, the **middle tier** (a **web server** such as Apache or IIS for presentation, and an **application server** for business logic, using PHP, JSP, ASP or Java EE) and the **data tier** (a database such as MySQL, Oracle or SQL Server).

**Web apps** are installed once and reached from anywhere but depend on Internet speed and use more bandwidth; **desktop apps** must be installed and updated on each computer. **Browsers** are graphical (Chrome, Firefox, Internet Explorer) or text-only (such as **Lynx**). Sites are published to a server with an **FTP** client.

## Protocols

- **TCP** (transport layer): reliable, ordered delivery.
- **IP** (network layer): addressing and routing, in **IPv4 and IPv6**.
- **HTTP** (application layer): how browsers and servers communicate; **HTTPS** adds encryption.
- **SMTP** sends email, while **POP** downloads messages to a device and **IMAP** keeps them on the server.
- **FTP** transfers files.
- **DNS** translates domain names into IP addresses, and **DHCP** assigns IP addresses automatically.
- **SSH** gives secure remote login.

Source: Akinola, Web Design with HTML, CSS, JavaScript and PHP, Chapter 1 (Website versus Web Application); web protocols.pdf. The book lists Mosaic as a text-only browser; Mosaic was a graphical browser, so that example is left out.
