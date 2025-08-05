# Agri-Manager

Demo backend and UI for inventory tracking and reports.

## Scripts
- `npm test` – run sample inventory operations and output reports
- `npm start` – start the express server and serve the reports UI

## Endpoints
- `POST /inventory/import` – add stock to inventory
- `POST /inventory/consume` – record consumption and update inventory
- `GET /reports/consumption` – consumption of materials per field
- `GET /reports/profit` – net profit per month

Open `http://localhost:3000/` to view the reports UI.
