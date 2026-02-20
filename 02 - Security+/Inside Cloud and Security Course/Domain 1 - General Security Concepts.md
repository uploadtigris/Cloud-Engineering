**12% of exam**

Security Controls --> countering and minimizing loss or unavailability

- Categories
	- Technical
	- Physical
	- Managerial
	- Operational

- safeguards --> proactive | coutermeasures --> reactive

- Control Types (can overlap)
	- Deterrent --> discourage
	- Preventive --> stop
	- Detective --> discover or detect
	- Compensating --> other options to aid
	- Corrective --> return to normal
	- Directive --> direct, confine, or control

--------------------------

**CIA**
- Confidentiality
	- only authorized can access
- Integrity
	- data or configs do not change
- Availability

Non-repudiation
- *no one* can deny a transaction
- Digital Signatures
	- doc was not modified after it was signed
	- REMEMBER: **shared accounts** prevent non-repudiation

AAA
- Authentication --> Identity
- Authorization --> Access
- Accounting --> Records

Identification --> subject claims identity (think username)
Authentication --> subjects proves identity (think password)
Authorization --> Access given identity
Accountability --> audit logs and trails

**identifications + authentication + auditing = ACCOUNTABILITY**

Authorization Models
- Non-discretionary Access Control
	- system wide restrictions
- Discretionary Access Control (DAC)
	- every object has an **owner**
- Role Based Access Control (RBAC)
	- roles or groups
- Rule-based Access Control 
	- global rules for all subjects
- MAC - Mandatory Access Control
	- every object has 1+ labels
	- labels determine access based on labels
- Attribute-Based Access Control
	- access based on attributes

Access Control Subjects vs. Objects
- Subjects
	- user, group, service access resources (objects)
- Objects
	- resources > files, folders, shares, printers

Zero Trust
1. Assume breach
2. Verify explicitly
3. Lead Privilege
- security
	- identity is the control plane

Access policy enforcement
- policy enforcement point
	- enabling, monitoring, and terminating connection b/w subject and object (resource)
	- evaluates requests against policies & applies controls
- policy decision point
	- where access decisions are made
	- considers 5W (who,what,when,where,why)

Zero Trust Network Architecture
- Control Plane --> drives the policy-based decision logic for zero trust
	- Adaptive identity (context of request)
	- Threat Scope Reduction
	- Policy-Drive Access Control
	- Policy Administrator (PA)
		- PA + PE = Policy Decision Point (PDP)
	- Policy Engine (PE)
- Data Plane --> enforces the decisions define in control pane
	- Implicit Trust Zones
		- traditional security; firewalls and other security devices formed a perimeter
	- Subject/System
		- subject > user
		- system >non-human entity user by subject to access resource
	- Policy Enforcement Point

![[Pasted image 20260215192443.png]]

------------------------------------
Deception and Disruption
- Honeypot
	- Only ENTICE, not ENTRAP
	- allowing to download would be considered Entrapment
	- goal is to distract from assets and isolate in a padded cell until you can track them down
- Honeyfile
	- decoy file to attract attention of attack
- Honeytoken
	- fake record inserted into a database to detect data theft
