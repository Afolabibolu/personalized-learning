# Why Digital: Communication Abstractions and Signalling

## Why digital?

The purpose of communication technologies is to **empower users to send messages to each other**. There are two main reasons why digital communication, and more generally building systems with the digital abstraction, is a good idea:

1. **The digital abstraction enables the composition of modules to build large systems.**
2. **It allows sophisticated algorithms to process data** to improve the quality and performance of the components.

Yet physical links are **analog** at the lowest level, so data must be converted between digital and analog as it travels. **Analog** representations, like analog TV (a luminance value per point of a picture in scan order) or the analog telephone (sound waves to electrical signals), map well to physical links. Their problem is that **errors accumulate in analog systems**: passing a voltage of 0.12345678 V through a chain of COPY blocks gives something like 0.12?????? V, and the noise added by each stage cannot be undone. A digital system re-interprets each value as 0 or 1 at every stage, so small noise does not build up.

## Clocking transmissions

The sender and receiver must **agree on a clock rate**. Periodic events are timed by a clock signal, and each bit is sent as a number of discrete voltage samples, the **samples per bit**. If only the samples are sent, the receiver **infers a clock edge every time there is a transition** in the received samples, extrapolates the remaining edges from the known sample rate, and chooses the middle sample (or averages all of them) to decide each bit. Two problems must be solved for this to work: **coping with differences between the sender's and receiver's clock frequencies**, and **ensuring frequent transitions between 0s and 1s**.

## Communication abstractions

The simplest network is a **single physical communication link**. At its ends are modules such as the **mapper**, which maps bits to signals and arranges for samples to be transmitted, and the **demapper** at the receiver; **channel coding** and **channel decoding** modules that add and use redundancy to correct errors; and **source coding**, which compresses the original data into a message. A message may be broken into **packets** and sent over several links through switches. Over each link, three abstractions are used: **packets, bits and signals**, which can be thought of as three layers, one on top of the other. The course takes them in the order bits, signals, packets.

The **single-link view** shows one link with the mapper, channel coder and their counterparts; the **network view** shows packets travelling over many links and switches between end points.

Source: CSC 222 Digital Communication lecture slides (Dr Adeniji Oluwashola David), Lecture 1 (Why Digital? Communication Abstractions and Digital Signaling)
