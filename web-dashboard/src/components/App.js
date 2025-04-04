import React, { useState, useEffect } from "react";
import { fetchTransactions, checkFraud } from "./api";
import TransactionChart from "./components/TransactionChart";  // Import the chart component

function App() {
    const [transactions, setTransactions] = useState([]);

    useEffect(() => {
        const loadTransactions = async () => {
            const data = await fetchTransactions();
            setTransactions(data);
        };
        loadTransactions();
    }, []);

    return (
        <div>
            <h1>🚀 Bitcoin Fraud Detection Dashboard</h1>
            
            <TransactionChart />  {/* Add the real-time chart */}

            <table>
                <thead>
                    <tr>
                        <th>Tx ID</th>
                        <th>Sender</th>
                        <th>Receiver</th>
                        <th>Amount</th>
                        <th>Fraudulent?</th>
                    </tr>
                </thead>
                <tbody>
                    {transactions.map(tx => (
                        <tr key={tx.transaction_id}>
                            <td>{tx.transaction_id}</td>
                            <td>{tx.sender}</td>
                            <td>{tx.receiver}</td>
                            <td>{tx.amount}</td>
                            <td style={{ color: tx.is_fraud ? "red" : "green" }}>
                                {tx.is_fraud ? "🚨 Yes" : "✅ No"}
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default App;
