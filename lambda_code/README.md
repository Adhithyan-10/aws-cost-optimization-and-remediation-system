# Lambda Function Implementation

👉 **[View Lambda Function Code](./lambda_function.py)**

This folder contains the AWS Lambda function used for automated cloud cost optimization and EC2 remediation.

The function was implemented using:

- Python
- Boto3 (AWS SDK for Python)

The Lambda function is automatically triggered by Amazon SNS whenever AWS Budget alerts are generated.

---

# Function Responsibilities

The Lambda function performs the following operations:

- Receives SNS-triggered budget alert events
- Identifies running EC2 instances
- Filters EC2 instances using resource tags
- Performs Dry Run validation
- Stops EC2 instances during real execution
- Generates execution logs in CloudWatch

---

# AWS Services Used in the Code

- AWS Lambda
- Amazon EC2
- Amazon SNS
- Amazon CloudWatch
- IAM
- AWS Budgets

---

# Boto3 Usage

The project uses the Boto3 SDK to interact with AWS services programmatically.

Boto3 operations used:
- `describe_instances()`
- `stop_instances()`

These APIs allow Lambda to identify and manage EC2 resources automatically.

---

# DRY_RUN Environment Variable

The Lambda function uses an environment variable named:

```python
DRY_RUN
```

Values:
- `true` → Safe testing mode
- `false` → Real execution mode

This prevents accidental stopping of EC2 instances during initial validation.

---

# Tag-Based Filtering

The Lambda function filters instances using:

```python
Environment = dev
```

This ensures that only intended EC2 instances are targeted during automation execution.

---

# CloudWatch Logging

Execution logs are automatically generated in Amazon CloudWatch Logs.

The logs help:
- Monitor Lambda execution
- Verify EC2 stop operations
- Troubleshoot failures
- Audit automation behavior

---

# Automation Workflow

```text
AWS Budget Alert
        ↓
Amazon SNS Trigger
        ↓
AWS Lambda Execution
        ↓
EC2 Instance Detection
        ↓
Dry Run / Real Execution
        ↓
EC2 Stop Operation
        ↓
CloudWatch Logging
```

---

# Lambda Function Logic Overview

The Lambda function performs the following workflow:

1. Receives SNS-triggered budget alert events
2. Uses Boto3 to identify running EC2 instances
3. Filters instances tagged with:
   ```text
   Environment = dev
   ```
4. Checks the `DRY_RUN` variable
5. Either:
   - Simulates stopping the instance
   - Or performs real EC2 stop operation
6. Generates execution logs in CloudWatch

---

# Technologies Used

- Python
- Boto3
- AWS Lambda
- Amazon SNS
- Amazon EC2
- IAM
- Amazon CloudWatch
- Event-Driven Architecture
- Serverless Automation

---

# Key Learning Outcomes

- Event-driven serverless automation
- Infrastructure management using Python and Boto3
- Automated cloud cost optimization
- EC2 automation using Lambda
- IAM permission management
- CloudWatch logging and observability
- Safe testing using DRY_RUN execution
