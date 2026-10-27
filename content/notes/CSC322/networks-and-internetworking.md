# Network Types, Topologies and Internetworking

## Types of network

A **computer network** is a cluster of computers sharing a communication path in order to share resources. Uses include e-mail and messaging, sharing printers and files, and accessing remote software.

- **PAN (personal area network):** a single person's workspace, 1 to 100 m, using Bluetooth, IrDA or Zigbee. Very fast and cheap.
- **LAN (local area network):** a building or campus of up to a few kilometres, connecting PCs to share printers and data. Early LANs were the Cambridge Ring (1974), Ethernet (Xerox PARC, 1973–74) and ARCNET (1976). LANs use Ethernet or WiFi and are **client/server** (a central server controls access) or **peer-to-peer** (every device contributes equally). A **VLAN** divides one physical network into separate virtual networks.
- **CAN (campus area network):** several buildings of a school or college, 1 to 5 km.
- **MAN (metropolitan area network):** a city, 5 to 50 km, connecting LANs usually over optical fibre; a cable TV network is an example.
- **WAN (wide area network):** above 50 km, with high cost and maintenance; the Internet is the most common example.

## Topologies

- **Bus:** all devices share one cable. Cheap, but a cable fault stops the network and traffic collides.
- **Ring:** each device connects to two neighbours in a loop. Orderly, but one break can stop the ring.
- **Star:** every device connects to a central hub or switch. Easy to manage, but the hub is a single point of failure.
- **Mesh:** every device links to every other. Very reliable but costly in cables and ports.

## Internetworking

**Internetworking** joins separate networks through intermediate devices such as **routers** or **gateways**, so they work as one large network. Joining two LANs with a switch or hub merely extends the LAN; joining them with a router is internetworking, which works at Layer 3. Its three units are:

- **Intranet:** the internal IP network of one organisation, closed to outsiders.
- **Extranet:** an organisation's network with limited connections to other networks.
- **Internet:** the worldwide interconnection of networks that grew from ARPANET.

Internetworking solved isolated LANs, duplicated resources and the lack of network management. Its challenges are interoperability, reliability, centralised support and flexibility.

## Internetwork addresses

- **Data-link (physical) addresses** identify each physical network connection.
- **MAC addresses**, a kind of data-link address, are 48 bits long, written as 12 hexadecimal digits. The first six digits are the manufacturer's **Organizational Unique Identifier (OUI)**, and they are burned into ROM.
- **Network-layer (logical) addresses** are hierarchical, such as IP addresses.

Source: CSC322-Combined.pdf (CSC 322 lecture notes), Lecture 1 (types of computer network) and Lecture 2 (internetworking and internetwork addresses); topologies are general knowledge, following the CSC 322 past papers (2021/22 paper, Question 4c)
