[[AI Study Notes]]

The MIME specification extends the email message format beyond plain text, **enabling the transfer of graphics, audio, and video files over the Internet mail system**. S/MIME is an enhanced version of the MIME protocol that enables email security features by providing encryption, authentication, message integrity, and other related services.

- True

What is the name of a network protocol that enables secure file transfer over SSH?

- SFTP

SFTP is an extension of the FTP protocol that adds support for SSL/TLS encryption.

- False; **SFTP (SSH File Transfer Protocol)** is **not** an extension of FTP. It's a completely separate protocol that runs over **SSH (Secure Shell)**, typically on port 22
- **FTPS (FTP Secure)** is what you're thinking of - it's FTP with SSL/TLS encryption added, running on ports 21 (control) and 990 (implicit FTPS).

A type of cryptographic network protocol for secure data communication, remote command-line login, remote command execution, and other secure network services between two networked computers is known as:

- SSH

A suite of protocols and technologies providing encryption, authentication, and data integrity for network traffic?

- IPSec
	- **Encryption** (ESP - Encapsulating Security Payload)
	- **Authentication** (AH - Authentication Header)
	- **Data integrity** (through hashing)
	- Works at the **network layer** (Layer 3)

Which part of IPsec provides authentication, integrity, and confidentiality?

- ESP
	- encapsulating security payload
	- core IPsec protocol providing confidentiality, data origin authentication, and connection-less integrity for IP packets.
	- Unlike Authentication Header (AH), ESP encrypts the payload, making it a preferred choice for VPNs to prevent eaves dropping and data tampering

Which protocol enables secure, real-time delivery of audio and video over an IP network?

- Secure Real-time Transport Protocol (SRTP)
- extension of RTP designed to provide encryption, message auth, integrity, and replay protection

An encryption protocol primarily used in Wi-Fi networks implementing the WPA2 security standard is called:

- CCMP
- Counter Mode Cipher Block Chaining Message Authentication Code Protocol (CCMP)
- secure, AES-based (Advanced Encryption Standard) encryption protocol for 802.11i (WPA2) wireless networks.
- developed to provide stronger security for wireless LANs (WLAN) by addressing vulnerabilities in the older WEP/TKIP standards.

A security protocol designed to improve the security of existing WEP implementations is known as:

- TKIP
- Temporal Key Integrity Protocol
- legacy wireless security encryption method used in early Wi-Fi protected access (WPA).
- dynamically updates encryption keys for each packet to improve security
- primarily designed as a software-up-gradable patch for old hardware

Which of the following answers refer(s) to **deprecated/insecure encryption protocols** and cryptographic hash functions? (Select all that apply)

- DES --> Data Encryption Standard --> small key size
- MD5 --> Message Direct 5 --> vulnerable to collision attacks
- SHA-1 --> Secure Hash Algo 1 --> collision vulnerabilities. demonstrated by google in 2017
- SSL --> Secure Sockets Layer --> before TLS, vulnerable to POODLE and other attacks
- RC4 --> Rivest Cipher 4 --> multiple vulnerabilities discovered

Examples of techniques used for encrypting information include symmetric encryption (also called public-key encryption) and asymmetric encryption (also called secret-key encryption, or session-key encryption).

- False

Examples of techniques used for encrypting information include symmetric encryption (also called public-key encryption) and asymmetric encryption (also called secret-key encryption, or session-key encryption).

- false, it is backwards
- asymmetric --> public-key encryption
	- uses a key pair: public key (encrypt) and a private key (decrypt)
- symmetric --> secret-key encryption, session key encryption
	- using the **same key** for encryption and decryption

Which of the algorithms listed below are **not** symmetric ciphers? (Select 3 answers)

- DHE --> Diffie-Hellman Ephemeral --> **asymmetric** key exchange \ public-key cryptography
- ECC --> Elliptic Curve Cryptography --> **Asymmetric** --> modern alternative to RSA
- RSA --> Rivest-Shamir-Adleman --> **asymmetric** encryption, public/private key pairs 

Which of the following algorithms do(es) not fall into the category of asymmetric encryption? (Select all that apply)

- AES --> one shared key // symmetric
- DES --> one shared key
- IDEA --> one shared key
- RC4 --> on shared key

The term "KEK" refers to a type of cryptographic key often used in key management systems to add an additional layer of security when encrypting and decrypting other cryptographic keys.

- KEK == Key Encryption Key

Which of the following answers refers to a protocol used to set up secure connections and **exchange of cryptographic keys** in IPsec VPNs?

- **Internet Key Exchange (IKE)**

Which of the following answers refers to a cryptographic key exchange protocol that leverages ECC for enhanced security and efficiency?

- ECDHDE = **Elliptic Curve** Diffie-Hellman **Ephemeral**
- Key exchange protocol using ECC = Elliptic Curve Cryptography --> **Asymmetric**
- provides PFS (perfect forward secrecy) - new keys for each session

Which of the answers listed below refers to a solution designed to strengthen the security of session keys?

- PFS = perfect forward secrecy 
- ensures that each session has a unique, ephemeral (short lived) key
- if one key is compromised, past and future sessions remain secure
- if the server's private key is stolen later, old traffic can't be decrypted

Which of the following answers refers to *a public-key **cryptosystem** used for digital signatures, secure key exchange, and encryption*?

- RSA = Rivest-Shamir-Adleman
- can sign and verify signatures
- key exchange
- encryption

Which cryptographic solution would be best suited for low-power devices, such as IoT devices, embedded systems, and mobile devices?

- ECC = Ellipctic Curve Cryptography
- smallest key sizes
- lower computational requirements
- less power consumption
- less memory usage

Which of the cryptographic algorithms listed below is the least vulnerable to attacks?

- AES = Advanced Encryption Standard
- most secure
- no practical attacks against full AES
- industry standard since 2001