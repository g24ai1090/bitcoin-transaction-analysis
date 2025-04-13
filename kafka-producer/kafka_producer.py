from kafka import KafkaProducer
import json
import requests
import time

# API Token for BlockCypher API
API_TOKEN = "793a7f695a1847e28e3ade37629d4d74"

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='kafka-service:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def get_latest_transactions():
    try:
        # Step 1: Get latest block hash
        latest_block_resp = requests.get(f"https://api.blockcypher.com/v1/btc/main?token={API_TOKEN}")
        latest_block_resp.raise_for_status()
        latest_block = latest_block_resp.json()
        latest_hash = latest_block.get("hash")

        if not latest_hash:
            print("Could not retrieve latest block hash.")
            return []

        # Step 2: Get txids from that block
        block_resp = requests.get(f"https://api.blockcypher.com/v1/btc/main/blocks/{latest_hash}?token={API_TOKEN}")
        block_resp.raise_for_status()
        block_data = block_resp.json()
        txids = block_data.get("txids", [])[:2]  # Limit to first 2 transactions for safety

        transactions = []
        for txid in txids:
            # Step 3: Get transaction details using txid
            tx_resp = requests.get(f"https://api.blockcypher.com/v1/btc/main/txs/{txid}?token={API_TOKEN}")
            tx_resp.raise_for_status()
            transactions.append(tx_resp.json())
            time.sleep(0.3)  # Sleep to respect rate limit (3 requests per second)

        return transactions

    except requests.exceptions.RequestException as e:
        print(f"Error fetching transactions: {e}")
        return []

def send_to_kafka():
    transactions = get_latest_transactions()
    if transactions:
        for tx in transactions:
            # Send the transaction to Kafka
            producer.send('bitcoin-transactions', tx)
            print("Transaction sent to Kafka:", tx.get("hash"))
        producer.flush()  # Ensure all messages are sent
    else:
        print("No transactions found to send.")

if __name__ == "__main__":
    send_to_kafka()
