const API_URL = "https://fraud-detection-831585962225.us-central1.run.app";

export async function fetchTransactions() {
    const response = await fetch(`${API_URL}/top-transactions`);
    return response.json();
}

export async function checkFraud(transaction) {
    const response = await fetch(`${API_URL}/detect-fraud`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(transaction)
    });
    return response.json();
}
