import React from 'react';
import CrudTable from './CrudTable.jsx';

export default function Settings() {
  const columns = [
    { name: 'key', label: 'Key' },
    { name: 'value', label: 'Value' },
  ];
  return <CrudTable title="Settings" endpoint="/api/settings" columns={columns} />;
}
