# HTML Tags, Tables and Links

## Getting started

To design a web page you need a **folder** for your HTML files, a **browser**, and a **simple text editor** such as **Notepad** or WordPad (word processors such as Microsoft Word add formatting you do not want). Internet access is not needed while designing. The process is: type the text and tags in the editor, **save the file as HTML**, open it in the browser, and switch back to make corrections.

## HTML basics

**HTML (HyperText Markup Language)** is the language for writing web pages. The text is "marked up" with **tags**, more accurately called **elements**, which control how it looks and is structured; the **browser acts as an interpreter** for HTML. Most tags come in pairs, an **opening tag** and a **closing tag** with a slash, around the content they affect:

```html
<html>
  <head><title>CSC 293</title></head>
  <body>
    <h1>Welcome</h1>
    <p>This is a <b>bold</b> word.</p>
  </body>
</html>
```

The **head** holds information about the page, such as its **title** (shown in the browser tab), and the **body** holds what is displayed. Common tags include headings **h1 to h6**, **p** (paragraph), **br** (line break), **hr** (horizontal rule), **b** and **i**, lists (**ul**, **ol** and **li**), and **img** with a **src** attribute for images. Attributes inside the opening tag add settings, as in `<img src="logo.png" alt="Logo">`. Tags should be **properly nested**: the last tag opened is the first closed.

## Tables

A **table** is built with **table**, **tr** (table row), **td** (table data, a cell) and **th** (a heading cell, usually bold and centred). Attributes include **border** (the thickness of the lines), **cellspacing** (the space between cells), **cellpadding** (the space between a cell's edge and its content) and **width**. Cells can span columns (**colspan**) or rows (**rowspan**), hold images, have their own background colours, and act as links.

## Links

Links use the **anchor tag**, **a**, with an **href** attribute:

- **Page jump**: mark a place with a name or id, then link to it with `href="#section"`.
- **Another page in your site**: `<a href="about.html">About us</a>`.
- **A page anywhere in the world**: use the full URL, as in `href="https://www.ui.edu.ng"`.
- **Email**: `href="mailto:name@example.com"` opens the visitor's email program.

A **link button** can also be made with a form button. Every page should link back to the home page so visitors do not get lost.

Source: Akinola, Web Design with HTML, CSS, JavaScript and PHP, Chapters 3 to 6 (Basic Tags, Table Tags, Page Jumps, Linking Web Pages)
