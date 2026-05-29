# 🚀 Automated Cloud Cost Optimization & Remediation System

> Intelligent cloud cost remediation through event-driven serverless automation.

[![AWS](https://img.shields.io/badge/AWS-Cloud-orange)]()
[![Lambda](https://img.shields.io/badge/AWS-Lambda-yellow)]()
[![SNS](https://img.shields.io/badge/AWS-SNS-purple)]()
[![EC2](https://img.shields.io/badge/AWS-EC2-blue)]()
[![CloudWatch](https://img.shields.io/badge/AWS-CloudWatch-green)]()
[![Python](https://img.shields.io/badge/Python-3.13-blue)]()
[![Boto3](https://img.shields.io/badge/Boto3-AWS_SDK-orange)]()

---

## 📌 Project Overview

Cloud costs can quickly increase when development resources remain running during idle periods. Organizations often rely on manual monitoring and delayed interventions, resulting in unnecessary spending and operational overhead.

This project implements a **fully automated, event-driven cost optimization system** using AWS managed services. When an AWS Budget threshold is exceeded, the system automatically triggers a remediation workflow that identifies and stops development EC2 instances while protecting production resources.

The solution follows a **serverless architecture**, requires **zero manual intervention**, and includes a **DRY_RUN safety mechanism** for secure testing before live execution.

---

## 🎯 Problem Statement

Many cloud environments suffer from:

* Development EC2 instances running continuously
* Lack of automated cost governance
* Delayed response to budget threshold breaches
* Manual monitoring and remediation efforts
* Increased operational costs

---

## ✅ Solution

This project automatically:

1. Monitors AWS spending using AWS Budgets
2. Detects budget threshold breaches
3. Publishes alerts through Amazon SNS
4. Triggers an AWS Lambda function
5. Identifies EC2 instances tagged:

```text
Environment=dev
```

6. Stops matching development instances
7. Sends notifications to stakeholders
8. Logs every action in CloudWatch

---

# 🏗️ Architecture

![Architecture](architecture/ARCCC.png)

📂 Detailed Architecture Documentation:

➡️ **[Architecture Folder](architecture/README.md)**

---

# 🔄 End-to-End Workflow

```text
AWS Budget Threshold Exceeded
            │
            ▼
      Amazon SNS
            │
     ┌──────┴──────┐
     ▼             ▼
 Email Alert    AWS Lambda
                    │
                    ▼
          EC2 Instance Discovery
                    │
                    ▼
       Filter Environment=dev
                    │
                    ▼
             DRY_RUN Check
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
    DRY_RUN=true          DRY_RUN=false
    Log Only              Stop Instances
                                │
                                ▼
                     CloudWatch Logs
```

---

# 🛠️ AWS Services Used

| Service           | Purpose                                 |
| ----------------- | --------------------------------------- |
| AWS Budgets       | Cost monitoring and threshold alerts    |
| Amazon SNS        | Event notification and message delivery |
| AWS Lambda        | Serverless automation engine            |
| Amazon EC2        | Compute resources being managed         |
| AWS IAM           | Security and access control             |
| Amazon CloudWatch | Monitoring, logging and observability   |

---

# 🔐 Security Features

### Least Privilege Access

The Lambda function follows IAM best practices and can be configured with:

* ec2:DescribeInstances
* ec2:StopInstances
* CloudWatch logging permissions

### Environment-Based Protection

Only instances tagged:

```text
Environment=dev
```

are eligible for remediation.

Production resources remain protected.

### DRY_RUN Safety Mode

Before enabling live remediation:

```text
DRY_RUN=true
```

simulates the workflow without stopping resources.

---

# ⚙️ Key Features

✅ Automated Cost Governance

✅ Event-Driven Architecture

✅ Serverless Implementation

✅ Real-Time Notifications

✅ CloudWatch Observability

✅ Environment-Based Remediation

✅ Production Safety Controls

✅ DRY_RUN Testing Mode

✅ Boto3 Automation

✅ Least Privilege Security

---

# 📂 Repository Structure

```text
Project-5-Automated-Cost-Optimization-System
│
├── architecture/
│   ├── ARCCC.png
│   └── README.md
│
├── implementation_walkthrough/
│   ├── README.md
│   ├── 1-SNS-TOPIC.png
│   ├── 2-SNS-SUBSCRIPTION.png
│   ├── ...
│
├── lambda_code/
│   └── README.md
│
├── documentation/
│   ├── AWS_Cost_Optimization_Final.pdf
│   └── README.md
│
├── notes/
│   └── README.md
│
├── demo_video/
│   └── README.md
│
└── README.md
```

---

# 📖 Project Resources

## 📐 Architecture

➡️ [View Architecture](architecture/README.md)

---

## 🛠️ Implementation Walkthrough

➡️ [View Implementation Walkthrough](implementation_walkthrough/README.md)

Step-by-step screenshots covering:

* Budget Creation
* SNS Configuration
* Lambda Deployment
* IAM Permissions
* EC2 Tagging
* CloudWatch Logs
* Budget Alerts
* Remediation Testing

---

## ⚡ Lambda Automation Logic

➡️ [View Lambda Documentation](lambda_code/README.md)

Includes:

* Python Workflow
* Boto3 Usage
* EC2 Discovery Logic
* Tag Filtering
* DRY_RUN Validation
* Stop Instance Logic

---

## 📝 Project Notes

➡️ [View Detailed Notes](notes/README.md)

Contains:

* Concepts
* Architecture Explanation
* AWS Service Roles
* Security Design
* Interview Questions
* Common Mistakes
* Learning Outcomes

---

## 📘 Complete Project Documentation

➡️ [Open Full Documentation](documentation/AWS_Cost_Optimization_Final.pdf)

Comprehensive 16-page documentation covering:

* Executive Summary
* Architecture
* IAM Security
* DRY_RUN Design
* Implementation
* Monitoring
* Remediation Proof
* Challenges
* Future Roadmap

---

## 🎥 Project Demo

➡️ [Watch Demo Video](demo_video/README.md)

Demonstrates:

* Budget Alert Generation
* SNS Trigger
* Lambda Execution
* CloudWatch Monitoring
* EC2 Remediation

---

# 📊 Key Outcomes

| Metric              | Result     |
| ------------------- | ---------- |
| Manual Intervention | 0          |
| Architecture Type   | Serverless |
| Monitoring          | CloudWatch |
| Notification System | SNS        |
| Remediation Speed   | ~2 Seconds |
| Production Impact   | None       |
| Dev Coverage        | 100%       |

---

# 🚀 Future Improvements

* Slack Integration
* Microsoft Teams Integration
* AWS Chatbot Notifications
* Multi-Environment Support
* Step Functions Orchestration
* AWS Organizations Support
* Cost Explorer Integration
* RDS Remediation
* EBS Optimization
* NAT Gateway Cleanup
* Multi-Account Governance

---

# 👨‍💻 Author

### Adhithyan Sivaraman T

Cloud & DevOps Engineer

🔗 GitHub: https://github.com/Adhithyan-10

🔗 LinkedIn: [www.linkedin.com/in/adhithyan-sivaraman-t-399b5b362](http://www.linkedin.com/in/adhithyan-sivaraman-t-399b5b362)

---

## ⭐ If you found this project useful

Consider giving the repository a star and exploring other AWS Cloud & DevOps projects in my portfolio.

---

> Building practical AWS Cloud & DevOps projects focused on automation, scalability, security, and operational excellence.
