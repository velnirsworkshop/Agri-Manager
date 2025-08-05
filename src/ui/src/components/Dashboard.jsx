import React, { useEffect, useState } from 'react';

export default function Dashboard() {
  const [incomes, setIncomes] = useState([]);
  const [expenses, setExpenses] = useState([]);

  useEffect(() => {
    fetch('/api/incomes')
      .then((res) => res.json())
      .then(setIncomes)
      .catch(() => setIncomes([]));
    fetch('/api/expenses')
      .then((res) => res.json())
      .then(setExpenses)
      .catch(() => setExpenses([]));
  }, []);

  const totalIncome = incomes.reduce((sum, i) => sum + (Number(i.amount) || 0), 0);
  const totalExpense = expenses.reduce((sum, e) => sum + (Number(e.amount) || 0), 0);
  const netProfit = totalIncome - totalExpense;

  return (
    <div>
      <h2>Dashboard</h2>
      <p>Total Income: {totalIncome}</p>
      <p>Total Expenses: {totalExpense}</p>
      <p>Net Profit: {netProfit}</p>
    </div>
  );
}
