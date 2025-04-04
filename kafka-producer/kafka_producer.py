from kafka import KafkaProducer
import json
import requests

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='kafka-service:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Fetch transactions from a public blockchain API
def get_bitcoin_transactions():
    url = "https://api.blockcypher.com/v1/btc/main"
    response = requests.get(url).json()
    return response

# Push transactions to Kafka
def send_to_kafka():
    transaction_data = get_bitcoin_transactions()
    producer.send('bitcoin-transactions', transaction_data)
    producer.flush()
    print("Transaction sent to Kafka:", transaction_data)

# Run the producer
if __name__ == "__main__":
    send_to_kafka()
