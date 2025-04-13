from kafka import KafkaConsumer
import json
from google.cloud import bigquery
import logging

# Setup logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Starting Kafka consumer for Bitcoin transactions...")

# Initialize Kafka Consumer
try:
    consumer = KafkaConsumer(
        'bitcoin-transactions',
        bootstrap_servers='kafka-service:9092',
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='btc-consumer-group'
    )
    logging.info("Kafka consumer initialized successfully.")
except Exception as e:
    logging.exception("Failed to initialize KafkaConsumer.")
    raise e

# Initialize BigQuery Client
try:
    client = bigquery.Client()
    dataset_id = "virtualbox-assignmnt.bitcoin_analysis"
    table_id = f"{dataset_id}.transactions"
    logging.info(f"BigQuery client initialized. Target table: {table_id}")
except Exception as e:
    logging.exception("Failed to initialize BigQuery client.")
    raise e

# Process messages from Kafka
for message in consumer:
    logging.debug("Received new message from Kafka.")
    transactions = message.value
    logging.debug(f"Raw message value: {transactions}")

    # Handle single or list of transactions
    if not isinstance(transactions, list):
        transactions = [transactions]  # wrap single transaction into a list

    logging.debug(f"Processing {len(transactions)} transaction(s).")
    for idx, transaction in enumerate(transactions):
        logging.debug(f"Processing transaction {idx + 1}: {transaction.get('hash', 'no-hash')}")

        try:
            inputs = transaction.get("inputs", [])
            outputs = transaction.get("outputs", [])

            sender = inputs[0].get("addresses", ["unknown"])[0] if inputs else "unknown"
            receiver = outputs[0].get("addresses", ["unknown"])[0] if outputs else "unknown"
            amount = outputs[0].get("value", 0) / 1e8 if outputs else 0

            row = {
                "transaction_id": transaction.get("hash", "unknown"),
                "sender": sender,
                "receiver": receiver,
                "amount": amount
            }

            logging.debug(f"Prepared row for BigQuery insertion: {row}")

            # Insert row into BigQuery
            errors = client.insert_rows_json(table_id, [row])
            if errors:
                logging.error(f"BigQuery insert error for transaction {row['transaction_id']}: {errors}")
            else:
                logging.info(f"Inserted transaction into BigQuery: {row['transaction_id']}")

        except Exception as e:
            logging.exception(f"Exception while processing transaction: {transaction}")
