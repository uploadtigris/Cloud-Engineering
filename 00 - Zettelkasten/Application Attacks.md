Injection attack
- adding your own info into a data stream
- enabled bc of bad programming

Buffer overflow
- overwriting a buffer of memory
- developers need to perform bounds checking
- not a simple exploit
	- usually crashes the application

Replay attack
- finding useful info transmitted over the network
- need access to the raw network data
- not an on-path attack
	- on-path - gathering info
	- replay - sending info to server to gain access

Privilege escalation
- gain higher-level access to a system
- admin access
- horizontal
	- user A --> user B
- prevent using 
	- anti-virus
	- data execution prevention
	- address space layout randomization

Cross-site request forgery
- logged in , website trusts your browser
- cryptographic token to prevent forgery

![[Pasted image 20260203142733.png]]

Directory traversal
- path traversal
- software vulnerabilities
- app code vulnerability

![[Pasted image 20260203142917.png]]

^^ this type of request is a sign of a directory traversal attack as the ".." is trying to move up a dirrectory