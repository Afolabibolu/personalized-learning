# Basic Introduction to Linux

## UNIX and Linux

UNIX is an operating system first developed in the 1960s. There are many versions with common features; the most popular are Solaris, Linux and macOS. **Linux** is a "clone" of the original UNIX that contains none of its code. Linux is free and open source, unlike the original UNIX, and command lines work the same on both.

**Why Linux:** it is free, low-cost and very stable; it is called the most secure OS and the best multi-user, multitasking OS; it runs the world's fastest supercomputers; it develops quickly; and it is very popular for servers. Popular distributions include Ubuntu, Fedora/Red Hat and Mandriva. Ubuntu is easy for beginners.

## The terminal and the shell

A **terminal** is a wrapper program that runs a **shell**. Bash is the default shell on most Linux installations. The prompt shows the user name and the machine name. Even on the command line, the mouse is handy for scrolling, copying and pasting.

## The file system

Everything hangs from the **root directory /**. Below it are bin (essential user commands), dev (device files), etc (configuration files) and home (users' home directories). There are directory files and ordinary files.

When you log in, the working directory is your **home directory**. The directory you are in at any moment is the **working (current) directory**, and **pwd** prints its absolute path.

- An **absolute path** gives every parent up to the root, for example /home/Watson/IBT2017/Linux/Session1/file1.
- A **relative path** starts from the current working directory, for example ./Linux/Session1/file1.
- **~** means your home directory, **.** the current directory and **..** the parent directory.

File names: no two files in the same directory can share a name, but files in different directories can. Linux is **case-sensitive**, so Sanger, sanger and SANGER are three different files. Extensions are usually optional.

## Commands

A command has the form `command [-options] [arguments]`, for example `ls -lh /home/Watson`.

- **pwd** shows the working directory.
- **ls** lists contents. Its options include -l (details), -a (hidden files), -lh (readable sizes), -R (recursive) and -lS (sort by size).
- **mkdir dirname** creates a directory.
- **cd path** changes directory. Plain cd goes home, and cd ~user goes to that user's home.
- **rmdir dirname** removes a directory, but only if it is empty. Otherwise it says "Directory not empty"; use rm -r to remove recursively.
- **cp from to** copies, silently overwriting the target. **mv** moves or renames. **rm** removes.
- **man commandname** shows help.

**Shortcuts:**
- Ctrl+A moves to the start of the line.
- Ctrl+C ends a running program.
- Ctrl+D logs out.
- Ctrl+L clears the screen.
- Tab autocompletes, and Tab Tab lists the completions.

Source: Week 9 and 10 Basic Introduction to Linux.pptx
