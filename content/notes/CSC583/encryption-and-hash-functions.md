# Encryption and Hash Functions

## Encryption

Encryption encodes information so that only authorised parties can read it. It does not stop interception, but it denies the content to the interceptor. **Plaintext** is turned into **ciphertext** with a key, usually pseudo-random. Encryption protects military and government communication, **data at rest** (files, USB drives) and **data in transit** (the Internet, ATMs, Bluetooth).

**Symmetric-key encryption** uses the same key, a shared secret, to encrypt and decrypt. Having to share that key is its main drawback.
- **Stream ciphers** encrypt one digit (byte) at a time.
- **Block ciphers** encrypt fixed blocks, padding the plaintext. 64-bit blocks were common; AES uses 128-bit blocks.
- Examples: AES (Rijndael), Twofish, Serpent, Blowfish, 3DES, RC4, IDEA.
- A **message authentication code** (for example CBC-MAC) detects tampering. Symmetric ciphers alone cannot give non-repudiation.
- Weak random key generation has broken systems, so high-entropy sources are essential.

**Asymmetric (public-key) encryption** uses a mathematically linked pair of keys. The **public key** encrypts or verifies a signature; the **private key** decrypts or signs. Deriving the private key from the public one is computationally infeasible, so no secret key has to be exchanged. The **three-pass protocol** uses commutative ciphers so neither party ever sends a key.

## Problems with public keys

- **Authenticity of public keys:** solved with a **public-key infrastructure (PKI)**, where **certificate authorities** certify key ownership, or with PGP's "web of trust".
- **Man-in-the-middle:** an attacker substitutes public keys. Certificates reduce the risk, but a compromised CA undoes them. SSL/TLS relies on this approach.
- **Cost:** public-key algorithms are slow, so **hybrid cryptosystems** encrypt a short session key with public keys and the data with a fast symmetric cipher.
- **Key revocation:** a revocation must be spread by pushing or pulling. A leaked key calls for perfect forward secrecy and timestamps.
- Only the **one-time pad** is provably secure against any adversary. Every public-key scheme is open to brute force, so its strength is its "work factor".

Examples include Diffie–Hellman, DSS, ElGamal and RSA.

## Hash functions

A **hash function** maps data of any size to a fixed-size **hash value**. A cryptographic hash makes it easy to check that data matches a stored hash, but hard to find data with the same hash.

**Uses:** hash tables (fast lookup), caches, Bloom filters, finding duplicate or similar records, protecting data (which needs collision resistance), finding similar substrings, geometric hashing, and in cryptography authentication, HMAC message integrity, fingerprinting and efficient digital signatures. To check a message, the sender hashes it and sends the encrypted hash with it; the receiver rehashes and compares.

**Properties:** determinism, uniformity, a defined or variable range, data normalisation, continuity (for similarity search) and **non-invertibility** (one-way).

**Algorithms:** trivial, perfect and minimal perfect hashing, z mod n for uniform data, special-purpose, **rolling hash** (for substring search), **universal hashing** (collision chance 1/n), checksums, SHA-1 and **locality-sensitive hashing**, which tries to make similar items collide.

Source: Lecture One (1).pdf (Lessons Four, Five, Nine and Ten)
