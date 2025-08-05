import React, { useState } from 'react';
import Dashboard from './components/Dashboard.jsx';
import Fields from './components/Fields.jsx';
import Treatments from './components/Treatments.jsx';
import Incomes from './components/Incomes.jsx';
import Expenses from './components/Expenses.jsx';
import Inventory from './components/Inventory.jsx';
import Settings from './components/Settings.jsx';

const tabs = {
  Dashboard,
  Fields,
  Treatments,
  Incomes,
  Expenses,
  Inventory,
  Settings,
};

export default function App() {
  const [activeTab, setActiveTab] = useState('Dashboard');
  const Current = tabs[activeTab];
  return (
    <div>
      <nav style={{ display: 'flex', gap: '0.5rem' }}>
        {Object.keys(tabs).map((tab) => (
          <button key={tab} onClick={() => setActiveTab(tab)} disabled={activeTab === tab}>
            {tab}
          </button>
        ))}
      </nav>
      <div style={{ marginTop: '1rem' }}>
        <Current />
      </div>
    </div>
  );
}
