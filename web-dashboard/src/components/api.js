const API_URL = "https://fraud-detection-api.cloud.run";

export async function fetchTransactions() {
    const response = await fetch(`${API_URL}/get-transactions`);
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
