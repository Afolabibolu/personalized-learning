# HTML Forms

## The form tag

A **form** collects information from visitors, such as an order, a registration or feedback. A form starts with

```html
<form method="post" action="process.php">
  ...
</form>
```

**FORM is a container element**: everything between the opening and closing tags is part of the form. **METHOD** tells the browser how to send the data, usually **POST** or **GET**, and **ACTION** tells it **where to send the data**, normally a script on the server. The book warns that using a **mailto:** email address as the action works in few browsers and sends the data still encoded, so a server script is better.

## Input elements

Most fields use the **input** element, whose **type** attribute decides what appears. Each field has a **name** so the data can be identified when it is sent.

- **Text box**: `<input type="text" name="fullname" size="30">` for one line of text.
- **Password box**: `type="password"` shows dots or asterisks instead of the characters typed.
- **Radio buttons**: `type="radio"` with the **same name** for a group, so **only one can be chosen**, such as a payment method.
- **Check boxes**: `type="checkbox"`, where **several can be ticked**, such as the foods ordered.
- **Hidden text**: `type="hidden"` sends a value the visitor does not see.
- **Submit** and **reset** buttons: `type="submit"` sends the form, and `type="reset"` **clears** it back to its starting values. An **image** can also be used as the submit button (`type="image"`).

## Menus and text areas

A **pop-up menu (drop-down list)** uses **select** with one **option** element per choice, such as a list of soups; it saves space when there are many choices. A **text area**, `<textarea name="comments" rows="4" cols="40"></textarea>`, accepts **several lines** of text, such as delivery instructions.

## Designing a good form

Plan the fields the business needs, label each one clearly, group related fields, use radio buttons for one choice and check boxes for many, and give a clear submit button. For an online food order, for example, the form might use text boxes for the name and phone number, check boxes or menus for the food items and quantities, radio buttons for delivery or pick-up, a text area for instructions, and a submit button that triggers a total cost calculation in JavaScript.

## Advantages and disadvantages of HTML

HTML is **simple, free, supported by every browser** and needs only a text editor. But it creates only **static** pages on its own, needs much code for complex pages, and offers limited security, so it is combined with CSS, JavaScript and server-side languages.

Source: Akinola, Web Design with HTML, CSS, JavaScript and PHP, Chapter 7 (Creating Forms)
