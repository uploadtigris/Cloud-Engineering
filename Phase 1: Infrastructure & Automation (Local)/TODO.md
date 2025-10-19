# 🐧 Phase 1: Infrastructure & Automation (Local)

**Goal:** Automate and containerize Linux workloads.

---

## ✅ Step-by-Step Checklist

### 🖥️ Setup Environment
- [ ] Install a Linux distribution (Ubuntu Server, Debian, or CentOS) on a local VM using VirtualBox, VMware, or GNOME Boxes  
- [ ] Update and secure the system (`sudo apt update && sudo apt upgrade`)  
- [ ] Configure static IP or ensure SSH access to your VM  

---

### 🌐 Build Your Web Server
- [ ] Choose a web server: **NGINX** or **Apache**  
- [ ] Install it (`sudo apt install nginx` or `sudo apt install apache2`)  
- [ ] Verify the server works by visiting `http://localhost` or the VM’s IP address  
- [ ] Customize your web page content (e.g., simple HTML file in `/var/www/html/`)  

---

### ⚙️ Automate Setup
- [ ] Create a **Bash script** (`setup_webserver.sh`) that:
  - Installs the web server
  - Configures a custom index.html
  - Starts and enables the service  
- [ ] Test your script from a clean VM snapshot  
- [ ] *(Optional)* Recreate the same setup using **Ansible**:
  - Write an `ansible-playbook.yml` with tasks for installation, configuration, and service management  
  - Test it using `ansible-playbook -i inventory.yml ansible-playbook.yml`

---

### 🐳 Containerize the Web Server
- [ ] Install **Docker** on your local system  
- [ ] Create a `Dockerfile` for your web server  
  - Use a base image like `ubuntu` or `nginx`  
  - Copy your `index.html` into the image  
  - Expose port 80  
- [ ] Build and run the image locally  
  - `docker build -t my-webserver .`  
  - `docker run -d -p 8080:80 my-webserver`  
- [ ] Verify your containerized web server by visiting `http://localhost:8080`  

---

### 🧩 (Optional) Use Docker Compose
- [ ] Create a `docker-compose.yml` file that:
  - Defines your **web** container  
  - Optionally defines a **database** container (e.g., MySQL or PostgreSQL)  
  - Configures a network between them  
- [ ] Test starting both services with `docker-compose up -d`  

---

## 🧠 Skills Learned
- Linux Administration  
- Networking Fundamentals  
- Docker & Containerization  
- Scripting & Automation (Bash / Ansible)  
