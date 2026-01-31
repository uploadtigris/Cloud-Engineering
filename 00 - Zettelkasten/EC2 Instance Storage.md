EBS overview
- what is it?
	- Elastic Block store
	- network drive you can attach toy our instances while they run
	- persist data
	- CCP level - only one instances at a time
	- bound to AZ zone
	- "network USB stick"
	- "Delete on termination attribute" > disabled by default
		- use: preserve Root volume when instance is terminated

EBS Snapshots
- EBS SS Archive
	- 75% cheaper
	- 24 - 72 hours to restore
- Recycle Bins
	- setup rules to retain to prevent accidental deletion
	- 1 day - 1 year
- Fast Snapshot Restore (FSR)
	- force full initialization of snapshot to have no latency on the first use (expensive)

AMI Overview
- **AMI = amazon machine image**
- customization of an EC2 Image
	- software, configs, OS, monitoring...
	- fast boot / config time
- AMI are built for a specific region (can be copied to new AZ)
- you can launch EC2 instances from:
	- A Public AMI: AWS provided
	- your own AMI: you make and maintain yourself
	- An AWS Marketplace AMI: an AMI someone else made (and potentially sells)
- PROCESS
	- start EC2
	- stop instance
	- build an AMI - will also create EBS snapshot
	- launch instances from other AMIs

EC2 Instance Store
- EBS volumes are network drives good , limited performance
- **high-performance hardware disk**
- Better I/O performance
- Lose their storage if stopped (ephemeral)
- buffer / cache / scratch data / temp content
- risk of data loss
- backups and replication are your responsibility

![[Pasted image 20260131114724.png|400]]

EBS Volume Types
- 6 types
	- gp2 / gp3 (SSD) --> balance price and performance
	- io l / io2 Block Express (SSD) --> highest performance SSD volume for mission-critical low-latency or high-throughput workloads
	- st l (HDD) --> low cost HDD volume designed for frequent access
	- sc l (HDD) --> lowest cost HDD volume design for less frequent access
- characterized by Size | Throughput | IOPS (I/O Ops Per Sec)
- EBS Multi-Attach 
	- attach same EBS volume to multiple EC2 instances in the same AZ
	- ea. instance has full read & write permissions to the high-performance volume
	- use case:
		- higher application availability in clustered Linux applications
		- apps must manage concurrent write operations
	- Limitation: **up to 16 EC2 instance at a time**
	- must use a file system that's cluster-aware
- EBS Encryption
	- minimal impact on latency
	- leverages keys from KMS (AES-256)
	- copying a unencrypted snapshot allows encryption
		- create EBS snapshot of volume
		- encrypt using copy
		- create new volume from snapshot
		- attach new volume to original instance
	- snapshots of encrypted volumes are encrypted

Amazon EFS
- Managed NFS , can be mounted on many EC2
- multi-AZ compatible
- highly available, scalable, expensive (3x gp2), pay per use
- use
	- content management, web serving, data sharing, wordpress
- NFSv4.1 protocol
- security group to control access
- compatible with Linux based AMI (not windows)
- encryption at rest using KMS
- POSIX , standard file API
- scales automatically, pay per use, no capacity planning

EFS - performance & storage classes
- EFS Scale
	- 1000+ concurrent , 10GB+/s
	- can grow to Petabyte-scale network
- Performance Mode (set at creation)
	- General Purpose (default) - for latency sensitive
	- Max I/O - high latency, throughput, highly parallel
- Throughput mode
	- **bursting** - 1TB = 50MiB/s & bursting to 100 MiB/s
	- **provisioned** - de-correlated storage to throughput
	- **elastic** - auto scales throughput

