# Embedded Systems and Microcontrollers

## Embedded systems

An **embedded system** is a computer system designed for **specific control functions** within a larger system, often with **real-time** computing constraints. It is embedded as part of a complete device that includes hardware and mechanical parts. A typical embedded computer has a CPU, memory and I/O, connected by a shared bus.

Its key characteristic is being **dedicated** to a particular task. Designers can therefore optimize it to **reduce size and cost** and increase **reliability** and **performance**, and many embedded systems are mass-produced. They range from digital watches and MP3 players to traffic lights, factory controllers and the control of nuclear power plants, in telecommunications, networking, transport and medical equipment.

## Characteristics

1. Embedded systems do a **specific task** rather than serve as general-purpose computers. Some have **real-time** performance constraints for safety or usability; others have low requirements, so the hardware can be simplified to cut costs.
2. They are **not always standalone**: many are small parts of a larger device, such as the tuning system in the Gibson Robot Guitar or a subsystem in a car.
3. Their programs, called **firmware**, are stored in **read-only memory** or **flash memory**, and they run with **limited resources**: little memory and a small or no keyboard and screen.

User interfaces range from none, through buttons, LEDs and character LCDs, to touch screens.

## Memory in embedded systems

Embedded systems keep their **firmware** in **ROM** or **flash memory**, which keep their contents without power, and use **RAM** for working data. ROM takes longer to access than RAM but does not lose information when the power is off. The **Harvard architecture**, with separate program and data memories, is often used in embedded applications.

## Microcontrollers

A **microcontroller** is a programmable digital processor **with the necessary peripherals** on the chip. It can be thought of as a microprocessor with built-in peripherals, and may mix analog and digital circuits.

## Microcontrollers versus microprocessors

1. A **microprocessor** needs **external memory** for programs and data, so instructions involve moving data to and from that memory. It usually has **greater computing power** and a **higher clock speed**.
2. A **microcontroller** has the required **on-chip memory** and peripherals.
3. A microcontroller needs few additional interfacing ICs and works as a **standalone** system.
4. Microcontrollers are also called **embedded controllers**. Their clock speeds are limited to a few tens of MHz, and many are application specific.

So a microprocessor suits systems that need computing power and flexibility, such as a personal computer, while a microcontroller suits small, low-cost, dedicated control tasks with fewer parts.

Microcontrollers have gone through a "silent" (invisible) evolution since the early 1970s: their impact is not well known to ordinary users, though the technology has changed greatly.

Source: CSC 412 MICROPROCESSOR INTERFACING.pdf (CSC 412 course material, Adebola K. Ojo), Study Sessions 4, 5 and 12
