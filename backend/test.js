const { importMaterial, consumeMaterial, getInventory } = require('./inventory');
const { consumptionByField, profitByMonth } = require('./reports');

importMaterial('PesticideA', 100, 50, '2024-01-10');
consumeMaterial('PesticideA', 10, 'Field1', 5, 0, '2024-01-11');
consumeMaterial('PesticideA', 20, 'Field2', 10, 0, '2024-02-05');
importMaterial('Seeds', 50, 20, '2024-02-01');
consumeMaterial('Seeds', 5, 'Field1', 2, 30, '2024-02-10');

console.log('Inventory:', getInventory());
console.log('Consumption by field:', consumptionByField());
console.log('Profit by month:', profitByMonth());
