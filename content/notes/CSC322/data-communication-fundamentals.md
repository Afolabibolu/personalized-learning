# Data Communication Fundamentals

## Communication and its components

**Communication** is the process in which computers transfer information and instructions to each other and share resources. A **computer network** is an interconnected collection of **autonomous** computers: no computer can start, stop or control another.

A communication system has five components:

1. **Message:** the information to be sent (text, audio, video).
2. **Sender:** the device that sends it (computer, phone, camera).
3. **Receiver:** the device that receives it.
4. **Transmission medium (channel):** the wired or wireless link between them.
5. **Protocol:** the set of rules both sides follow; without it the message is meaningless.

Two key Internet protocols are:

- **TCP (Transmission Control Protocol):** divides messages into packets at the source, reassembles them at the destination and checks that they arrived correctly.
- **IP (Internet Protocol):** handles the destination address so each packet reaches the right computer.

A **protocol** defines the rules for exchanging messages between peers, while a **service** is what one layer offers the layer above it.

## Types of data flow

- **Simplex:** one way only; one device sends and the other only receives (a keyboard, a speaker).
- **Half duplex:** both devices send and receive, but not at the same time (a walkie-talkie).
- **Full duplex:** both send and receive at the same time (mobile phones, landlines).

Communication may also be **unicast** (one to one), **multicast** (one to a group) or **broadcast** (one to all).

## Network criteria

A good network is judged on:

- **performance:** transit time, response time, throughput and delay;
- **reliability:** frequency of failure and recovery time;
- **security:** protection from unauthorised access and damage.

The **data rate** depends on the available **bandwidth**, the **number of signal levels** used and the **quality (noise level)** of the channel.

## Transmission and propagation time

- **Transmission time** = message size ÷ bandwidth.
- **Propagation time** = distance ÷ propagation speed.

**Example:** a 1.5-kbyte e-mail (12,000 bits) on a 1 Gbps link takes 12,000 ÷ 10⁹ = **12 μs** to transmit. Over 15,000 km at 2.4 × 10⁸ m/s it takes 1.5 × 10⁷ ÷ 2.4 × 10⁸ = **62.5 ms** to propagate. For a short message, propagation dominates.

Source: CSC322-Combined.pdf (CSC 322 lecture notes), Lecture 1 (definition, components, TCP and IP, types of data communication); service versus protocol, network criteria, data-rate factors and the timing formulas are general knowledge, following the CSC 322 past papers (2021/22 and 2024/25 papers)
