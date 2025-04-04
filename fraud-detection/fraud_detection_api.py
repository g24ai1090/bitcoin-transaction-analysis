from fastapi import FastAPI, HTTPException
import joblib
import numpy as np

# Load trained model
model = joblib.load("fraud_detection_model.pkl")

app = FastAPI()

@app.post("/detect-fraud")
def detect_fraud(transaction: dict):
    try:
        amount = transaction["amount"]
        fee = transaction["fee"]
        time = transaction["time"]
        
        # Predict fraud
        prediction = model.predict(np.array([[amount, fee, time]]))[0]
        return {"is_fraudulent": bool(prediction)}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
