"""Inventory data access helpers.

This module provides CRUD helpers backed by the SQLite database defined in
``src/db/connection.py``. It replaces earlier in-memory stubs so that the REST
API operates on persistent data.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from src.db.connection import get_connection


def list_inventory() -> List[Dict[str, Any]]:
    """Return all inventory items."""
    conn = get_connection()
    cur = conn.execute("SELECT * FROM inventory")
    rows = [dict(row) for row in cur.fetchall()]
    conn.close()
    return rows


def get_inventory(item_id: int) -> Optional[Dict[str, Any]]:
    """Return a single inventory item by id."""
    conn = get_connection()
    cur = conn.execute("SELECT * FROM inventory WHERE id = ?", (item_id,))
    row = cur.fetchone()
    conn.close()
    return dict(row) if row else None


def create_inventory(data: Dict[str, Any]) -> Dict[str, Any]:
    """Create a new inventory item and return it."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO inventory (item_name, quantity, unit, cost, expiration_date)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            data["item_name"],
            data["quantity"],
            data.get("unit"),
            data.get("cost"),
            data.get("expiration_date"),
        ),
    )
    conn.commit()
    item_id = cur.lastrowid
    conn.close()
    return {"id": item_id, **data}


def update_inventory(item_id: int, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Update an inventory item and return the updated record."""
    existing = get_inventory(item_id)
    if not existing:
        return None
    fields = {k: v for k, v in data.items() if v is not None}
    if not fields:
        return existing
    updates = [f"{k} = ?" for k in fields]
    values = list(fields.values())
    values.append(item_id)
    conn = get_connection()
    conn.execute(
        f"UPDATE inventory SET {', '.join(updates)} WHERE id = ?",
        values,
    )
    conn.commit()
    conn.close()
    return get_inventory(item_id)


def delete_inventory(item_id: int) -> Optional[Dict[str, Any]]:
    """Delete an inventory item and return the deleted record if it existed."""
    item = get_inventory(item_id)
    if not item:
        return None
    conn = get_connection()
    conn.execute("DELETE FROM inventory WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()
    return item


__all__ = [
    "list_inventory",
    "get_inventory",
    "create_inventory",
    "update_inventory",
    "delete_inventory",
]

