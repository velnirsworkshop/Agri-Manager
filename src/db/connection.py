from __future__ import annotations

import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SCHEMA_FILE = BASE_DIR / "schema.sql"
DEFAULT_DB = BASE_DIR / "agri_manager.db"

def get_connection(db_path: str | Path = DEFAULT_DB) -> sqlite3.Connection:
    """Return a SQLite connection and initialize schema if database is new."""
    db_path = Path(db_path)
    initialize = not db_path.exists()
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    if initialize and SCHEMA_FILE.exists():
        with open(SCHEMA_FILE, "r", encoding="utf-8") as f:
            conn.executescript(f.read())
    return conn
