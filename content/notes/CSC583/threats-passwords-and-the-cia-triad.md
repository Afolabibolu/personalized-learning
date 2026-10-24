# Threats, Passwords and the CIA Triad

## Assessing the threat

There are two extreme attitudes to security. One assumes there is no real threat and acts only after an incident, which is reactive. The other overestimates hackers. Both are wrong. Weigh how attractive your system is to intruders against the security measures in place. The greatest external threat is not hackers but **malware and denial of service**.

## Six classes of attack

1. **Malware:** software with a malicious purpose. Viruses replicate, often through the victim's email address book. Trojan horses look benign but carry malware. Worms spread without user action. Ransomware encrypts files for a ransom. Spyware tracks you. Malware is the most prevalent danger.
2. **Security breaches (cracking):** any attempt at unauthorised access, including **social engineering**, which exploits human nature rather than technology.
3. **Denial of service (DoS):** floods a system so legitimate users are blocked. It is probably the most common attack on the Web.
4. **Web attacks:** SQL injection, the most common, and cross-site scripting.
5. **Session hijacking:** taking over an authenticated session. It is complex, so it is less common.
6. **DNS poisoning:** compromising DNS to redirect users to malicious sites.

The Types of Threats slides add insider threats (negligence or malice), eavesdropping and sniffing, unpatched software, brute-force and dictionary attacks, and cloud risks.

## Terminology

- A **hacker** is an expert who learns a system through its flaws. **White hats** report flaws to the vendor and do penetration tests. **Black hats** cause harm and are also called crackers. **Grey hats** are mostly law-abiding.
- **Script kiddies** use downloaded tools without understanding them.
- **Sneakers** are hired to break in legally to assess security.
- **Devices:** a **firewall** filters traffic in and out, a **proxy server** hides internal IP addresses, and an **intrusion-detection system (IDS)** watches for suspicious activity.
- **Activities:** **authentication** checks credentials, and **auditing** reviews logs and procedures against standards.

## Passwords

A password is a secret string used for authentication. Passwords that are too hard to remember get written down, reset often or reused. Good choices combine unrelated words, or take the first letters of a sentence, as in 'TyIgtIoFJ6!'.

**Security factors:**
- how fast an attacker can try guesses;
- how passwords are stored: never as plain text, but in a cryptographically protected form or as a one-way hash.

**Verifying over a network:** plain transmission can be snooped; TLS-encrypted channels are safer; hash-based challenge-response is a further method. **Cracking** uses brute force or dictionary attacks, and tools such as John the Ripper and L0phtCrack test strength.

## The CIA triad

- **Confidentiality:** only authorised users can access information.
- **Integrity:** data has not been changed inappropriately and comes from its claimed source.
- **Availability:** information is there when needed, which includes defending against DoS attacks.

Humans are the weakest link. Security combines **prevention**, such as IDs and passwords, with **detection**, such as audit trails, balanced to fit the context.

Source: Lecture One (1).pdf (Lecture One, Lecture Two, Lesson Six); Types-of-Threats-to-Computer-Security (2).pdf
