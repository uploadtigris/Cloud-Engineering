```markdown
## ☸️ Phase 2: Container Orchestration (Intermediate)

**Goal:** Learn Kubernetes the right way — small and local first.  
You’ll build a local cluster, deploy your own app, manage scaling, and visualize it all with Rancher.

---

### 🧩 Projects & To-Do List

#### 1️⃣ Set Up Your Local Kubernetes Cluster
- [ ] Install **k3s** or **minikube** on your local system.  
- [ ] Verify installation using:  
  ```bash
  kubectl version --client
  kubectl get nodes
  ```
- [ ] Configure a **3-node cluster** (one master, two workers).  
- [ ] Confirm all nodes are `Ready`:
  ```bash
  kubectl get nodes -o wide
  ```

#### 2️⃣ Deploy Your Dockerized App
- [ ] Choose or build a simple Dockerized app (e.g., a Flask or Node.js web app).  
- [ ] Create Kubernetes **Deployment** and **Service** YAML manifests.  
- [ ] Apply manifests:
  ```bash
  kubectl apply -f deployment.yaml
  kubectl apply -f service.yaml
  ```
- [ ] Verify pods are running:
  ```bash
  kubectl get pods
  ```

#### 3️⃣ Expose Services & Manage Scaling
- [ ] Expose your app to the cluster network using a **Service**.  
- [ ] Test the app locally using:
  ```bash
  minikube service <service-name>
  ```
- [ ] Scale the app horizontally:
  ```bash
  kubectl scale deployment <deployment-name> --replicas=3
  ```
- [ ] Verify the scaling:
  ```bash
  kubectl get pods -o wide
  ```

#### 4️⃣ Install Rancher for Cluster Management
- [ ] Deploy **Rancher** using Helm or Docker.  
- [ ] Access Rancher UI from your browser.  
- [ ] Add your local cluster to Rancher.  
- [ ] Explore the dashboard to view pods, services, and resource utilization.

---

### 🧠 Skills Learned
- Kubernetes Basics  
- YAML Configuration  
- Container Orchestration  
- Helm Package Management  
- Rancher UI Visualization
```
