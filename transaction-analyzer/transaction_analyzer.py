from fastapi import FastAPI
from google.cloud import bigquery
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "Transaction Analyzer API is running!"}

client = bigquery.Client()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/top-transactions")
def get_top_transactions():
    query = """
    SELECT sender, receiver, amount, is_fraud
    FROM `virtualbox-assignmnt.bitcoin_analysis.transactions`
    ORDER BY amount DESC
    LIMIT 10
    """
    results = client.query(query).result()
    return [
        {
            "sender": row.sender,
            "receiver": row.receiver,
            "amount": row.amount,
            "is_fraud": row.is_fraud
        }
        for row in results
    ]