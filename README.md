📌 Overview of the Bitcoin Analysis Platform, including deployment instructions.

md
Copy
Edit
# 🚀 Cloud-Based Auto-Scaling Bitcoin Transaction Analysis Platform

## 📌 Overview
This project is a **cloud-based** and **auto-scaling** platform that analyzes Bitcoin transactions, detects fraud, and provides real-time analytics using **Google Cloud Platform (GCP)** and **Kubernetes (GKE)**.

## ⚙️ Key Components
- **Kafka Producer:** Fetches Bitcoin transactions and pushes them to Kafka.
- **Kafka Consumer:** Consumes transactions and stores them in BigQuery.
- **Transaction Analyzer API:** FastAPI-based microservice for querying transaction analytics.
- **Fraud Detection Model:** Uses ML to detect fraudulent transactions (Google Cloud Functions).
- **Web Dashboard:** React-based UI for visualizing transaction analytics.
- **Google Kubernetes Engine (GKE):** Deploys and manages microservices.
- **BigQuery:** Stores and processes blockchain transaction data.
- **Cloud IAM & VPC Security:** Manages secure access to services.

---

## 🚀 Deployment Guide

### **1️⃣ Setup Google Cloud Project**
1. Create a **GCP project** and enable the following APIs:
   ```bash
   gcloud services enable compute.googleapis.com \
                           container.googleapis.com \
                           cloudfunctions.googleapis.com \
                           bigquery.googleapis.com \
                           run.googleapis.com
2️⃣ Create & Connect to Kubernetes Cluster

gcloud container clusters create bitcoin-cluster --num-nodes=3
gcloud container clusters get-credentials bitcoin-cluster
3️⃣ Deploy Kafka & PostgreSQL

kubectl apply -f /gke/kafka-cluster.yaml
kubectl apply -f /gke/postgres-deployment.yaml
4️⃣ Deploy Microservices

kubectl apply -f /kafka-producer/deployment.yaml
kubectl apply -f /kafka-consumer/deployment.yaml
kubectl apply -f /transaction-analyzer/deployment.yaml
5️⃣ Deploy Fraud Detection Cloud Function

cd /fraud-detection/
bash cloud_function_deploy.sh
6️⃣ Deploy Web Dashboard

cd /web-dashboard/
npm install
npm run build
gcloud builds submit --tag gcr.io/my-project/web-dashboard
gcloud run deploy bitcoin-fraud-dashboard --image gcr.io/my-project/web-dashboard --platform managed --allow-unauthenticated
7️⃣ Set Up Ingress & Test Services

kubectl apply -f /gke/ingress.yaml
kubectl get ingress
✅ Testing
🔹 API Testing (Transaction Analyzer)

curl http://<TRANSACTION_ANALYZER_IP>:8000/api/transactions
🔹 Fraud Detection Model

curl -X POST https://REGION-PROJECT_ID.cloudfunctions.net/fraud-detection -H "Content-Type: application/json" -d '{"transaction_id": "56789", "amount": 5000}'
🔹 Kafka Logs

kubectl logs -l app=kafka-producer
kubectl logs -l app=kafka-consumer
🏗 Folder Structure

/bitcoin-analysis-platform/
│── /kafka-producer/          # Fetch & push transactions to Kafka
│── /kafka-consumer/          # Consume transactions & store in BigQuery
│── /transaction-analyzer/    # FastAPI for analytics
│── /fraud-detection/         # ML-based fraud detection (Cloud Functions)
│── /web-dashboard/           # React.js frontend
│── /configs/                 # Configuration files
│── /gke/                     # Kubernetes deployment files
│── /scripts/                 # Automation scripts
│── README.md                 # Documentation
│── .gitignore                # Ignore unnecessary files
