# Input, Output and User Interface Design

## The human-computer layer

After requirements, logical design and architecture are settled, the analyst decides **how users will interact with the system** and how it communicates back: **USER → INPUT/UI → PROCESSING → DATABASE/INFORMATION → OUTPUT/UI → USER**. **A technically correct system can still fail if users cannot understand it**, enter data accurately or recover from errors.

## Input design

**Input design** determines **what data should be captured, how, by whom, with which controls and under which rules** before it is accepted. Its objectives are to capture the correct data, **minimise unnecessary entry**, reduce errors and duplication, make entry fast, stay consistent with the database and business rules, give feedback and **protect sensitive input** such as passwords.

Common **input controls** include text boxes, drop-down lists, date pickers, **radio buttons** (when **only one** option may be chosen, such as a payment method: bank transfer, card or USSD) and **checkboxes** (for **independent** selections, such as notification channels: email, SMS, WhatsApp). Principles of good input design:

- do not ask for what the system already knows;
- use **meaningful labels** and **selection controls** for values from a fixed list;
- **group related information**;
- use safe, easily changed **defaults**;
- mark required fields clearly;
- give immediate feedback; and
- **preserve user input when an error occurs**.

## Validation and verification

**Validation** checks that data is **reasonable and acceptable** (type, range, format, presence, length and consistency checks); **verification** checks that data was **entered correctly** (double entry or confirming a password). **Client-side validation** gives fast feedback in the browser, but **server-side validation** is essential because client checks can be bypassed.

## Output design

**Output design** decides what information the system presents, in what form, to whom and when. Reports are:

- **operational**: day-to-day transactions, such as a daily class list;
- **management**: summaries and exceptions for decision makers; and
- **analytical**: trends and comparisons over time.

Outputs may be on screen, printed, emailed or exported, and should be accurate, timely, clear and relevant.

## Interface design

Good user interfaces apply **usability** (easy to learn and use), **accessibility** (usable by people with disabilities), **consistency** (the same layouts and terms), **feedback** (confirming actions), **visibility** (options easy to find), **error prevention** and **user control** (undo and cancel). The **UI** is what users see and touch; **UX** is the overall experience. Designers build forms, reports, **navigation structures** and **prototypes**, then **evaluate** them against usability and accessibility criteria.

Source: Input, Output and User Interface Design note; the slide deck on input, output and UI design. The definitions of validation versus verification and of the three report types follow the note's headings, with wording from general knowledge.
