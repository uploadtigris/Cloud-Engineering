HTTP
- URL -> Universal Resource Locator
![[Pasted image 20260207132507.png]]
- DNS -> Domain Name System
	- browser cache
	- OS cache
	- DNS resolver
	- DNS Server
		- recursive lookup process
![[Pasted image 20260207132919.png]]
## SSL, TLS, HTTPS
![[Pasted image 20260207133442.png]]

signed certificate
- CA signs the certificate with it's private key
- Client browser has a list of trusted CAs
- browser verifies the certificate with it's store copy of CAs public key

session key
- client generates a random session key
- client uses the server's public key to encrypt the session key
- only the server's public key can decrypt the session key
	- this is asymmetric encryption

"Change cipher spec"
- "I'm done negotiating, and I'm now switching to encrypted communication using the session key we just agreed on."
- this is NOT defining any hash or encryption algorithm, that was determined during the Client Hello and Server Hello messages

Symmetric Encryption
- when client and server has the session key, they use symmetric encryption (like AES) to encrypt/decrypt all data
- symmetric is faster fast asymmetric

SSL/TLS
- TLS (Transport Layer Security) is the successor to SSL
- when someone says HTTPS, they mean HTTP over TLS (historically SSL)
- TLS is **the entire process**
	- TCP handshake occurs at the transport layer
	- TLS takes over
		- certificate exchange and verification
		- the key exchange process
		- negotiating which encryption algos to use (cipher suite)
		- encrypting all the data transmission
		- ensuring data integrity
	- We now only use TLS 1.2 and 1.3