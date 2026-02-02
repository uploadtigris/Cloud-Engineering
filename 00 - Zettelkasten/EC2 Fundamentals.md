[[SSH Troubleshooting]]

Private & Public IP addresses
API Keys & Access Tokens
Types
- Memory optimized
- storage optimized
different sizes

Security Groups
- reference by IP or security group
- basically a firewall
- lives "outside" the EC2 instance
- SOP to maintain separate security group for SSH access
- if timeout --> security group issue
- if "connection refused" --> application error / not launched
- by default
	- **all inbound traffic *blocked***
	- **all outbound traffic *authorized***

Ports to know
- 22 = SSH (Secure Shell) - log into a Linux Instance
- 21 = FTP (File Transfer Protocol) - upload files into a file share
- 22 = SFTP (Secure File Transfer Protocol)
- 80 = HTTP -- access unsecured websites
- 443 = HTTPS -- access secured websites
- 3389 = RDP (Remote Desktop Protocol) -- log into a Windows Instance

SSH
- SSH --> mac, linux, windows 10 and above
- EC2 Instance Connect --> all OS (for linux only amazon linux 2)
- `ssh user@192.168.1.1`
	- creating a key
	- `ssh -i EC2.pem users@192.168.1.1`
		- shows status of key file
	- `chmod 0400 EC2.pem`
		- change the permissions of the file so that only the owner can read the file, and no one else (group or others) has any access
	- `ssh -i EC2.pem users@192.168.1.1`
		- now this command will allow us to remote into another machine

EC2 Instance Roles Demo
- `aws iam list-users`
- need to add IAM roles onto instances for user access
- roles is in IAM
- ***Instance > actions > security > Modify IAM role (choose role)***

EC2 Instance Purchasing
- on-demand instances -- short workload, predictable pricing, pay by second
	- pay for what you use
		- linux/windows -- billing is per second / after first minute
		- all other OS -- billing per hour
	- highest upfront payment
	- no long-term commitment
	- **recommend for ST and Un-interrupted WLs, cannot predict app behavior**
- reserved (1 & 3 years)
	- reserved instances -- long workloads
	- convertible reserved instances -- long WLs w/ flexible instances
- savings plans (1&3 years) -- commitment to an amount of usage, long workload
- spot instances -- shorts WLs, cheap, can lost instances (not reliable)
- dedicated hosts -- book entire physical server, control instance placement
- dedicated instances -- no other customers will share your hardware
- capacity reservation -- reserve capacity in a specific AZ for any duration

Spot Instances & Spot Fleet
- can get a discount of up to 90% as compared to on-demand
- define max spot price and get the instance while current spot price < max
	- hourly spot price varies based on offer and capacity
	- if current spot price > max price
		- stop or terminate your instance
- **when to use**
	- batch jobs, data analysis, or workloads that are resilient to failures