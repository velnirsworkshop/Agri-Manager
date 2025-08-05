CREATE TABLE IF NOT EXISTS fields (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    area REAL,
    crop_type TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS treatments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    field_id INTEGER,
    treatment_type TEXT,
    treatment_date TEXT,
    product TEXT,
    quantity REAL,
    cost REAL,
    notes TEXT,
    FOREIGN KEY(field_id) REFERENCES fields(id)
);

CREATE TABLE IF NOT EXISTS incomes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    field_id INTEGER,
    source TEXT,
    amount REAL NOT NULL,
    income_date TEXT,
    notes TEXT,
    FOREIGN KEY(field_id) REFERENCES fields(id)
);

CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    field_id INTEGER,
    description TEXT,
    amount REAL NOT NULL,
    expense_date TEXT,
    notes TEXT,
    FOREIGN KEY(field_id) REFERENCES fields(id)
);

CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT NOT NULL,
    quantity REAL NOT NULL,
    unit TEXT,
    cost REAL,
    expiration_date TEXT
);

CREATE TABLE IF NOT EXISTS dropdown_lists (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL,
    value TEXT NOT NULL
);
