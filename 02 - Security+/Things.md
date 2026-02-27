NetFlow
- network traffic
sFlow
- network traffic
IPFIX
- network traffic
NXLog
- collecting and centralizing logs

Nessus
- vulnerability scanner

WAF

attestation
- evidence or proof of something.

Digital Signatures

Certificates

SCAP - Security Content Automation Protocol
- monitoring and measuring controls based on NIST - national institute of standards & technology 800-53

SPF - Sender policy framework
- enumerates IP addr of authorized systems permitted to send emails in DNS TXT records for a domain

Root of trust
- module utilized to validate and monitor each boot stage

Kerberos
- uses authentication tickets and ticket-granting tickets to provide session keys

MSA - Master Service
- one company providing another a service
BPA - Business Partners
- collaboration
NDA
- protect confidential information
SLA
- performance metrics and up-time guarantees

**Focus on Incident Handling & Security Automation**
- Preparation → Identification → Containment → Eradication → Recovery → Lessons Learned
- **CIRT (Cyber Incident Response Team)** may be internal or third-party
- Order of volatility matters — collect evidence from most to least volatile: CPU registers/cache → RAM → swap/pagefile → disk → logs → archives.
- Chain of custody — maintaining documented evidence handling so it holds up legally
- SOAR (Security Orchestration, Automation, and Response)
	- Think of it as SIEM + automation + response playbooks combined
	- **SIEM** collects and correlates logs. SOAR acts on them.
- **Playbooks & Runbooks** — playbooks are high-level response plans for specific incident types. Runbooks are the step-by-step technical execution.
