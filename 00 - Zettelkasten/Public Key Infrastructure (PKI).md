**How to trust that a particular person or device is really who they say they are**

policies, procedures, hardware, software, people
- ex. digital certs

Also include binding public keys to people or devices

*Symmetric encryption*
- same key used to encrypt is used to decrypt
- needs to be secret
- "shared secret" // secret key algorithm
- does NOT scale well
- very fast

*Asymmetric encryption*
- public key
	- cannot reverse engineer the private key
- private key

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

two files will be created `id_ed25519`, private key ( do not share ) & `id_ed25519.pub`, public key

Key escrow
- someone else holds your decryption keys