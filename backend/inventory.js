const inventory = {};
const records = [];

function importMaterial(material, quantity, cost = 0, date = new Date()) {
  if (!inventory[material]) inventory[material] = 0;
  inventory[material] += quantity;
  records.push({ type: 'import', material, quantity, cost, date: new Date(date) });
}

function consumeMaterial(material, quantity, field, cost = 0, revenue = 0, date = new Date()) {
  if (!inventory[material]) inventory[material] = 0;
  inventory[material] -= quantity;
  records.push({ type: 'consumption', material, quantity, field, cost, revenue, date: new Date(date) });
}

function getInventory() {
  return inventory;
}

function getRecords() {
  return records;
}

module.exports = { importMaterial, consumeMaterial, getInventory, getRecords };
