## ☁️ Phase 3: Cloud Infrastructure

**Goal:** Migrate what you’ve built to the cloud.  
You’ll learn how to deploy your application to AWS using core services, manage infrastructure as code, and automate deployments with CI/CD.

---

### 🧩 Projects & To-Do List

#### 1️⃣ Set Up Your AWS Environment
- [ ] Create an **AWS Free Tier** account.  
- [ ] Set up the **AWS CLI** locally and configure your credentials:
  ```bash
  aws configure
  ```
- [ ] Verify your access:
  ```bash
  aws s3 ls
  ```

#### 2️⃣ Deploy Your Application to AWS
- [ ] Launch an **EC2 instance** and deploy your app manually to understand the process.  
- [ ] Store any static assets or data in an **S3 bucket**.  
- [ ] Set up **IAM** users and roles with least-privilege permissions.  
- [ ] Configure **security groups** to control inbound and outbound traffic.  
- [ ] Test access to your application via the EC2 public IP or domain.

#### 3️⃣ Implement Infrastructure as Code (IaC)
- [ ] Choose **CloudFormation** or **Terraform** for managing AWS resources.  
- [ ] Write IaC templates to automate:
  - EC2 instance creation  
  - S3 bucket setup  
  - IAM role and policy creation  
- [ ] Deploy your stack:
  ```bash
  # For CloudFormation
  aws cloudformation deploy --template-file template.yaml --stack-name my-app-stack

  # For Terraform
  terraform init
  terraform apply
  ```

#### 4️⃣ Add CI/CD with GitHub Actions
- [ ] Create a `.github/workflows/deploy.yml` file.  
- [ ] Set up environment secrets in your GitHub repository (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY).  
- [ ] Configure workflow steps to:
  - Build your app  
  - Deploy to EC2 or S3 automatically  
- [ ] Test your workflow by committing changes and confirming automatic deployment.

---

### 🧠 Skills Learned
- AWS Core Services (EC2, S3, IAM)  
- Infrastructure as Code (IaC)  
- CI/CD Automation  
- Cloud Security & Deployment Pipelines  
