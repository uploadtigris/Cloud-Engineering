## RHCSA → RHCE Study Roadmap

### Phase 1: RHCSA Foundation (8-12 weeks)

**Weeks 1-2: Linux Fundamentals**

- _Linux Bible_ Chapters 1-4: Introduction, shell basics, file system navigation
- _How Linux Works_ Chapters 1-3: Boot process, commands, devices
- **Practice**: Set up a RHEL 9 (or CentOS Stream/Rocky Linux) VM, get comfortable with the command line

**Weeks 3-4: File Management & Text Processing**

- _Linux Bible_ Chapters 5-7: File permissions, text editors (vim!), filters
- **Practice**: Master vim, practice file permissions extensively, work with grep/sed/awk

**Weeks 5-6: System Administration Basics**

- _Linux Bible_ Chapters 8-11: Process management, system monitoring, users/groups
- _How Linux Works_ Chapter 4: Disks and filesystems
- **Practice**: Create users, manage processes, understand systemd basics

**Weeks 7-8: Storage & File Systems**

- _Linux Bible_ Chapters related to storage
- _How Linux Works_ Chapter 4 (continued): Partitions, LVM, mounting
- **Practice**: Create partitions, configure LVM, mount file systems, work with `/etc/fstab`

**Weeks 9-10: Networking & Services**

- _Linux Bible_ Networking chapters
- _How Linux Works_ Chapter 9: Network configuration
- **Practice**: Configure static IPs, hostname resolution, firewalld, basic SSH

**Weeks 11-12: Critical RHCSA Topics**

- SELinux basics (contexts, booleans, troubleshooting)
- Systemd service management
- Scheduled tasks (cron, at)
- Software management (dnf/yum, repositories)
- **Practice**: Mock exams, timed scenarios

### Key RHCSA Skills Checklist

- [ ] Understand and use essential tools
- [ ] Operate running systems (boot targets, processes)
- [ ] Configure local storage (partitions, LVM, file systems)
- [ ] Create and configure file systems (ext4, xfs, NFS)
- [ ] Deploy, configure, and maintain systems
- [ ] Manage users and groups
- [ ] Manage security (firewall, SELinux basics)

### Phase 2: RHCE Advancement (6-8 weeks after RHCSA)

**Weeks 1-2: Ansible Fundamentals**

- Learn YAML syntax
- Ansible installation and configuration
- Inventory files, ad-hoc commands
- **Practice**: Write basic playbooks, use ansible-doc extensively

**Weeks 3-4: Ansible Playbooks & Roles**

- Variables, facts, conditionals, loops
- Handlers and templates (Jinja2)
- Roles and ansible-galaxy
- **Practice**: Create reusable roles, template configurations

**Weeks 5-6: Advanced Automation**

- Ansible Vault for secrets
- Error handling, troubleshooting playbooks
- Managing system configurations with Ansible
- **Practice**: Automate complete system setups

**Weeks 7-8: RHCE Exam Topics**

- Storage management via Ansible
- User/group automation
- Service and firewall configuration
- SELinux automation
- **Practice**: Full automation scenarios, timed mock exams

### Study Tips

**For both exams:**

- These are **performance-based** exams - reading isn't enough, you need hands-on practice
- Set up at least 2-3 VMs to practice multi-system scenarios
- Time yourself - RHCSA is 3 hours, RHCE is 4 hours
- Use `man` pages and documentation during practice (they're allowed in the exam)
- Focus on speed and accuracy

**Resources beyond your books:**

- Red Hat's official exam objectives (free PDFs on their website)
- Practice environments: use VirtualBox/KVM with RHEL 9 or compatible (Rocky Linux, AlmaLinux)
- Sander van Vugt's courses and practice exams (highly recommended)

**Practice routine:**

- Daily: 1-2 hours of reading/learning
- 3-4 times/week: 2-3 hours hands-on labs
- Weekly: Timed full practice exam scenarios