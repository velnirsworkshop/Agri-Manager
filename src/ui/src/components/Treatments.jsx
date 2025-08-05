import React from 'react';
import CrudTable from './CrudTable.jsx';

export default function Treatments() {
  const columns = [
    { name: 'field', label: 'Field' },
    { name: 'date', label: 'Date' },
    { name: 'description', label: 'Description' },
  ];
  return <CrudTable title="Treatments" endpoint="/api/treatments" columns={columns} />;
}
