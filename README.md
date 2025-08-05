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
## Εγκατάσταση

1. Βεβαιωθείτε ότι έχετε εγκατεστημένο το [Node.js](https://nodejs.org/) (έκδοση 18 ή νεότερη).
2. Εγκαταστήστε τις εξαρτήσεις του έργου:
   ```bash
   npm install
   ```

## Εκτέλεση

Για να εκκινήσετε τον τοπικό διακομιστή ανάπτυξης:

```bash
npm start
```
