# CSS and Page Layout

## What CSS is

**Cascading Style Sheets (CSS)** describe **how HTML elements should be presented**: colours, fonts, spacing and layout. HTML gives the structure and CSS gives the style, which keeps content and presentation separate.

## Rules

A **CSS rule** has two parts:

- the **selector**, which says which element or elements the rule applies to; and
- the **declaration**, which says how they are styled. A declaration has a **property** and a **value**, separated by a **colon**, inside **curly brackets**; several declarations are separated by semicolons.

```css
h1 { color: navy; font-family: Arial; }
```

Here **h1 is the selector**, and `color: navy` is a declaration. One rule styles **every** h1 element, and a selector can list several elements, such as `h1, h2, h3`.

## Three ways to add CSS

1. **Inline style**: a `style` attribute on one element, as in `<p style="color: red">`. No selector is needed, because it applies only to that element.
2. **Internal (embedded) style sheet**: rules inside a `<style>` element in the page's **head**, for one page.
3. **External style sheet**: rules in a separate **.css** file, linked from each page with `<link rel="stylesheet" href="style.css">`.

**External style sheets** are preferred for a **whole, multi-page site**: one file controls the look of every page, so a change is made **once**, pages are smaller and load faster because the file is cached, and the design stays consistent. An internal style sheet can still override rules in the external one for a single page.

## Common properties

Colours use `color` and `background-color`; fonts use `font-family`, `font-size` and `font-weight`; and `text-align` aligns text. Links are styled with the pseudo-classes **a:link**, **a:visited**, **a:hover** and **a:active**, for example `a:hover { color: orange; }`. The **box model** gives each element **margin**, **border** and **padding** around its content.

## Layout with Flexbox and Grid

**Flexbox** (`display: flex`) arranges items in **one dimension**, a row or a column, and is ideal for navigation bars and aligning items. **CSS Grid** (`display: grid`) arranges items in **two dimensions**, rows and columns together, and suits whole-page layouts. They work well **together**: Grid for the page structure and Flexbox inside each area. Combined with **media queries**, they make layouts **responsive**.

Source: Akinola, Web Design with HTML, CSS, JavaScript and PHP, Chapters 8 and 9 (Cascaded Style Sheets; CSS Properties and Values). The section on Flexbox and Grid is from general knowledge, because the 2024/25 paper asks about them.
