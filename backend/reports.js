const { getRecords } = require('./inventory');

function consumptionByField() {
  const totals = {};
  for (const r of getRecords()) {
    if (r.type === 'consumption') {
      if (!totals[r.field]) totals[r.field] = {};
      totals[r.field][r.material] = (totals[r.field][r.material] || 0) + r.quantity;
    }
  }
  return totals;
}

function profitByMonth() {
  const totals = {};
  for (const r of getRecords()) {
    const month = r.date.toISOString().slice(0, 7); // YYYY-MM
    if (!totals[month]) totals[month] = 0;
    const revenue = r.revenue || 0;
    const cost = r.cost || 0;
    totals[month] += revenue - cost;
  }
  return totals;
}

module.exports = { consumptionByField, profitByMonth };
