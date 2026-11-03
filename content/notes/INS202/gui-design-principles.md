# GUI Design Principles

## Good GUIs

In the lecture's comparison, App A hides the transfer button in a submenu and shows only "Error 4402", while App B has a clear "Send Money" button, a confirmation screen and plain error messages. **Usable is not the same as pretty**: good design means **efficient, accurate, low-friction task completion** aligned with user expectations.

## Nielsen's ten usability heuristics

1. **Visibility of system status**: keep users informed with timely feedback.
2. **Match between the system and the real world**: use the users' language and familiar concepts.
3. **User control and freedom**: give an "emergency exit", undo and redo.
4. **Consistency and standards**: the same words and actions mean the same things.
5. **Error prevention**: design so errors are less likely.
6. **Recognition rather than recall**: keep options visible.
7. **Flexibility and efficiency of use**: shortcuts for experts.
8. **Aesthetic and minimalist design**: no irrelevant information.
9. **Help users recognise, diagnose and recover from errors**: plain-language messages that suggest a fix.
10. **Help and documentation**.

## Shneiderman's eight golden rules

1. **Strive for consistency**.
2. **Seek universal usability** (cater to novices and experts).
3. **Offer informative feedback**.
4. **Design dialogues to yield closure**.
5. **Prevent errors** (offer simple error handling).
6. **Permit easy reversal of actions**.
7. **Support an internal locus of control** (users feel in charge).
8. **Reduce short-term memory load**.

The two frameworks overlap and complement each other; naming the specific violated principle is better than vague complaints.

## Colour and typography

**Colour** balances harmony, functional meaning, cultural sensitivity and accessibility: WCAG asks for a contrast ratio of at least **4.5:1** for normal text, and **colour must never be the only carrier of critical information**. **Typography** shapes legibility through hierarchy, a line length of **50 to 75 characters** and leading (line spacing) of **120 to 150%**.

## Icons and navigation

**Icons** use recognition over recall but succeed only when **simple, consistent, and universal or paired with text**. Navigation patterns include **tab bars**, **hamburger menus** (which save space but reduce discoverability), **breadcrumbs** (showing the user's location) and **sidebars**. Menus may be **pull-down**, **pop-up** or **contextual** (showing only relevant choices).

## Forms

Good forms use clear labels, logical grouping, sensible defaults, **inline validation** and **specific, constructive error messages** placed beside the field. **Redundancy is accessibility**: colour, icons and text should reinforce each other.

Source: INS 202 Lecture 6 GUI Principles. The full wording of the ten heuristics and eight rules follows Nielsen and Shneiderman, as the slides list them only in part.
