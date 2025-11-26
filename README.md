# End-to-End ML Pipeline – Wine Quality Prediction (Regression Problem)

Machine Learning • MLOps • Flask • Docker • AWS EC2 • GitHub Actions CI/CD • Modular Pipeline Architecture

## Project Overview

This is a production-ready End-to-End Machine Learning Pipeline for predicting Wine Quality (Regression Problem).
The project demonstrates real-world ML Engineering + MLOps skills used in top product-based companies.

It includes:

- Modular, config-driven ML pipeline
- Automated ingestion → validation → transformation → model training
- Flask web application for inference
- Docker containerization
- CI/CD pipeline using GitHub Actions
- Deployment on AWS EC2 (production-grade)

This project is designed to showcase ML engineering, scalability, reproducibility, automation, and clean architecture, making it ideal for AI/ML Engineer, MLOps Engineer, Data Scientist, ML Developer roles.

## Problem Statement

Predict wine quality score (0–10) based on physicochemical properties.

Type: Regression

Dataset Example Features:

Fixed acidity,
Volatile acidity,
Citric acid,
Residual sugar,
pH,
Alcohol,
Sulphates,
Chlorides,
Density,
etc.

## Project Architecture

```bash
mlProject/
│
├── src/mlProject/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── config/
│   │   ├── configuration.py
│   │   └── __init__.py
│   │
│   ├── entity/
│   │   └── config_entity.py
│   │
│   ├── utils/
│   │   └── common.py
│   │
│   ├── pipeline/
│   │   └── training_pipeline.py
│   │
│   └── constants/
│       └── __init__.py
│
├── config/config.yaml
├── params.yaml
├── schema.yaml
├── app.py  ← Flask app for prediction
├── main.py ← Pipeline trigger
├── Dockerfile
├── requirements.txt
├── .github/workflows/cicd.yaml
└── README.md
```

## Technologies Used

### Machine Learning

- Regression models (Linear, RandomForest, XGBoost)
- Scikit-learn
- Pandas, NumPy
- Scaler + preprocessing

### Backend

- Flask

### MLOps

- Modular folder structure
- YAML-driven configuration
- Logging + exception handling
- GitHub Actions CI/CD
- Docker containerization
- AWS EC2 deployment

## How to Run the Project Locally

### 1. Create Conda Environment

```bash
conda create -n wine python=3.8 -y
conda activate wine
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Run Training Pipeline

```bash
python main.py
```

### 4. Run Flask App

```bash
python app.py
```

## Docker Setup

### Build Docker Image

```bash
docker build -t wine-quality-app .
```

### Run Docker Container

```bash
docker run -d -p 8080:8080 wine-ml-app
```

## AWS CI/CD Deployment (GitHub Actions + Docker + EC2)

This is production-level deployment used in real companies.

### 1. Create IAM User

1. Go to AWS → IAM → Users → Create User
2. Access type: Programmatic access

Attach policies:

- AmazonEC2FullAccess → manage EC2
- AmazonEC2ContainerRegistryFullAccess → manage Docker images in ECR

Important: Copy Access Key ID and Secret Access Key — you’ll add them to GitHub Secrets.

### 2. Create EC2 Instance

- OS: Ubuntu 22.04
- Type: t2.micro / t3.micro
- Open ports

#### Type Port Purpose

```bash
SSH 22 Login
Custom TCP 5000 Flask
Custom TCP 80 Optional
```

### 3. Install Docker on EC2

```bash
sudo apt update -y
sudo apt install docker.io -y
sudo usermod -aG docker ubuntu
newgrp docker
```

### 4. Configure EC2 as Self-Hosted GitHub Runner

1. Go to GitHub → Repository → Settings → Actions → Runners
2. Click New self-hosted runner → choose OS → follow auto-generated commands.
3. This allows GitHub Actions to deploy directly to your EC2 instance.

### 5. Add GitHub Secrets

Go to GitHub → Repository → Settings → Secrets & Variables → Actions → New repository secret

#### Secret Name Value

```bash
| Secret Name             | Value                                             |
| ----------------------- | ------------------------------------------------- |
| `AWS_ACCESS_KEY_ID`     | IAM user access key                                 |
| `AWS_SECRET_ACCESS_KEY` | IAM → Secret key                                  |
| `AWS_REGION`            | e.g., `us-east-1`                                 |
| `AWS_ECR_REPOSITORY`    | e.g., `wine-ml-repo`                              |
| `EC2_PUBLIC_IP`         | Your EC2 IPv4 address                             |
| `EC2_SSH_KEY`           | Your `.pem` private key content (paste full text) |
```

### 6. GitHub Actions Workflow (.github/workflows/cicd.yaml)

Builds Docker image

- SSH into EC2
- Pulls from repo
- Rebuilds container
- Starts Flask app

### 7. Access Flask Application

- Open browser: http://<EC2_PUBLIC_IP>:8080
- The app is live in production, fully containerized and CI/CD-driven.

## WorkFlows (To update file):

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.py ## Web Application file
