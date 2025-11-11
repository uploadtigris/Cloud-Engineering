## **11/9/2025**

I had a conversation with a GPT Chatbot and come up with this roadmap for me to follow for now.

## ERP Cloud Engineering Roadmap

### Phase 1 — Linux Foundations  
- Learn system administration using **Rocky Linux** and *The Linux Bible* by C. Negus 
- Practice user management, networking, automation, and shell scripting  
- Earn the **RHCSA certification** to validate practical Linux skills  

### Phase 2 — Cloud Infrastructure  
- Start with **AWS Certified Cloud Practitioner (CCP)** to understand core services  
- Advance to **AWS SysOps Administrator** and **AWS Networking** to manage production infrastructure  
- Apply Linux knowledge to deploy and maintain secure cloud systems  

### Phase 3 — ERP & Operations Projects  
- Choose an ERP platform (Odoo, SAP, or Oracle Cloud ERP)  
- Integrate ERP systems with **AWS services** (EC2, S3, RDS, etc.)  
- Build small projects focused on automation and operational efficiency  

### Phase 4 — Data Engineering  
- Learn **AWS Data Engineer** concepts (Glue, Athena, Redshift)  
- Develop ETL workflows and analytics pipelines for ERP data  
- Build dashboards and forecasting models for operations and supply chain insights  

### Focus Summary  
- **Core Stack:** Rocky Linux • AWS • ERP Systems  
- **Certifications:** RHCSA • AWS CCP • AWS SysOps • AWS Data Engineer  
- **Goal:** Become an **ERP Cloud Engineer** with expertise in Linux, cloud infrastructure, and data-driven operations

I need to update the rest of my Cloud Engineering roadmap repo to reflect this.
I will begin with going through *the Linux Bible* and practice using Rocky Linux in a VM on my Fedora Workstation in the Virtual Machine Manager Hypervisor.

UPDATE: Cloud Engineering roadmap repo has been updated

## **11/11/25**
- Today is learning about Emulation and getting started with Rocky Linux, a 1 for 1 binary copy of RHEL, and a continuation of CentOS.
- Learning about the Hardware Emulator QEMU. Getting my Desktop running CachyOS Linux ready to run Rocky Linux.
- QEMU basically handles the *User Space* part of the Hypervisor.
- *User space* is a protected area in an operating system where user applications, like web browsers or word processors, run without direct access to the kernel's core functions.
- Learning about KVM -- Kernel-based Virtual Machine ; Turns linux into a "native type 1 hypervisor".
- Learning about Libvert, a virtualization API that allows for universal management of different virtualization technologies on Linux.

Ran the following commands
```bash
#updating the CachyOS system
sudo pacman -Syu
```
```bash
#downloading the required tooling
sudo pacman -Syu qemu virt-manager dnsmasq vde2 bridge-utils openbsd-netcat libvirt
```
*Unpacking the above command:*

qemu --> handles the [User Space](https://en.wikipedia.org/wiki/User_space_and_kernel_space) part of the [Hypervisor](https://en.wikipedia.org/wiki/Hypervisor)

virt-manager --> GUI for handling the virtual machines

dnsmasq --> [DHCP](https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol) support for the Virtual Machines. 

vde2 --> vde stands for "[Virtual Distributed Ethernet](https://en.wikipedia.org/wiki/Virtual_Distributed_Ethernet)" 

bridge-utils --> tools related to [Network Bridging](https://en.wikipedia.org/wiki/Network_bridge)

openbsd-netcat --> "The nc (or netcat) utility is used for just about anything under the sun involving [TCP](https://en.wikipedia.org/wiki/Transmission_Control_Protocol), [UDP](https://en.wikipedia.org/wiki/User_Datagram_Protocol), or [UNIX-domain sockets](https://en.wikipedia.org/wiki/Unix_domain_socket)." ~ [OpenBSD Man Pages](https://man.openbsd.org/nc.1)
```bash
# Checking that the modules have been loaded
❯ lsmod | grep kvm_amd
kvm_amd               258048  0
kvm                  1499136  1 kvm_amd
ccp                   196608  1 kvm_amd
```
They were loaded :)

```bash
# If the modules were NOT loaded, you'll need to load them with modprobe
sudo modprobe kvm_amd
```
```bash
#enabling libvirtd to start at boot
sudo systemctl enable --now libvirtd
```
```bash
#start the service
sudo systemctl start libvirtd
```
```bash
#check that libvirtd is running
systemctl status libvirtd
```
You'll need to add the current user to the libvirt libraries to give them permissions to user them.
```bash
sudo usermod -aG libvirt $(whoami)
```
Then, log out and back in to have the user fully be added to the permissions group.

For me, I was now able to open up a Rocky Linux 10 ISO in Virutal Machine Manager using the now configured QEMU/KVM connection.

***************************************
CachyOS is having issues handling the VDE or Network Bridging. So, I will move to my Fedora 42 Desktop for now where virtualization in Virtual Machine Manager is flawless.

Fedora 43 is available for download but has reported issues. I am waiting until these kinks are ironed out.
***************************************

### Docker vs. VM

- Type 1 Hypervisor: Bare metal. Ex: Proxmox. Gives VMs _direct access_ to Hardware. 
- Type 2 Hypervisor: Runs as an application atop an existing OS. _Simulates_ the hardware environment.

The power of the Docker container is that the Docker file will describe the installation steps and all required dependencies. This way, any computer running docker would be able to run the docker container containing an application without having to save the entire state of the OS.

Situations where VMs excel are:
The environment is completely isolated. Secure. Identical environment down to the OS level.
When we need an environment that is completely replicating some destination environment.


The Linux Kernel Features that make containers possible (these two features form the backbone of container technology)

Cgroups → a Linux kernel feature that allows the management, limitation, and monitoring of resource usage (like CPU and memory) for groups of processes. They help in organizing processes into hierarchical groups, enabling fine-grained control over resource allocation and prioritization. (think “budget of resources to be distributed across the applications”)

Namespaces → partition the linux kernel so that one “set” of processes sees one set of resources while another set of processes sees another set of resources. It is SO isolated that processes with different namespaces cannot see or interact with each other.
