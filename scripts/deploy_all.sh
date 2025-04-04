#!/bin/bash

kubectl apply -f /gke/kafka-cluster.yaml
kubectl apply -f /gke/postgres-deployment.yaml
kubectl apply -f /gke/ingress.yaml

gcloud run deploy bitcoin-fraud-dashboard \
    --image gcr.io/my-project/web-dashboard \
    --platform managed \
    --allow-unauthenticated

