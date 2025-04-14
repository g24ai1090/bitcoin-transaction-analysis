import streamlit as st
import requests

# Set the page title
st.set_page_config(page_title="Transaction Analyzer", layout="wide")

# Title
st.title("Transaction Analyzer")

# API endpoint URL
url = "http://34.123.54.114/top-transactions"

# Function to fetch top transactions from the API
def get_top_transactions():
    headers = {"Host": "transaction-analyzer.local"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Display top transactions
top_transactions = get_top_transactions()

if top_transactions:
    st.subheader("Top 10 Transactions")
    st.write(top_transactions)
else:
    st.error("Failed to retrieve data. Please check the API.")
