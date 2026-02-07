system hardening
- updates
- user accounts 
	- password length and complexity
	- account limitations

Encryption
- Full disk encryption (FDE)
	- bit-locker
- Encrypt all network communication
	- HTTPS
	- VPNs

The endpoint

Endpoint detection and response (EDR)
- detect a threat
	- behavioral analysis, machine learning, process monitoring
	- lightweight agent on endpoint
- Investigate the threat
	- root cause analysis
- respond
	- isolate the system, quarantine, rollback
	- can be done via API

Host-based firewall
- software based
- allow / disallow incoming / outgoing traffic

finding intrusions
- host-based intrusion prevention system (HIPS)
- HIPS identification
	- recognize and block known attacks
	- secure OS and app configs, validate incoming requests

Open ports and services
- closing the ports
- next gen firewall can auto open/close ports
- installing apps can open ports
	- sometimes ALL ports

Default password changes

removal of unnecessary software