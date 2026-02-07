open permissions
- very easy to leave a door open
- increasingly common with cloud storage

unsecured admin accounts
- the Linux root account
- can be a misconfiguration
- **disable direct login to the root account**
- protect accounts with admin / root access

Insecure protocols
- some protocols aren't encrypted
	- Telnet, FTP, SMTP, IMAP
- Verify with a packet capture
	- if you can read everything, this is NOT secure
- use encrypted
	- SSH, SFTP, IMAPS, etc.

Default setting
- every app and network device has a default login
- Mirai botnet
	- take advantage of default configurations
	- this is OPEN SOURCE software

Open ports and services
- services will open ports
- often managed with a firewall
- firewall rule-sets can be complex (**possible security risk!**)