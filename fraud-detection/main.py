import joblib
import numpy as np
import json

# Load the trained model
model = joblib.load("fraud_detection_model.pkl")

def detect_fraud(request):
    try:
        request_json = request.get_json()
        amount = request_json["amount"]
        fee = request_json["fee"]
        time = request_json["time"]

        prediction = model.predict(np.array([[amount, fee, time]]))[0]
        return {"is_fraudulent": bool(prediction)}
    except Exception as e:
        return {"error": str(e)}, 400
