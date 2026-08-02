# Employee Management System - End-to-End DevOps CI/CD Pipeline

## Project Description

This project demonstrates an End-to-End DevOps CI/CD pipeline for a Python Flask-based Employee Management System. The application is integrated with GitHub, Jenkins, Docker, Docker Hub, AWS EC2, Prometheus, Grafana, Node Exporter, Bash scripting, and Cron to automate build, deployment, monitoring, and backup processes.

---

## Tech Stack

- Python Flask
- Git
- GitHub
- Jenkins
- Docker
- Docker Hub
- AWS EC2 (Ubuntu)
- Prometheus
- Grafana
- Node Exporter
- Bash Scripting
- Cron

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/employee-management-devops.git
cd employee-management-devops
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python app.py
```

### 6. Build Docker Image

```bash
docker build -t employee-management .
```

### 7. Run Docker Container

```bash
docker run -d -p 5000:5000 --name employee-app employee-management
```

---

## CI/CD Workflow

1. Developer pushes code to the GitHub repository.
2. GitHub Webhook automatically triggers the Jenkins pipeline.
3. Jenkins builds the Docker image.
4. Jenkins tags the Docker image.
5. Jenkins pushes the image to Docker Hub.
6. Jenkins stops the existing Docker container.
7. Jenkins deploys the latest Docker container on the AWS EC2 instance.
8. Prometheus collects EC2 metrics through Node Exporter.
9. Grafana visualizes the infrastructure metrics using dashboards.
10. Bash script and Cron automate scheduled project backups.

---

## Deployment

The application is deployed on an AWS EC2 Ubuntu instance and runs inside a Docker container.

Application URL:

```
http://<Your-EC2-Public-IP>:5000
```

Replace `<Your-EC2-Public-IP>` with your current EC2 public IP.

---

## Monitoring

Infrastructure monitoring is implemented using:

- Prometheus
- Node Exporter
- Grafana

The monitoring dashboard displays:

- CPU Usage
- Memory Usage
- Disk Usage
- Network Traffic
- Filesystem Usage

---

## Author

**Oviya C M**