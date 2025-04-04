#!/bin/bash

gcloud container clusters create bitcoin-cluster --num-nodes=3

kubectl apply -f /gke/kafka-cluster.yaml
kubectl apply -f /gke/postgres-deployment.yaml
kubectl apply -f /gke/ingress.yaml
