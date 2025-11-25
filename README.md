# ☁️ Cloud Engineering Roadmap (Networking-Focused)

A personal roadmap documenting my progression from **Help Desk Technician** to **Cloud Engineering** with a strong emphasis on **Linux, Networking, and Cloud Infrastructure Automation**.

This repository stores my notes, labs, diagrams, and hands-on projects as I develop foundational and professional engineering skills.

---

# 🧱 Core Philosophy

Move from “resetting passwords” → to “building automated, scalable, reliable cloud platforms.”

This roadmap emphasizes:

* **Linux mastery (RHCSA-first approach)**
* **Deep networking fundamentals (CCNA path)**
* **Practical DevOps skills (Terraform, GitHub Actions, CI/CD)**
* **Cloud networking & infrastructure (AWS Networking Specialty path)**
* **Production-minded SRE concepts (monitoring, reliability, automation)**

---

# 🚀 Learning Roadmap Overview

| Phase | Focus Area                                            | Why It Matters                                                              |
| ----- | ----------------------------------------------------- | --------------------------------------------------------------------------- |
| 1     | **Linux + RHCSA**                                     | Core skill for DevOps/SRE/Cloud; required for real-world production systems |
| 2     | **Networking Fundamentals → CCNA**                    | Strengthens routing, VPN, DNS, subnets, troubleshooting                     |
| 3     | **Cloud Foundations (AWS CCP + SAA coursework only)** | Learn AWS fundamentals without paying for exams                             |
| 4     | **DevOps Foundations**                                | Git, shell scripting, Docker, CI/CD basics                                  |
| 5     | **Terraform + Ansible (IaC)**                         | Automate cloud infrastructure and configuration                             |
| 6     | **AWS Cloud Networking**                              | VPC, routing, TGW, hybrid infrastructure                                    |
| 7     | **AWS Networking Specialty Prep**                     | Deep networking expertise for Cloud/DevOps roles                            |
| 8     | **SRE & Kubernetes**                                  | Reliability engineering, containers at scale                                |

---

# 🧰 Phase 1: Linux + RHCSA

**Goal:** Become competent in real-world Linux administration.

### Focus

* RHEL/AlmaLinux labs
* Systemd, SELinux, networking, storage
* User/group management
* Bash scripting fundamentals

### Projects

* Install AlmaLinux in a VM
* Automate user and package setup with shell scripts
* Build small automation scripts (service restarts, log parsing, backups)

**Outcome:** Ready for RHCSA exam (even if not taking it).

---

# 🌐 Phase 2: Networking Fundamentals → CCNA

**Goal:** Build strong, job-ready networking fundamentals.

CCNA replaces Network+. It covers:

* IP addressing & subnetting
* Routing fundamentals
* Switching, VLANs, STP
* Firewalls, ACLs
* DNS, DHCP, NAT
* VPNs & tunnels
* Troubleshooting packet flow

**Why this matters:**
DevOps, SRE, and Cloud roles rely heavily on VPC routing, service traffic flow, gateways, DNS failures, and access issues.

---

# ☁️ Phase 3: Cloud Foundations (CCP + SAA Coursework Only)

**Goal:** Learn cloud architecture fundamentals **without paying for tests**.

Recommended courses:

* AWS Cloud Practitioner (course only)
* AWS Solutions Architect Associate (course only)

**Why:**
AWS Networking Specialty assumes you understand foundational AWS architecture, even if you're not certified.

You do *not* need to take the exams — the knowledge is what matters.

---

# 🔧 Phase 4: DevOps Foundations

**Goal:** Learn the core tools used by DevOps/SRE engineers.

* Git & GitHub
* Linux scripting
* Docker containerization
* Basic CI/CD with GitHub Actions

### Projects

* Containerize a small Flask/Node app
* Build GitHub Actions pipelines
* Deploy containers to a VM

---

# 🏗 Phase 5: Infrastructure as Code (IaC)

**Goal:** Provision and automate cloud infrastructure at scale.

### Tools

* **Terraform** (primary IaC tool for cloud roles)
* **Ansible** (config management)

### Projects

* Build VPCs, subnets, route tables with Terraform
* Automate Linux configuration using Ansible
* Create reusable Terraform modules

---

# 🔌 Phase 6: AWS Cloud Networking

**Goal:** Master cloud-level networking concepts.

### Core Topics

* VPC design
* Routing (IGW, NAT, TGW, route tables)
* Load balancers
* Hybrid VPN
* Direct Connect basics
* DNS (Route 53), CloudFront
* Network troubleshooting

### Projects

* Multi-tier VPC
* ALB + EC2 deployment
* Site-to-site VPN simulation using strongSwan
* Multi-account networking architecture

---

# 🎓 Phase 7: AWS Networking Specialty Prep

**Goal:** Build deep expertise in cloud networking.

**Important:**
AWS Networking Specialty **recommends** AWS Solutions Architect — but you do NOT need the cert, only the knowledge (covered in Phase 3).

### Topics

* Advanced routing scenarios
* Transit Gateway deep dive
* VPC peering & private link
* Hybrid & multi-region architecture
* High availability networking patterns

---

# 🧩 Phase 8: SRE & Kubernetes

**Goal:** Learn how production systems stay reliable.

### Topics

* Kubernetes fundamentals
* Observability (logs, metrics, tracing)
* Reliability engineering
* Incident response
* SLIs, SLOs, SLAs
* Automated healing strategies

### Projects

* Deploy app to Kubernetes cluster
* Implement monitoring with Prometheus + Grafana
* Build alerting/automation workflows

---

# 🛠 Tools Breakdown

| Category       | Skills / Tools                                                |
| -------------- | ------------------------------------------------------------- |
| **Linux**      | RHEL/AlmaLinux, systemd, SELinux, Bash                        |
| **Networking** | CCNA topics: routing, VPN, DNS, subnets, ACLs                 |
| **Cloud**      | AWS core services, VPC, IAM, ALB, Route 53                    |
| **IaC**        | Terraform, Ansible                                            |
| **DevOps**     | Docker, GitHub Actions, CI/CD                                 |
| **SRE**        | Kubernetes, Observability, Monitoring, Reliability principles |

---

# 🎯 Long-Term Goal

Become a **DevOps/SRE Engineer** with a specialization in:

* **Cloud networking**
* **Linux platform operations**
* **Infrastructure automation (IaC)**
* **Reliability engineering**

This combines the strongest elements of Cloud, Networking, and DevOps into one powerful career path.

---

# 🧭 Current Next Step

Begin **Phase 1** — RHCSA labs on AlmaLinux (or RHEL Developer subscription).
