# Implementation Walkthrough

This document provides a complete step-by-step walkthrough of the AWS Automated Cost Optimization and Governance project implementation.

---

# Step 1 — AWS Budget Creation

![AWS Budget](14-AWS-BUDGET-CREATED.png)

An AWS Budget was created to monitor monthly cloud spending.  
The configured threshold triggers alerts whenever the estimated cost exceeds the defined budget limit.  
This budget acts as the starting point for the automation workflow.

---

# Step 2 — SNS Topic and Subscription Setup

![SNS Subscription](2-SNS-SUBSCRIPTION.png)

An Amazon SNS topic was configured to distribute budget alert notifications.  
Both Email and Lambda subscriptions were attached to the topic to enable alert delivery and automated execution.  
This allows the system to notify users and trigger remediation actions simultaneously.

---

# Step 3 — Lambda Function Implementation

![Lambda Code](4-LAMBDA-CODE.png)

The AWS Lambda function contains the automation logic responsible for identifying and stopping EC2 instances during budget threshold violations.  
The function uses the Boto3 SDK to interact with AWS services programmatically.  
CloudWatch Logs were also enabled for monitoring and debugging execution behavior.

---

# Step 4 — Environment Variable Configuration

![Lambda Environment Variables](5-LAMBDA-ENV-VARIABLES.png)

Environment variables were configured to control Lambda execution behavior dynamically.  
The `DRY_RUN` variable enables safe testing without actually stopping EC2 instances.  
This provides a secure way to validate automation before real execution.

---

# Step 5 — IAM Role and Permissions

![IAM Role Permissions](6-IAM-ROLE-PERMISSIONS.png)

An IAM role with required permissions was attached to the Lambda function.  
The role allows the function to access EC2 resources and perform instance management operations securely.  
Least privilege access principles were followed during permission assignment.

---

# Step 6 — EC2 Instance Validation

![EC2 Instance](7- EC2-INSTANCE.png)

An EC2 instance was launched to simulate a running workload for testing the automation system.  
The Lambda function identifies running instances during budget alert execution.  
This instance acts as the target resource for automated cost optimization.

---

# Step 7 — EC2 Resource Tagging

![EC2 Tags](8-EC2-TAGS.png)

Resource tags were added to improve resource organization and identification.  
Tags help in implementing governance strategies and selective automation logic.  
This also improves cloud resource visibility and management.

---

# Step 8 — SNS Manual Trigger Testing

![SNS Publish Message](9-SNS-PUBLISH-MESSAGE.png)

A manual SNS message was published to simulate a budget alert event.  
This allowed testing of the complete automation pipeline without waiting for actual billing threshold triggers.  
The test validates SNS-to-Lambda integration successfully.

---

# Step 9 — CloudWatch Logs (Dry Run Mode)

![CloudWatch Logs Dry Run](10-CLOUDWATCH-LOGS-(DRY RUN).png)

The Lambda function was initially tested in Dry Run mode.  
The logs confirm that the target EC2 instance was identified successfully without stopping it.  
This step ensures safe verification before enabling real execution.

---

# Step 10 — CloudWatch Logs (Real Execution)

![CloudWatch Logs Real Execution](11-CLOUDWATCH-LOGS-(REAL EXECUTION).png)

After successful validation, Dry Run mode was disabled for real execution testing.  
The logs confirm that the Lambda function successfully stopped the running EC2 instance.  
This demonstrates successful automated cost optimization.

---

# Step 11 — CloudWatch Log Group Monitoring

![CloudWatch Log Group](13-CLOUDWATCH-LOG-GROUP.png)

CloudWatch Log Groups were used for centralized monitoring and troubleshooting.  
Execution logs provide operational visibility into Lambda activity and automation status.  
This improves observability and debugging capabilities within the system.

---

# Step 12 — Email Notification Validation

![Email Notification](16-dry-test-email.png)

SNS Email notifications were successfully delivered during testing.  
This confirms that alert notifications are properly integrated with the monitoring workflow.  
The notification system helps administrators stay informed about budget events and automated actions.

---

# Conclusion

This implementation demonstrates how AWS Budgets, SNS, Lambda, EC2, IAM, and CloudWatch can work together to build an automated cloud cost governance solution.

The project helps:
- Monitor cloud spending
- Trigger automated actions
- Reduce unnecessary EC2 costs
- Improve governance and operational visibility

---

# Future Enhancements

- CloudWatch Dashboard Integration
- Slack / Microsoft Teams Notifications
- Multi-Environment Resource Filtering
- Automated Reporting
- Cost Analytics Dashboard
- Step Functions Based Workflow Automation

