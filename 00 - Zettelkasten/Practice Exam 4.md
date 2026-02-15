Stream Cipher?
Block Cipher
CBC
GCM
- Galois/Counter Mode
- high-performance, authenticated encryption mode for block ciphers (usually AES) that provides both data confidentiality and integrity
ECB
CTM
CFB
TPM
- Trusted Platform Module
- hold encrypt algos and keys, used to check for encrypted signature on boot drive. unencrypts in order to boot.
HSM
- Hardware Security Module
- holds encrypt algos and key, used to encrypt stored and streaming data. can be done with a program and CPU but HSMs are dedicated / secure and faster

Which of the following answers refers to a **legacy symmetric-key block cipher** encryption algorithm?

- DES --> Data Encryption standard
- obsolete

Which of the answers listed below refers to a **deprecated stream cipher used in some legacy** applications, such as WEP?

- RC4
- Rivest Cipher 4
- 1987
- encrypts data byte-by-byte using variable length key
- now considered insecure

Which of the following answers refers to a **deprecated** (l**argely replaced by AES**) symmetric-key block cipher encryption algorithm?

- IDEA
- International data encryption algorithm
- symmetric block cipher for secure data encryption

An IV is a random or pseudo random value used in cryptography to ensure that the same plaintext input does not produce the same ciphertext output, even when the same encryption key is used. The IV is typically used with encryption algorithms in block cipher modes to enhance security by introducing randomness to the encryption process.

- True
- IV (Initialization Vector)

Which of the answers listed below refers to a logical operation commonly used in the context of cybersecurity, particularly in encryption and obfuscation techniques?

- XOR

Which of the following answers refers to a block cipher mode that works by chaining the ciphertext blocks together, such that each ciphertext block depends on the previous block?

- CBC
- Cipher Block Chaining
- symmetric block cipher mode where each plaintext block is XORed with the previous ciphertext block before encryption, ensuring identical plaintext blocks produce unique ciphertext

Which block ***mode*** **transforms a block cipher into a stream cipher** enabling the encryption of individual bits or bytes of data?

- CFB
- mode of operation enhancing security by ensuring each block of plaintext is XORed with the previous ciphertext block before encryption

A block cipher mode that combines a unique counter with encryption key to generate a stream of pseudo-random data blocks which are then used for encrypting data is called:

- CTM
- counter mode
- turns a block cipher into parallelizable stream cipher

Which of the block cipher modes listed below is the simplest/weakest and therefore not recommended for use?

- ECB
- Electronic Codebook
- encrypting identical plaintext blocks int identical ciphertext blocks using the same key

In cryptography, the number of bits in a key used by a cryptographic algorithm is referred to as key size or key length. The key length determines the maximum number of combinations required to break the encryption algorithm, therefore typically a longer key means stronger cryptographic security.

- True

Which of the following answers refers to a centralized server that is used to distribute cryptographic keys and authenticate users and services within a computer network?

- KDC
- key distribution center in Kerberos uses symmetric block ciphers
- primarily AES or older DES
- acts as a trusted third party, encrypting tickets with keys shared only with service servers, while authenticating users
- modern KDC configs are phasing out weak ciphers like RC4 in favor of AES

In a Kerberos-protected network, this type of secure token is granted to users during their initial login to enable them access to multiple network services without the need to re-enter their login credentials.

- TGT
- Ticket Granting Ticket
- **kerberos security token** issued by the KDC after initial user authentication
- not a block chipher algo itself, instead a data structure encrypted using symm algos to securely grant access to network resources.
