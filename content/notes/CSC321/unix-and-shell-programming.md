# Unix, Pipes, Filters and Shell Programming

## The Unix operating system

Unix was developed at **Bell Labs** in the 1970s by **Ken Thompson, Dennis Ritchie** and others. It is written in the **C** language and was the first **portable** operating system: its code can be modified for new hardware. Its properties include:

- multi-user and multitasking operation;
- portability;
- a hierarchical file structure starting at the root directory;
- communication through the shell and kernel, and support for TCP/IP;
- pipes and filters for building complex programs from simple ones;
- many software development tools.

Unix-like systems include **Solaris, Darwin, AIX, HP-UX, FreeBSD, NetBSD, IRIX, macOS** and **Linux**, a freely available flavour of Unix.

## Unix architecture

Unix has a layered architecture:

- **Hardware:** the physical devices.
- **Kernel:** the heart of the system. It handles memory allocation, scheduling, swapping between memory and disk, and data transfer with peripherals, and its two main jobs are process management and file management.
- **Shell:** the command interpreter, the bridge between user and kernel. Unix shells include Bourne-like shells (sh, ash, ksh, bash) and C-shell-like shells, and Ubuntu's /bin/sh is Dash.
- **Files and directories:** all data is held in files, organised into an upside-down tree called the file system.

Users log in with a case-sensitive user ID and password and then get the **$ prompt**.

## Standard input, output and redirection

**Standard input** is where the OS normally expects input (the keyboard), and **standard output** is where it sends output (the monitor). **Standard error** is where error messages are written. In Unix all three can be **redirected**:

- **>** sends a command's output to a file, **overwriting** it, so `echo hello > testfile01.txt` leaves the file holding just "hello".
- **>>** **appends** the output to the end of an existing file.
- **<** takes the command's input from a file instead of the keyboard.

## Pipes and filters

The **pipe** symbol **|** joins commands so that the **standard output of the command on the left becomes the standard input of the command on the right**, and many commands can be chained. Pipes pass output to another command, not to a file. They are **unidirectional** (left to right), and work only with commands that produce standard output.

A **filter** is a command that takes its input from another program, performs some operation on it, and writes the result to standard output, for example to restructure or cull text.

## Shell programming

A **shell program (script)** is a sequence of shell and OS commands stored in a file. There is one kernel, but there may be several shells running, one for each logged-in user, and each user can customise their shell.

Source: CSC 321 DLC Final.pdf (Computer Operating System course book), Study Session 11 (Unix, its properties, types and architecture), Study Session 12 (standard input and output, redirection, pipes, filters) and Study Session 13 (shell programming)
