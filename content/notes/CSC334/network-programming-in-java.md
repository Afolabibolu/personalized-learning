# Network Programming in Java

## Clients, servers and java.net

In the **client-server relationship**, the client requests an action and the server performs it and responds. Java's networking classes are in **java.net**. Its **socket-based communications** let programs treat networking like file I/O, reading from and writing to a socket.

There are two kinds of socket:

- **Stream sockets:** a process establishes a **connection** to another, and data flows in continuous streams. They use **TCP** and are **connection-oriented** and reliable.
- **Datagram sockets:** individual **packets** are sent. They use **UDP** and are **connectionless**; packets can be lost, duplicated or arrive out of order, so the programmer must handle reliability. This is why they are not appropriate for everyday programmers.

Connectionless services generally offer **greater performance but less reliability**.

## URLs and web resources

HTTP uses **URIs** to locate resources on the web. An applet can call its AppletContext's **showDocument** method with a **URL** to display a web page, and a JEditorPane's **setPage** method downloads and displays a file from a web server. A JEditorPane generates **HyperlinkEvents** only if it is uneditable.

## Establishing a simple server (five steps)

1. Create a **ServerSocket**: `new ServerSocket(portNumber, queueLength)`. Port numbers run from **0 to 65,535**; those below **1024** are reserved for system services. An in-use or invalid port causes a **BindException**.
2. **Listen** for a client: the **accept** method blocks until a client connects, then returns a **Socket**.
3. Get the Socket's **OutputStream and InputStream**, often wrapped as ObjectOutputStream and ObjectInputStream. Create the output stream first and flush it.
4. **Process:** the server and client communicate through the streams.
5. **Close** the streams and the socket.

A **multithreaded server** can give each accepted Socket its own thread, or draw threads from a pool, to serve many clients at once.

## Establishing a simple client (four steps)

1. Create a **Socket** connected to the server: `new Socket(serverAddress, port)`.
2. Get its input and output streams with getInputStream and getOutputStream.
3. Process the communication.
4. Close the streams and the socket.

The course builds a client/server chat application this way.

## Connectionless communication with datagrams

A **DatagramSocket** sends and receives **DatagramPackets**. Each packet carries the data, its length, and the destination address and port. The server waits on `receive(packet)` and can echo packets back with `send`. No connection is set up first, as in sending mail rather than making a phone call.

Source: CSC 334- Systems Programming - new1.docx (course book), Unit 12 (Java networking, stream and datagram sockets, URLs, reading a file on a web server), Unit 13 (stream-socket server and client), Units 14 and 15 (datagram client and server)
