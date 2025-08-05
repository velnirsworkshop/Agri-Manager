import React from 'react';
import CrudTable from './CrudTable.jsx';

export default function Expenses() {
  const columns = [
    { name: 'item', label: 'Item' },
    { name: 'amount', label: 'Amount' },
  ];
  return <CrudTable title="Expenses" endpoint="/api/expenses" columns={columns} />;
}
