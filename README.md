 DevOps Intern Task – Docker, CI/CD & AWS Monitoring

 Overview
This project demonstrates Docker containerization, CI/CD automation using GitHub Actions, and AWS cloud monitoring with alerts.

The application displays:

Hello from DevOps Intern

Task 1: Application Deployment & Automation

 Docker Setup

 Build Docker Image
```bash
docker build -t devops-intern-app .
```

 Run Docker Container
```bash
docker run -d -p 8080:8080 --name devops-intern devops-intern-app
```

 Access the Application
Open your browser and visit:
```
http://localhost:8080
```

 CI/CD (GitHub Actions)

- Public GitHub repository created with proper README
- GitHub Actions workflow configured
- Docker image builds automatically on every push to `main` branch
- CI pipeline verifies successful Docker build


 Task 2: AWS EC2 + CloudWatch + Alerts

 EC2 Deployment
- Launched AWS EC2 instance
- Installed Docker on EC2
- Deployed and ran the containerized application

 CloudWatch Monitoring
- Enabled EC2 monitoring
- Created CloudWatch Alarm:
  - Metric: CPUUtilization
  - Threshold: Greater than 70%
  - Evaluation period configured

 SNS Notification Setup
- Created SNS Topic
- Subscribed email for notifications
- Connected SNS topic to CloudWatch Alarm

 Alert Testing
- Simulated high CPU usage on EC2
- CloudWatch alarm triggered successfully
- Received SNS email alert notification


 Tech Stack
- Docker
- GitHub Actions
- AWS EC2
- AWS CloudWatch
- AWS SNS


