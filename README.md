# 🛰️ AWS EC2 Instance Metadata Fetcher

![AWS EC2](https://img.shields.io/badge/AWS-EC2-orange)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![Helm](https://img.shields.io/badge/Helm-Chart-red)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Minikube-326CE5)

This project is a complete DevOps solution showcasing scripting, containerization, and Kubernetes deployment using Helm. It includes a Python-based EC2 metadata fetcher supporting both IMDSv1 and IMDSv2 protocols, which runs in a Docker container and is deployed to a Minikube cluster.

---

## 📋 Table of Contents
- [🚀 Project Overview](#-project-overview)
- [🛠 Prerequisites](#-prerequisites)
- [📁 Project Structure](#-project-structure)
- [✅ Scenario 1: Python Metadata Fetcher](#-scenario-1-python-metadata-fetcher)
- [📦 Scenario 2: Docker Containerization](#-scenario-2-docker-containerization)
- [📦 Scenario 3: Helm Deployment](#-scenario-3-helm-deployment)
- [🧪 Complete Workflow](#-complete-workflow)
- [ Conclusion](#-Conclusion)

---

## 🚀 Project Overview

This hands-on project covers:

- Python script for EC2 metadata retrieval using IMDSv1/IMDSv2
- Mock metadata server using Flask (simulating EC2 endpoint)
- Dockerization with Alpine Linux base
- Helm-based Kubernetes deployment on Minikube
- LocalStack support for AWS simulation

---

## 🛠 Prerequisites

Ensure the following tools are installed:
**Required Tools**
- Docker Desktop
- Python 3.8+
- AWS CLI v2
- kubectl
- Helm 3
- Minikube
- LocalStack

---

## Project Structure


ec2-metadata-fetcher/
├── fetch_metadata.py         # Python script for metadata fetching
├── mock_metadata_server.py   # Flask-based EC2 metadata mock server
├── Dockerfile                # Container definition using Alpine + Python
├── helm-chart/               # Helm chart directory
│   ├── Chart.yaml            # Chart metadata
│   ├── values.yaml           # Config values
│   └── templates/
│       └── deployment.yaml   # K8s deployment manifest
└── README.md                 # Project documentation


---

## ✅ Scenario 1: Python Metadata Fetcher

### Features:
- Accepts `v1` or `v2` as an argument (IMDS version)
- Fetches:
  - `instance-id`
  - `instance-type`
  - `availability-zone`
- Outputs data in JSON format
- Works with a Flask mock server simulating EC2 metadata

### Run Locally

**Start the mock metadata server:**

python mock_metadata_server.py

**Run the fetcher:**

python fetch_metadata.py v1
python fetch_metadata.py v2

---

## 📦 Scenario 2: Docker Containerization
Dockerfile (Alpine + Python)
**Build the Docker image:**
docker build -t <your-dockerhub-username>/ec2-fetcher .

**Run the container:**
docker run -it <your-dockerhub-username>/ec2-fetcher /bin/sh

**Push to Docker Hub:**
docker push <your-dockerhub-username>/ec2-fetcher

---

## 📦 Scenario 3: Helm Deployment
Deploy to your local Minikube cluster using Helm.

 **Install the Helm chart:**
helm --install ec2-fetcher ./helm-chart

**Access the pod:**
kubectl get pods

**Exec into the pod:**
kubectl exec -it <pod-name> -- /bin/sh

**Inside the container, run:**
python fetch_metadata.py v1

---

## 🧪 Complete Workflow:

1. Start LocalStack or the mock metadata server to simulate EC2
2. Run the Python fetcher locally to verify metadata retrieval
3. Build the Docker image and test the container
4. Push the Docker image to Docker Hub (optional)
5. Deploy the image to Minikube using Helm
6. Exec into the pod and test the script inside Kubernetes

---

## Conclusion:

This project demonstrates a complete DevOps workflow:
Application development (Python script)
Containerization (Docker)
Orchestration (Kubernetes/Helm)
Local testing (Minikube/LocalStack)
The solution aligns with modern DevOps best practices and can be extended for production use.
