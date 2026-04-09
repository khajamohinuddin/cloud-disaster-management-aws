# Cloud-Based Multi-Regional Disaster Management & Recovery System (AWS)

## Overview

This project presents a cloud-native, multi-regional disaster management system designed to ensure high availability, rapid response, and automated recovery during critical events.

Built using AWS services, the system simulates real-time disaster scenarios (such as floods, earthquakes, and cyclones) and orchestrates alerting, logging, and recovery workflows across distributed regions.

---

## Key Features

* Multi-region deployment for high availability
* Real-time alert processing using AWS Lambda
* Multi-channel notifications via AWS SNS and Telegram Bot
* Event logging using DynamoDB
* Automated recovery workflow for high-severity disasters
* Monitoring and logging using CloudWatch

---

## Tech Stack

* AWS (Lambda, SNS, DynamoDB, CloudWatch, EC2, S3)
* Python (Boto3)
* Telegram Bot API

---

## System Architecture

The system follows a serverless, event-driven architecture:

1. Disaster event is triggered via API or input payload
2. API Gateway forwards request to AWS Lambda
3. Lambda processes the event and:

   * Publishes alerts to SNS
   * Sends notifications via Telegram
   * Logs event in DynamoDB
4. For high-severity events:

   * Recovery Lambda triggers failover mechanisms
5. CloudWatch monitors logs and system behavior
6. Backup and data storage handled via S3

Refer to the architecture diagram in `/architecture/architecture_diagram.png`.

---

## Project Structure

```
multi-regional-disaster-management/
│
├── lambda/
│   ├── lambda_alert.py
│   ├── lambda_logger.py
│   ├── lambda_telegram.py
│   └── lambda_recovery.py
│
├── architecture/
│   └── architecture_diagram.png
│
├── docs/
│   └── project_report.pdf
│
├── README.md
└── requirements.txt
```

---

## Sample Input

```json
{
  "disaster_type": "Flood",
  "region": "Andhra Pradesh",
  "severity": "High"
}
```

---

## How It Works

* Event is triggered manually or via API
* Lambda processes and distributes the event
* Notifications are sent instantly
* Event is stored for tracking and analysis
* Recovery workflow is triggered if severity is high

---

## Outcomes

* Improved system reliability using multi-region redundancy
* Reduced response time for disaster alerts
* Demonstrated scalable and fault-tolerant architecture
* Showcased practical use of serverless computing

---

## Future Enhancements

* Integration with real-time weather APIs
* AI-based disaster prediction models
* Mobile application for user alerts
* Location-based alert system
* Secure data handling and access control

---

## Author

Khaja
AI & Data Science Student
KL University

---

## Note

This project demonstrates a conceptual implementation of a disaster management system using AWS cloud services.
