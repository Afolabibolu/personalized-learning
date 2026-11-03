# Computing Systems, Data and Networks

## Layers

The **layers of a computing system**, from the inside out:

- **Information**, the innermost layer, represented in binary.
- **Hardware**: gates, circuits, the CPU and memory.
- **Programming**: making the hardware work, for example with drivers.
- **Operating system.**
- **Application**: solving real-life problems and interacting with users.
- **Communication**: linking to other systems.

The **CPU** (made by Intel, AMD, MediaTek and others) has a **control unit**, which directs the execution of stored instructions, and an **ALU** for arithmetic and logical operations such as comparisons.

**Main memory** is **RAM**, which is volatile and holds the operating system, the running program, its data and intermediate results, and **ROM**, which is non-volatile and holds the booting instructions. Each memory location has a **unique address** that never changes, while its contents can. **Secondary storage**, such as hard disks and cloud storage, is not directly accessible by the CPU. A **KB** is 1,024 bytes; MB, GB and TB are about a million, a billion and a trillion bytes.

## Data

**Data** is raw facts: textual, numeric, pictorial, sound or video. It must be **digitised** before a computer can process it. A **bit** is 0 or 1, a **byte** is 8 bits and a **nibble** 4. **n bits give 2ⁿ values**: 4 bits give 16, and 25 things need 5 bits, because 2⁵ = 32. Hexadecimal (0–9, A–F) is used by humans for addresses and colours; the computer still works in binary.

**ASCII** codes English and Latin characters. **Unicode** extends it to Asian and international characters and symbols, with over 140,000 characters, and its first characters match ASCII. **Images** are grids of **pixels** with **RGB** values from 0 to 255; more pixels mean higher **resolution**. Multimedia uses **lossy** compression, for example the discrete cosine transform, while text uses **lossless** compression.

## Networks

A **network** is a set of **nodes** connected by communication links, so they can share files, printers and the Internet.

- A **LAN** is a small, high-speed network for an office, building or campus.
- A **MAN** spreads over a city.
- A **WAN** spans cities, countries or continents, and is slower than a LAN.

A **server** is a dedicated computer that answers requests from **clients**.

**Topologies**:

- **Bus**: one shared cable. It is cheap, but a break disrupts everything.
- **Star**: a central hub or switch. One device failing doesn't affect others, but hub failure stops the network.
- **Ring**: a closed loop with data flowing one way.
- **Mesh**: every device linked to every other, which gives redundancy but is expensive.
- **Hybrid**: a combination of two or more.

The **Internet** is a giant network of networks using the **TCP** standard. A **protocol** is a set of rules for exchanging messages. (The slides call the Internet "the World Wide Web"; in fact the Web is one service that runs on the Internet.)

Source: COS 102 Lecture 1 (layers, parts of a computer, data representation); COS 102 Networking & The Internet (Lecture 2)
