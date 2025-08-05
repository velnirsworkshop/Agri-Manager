import React from 'react';
import CrudTable from './CrudTable.jsx';

export default function Incomes() {
  const columns = [
    { name: 'source', label: 'Source' },
    { name: 'amount', label: 'Amount' },
  ];
  return <CrudTable title="Incomes" endpoint="/api/incomes" columns={columns} />;
}
