# The MATLAB Environment, Variables and Script Files

## The environment

**MATLAB** (matrix laboratory) is an interactive environment and language for numerical computing, plotting and simulation. Its desktop has a **Command Window**, where commands are typed and run at the `>>` prompt; a **Workspace**, which lists the variables in memory; a **Current Folder** browser; and an **Editor** for writing programs.

## Variables and operators

A **variable** is created by assignment: `m = 1.23` stores 1.23 in m. Names must start with a letter, may contain letters, digits and underscores, and are **case sensitive** (m and M differ). Ending a statement with a **semicolon** suppresses the display of its result. Every value is treated as an array; a single number is a 1 × 1 array.

Arithmetic operators are `+`, `-`, `*`, `/` and `^` (power). Precedence follows the usual rules: brackets first, then powers, then multiplication and division, then addition and subtraction. Useful constants and functions include `pi`, `exp(x)`, `sqrt(x)`, `sin(x)` and `cos(x)` (in radians), `sind(x)` (in degrees), `log(x)` (natural log) and `abs(x)`. `clc` clears the Command Window, `clear` removes variables, and `help name` explains a function.

## Script files

A **script file** is a plain-text file with the extension **.m** that holds a sequence of MATLAB commands. Running it (by typing its name or pressing Run) executes the commands in order in the workspace, so scripts are used for tasks such as the course's practical tests: computing the pressure of a perfect gas with p = mRT/V over a range of temperatures, or evaluating the Rankine-Hugoniot equation for a shock wave. Comments start with `%`; a block of code can be grouped into a section with `%%`. Good scripts begin with comments that say what they do, and give their inputs as clearly named variables.

## Output

Leaving off the semicolon shows a variable's value. `disp(x)` displays a value or text, and `fprintf` prints formatted text: `fprintf('p = %.2f kPa\n', p)` prints p with two decimal places. `input('prompt')` reads a value from the user.

Source: Written from general knowledge of CSC 231; no course file covered this topic.
