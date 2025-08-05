import React from 'react';
import CrudTable from './CrudTable.jsx';

export default function Inventory() {
  const columns = [
    { name: 'item', label: 'Item' },
    { name: 'quantity', label: 'Quantity' },
  ];
  return <CrudTable title="Inventory" endpoint="/api/inventory" columns={columns} />;
}
