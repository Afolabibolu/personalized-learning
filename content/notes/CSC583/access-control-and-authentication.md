# Access Control and Authentication

## Access control

Access control, in the general sense, covers authorization, authentication, access approval and audit. **Subjects** perform actions and **objects** are the resources being protected; both are software entities. Giving every process a user starts the same authority breaks the **principle of least privilege**.

Access control models fall into two classes:
- **Capability-based:** holding an unforgeable reference grants access, like owning a house key.
- **ACL-based:** access depends on whether your identity is on the object's list, like a bouncer checking a guest list.

Access control systems provide four services:
1. **Authorization:** what a subject can do.
2. **Identification and authentication (I&A):** only legitimate subjects can log on.
3. **Access approval:** grants or rejects requests during operation by comparing them with the policy.
4. **Accountability:** records what a subject did.

The basic permissions are **Read**, **Write** and **Execute**.

## Access control models

- **Discretionary access control (DAC):** the object's owner decides who may access it and with what rights.
- **Mandatory access control (MAC):** access is allowed only if rules permit it. It is used for highly sensitive government and military data. Subjects and objects carry **sensitivity labels**, and a subject's level must be equal to or higher than the object's. It is applied as **rule-based** (label-matching) or **lattice-based** access control.
- **Role-based access control (RBAC):** the system, not the owner, sets the policy, and a role is a set of permissions. There are three rules: role assignment, role authorization and transaction authorization.

## Authorization and authentication

**Authorization** defines access policy, for example that HR staff may read employee records. It has a policy definition phase and a policy enforcement phase, and follows least privilege. **Authentication** confirms a claimed identity, whereas identification only states it.

There are three types of authentication:
1. trust in someone known to be genuine, such as a reputable store;
2. comparing attributes with known genuine items, such as watermarks on banknotes;
3. external documents, such as a chain of custody or certificates.

The **factors of authentication** are:
- **knowledge:** something you know, such as a password or PIN;
- **ownership:** something you have, such as a token, ID card or phone;
- **inherence:** something you are, such as a fingerprint, retina or voice.

Lesson Three adds a fourth, **where you are**, for example inside the firewall. Strong authentication checks at least two factors.

## Non-repudiation

**Non-repudiation** means the maker of a statement cannot successfully deny it. In security it ties actions to a unique individual, so key cards and passwords must never be shared. In digital form it provides proof of the **integrity and origin** of data:
- A hash such as **SHA-2** shows the data is unchanged.
- **Digital signatures** within a public-key infrastructure show who sent it. Signing gives no confidentiality, because anyone can use the public key.

To guard against disputed signatures, **trusted third parties** are used, such as forensic analysts and notaries; notaries are preferred.

Source: Lecture One (1).pdf (Lessons Three, Seven and Eight)
