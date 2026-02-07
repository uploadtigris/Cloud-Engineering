pass the hash
- client send auth request to server
- attacker in on-path and receives the username and the hashed password
- encryption can stop this
- salting can help also

Browser cookies and session IDs
- session IDs
	- attacker could use this to gain access to server without any credentials being entered by the victim

Session hijacking (Sidejacking)
- attacker uses the Clients session ID
- prevention
	- encrypt end to end
	- require encryption (HTTPS) --> end to end
	- encrypt session connection between client and VPN concentrator
![[Pasted image 20260203141751.png]]