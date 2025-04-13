import React, { useEffect, useState } from "react";
import { Line } from "react-chartjs-2";
import { fetchTransactions } from "../api";
import { Chart, registerables } from "chart.js";

Chart.register(...registerables);

const TransactionChart = () => {
    const [chartData, setChartData] = useState({
        labels: [],
        datasets: [
            {
                label: "Transaction Amounts",
                data: [],
                backgroundColor: [],
                borderColor: [],
                fill: true,
            },
        ],
    });

    useEffect(() => {
        const loadTransactions = async () => {
            const transactions = await fetchTransactions();

            const labels = transactions.map(
                (tx) => `${tx.sender.slice(0, 4)}→${tx.receiver.slice(0, 4)}`
            );
            const amounts = transactions.map((tx) => tx.amount);
            const colors = transactions.map((tx) =>
                tx.is_fraud ? "rgba(255, 0, 0, 0.5)" : "rgba(0, 0, 255, 0.3)"
            );
            const borders = transactions.map((tx) =>
                tx.is_fraud ? "red" : "blue"
            );

            setChartData({
                labels,
                datasets: [
                    {
                        label: "Transaction Amounts",
                        data: amounts,
                        backgroundColor: colors,
                        borderColor: borders,
                        borderWidth: 1.5,
                        fill: true,
                        tension: 0.3,
                    },
                ],
            });
        };

        loadTransactions();
        const interval = setInterval(loadTransactions, 5000); // Refresh every 5 seconds
        return () => clearInterval(interval);
    }, []);

    return (
        <div>
            <h2>📊 Real-Time Bitcoin Transactions</h2>
            <Line data={chartData} />
        </div>
    );
};

export default TransactionChart;
