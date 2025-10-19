## 🧩 Phase 4: Monitoring & Scaling (Advanced Portfolio Project)

**Goal:** Simulate a production-grade deployment.  
You’ll build, deploy, monitor, and scale a cloud-based application using real-world DevOps tools and practices.

---

### 🚀 Projects & To-Do List

#### 1️⃣ Build a Small Web Service
- [ ] Create a lightweight **Flask app** or **REST API** (e.g., `/health`, `/data` endpoints).  
- [ ] Containerize it with Docker:
  ```bash
  docker build -t flask-service .
  docker run -p 5000:5000 flask-service
  ```
- [ ] Test locally before deployment:
  ```bash
  curl http://localhost:5000/health
  ```

#### 2️⃣ Deploy to Kubernetes in AWS
- [ ] Use **Terraform** to provision:
  - An **EKS (Elastic Kubernetes Service)** cluster  
  - **VPC**, **subnets**, and **security groups**  
- [ ] Configure `kubectl` to connect to your AWS EKS cluster:
  ```bash
  aws eks update-kubeconfig --region <region> --name <cluster-name>
  ```
- [ ] Apply Kubernetes manifests for your Flask app:
  ```bash
  kubectl apply -f deployment.yaml
  kubectl apply -f service.yaml
  ```
- [ ] Verify everything is running:
  ```bash
  kubectl get pods,svc
  ```

#### 3️⃣ Add Monitoring with Prometheus & Grafana
- [ ] Deploy **Prometheus** and **Grafana** to your cluster using Helm:
  ```bash
  helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
  helm repo add grafana https://grafana.github.io/helm-charts
  helm install prometheus prometheus-community/kube-prometheus-stack
  helm install grafana grafana/grafana
  ```
- [ ] Expose Grafana and log in via the UI.  
- [ ] Add dashboards for CPU, memory, and request latency.  
- [ ] Set up alerts for resource thresholds.

#### 4️⃣ Add Centralized Logging
- [ ] Choose between:
  - **ELK Stack (Elasticsearch, Logstash, Kibana)**  
  - **AWS CloudWatch Logs**  
- [ ] Configure application logs to be collected from pods.  
- [ ] Verify logs are searchable and correlated with app performance metrics.

#### 5️⃣ Test Scaling & Reliability
- [ ] Perform a **load test** using `k6` or `locust`.  
- [ ] Scale up replicas dynamically:
  ```bash
  kubectl scale deployment flask-service --replicas=5
  ```
- [ ] Observe metrics and logs to ensure smooth scaling.  
- [ ] Simulate failure by deleting pods and confirm auto-recovery.

---

### 🧠 Skills Learned
- End-to-End Cloud Infrastructure  
- Kubernetes in AWS (EKS)  
- Monitoring with Prometheus & Grafana  
- Centralized Logging (ELK / CloudWatch)  
- Scaling & Reliability Engineering  
