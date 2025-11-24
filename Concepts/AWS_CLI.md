# **Quick AWS CLI Guide**

### **1. Install & Configure**
```bash
aws configure
```
Enter your **Access Key ID**, **Secret Access Key**, **Region** (e.g., `us-east-2`), and **Output format** (`json`).

### **2. Create an S3 Bucket**
```bash
aws s3 mb s3://your-bucket-name --region us-east-2
```
Replace `your-bucket-name` with a unique name.

### **3. Upload a File**
```bash
aws s3 cp local-file.txt s3://your-bucket-name/
```

### **4. Deleting all contents of a bucket**
```bash
aws s3 rm s3://your-bucket-name --recursive
```

### **5. Delete a Bucket**
```bash
aws s3 rb s3://your-bucket-name --force
```
**Note:** Bucket must be empty.
