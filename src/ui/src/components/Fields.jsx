import React from 'react';
import CrudTable from './CrudTable.jsx';

export default function Fields() {
  const columns = [
    { name: 'name', label: 'Name' },
    { name: 'area', label: 'Area' },
  ];
  return <CrudTable title="Fields" endpoint="/api/fields" columns={columns} />;
}
