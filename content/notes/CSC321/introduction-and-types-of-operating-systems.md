# Introduction and Types of Operating Systems

## What an operating system is

Software is either **application software**, which accomplishes specific tasks for users (Microsoft Office, a database system), or **system software**, which integrates and manages the hardware so users see the computer as one functional unit. System software consists of the operating system and utilities such as disk formatters and device control software.

An **operating system (OS)** is the software that manages the computer hardware and all other software. It controls every file, every device, every section of main memory and every nanosecond of processing time. It acts as an intermediary between the user and the hardware, providing an environment in which programs run conveniently and efficiently.

**Goals:**

- make user programs easy to run;
- use the hardware efficiently;
- share hardware and software resources;
- make application software portable;
- protect users from one another;
- improve reliability.

An OS must also be able to evolve without disturbing running services.

## History

| Generation | Years | Technology | OS type |
| --- | --- | --- | --- |
| First | 1945–55 | Vacuum tubes | Plug boards, no OS |
| Second | 1955–65 | Transistors | Batch systems |
| Third | 1965–80 | Integrated circuits | Multiprogramming |
| Fourth | since 1980 | Large-scale integration | Personal computers |

Multiprogramming in the third generation kept the CPU busy nearly 100 percent of the time.

## Types

- **Single-user / multi-user** and **single-tasking / multitasking** (MS-DOS is single-tasking).
- **Batch:** jobs are grouped and run with no user interaction; efficiency is measured in **throughput**.
- **Multitasking (time-sharing, interactive, multiprogramming):** several programs reside in memory and share the processor, each getting a slice of time called a **quantum**.
- **Network OS:** runs on servers and manages users, accounts and shared resources such as printers.
- **Distributed OS:** independent computers with their own CPU and memory communicate over a network, giving remote access.
- **Real-time OS:** responses must meet strict deadlines. In **hard** real-time systems even the shortest delay is unacceptable (air bags); in **soft** real-time systems deadlines are less strict (an ATM).
- **Embedded OS:** a specialised OS that runs one task for a device that is not a computer, such as cars, traffic lights or digital cameras.

## Components

The four basic managers are the **memory, processor, device and file managers**, with a **network manager** added later and the **user interface** on top. Every manager must:

1. monitor its resources continuously;
2. enforce the policies that decide who gets what, when and how much;
3. allocate the resource; and
4. deallocate it.

Source: CSC 321 DLC Final.pdf (Computer Operating System course book), Study Session 1 (definition, goals, functions, history), Study Session 2 (types) and Study Session 4 (components)
