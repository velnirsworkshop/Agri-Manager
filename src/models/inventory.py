
from typing import Dict, Any, List, Optional
from .base import CRUDModel

_crud = CRUDModel()

def list_inventory() -> List[Dict[str, Any]]:
    return _crud.list()

def get_inventory(item_id: int) -> Optional[Dict[str, Any]]:
    return _crud.get(item_id)

def create_inventory(data: Dict[str, Any]) -> Dict[str, Any]:
    return _crud.create(data)

def update_inventory(item_id: int, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    return _crud.update(item_id, data)

def delete_inventory(item_id: int) -> Optional[Dict[str, Any]]:
    return _crud.delete(item_id)

from __future__ import annotations

from typing import Any, Dict, List, Optional

from src.db.connection import get_connection


def create_item(
    item_name: str,
    quantity: float,
    unit: str,
    cost: Optional[float] = None,
    expiration_date: Optional[str] = None,
) -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO inventory (item_name, quantity, unit, cost, expiration_date)
        VALUES (?, ?, ?, ?, ?)
        """,
        (item_name, quantity, unit, cost, expiration_date),
    )
    conn.commit()
    item_id = cur.lastrowid
    conn.close()
    return item_id


def get_items() -> List[Dict[str, Any]]:
    conn = get_connection()
    cur = conn.execute("SELECT * FROM inventory")
    rows = [dict(row) for row in cur.fetchall()]
    conn.close()
    return rows


def get_item(item_id: int) -> Optional[Dict[str, Any]]:
    conn = get_connection()
    cur = conn.execute("SELECT * FROM inventory WHERE id = ?", (item_id,))
    row = cur.fetchone()
    conn.close()
    return dict(row) if row else None


def update_item(
    item_id: int,
    item_name: Optional[str] = None,
    quantity: Optional[float] = None,
    unit: Optional[str] = None,
    cost: Optional[float] = None,
    expiration_date: Optional[str] = None,
) -> None:
    conn = get_connection()
    fields = {
        "item_name": item_name,
        "quantity": quantity,
        "unit": unit,
        "cost": cost,
        "expiration_date": expiration_date,
    }
    updates = [f"{k} = ?" for k, v in fields.items() if v is not None]
    values = [v for v in fields.values() if v is not None]
    if updates:
        values.append(item_id)
        conn.execute(
            f"UPDATE inventory SET {', '.join(updates)} WHERE id = ?",
            values,
        )
        conn.commit()
    conn.close()


def delete_item(item_id: int) -> None:
    conn = get_connection()
    conn.execute("DELETE FROM inventory WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()

