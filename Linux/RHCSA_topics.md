# 💻 RHCSA Exam Topics Checklist 🐧

## **Table of Contents**

* [Essential Linux Commands](#-1-essential-linux-commands)
* [User & Group Administration](#-2-user--group-administration)
* [Software Management](#-3-software-management-yum--dnf)
* [Firewalld & Networking](#-4-firewalld--networking)
* [System Services & Systemd](#-5-system-services--systemd)
* [Storage Management](#-6-storage-management)
* [SELinux](#-7-selinux)
* [Booting & GRUB](#-8-booting-grub--kernel)
* [Containers (Podman)](#-9-containers-podman)
* [File Permissions (Advanced)](#-10-file-access--permissions-advanced)
* [Bash Scripting](#-11-bash-scripting)
* [System Security](#-12-system-security--hardening)
* [Process Management](#-13-process-management)
* [Networking Services](#-14-networking-services)
* [Exam Strategy](#-15-rhcsa-exam-strategy)

---

# 🔧 **1. Essential Linux Commands**

<details>
<summary><strong>Click to expand</strong></summary>

### File & Directory Management

* [ ] Navigate filesystem (`cd`, `ls`, `pwd`)
* [ ] Create/remove files & directories
* [ ] Copy, move, rename files
* [ ] Use wildcards & globbing
* [ ] View files (`cat`, `less`, `head`, `tail`)
* [ ] Compare files (`diff`)
* [ ] File permissions (`chmod`, `umask`)
* [ ] File ownership (`chown`, `chgrp`)
* [ ] Hard links & soft links

### Viewing & Editing Text

* [ ] Use `grep` with regex
* [ ] Use `sed` for search/replace
* [ ] Use `awk` for column extraction
* [ ] Core `vim` usage

</details>

---

# 👥 **2. User & Group Administration**

<details>
<summary><strong>Click to expand</strong></summary>

* [ ] Create/modify/delete users
* [ ] Create/modify/delete groups
* [ ] User passwords & expiration policies
* [ ] Configure sudo access
* [ ] Manage `/etc/passwd`, `/etc/shadow`, `/etc/group`
* [ ] Configure `/etc/skel` for default user files

</details>

---

# 📦 **3. Software Management (YUM / DNF)**

<details>
<summary><strong>Click to expand</strong></summary>

* [ ] Install/remove/search packages
* [ ] Manage repositories
* [ ] View metadata & verify files
* [ ] Work with DNF modules

</details>

---

# 🔥 **4. Firewalld & Networking**

<details>
<summary><strong>Click to expand</strong></summary>

### Networking Basics

* [ ] Configure static & DHCP networking
* [ ] Manage `/etc/hosts`
* [ ] Test connectivity (`ping`, `curl`, `ss`, `nc`)
* [ ] Configure hostname

### Firewalld

* [ ] Work with zones
* [ ] Allow/block services
* [ ] Add/remove firewall rules
* [ ] Configure rich rules
* [ ] Configure port forwarding

</details>

---

# 🧠 **5. System Services & Systemd**

<details>
<summary><strong>Click to expand</strong></summary>

* [ ] Start/stop/enable/disable services
* [ ] Check service logs (`journalctl`)
* [ ] Analyze & troubleshoot service issues
* [ ] Manage system targets (CLI/GUI)
* [ ] Configure persistent logs

</details>

---

# 🧳 **6. Storage Management**

<details>
<summary><strong>Click to expand</strong></summary>

### Partitions & Filesystems

* [ ] Create partitions (`fdisk`, `parted`)
* [ ] Create filesystems (ext4, xfs)
* [ ] Manual mount/unmount
* [ ] Permanent mounting (`/etc/fstab`)
* [ ] Use UUIDs & labels

### LVM

* [ ] Create PV, VG, LV
* [ ] Extend LV & filesystem
* [ ] Reduce LV (ext4 only)
* [ ] Create & restore snapshots

### Additional Storage

* [ ] Create & activate swap
* [ ] Systemd automount
* [ ] Encrypted storage with LUKS

</details>

---

# 🔐 **7. SELinux**

<details>
<summary><strong>Click to expand</strong></summary>

* [ ] Check SELinux status and modes
* [ ] Manage SELinux booleans
* [ ] Modify SELinux file contexts (`semanage`, `restorecon`)
* [ ] Troubleshoot AVC denials
* [ ] Work with `getenforce` / `setenforce`

</details>

---

# 🐧 **8. Booting, GRUB & Kernel**

<details>
<summary><strong>Click to expand</strong></summary>

* [ ] Modify GRUB kernel parameters
* [ ] Switch kernel versions
* [ ] Reset root password (`rd.break`)
* [ ] Kernel boot troubleshooting

</details>

---

# 📦 **9. Containers (Podman)**

<details>
<summary><strong>Click to expand</strong></summary>

* [ ] Pull images
* [ ] Run containers
* [ ] Expose ports
* [ ] Use persistent volumes
* [ ] Create custom container images
* [ ] Convert containers to systemd services

</details>

---

# 📁 **10. File Access & Permissions (Advanced)**

<details>
<summary><strong>Click to expand</strong></summary>

* [ ] ACLs (list, add, remove)
* [ ] Default ACLs
* [ ] SUID, SGID, Sticky bit
* [ ] File attributes (`chattr`, `lsattr`)

</details>

---

# ✍️ **11. Bash Scripting**

<details>
<summary><strong>Click to expand</strong></summary>

* [ ] Basic script structure (`#!/bin/bash`)
* [ ] Variables
* [ ] Conditionals (if/else)
* [ ] Loops
* [ ] Read input
* [ ] Cron jobs
* [ ] Systemd timers

</details>

---

# 🔒 **12. System Security & Hardening**

<details>
<summary><strong>Click to expand</strong></summary>

* [ ] SSH configuration & key-based auth
* [ ] Locking down services
* [ ] PAM password policies
* [ ] Basic system hardening

</details>

---

# 🔄 **13. Process Management**

<details>
<summary><strong>Click to expand</strong></summary>

* [ ] Monitor processes (`ps`, `top`, `htop`)
* [ ] Kill/stop processes
* [ ] Adjust priorities (`nice`, `renice`)
* [ ] Use `journalctl` for log analysis

</details>

---

# 🛜 **14. Networking Services**

<details>
<summary><strong>Click to expand</strong></summary>

* [ ] Configure NFS client
* [ ] Auto-mount with `autofs`
* [ ] SSH key login setup
* [ ] Basic HTTP service management

</details>

---

# ⭐️ **15. RHCSA Exam Strategy**

<details>
<summary><strong>Click to expand</strong></summary>

* [ ] Strong with man pages
* [ ] Navigate `/usr/share/doc`
* [ ] Perform tasks without internet
* [ ] Work entirely from TTY
* [ ] Confidence using only CLI

</details>
