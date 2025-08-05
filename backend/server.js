const express = require('express');
const path = require('path');
const { importMaterial, consumeMaterial, getInventory } = require('./inventory');
const { consumptionByField, profitByMonth } = require('./reports');

const app = express();
app.use(express.json());
app.use(express.static(path.join(__dirname, '..', 'public')));

app.post('/inventory/import', (req, res) => {
  const { material, quantity, cost, date } = req.body;
  importMaterial(material, Number(quantity), Number(cost) || 0, date);
  res.json({ inventory: getInventory() });
});

app.post('/inventory/consume', (req, res) => {
  const { material, quantity, field, cost, revenue, date } = req.body;
  consumeMaterial(material, Number(quantity), field, Number(cost) || 0, Number(revenue) || 0, date);
  res.json({ inventory: getInventory() });
});

app.get('/reports/consumption', (req, res) => {
  res.json(consumptionByField());
});

app.get('/reports/profit', (req, res) => {
  res.json(profitByMonth());
});

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Server running on ${port}`));
