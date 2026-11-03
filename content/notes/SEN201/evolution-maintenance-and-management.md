# Evolution, Maintenance, Re-engineering and Project Management

## Evolution

Software development does not stop when a system is delivered: **after deployment it inevitably has to change to remain useful**, because of business changes and changing user expectations. Useful systems have long lifetimes: air traffic control systems may last **30 years or more**, business systems often more than 10. **System change proposals** drive evolution; they may come from unimplemented requirements, new requirements, bug reports or ideas for improvement. The evolution process includes **change analysis, release planning, system implementation and releasing the system to customers**. **Lehman's laws** describe how large systems change: a system in use must change continually, and its structure degrades as it changes unless work is done to maintain it.

## Maintenance

**Software maintenance** is the general process of changing a system after delivery. There are three types:

1. **Fault repairs**: coding errors are cheap to correct, design errors more expensive, and **requirements errors the most expensive**, because extensive redesign may be needed.
2. **Environmental adaptation**: when the hardware, operating system or support software changes.
3. **Functionality addition**: when requirements change with organisational or business change; usually the largest changes.

Maintenance takes a higher proportion of IT budgets than new development, **roughly two-thirds maintenance and one-third development**, and more is spent on new requirements than on fixing bugs. So it pays to design systems to reduce the cost of future change.

## Legacy systems and re-engineering

**Legacy systems** are old systems that are still useful, sometimes critical, but may use outdated languages and technology and be expensive to maintain. **Software re-engineering** makes them easier to understand and change. Its activities are:

1. **Source code translation** to a modern language or version.
2. **Reverse engineering**: analysing the program to document its organisation and functions.
3. **Program structure improvement**: making the control structure easier to read.
4. **Program modularisation**: grouping related parts and removing redundancy.
5. **Data re-engineering**: changing the data and database schemas to match.

## Project management

Projects need managing because professional software is always subject to **budget and schedule constraints**. **Software project management** plans, organises, controls and monitors development so that projects finish **on time, within budget and with acceptable quality**. People are an organisation's greatest assets, and good engineers are not always good managers. A **cohesive group** can set its own quality standards, members learn from and support each other, knowledge is shared, and refactoring and continual improvement are encouraged. Team management involves selecting members with the right balance of skills: programming, design, testing and quality assurance, and coordination.

Source: SEN 201 Lecture Notes.docx, Software Evolution, Software Maintenance, Legacy Systems and Software Re-engineering, Software Project Management (the notes name Lehman's laws without stating them; their summary here is from general knowledge)
