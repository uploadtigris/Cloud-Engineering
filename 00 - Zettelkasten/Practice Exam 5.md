DSA
- Asymmetric algorithm
- Provides authentication, integrity, and non-repudiation
- Specifically designed for creating a verifying digital signatures
RSA
- Asymmetric algorithm
- a public key used for encryption and a private key used for decryption
- used for secure communications, digital signatures, and key exchange
SHA
- family of cryptographic hash functions designed for various security-related applications, including digital signatures, password storage, secure communications, and data integrity verification
HMAC
- combines a cryptographic hash function with a secret key to provide a means of verifying both the authenticity and integrity of a message or data
- symmetric cryptographic method used to verify both data integrity and authenticity by combining a secret key with a hash function
- It acts as a digital seal, ensuring messages haven't been tampered with in transit and confirming the sender possesses the shared secret.
PBKDF2
- key stretching algorithm
P12
- file format for storing and exchanging personal identity information, including private keys and digital certificates
PKCS
- set of standards and specifications that define various cryptographic techniques, including formats for public keys, private keys, digital signatures, and digital certificates
CRC
- cyclical redundancy check
- non-cryptographic hash function often used for error-checking purposes
Salt
- a type of additional input that increases password complexity and provides better protection against brute-force, dictionary, and rainbow table attacks
- A pseudo-random data added to a password before hashing
- used to prevent the effectiveness of rainbow tables in cracking hashed passwords
Rainbow table
- _precomputed table for caching the outputs of a cryptographic hash function_, usually for cracking password hashes.
Digital Signature 
- cryptographic technique that verifies the authenticity and integrity of digital documents or messages by using a unique encrypted identifier from the sender
Digital Certificate
- An electronic document issued by a trusted Certificate Authority (CA) that binds a public key to an identity (person, organization, or website) and proves ownership of that key.
CRL
- periodic publication of all digital certificates that have been revoked
OCSP
- a protocol that enables on-demand querying of the revocation status of a digital certificate
- the fastest way to check the validity of a single digital certificate
- by having a client (like a web browser) send a real-time request to an **OCSP responder** operated by the Certificate Authority (CA) that issued the certificate

**algorithms used for generating and verifying digital signatures?**

- **ECDSA (Elliptic Curve Digital Signature Algorithm)** - An asymmetric algorithm using elliptic curve cryptography to create and verify digital signatures with smaller, more efficient keys than RSA.
	- provides authentication, integrity, and non-repudiation
	- based on elliptic curve cryptography
	- specifically designed for creating and verifying digital signatures
	- In the ECC family, best digital signature algorithm 
- **RSA (Rivest-Shamir-Adleman)** - A versatile asymmetric algorithm that can perform encryption, decryption, digital signatures, and key exchange using public/private key pairs based on prime number factorization.
- **GPG/PGP (GNU Privacy Guard / Pretty Good Privacy)** - An encryption program/standard that combines symmetric and asymmetric encryption to secure emails and files, often using a "web of trust" model instead of certificate authorities.