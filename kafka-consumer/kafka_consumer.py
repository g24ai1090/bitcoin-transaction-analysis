from kafka import KafkaConsumer
import json
from google.cloud import bigquery

# Initialize Kafka Consumer
consumer = KafkaConsumer(
    'bitcoin-transactions',
    bootstrap_servers='kafka-service:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Initialize BigQuery Client
client = bigquery.Client()
dataset_id = "my_project.bitcoin_analysis"
table_id = f"{dataset_id}.transactions"

# Process transactions and insert into BigQuery
for message in consumer:
    transaction = message.value
    rows_to_insert = [{
        "transaction_id": transaction.get("hash"),
        "sender": transaction.get("inputs", [{}])[0].get("addresses", ["unknown"])[0],
        "receiver": transaction.get("outputs", [{}])[0].get("addresses", ["unknown"])[0],
        "amount": transaction.get("outputs", [{}])[0].get("value", 0) / 1e8,  # Convert satoshis to BTC
    }]

    errors = client.insert_rows_json(table_id, rows_to_insert)
    if errors:
        print("Failed to insert:", errors)
    else:
        print("Transaction stored:", rows_to_insert)
