#!/bin/bash

gcloud functions deploy fraud-detection \
    --runtime python39 \
    --trigger-http \
    --allow-unauthenticated \
    --entry-point detect_fraud \
    --memory 512MB \
    --timeout 60s
