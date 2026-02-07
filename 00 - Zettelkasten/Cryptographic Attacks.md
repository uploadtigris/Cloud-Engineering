if algorithm is secure, attacker focus on the implementation

Collisions
- MD5 hash had collisions
- collision: when two plain texts result in the same hash
- **If an attacker can find collisions in a cryptographic hash function, they can substitute malicious data that produces the same hash as legitimate data**

Downgrade attack
- perfectly good algorithm, attacks takes advantage of poor implementation
- SSL Stripping 
	- strips the S off of HTTPS
	- attacker must sit in the middle of the conversation
	- difficult to implement
	- victim's browser page isn't encrypted

![[Pasted image 20260203144558.png]]