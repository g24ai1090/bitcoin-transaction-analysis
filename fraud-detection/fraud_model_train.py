import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load data
df = pd.read_csv("bitcoin_transactions.csv")

# Select features
# Convert timestamp to numeric value (e.g., Unix time)
df['time'] = pd.to_datetime(df['timestamp']).astype(int) / 10**9  # convert to seconds

X = df[['amount', 'fee', 'time']]
y = df['is_fraud']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "fraud_detection_model.pkl")
print("Model saved successfully!")
