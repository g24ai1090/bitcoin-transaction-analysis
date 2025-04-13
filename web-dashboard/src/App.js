import React, { useEffect, useState } from "react";
import { fetchTransactions } from "./api";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

function TransactionChart({ data }) {
  const chartData = data.map((tx) => ({
    label: `${tx.sender.slice(0, 4)}→${tx.receiver.slice(0, 4)}`,
    amount: tx.amount,
  }));

  return (
    <div className="chart-container">
      <h2>Top Transaction Amounts</h2>
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={chartData}>
          <XAxis dataKey="label" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="amount" fill="#8884d8" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}

function App() {
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    fetchTransactions().then(setTransactions);
  }, []);

  return (
    <div className="App">
      <h1>Bitcoin Fraud Detection Dashboard</h1>
      <TransactionChart data={transactions} />
      <table className="transaction-table"> <thead> <tr> <th>Sender</th> <th>Receiver</th> <th>Amount (BTC)</th> <th>Fraudulent?</th> </tr> </thead> <tbody> {transactions.map((tx, index) => ( <tr key={index}> <td>{tx.sender}</td> <td>{tx.receiver}</td> <td>{tx.amount}</td> <td>{tx.is_fraud ? "✅ Yes" : "❌ No"}</td> </tr> ))} </tbody> </table>
    </div>
  );
}

export default App;
