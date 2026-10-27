# Overview of the Operating System

## What an operating system is

An **operating system (OS)** is a program that acts as an interface between the user and the computer hardware and controls the execution of all kinds of programs. It manages hardware resources and provides common services for programs. All operating systems manage memory, processing, devices, files and networks.

## The four managers

- **Memory management:** keeps track of which parts of main memory are in use and by whom, decides which process gets memory in multiprogramming, and allocates and deallocates it.
- **Processor management:** decides which process gets the processor, when and for how long (process scheduling). The program that tracks processor and process status is the **traffic controller**.
- **Device management:** manages devices through their drivers, tracks them (the **I/O controller**), and decides which process gets a device and for how long.
- **File management:** keeps track of information, location, use and status of files (the file system).

Other activities include **security** (passwords against unauthorized access), **control over system performance** (recording delays between request and response), **job accounting**, **error detecting aids** (dumps, traces, error messages) and coordination between software and users.

## Types of operating system

- **Batch:** users do not interact with the computer directly; jobs with similar needs are batched together. Problems: no interaction, an often idle CPU, and difficulty setting priority.
- **Time-sharing:** many users at different terminals share one computer at the same time; the CPU switches between jobs so often that each user gets an immediate response.
- **Distributed:** several central processors serve multiple real-time applications and users.
- **Network:** runs on a server and manages data, users, groups, security and shared file and printer access.
- **Real-time:** the time to process and respond to inputs is so small that the system controls its environment.

**Multitasking** executes several jobs by switching between them so often that users can interact with each one; such systems are also called time-sharing systems. **Multiprogramming** is sharing one processor among two or more programs that are in memory at the same time, so the CPU always has a job to run.

## Services

An OS provides **program execution** (loading and running programs as processes, with synchronization, communication and deadlock handling), **I/O operation**, **file system manipulation** (permissions such as read-only or read-write, creating and deleting files and directories, backups), **communication** between processes by shared memory or message passing, **error handling**, **resource management** through schedulers, and **protection**, which controls the access of programs, processes and users to resources and authenticates users by password.

Source: Operating System CSC 421 for DLC2.docx (Ibadan Distance Learning Series, CSC 421 Operating System II), Unit 1
