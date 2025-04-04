from fastapi import FastAPI
from google.cloud import bigquery

app = FastAPI()
client = bigquery.Client()

@app.get("/top-transactions")
def get_top_transactions():
    query = """
    SELECT sender, receiver, SUM(amount) as total_amount
    FROM `my_project.bitcoin_analysis.transactions`
    GROUP BY sender, receiver
    ORDER BY total_amount DESC
    LIMIT 10
    """
    results = client.query(query).result()
    return [{"sender": row.sender, "receiver": row.receiver, "amount": row.total_amount} for row in results]
