# OS Architecture, Kernels and Shells

## The kernel, user mode and system calls

The **kernel** is the core of the OS. It manages system resources, is one of the first programs loaded at boot, and stays in memory until power-off. The CPU can execute **privileged instructions**, such as those managing memory protection, only in **kernel mode**. User programs run in **user mode**, so they cannot interfere with the OS or with each other.

A user program asks for a service through a **system call**, usually a software interrupt. The interrupt handler switches the mode bit to kernel mode and calls the right kernel routine. An illegal instruction or a forbidden memory access also traps to the OS, which reports an error and ends the program. This separation keeps the system secure and stable.

## Architectures

- **Monolithic:** every OS component sits in the kernel with unrestricted access. It is efficient, but errors are hard to isolate and faulty or malicious code can do damage.
- **Layered:** components are grouped into layers, each talking only to the layers above and below. This makes debugging and modification easier, but a request may pass through many layers, so it is slower.
- **Microkernel:** only a few services, such as low-level memory management, inter-process communication and basic synchronisation, run in the kernel; the rest run in user space and communicate by message passing. A failed user service does not affect the kernel, and the system is easy to extend and portable, but message passing slows it down.
- **Hybrid:** a microkernel with some non-essential code in kernel space for speed, a compromise between monolithic and microkernel designs.

Other kernel types are **nano kernels** (even smaller) and **exokernels** (experimental; they only protect and multiplex raw hardware).

## Functions of the kernel

- memory management, including virtual memory;
- scheduling processes on the processor;
- device management through device drivers;
- system call control;
- managing RAM and I/O requests;
- inter-process communication.

The OS gives the interface between user and hardware; the kernel, which is part of the OS, gives the interface between applications and hardware.

## User interface and shell

The **user interface** sits at the top of the OS. A **command-line interface (CLI)** shows a prompt where commands are typed; a **graphical user interface (GUI)** uses windows, icons and a pointer.

The **shell** is the outermost layer of the OS. It prompts for input, interprets commands for the kernel and handles the output. The two types are:

- **command-line shells:** Bash, cmd, C shell, Bourne shell, Korn shell;
- **GUI shells:** Windows Explorer.

A newer **GCLI** shell combines both.

Source: CSC 321 DLC Final.pdf (Computer Operating System course book), Study Session 3 (kernel, monolithic, layered and microkernel architectures), Study Session 5 (user interface) and Study Session 10 (kernels and shells)
