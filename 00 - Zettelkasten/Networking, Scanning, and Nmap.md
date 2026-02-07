1. 
![[Pasted image 20260207125105.png|500]]
## nmap flags
- nmap -flag IPADDR

- -sV --> what services are running and their versions
- -sS --> SYN Scan (default and most popular)
- -sU --> UDP Scan
- -O --> determine operating system
- -p- --> scan all 65,535 ports
- -6 --> Enables IPv6 Scanning
- -p 80 --> Port scan of HTTP
- -top-ports 2000 --> will scan the 2000 common ports
- -A --> aggressive scan (enables OS detection, version detection, script scanning, and trace route)
- -T0 --> Timing. T0 is the slowest, **in an attempt to not alert the IDS**. Could take hours.
- -T5 --> the fastest timing

2. What services are running on this IP?
![[Pasted image 20260207130808.png|500]]

**INSECURE:**

- 20/21 - FTP -> transfers files b/w computer using control (21) and data (20) channels
- 23 - Telnet -> provides remote command-line access to another computer
- 25 - SMTP (standard) -> sends email from client to server or b/w mail servers
- 69 - TFTP -> simple file transfer protocol
- 80 - HTTP --> web pages from servers to browsers
- 110 - POP3 -> downloads email from mail server to client, deleting it from server
- 143 - IMAP -> access & manage email on server while keeping messages store remotely
- 161/162 - SNMP (v1/v2) -> monitor/manage network devices; queries (161) and traps/alerts (162)
- 389 - LDAP -> queries/modifies directory services like AD for authentication and authorization
- 445 - SMB -> shares files, printers, and other resources over a network (windows environments)
- 514 - Syslog -> collects and forwards log messages from network devices/systems to central logging server

**SECURE:**

- 22 - SSH/SFTP/SCP -> remote access, file transfer, copy operations (secure)
- 88 - Kerberos -> authenticates users and services using tickets in a trusted network environment
- 443 - HTTPS -> delivers web content over an encrypted connection using SSL/TLS
- 587 - SMTP with STARTTLS -> sends email w/ encryption after initial connection
- 636 - LDAPS -> provides encrypted access to directory services (using SSL/TLS)
- 993 - IMAPS -> access email over an encrypted connection (using SSL/TLS)
- 995 - POP3S -> downloads email over encrypted connection (using SSL/TLS)
- 3389 - RDP (with TLS) -> provides remote desktop access to Windows systems (optional encryption)

**DEPENDS ON IMPLEMENTATION:**

- 53 - DNS
- 67/68 - DHCP
- 1433 - MS SQL
- 3306 - MySQL