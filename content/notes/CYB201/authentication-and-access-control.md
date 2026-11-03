# Authentication and Access Control

## Authentication

**Authentication** is the process of **confirming the identity of a user, device or system** before access to a network or information resource is granted. It is **the first line of defence** in preventing unauthorised entry. Standard measures include:

- **Passwords**, which should be complex (upper case, lower case, numbers and symbols), not reused, and kept in password managers.
- **Two-factor** and **multi-factor authentication (MFA)**, which combine something you know, something you have and something you are. MFA is regarded as the **gold standard** of authentication, though attackers seek ways around weaker forms such as SMS codes; app-based authenticators and security keys are recommended.
- **One-time passwords (OTP)**, valid for a single login or transaction.
- **Biometric verification**, using fingerprints, faces or other physical traits.

## Access control

**Access control** refers to the **policies and mechanisms that regulate who can enter a system and what actions they may perform** once access has been granted. It protects sensitive information, prevents unauthorised modification of data and keeps systems operating properly. In general it involves preventing unauthorised users from gaining access to resources, and preventing legitimate users from using resources in unauthorised ways. Access control implements a **security policy** that specifies who or what may access each resource and how.

The main models are:

- **Discretionary access control (DAC)**: an **identity-based** model in which access is based on the identity of the requester, and **owners decide** who may access their resources.
- **Mandatory access control (MAC)**: the **system (administrators)**, not users, decides access, based on security labels and clearances; control is not at the user's discretion.
- **Role-based access control (RBAC)**: access is granted according to **the roles that users hold** in the organisation, which makes permissions easier to manage.

A key best practice is the **principle of least privilege**: grant users **only the access they need for their role**, review access regularly and revoke it for users who no longer need it. Nearly all access controls can be overcome by an attacker with **physical access** to the equipment, so physical access must be restricted and data encrypted.

Source: CYB 201 - Week One slides; CYB 201 - Week Two slides (best practices); CYB 201 Note 1.pdf (access control models); CYB 201 Note 3 Security vulnerabilities.pdf (access-control problems)
