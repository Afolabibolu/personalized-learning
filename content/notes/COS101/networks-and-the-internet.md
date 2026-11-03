# Computer Networks and the Internet

## Networks

A **computer network** connects two or more autonomous computers, which may be located anywhere. Networks are classed by coverage:

- a **LAN** covers a room, building or campus;
- a **MAN** covers a city;
- a **WAN** covers a country or the globe;
- a **PAN** connects personal devices, by USB or wirelessly by Bluetooth.

Networks share hardware, software and information, and support communication (e-mail) and remote or distributed computing (grid computing).

The **topology** is the layout of devices and links:

- **Bus**: all devices share one cable.
- **Star**: devices connect to a central hub or switch. It is the most common in Ethernet LANs; the extended star is a **tree**.
- **Ring**: a frame travels round the loop. A dual ring sends data both ways, and token passing uses a ring.
- **Mesh**: all nodes are linked, for redundancy and fault tolerance. It is used by banks, but it is expensive.

**Media** are twisted-pair, coaxial and **fibre-optic** cable (high capacity, low noise and resistant to interference) or wireless (radio, microwave, infrared). **Devices** include hubs, switches, routers, access points, network interface cards and **modems**, which modulate and demodulate signals. In a **client/server** network a dedicated server answers client requests; in **peer-to-peer** every computer has equal responsibilities.

## The Internet

The **Internet** is a **network of networks**, created by **ARPA** and the US Department of Defense for scientific and military communication. In **1968** DARPA contracted BBN to build ARPAnet, and Vint Cerf's TCP specification followed in **1974**. It is a **packet-switching** network: messages are broken into packets that travel separately and are reassembled. **Circuit switching**, by contrast, gives a dedicated channel. All its computers use **TCP/IP**.

Every host has a unique **IP address**, a 32-bit number written as four parts from 0 to 255 (205.46.117.104). A **subnet mask** gives the network address when ANDed with the host address: 192.252.12.14 with 255.255.255.0 gives **192.252.12.0**. The **Domain Name System (DNS)** maps names such as ibm.com to IP addresses.

A **URL** has four parts: protocol, host, port and file, as in http://www.wlv.ac.uk:80/index.html. The default web port is **80**. An e-mail address is local part @ domain.

## Services

- The **World Wide Web** is a service on the Internet: pages written in **HTML** and fetched with **HTTP** by a **browser**. In HTML, <b> makes bold and <i> italic. So the WWW is not the Internet itself.
- **FTP** copies files.
- **Telnet** runs commands on a remote computer.
- **Search engines** find pages.

An **intranet** is a private company network using Internet standards (HTML, HTTP, TCP/IP). An **extranet** extends it to selected suppliers and customers, often over a VPN. A **firewall** regulates access between the internal network and the Internet.

Source: Week7_ComputerNetwork_InternetCOS101.pdf (CSC 101 slides); CSC 101 compiled by SISTER IZA.pdf (the CSC 101 slides compiled by a student) (communication and Internet slides); COS 101 / CSC 101 past questions. The slides' subnet example prints the network address as 192.152.12.0; ANDing gives 192.252.12.0
