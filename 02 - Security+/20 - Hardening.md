Restricting Applications
- Least functionality
	- only the necessary applications
- Secure Baseline Image
- Allow-listing
	- blocks everything except listed applications
	- **more secure** but complex to manage
- Block-listing
	- allows everything except listed apps
	- easier to manage but **less secure**

Unecessary Services
- Windows
	- services.msc
	- `sc stop [services name]`
- Linux
	- `top` --> process = service
	- find PID
	- `kill pid [PID]`

Trusted Operating Systems (TOS)
- stringent security
- Evaluation Assurance Level 6 (EAL)
	- Level 1 through 6
- Mandatory Access Control (MAC)
	- access permissions determined by policy
- SELinux (Security Enhanced)
	- set of control installed on top of another Linux distro
	- EAP L4+
		- Mac and Linux are normally at this level
- Trusted Solaris
	- secure, multi-level operations with MAC, detailed sys audits, data/process compartmentalization

Updates and Patches
- reverse engineering windows security patches
- **Hot-fix**
	- immediately should be applied
- **Updates**
- **Service Pack**
	- Hot-fixes and updates since release of the operating system
	
- 1. dedicated team to track vendor security patches
- 2. automated system-wide patching for OS and applications
- 3. include cloud
- 4. prioritize
- 5. create test environment
- 6. log the patches
- 7. process for test and deploy firmware updates
- 8. technical process for deploying hotfixes
- 9. evaluate non-critical patches

Patch Management
- planning, testing, implement, audit software packages
- 1. planning
	- Microsoft endpoint configuration manager
- 2. testing
- 3. Implementation

Group Policy
- windows --> `gpedit`
- Security Template
	- Group Policy Objectives
- used to create a secure baseline 
- Base-lining
	- measuring changes in the network, hardware, or software environment
	- "what is normal"

SELinux
- Mandatory Access Control (MAC)
	- system-enforced access control based on subject clearance and the object labels
- Context-based Permissions
	- schemes defined by various properties for a file or process
- Discretionary Access Control (DAC)
	- ea. object has a list of entities that are allowed to access it
- ***SELinux does NOT use DAC but uses MAC***
	- created by the NSA
	- default **context-based permission scheme** that's included in CentOS and RHEL
- User, Role, Type *contexts*
	- User --> what users can access an object
		- most common one
			- Unconfined_u (all users)
			- User_u (Unprivileged users)
			- Sysadmin_u (system administrators)
			- Root (Root user)
	- Role --> defines what role can access a given object
		- object_r --> files and directories
	- Type --> groups objects together that have **similar security requirements**
	- Level --> sensitivity level of file, dir, or processes
- Modes
	- disabled --> SELinux is essentially turned off, MAC is not going to be implemented
	- enforcing --> all security policies enforced
	- permissive --> SELinux is enabled, sec policies not enforced
- Policy types
	- targeted
	- strict --> complicated to enforce, everything is enforced

Data Encryption Level
- different levels of data organization

Secure Baseline
- analyze the state, vulnerabilities and threats
