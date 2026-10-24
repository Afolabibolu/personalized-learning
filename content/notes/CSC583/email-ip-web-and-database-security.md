# Email, IP, Web and Database Security

## Email security

Email uses a store-and-forward model. The mail user agent (MUA) sends an RFC 2822 message to a mail transfer agent (MTA), which finds the recipient's server through DNS and delivers the message. Cryptography protects email in three ways:
- **signing** a message, for integrity and the sender's identity;
- **encrypting the body**, for confidentiality;
- **encrypting server-to-server links**, for example with a VPN, which also hides headers.

**MIME** converts non-ASCII data for SMTP. A **message authentication code** uses a secret key to protect integrity and authenticity.

**Malicious email:**
- **spoofing** forges the sender address, because the core protocols do no authentication;
- **spam and worms** such as Klez and Sober harvest addresses;
- **email bombs** flood a mailbox by mass mailing, list linking or **zip bombs** (a huge compressible file).

The sending IP address can usually be found from the **"Received:"** lines in the header.

## IPsec

IPsec secures IP communication by authenticating and encrypting each packet. It works host-to-host, network-to-network or network-to-host, and provides peer authentication, data-origin authentication, integrity, confidentiality and replay protection. It works at the **Internet layer**, so it protects any application, whereas TLS and SSH work in the upper layers.

- **Authentication Header (AH):** connectionless integrity, data-origin authentication and optional anti-replay.
- **Encapsulating Security Payload (ESP):** adds **confidentiality**, normally protecting only the payload unless tunnelled.
- **Security Associations (SA)** hold the parameters, and **IKE** manages keys.

## Web application security

Most web attacks come from flawed code and unsanitised input:

- **Cross-site scripting (XSS):** injects client-side script into pages other users view. **Reflected (non-persistent)** XSS is the most common type. **Persistent (stored)** XSS is the more devastating and can spread like a worm on social sites.
- **SQL injection:** inserts malicious SQL into an entry field. Its subclasses include classic, blind (inference) and compounded injection.
- **Phishing:** masquerading as a trusted party to steal credentials. Types include spear phishing (about 91% of attacks), clone phishing, whaling (aimed at executives), rogue Wi-Fi, link manipulation, filter evasion, website forgery and phone phishing (vishing).

**Standards:** OWASP (the Top 10) and WASC. **Technology:** black-box and white-box testing, fuzzing, vulnerability scanners and web application firewalls.

## Database security

Database risks include misuse by authorised users, malware, overloads, physical damage, design bugs and data corruption. Controls include access control, auditing, authentication, encryption, integrity controls and backups.

- **System privileges** allow administrative actions, such as create table or backup database.
- **Object privileges** allow operations on objects, such as select, insert and update.

**Evaluation** uses vulnerability assessment or penetration testing, then compliance monitoring, abstraction (single sign-on), database activity monitoring, native audit trails kept away from administrators and privilege reviews.

## Distributed systems

A distributed system's components communicate by passing messages. Its traits are concurrency, no global clock and independent failure. Architectures are **client/server** and **peer-to-peer**. The **Distributed System Security Architecture (DSSA)** provides login, authentication and access control through a universally trusted certificate authority.

Source: Lecture One (1).pdf (Lessons Eleven to Fifteen)
