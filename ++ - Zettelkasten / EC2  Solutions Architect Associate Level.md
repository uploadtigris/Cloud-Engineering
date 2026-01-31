Private vs Public vs Elastic IP
- public IP
	- must be unique across the whole internet
	- can be geolocated easily
- private IP
	- machines connect to WWW using an internet gateway (a proxy)
	- only specified range of IPs can be used as private IP
- Elastic IP (public)
	- you can mask the failure of an instance or software by rapidly remapping the address to another instance in your account
	- can only have 5 in your account
	- ***AVOID using this***
		- reflect poor architecture
		- **Instead, use a random public IP and register a DNS name to it**
		- use a Load Balancer and don't use a public IP

EC2 Placement Groups
- EC2 instance placement strategy
- strategies
	- Cluster - clusters instances into a low-latency group in a single Availability Zone
		- **Great networking!**
		- if AZ fails, all fail
	- Spread - spreads instances across underlying hardware (max 7 instances per group per AZ) -- for **critical application**
		- multiple AZ on diff hardware
	- Partition - spreads instances across many different partitions (rely of different sets of racks) within an AZ. Scales to 100s of EC2 instances per group.

Elastic Network Interfaces (ENI) - Overview
- Virtual Network Card // NIC
- attributes
	- primary private IPv4 && one or more secondary IPv4
	- one elastic IP per private IPv4
	- one public IPv4
	- one or more security groups
	- a MAC address
- you can create ENI independently & attach them on the fly (move them) on EC2 instances for fail over
- bound to a specific availability zone (AZ)

EC2 Hibernate
