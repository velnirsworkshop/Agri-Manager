import React, { useEffect, useState } from 'react';

export default function CrudTable({ title, endpoint, columns }) {
  const [items, setItems] = useState([]);
  const [newItem, setNewItem] = useState({});
  const [editingId, setEditingId] = useState(null);
  const [editItem, setEditItem] = useState({});

  const fetchItems = () => {
    fetch(endpoint)
      .then((res) => res.json())
      .then(setItems)
      .catch(() => setItems([]));
  };

  useEffect(fetchItems, [endpoint]);

  const handleChange = (e, setter) => {
    setter((prev) => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleAdd = (e) => {
    e.preventDefault();
    fetch(endpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(newItem),
    }).then(() => {
      setNewItem({});
      fetchItems();
    });
  };

  const startEdit = (item) => {
    setEditingId(item.id);
    setEditItem(item);
  };

  const handleUpdate = (e) => {
    e.preventDefault();
    fetch(`${endpoint}/${editingId}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(editItem),
    }).then(() => {
      setEditingId(null);
      setEditItem({});
      fetchItems();
    });
  };

  const handleDelete = (id) => {
    fetch(`${endpoint}/${id}`, { method: 'DELETE' }).then(fetchItems);
  };

  return (
    <div>
      <h2>{title}</h2>
      <table border="1" cellPadding="4">
        <thead>
          <tr>
            {columns.map((col) => (
              <th key={col.name}>{col.label}</th>
            ))}
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {items.map((item) => (
            <tr key={item.id}>
              {columns.map((col) => (
                <td key={col.name}>{item[col.name]}</td>
              ))}
              <td>
                <button onClick={() => startEdit(item)}>Edit</button>
                <button onClick={() => handleDelete(item.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      <h3>Add {title}</h3>
      <form onSubmit={handleAdd} style={{ display: 'flex', gap: '0.5rem' }}>
        {columns.map((col) => (
          <input
            key={col.name}
            name={col.name}
            placeholder={col.label}
            value={newItem[col.name] || ''}
            onChange={(e) => handleChange(e, setNewItem)}
          />
        ))}
        <button type="submit">Add</button>
      </form>

      {editingId && (
        <form onSubmit={handleUpdate} style={{ display: 'flex', gap: '0.5rem', marginTop: '1rem' }}>
          {columns.map((col) => (
            <input
              key={col.name}
              name={col.name}
              placeholder={col.label}
              value={editItem[col.name] || ''}
              onChange={(e) => handleChange(e, setEditItem)}
            />
          ))}
          <button type="submit">Update</button>
          <button type="button" onClick={() => setEditingId(null)}>
            Cancel
          </button>
        </form>
      )}
    </div>
  );
}
