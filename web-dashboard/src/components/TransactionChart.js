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
                borderColor: "blue",
                backgroundColor: "rgba(0, 0, 255, 0.2)",
                fill: true,
            },
        ],
    });

    useEffect(() => {
        const loadTransactions = async () => {
            const transactions = await fetchTransactions();
            const labels = transactions.map(tx => tx.transaction_id);
            const amounts = transactions.map(tx => tx.amount);

            setChartData({
                labels,
                datasets: [
                    {
                        label: "Transaction Amounts",
                        data: amounts,
                        borderColor: "blue",
                        backgroundColor: "rgba(0, 0, 255, 0.2)",
                        fill: true,
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
