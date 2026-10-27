# Network-Layer Protocols and IP Addressing

## ARP

The **Address Resolution Protocol (ARP)** finds the **MAC address** of a node when its **IP address** is known.

1. The device first checks its **ARP cache** (viewed with `arp -a`).
2. If there is no entry, it broadcasts a request to the whole network.
3. The device with the matching IP address replies with its MAC address.
4. The address is stored in the cache, and communication begins.

Entries are **dynamic** (created automatically and removed periodically) or **static** (entered manually).

## RARP

The **Reverse Address Resolution Protocol (RARP)** does the opposite. A host that knows only its physical address broadcasts a RARP query, and a **RARP server** replies with the host's IP address.

## ICMP

The **Internet Control Message Protocol** lets hosts and routers report IP datagram problems **back to the sender**. It reports errors but does not correct them. ICMP messages travel inside IP datagrams, and **ping** uses ICMP echo request and reply. It handles five errors:

- **Destination unreachable:** the packet cannot be delivered.
- **Source quench:** a congested router asks the source to slow down (congestion control).
- **Time exceeded:** the TTL reached zero, for example in a routing loop, or not all fragments arrived in time.
- **Parameter problem:** a missing or bad value in the header.
- **Redirection:** tells a host to use a better router.

## IGMP

The **Internet Group Management Protocol** supports **multicasting** (one to many) by identifying which hosts on a LAN belong to which groups. Its messages are **Membership Query** (from the router), **Membership Report** (from a host joining a group) and **Leave Report**.

## The IPv4 datagram

| Field | Bits |
| --- | --- |
| Version, IHL | 4 each |
| Type of service | 8 |
| Total length | 16 |
| Identification | 16 |
| Flags | 3 |
| Fragment offset | 13 |
| Time to live, protocol | 8 each |
| Header checksum | 16 |
| Source and destination address | 32 each |

A datagram larger than a network's **MTU** is **fragmented**. All fragments keep the **identification**; the **more-fragments flag** marks all but the last; and the **fragment offset** gives each piece's position in 8-byte units. Each fragment carries its own 20-byte header.

## IPv4 address classes

Addresses are 32 bits, written in dotted decimal. By first byte:

- **Class A** 0–127;
- **Class B** 128–191;
- **Class C** 192–223;
- **Class D** 224–239 (multicast);
- **Class E** 240–255 (reserved).

Each byte must be 0–255, with no leading zeros. The move to **IPv6** uses **dual stack**, **tunnelling** and **header translation**.

Source: CSC322-Combined.pdf (CSC 322 lecture notes), Lecture 5 (ARP, RARP, ICMP, IGMP); the datagram, fragmentation, address classes and IPv6 transition are general knowledge, following the CSC 322 past papers (2020/21 and 2024/25 papers)
