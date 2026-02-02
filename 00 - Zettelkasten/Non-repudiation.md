Proof integrity
- we can verify that this is what was sent
- verified with the hash (message digest, fingerprint)
	- cannot verify WHO sent the data
	- **any** SMALL change will change the hash

Proof of origin
- digital signature provide non-repudiation
- only sender has the **private key**
- receivers get the **public key**
	- decrypts digital signature and provides the hash
	- receiver can run the text through the hashing algorithm to ensure the hashes match

