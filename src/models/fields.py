
from typing import Dict, Any, List, Optional
from .base import CRUDModel

_crud = CRUDModel()

def list_fields() -> List[Dict[str, Any]]:
    return _crud.list()

def get_field(item_id: int) -> Optional[Dict[str, Any]]:
    return _crud.get(item_id)

def create_field(data: Dict[str, Any]) -> Dict[str, Any]:
    return _crud.create(data)

def update_field(item_id: int, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    return _crud.update(item_id, data)

def delete_field(item_id: int) -> Optional[Dict[str, Any]]:
    return _crud.delete(item_id)

from __future__ import annotations

from typing import Any, Dict, List, Optional

from src.db.connection import get_connection


def create_field(name: str, area: Optional[float] = None, crop_type: Optional[str] = None) -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO fields (name, area, crop_type) VALUES (?, ?, ?)",
        (name, area, crop_type),
    )
    conn.commit()
    field_id = cur.lastrowid
    conn.close()
    return field_id


def get_fields() -> List[Dict[str, Any]]:
    conn = get_connection()
    cur = conn.execute("SELECT * FROM fields")
    rows = [dict(row) for row in cur.fetchall()]
    conn.close()
    return rows


def get_field(field_id: int) -> Optional[Dict[str, Any]]:
    conn = get_connection()
    cur = conn.execute("SELECT * FROM fields WHERE id = ?", (field_id,))
    row = cur.fetchone()
    conn.close()
    return dict(row) if row else None


def update_field(
    field_id: int,
    name: Optional[str] = None,
    area: Optional[float] = None,
    crop_type: Optional[str] = None,
) -> None:
    conn = get_connection()
    fields = {"name": name, "area": area, "crop_type": crop_type}
    updates = [f"{k} = ?" for k, v in fields.items() if v is not None]
    values = [v for v in fields.values() if v is not None]
    if updates:
        values.append(field_id)
        conn.execute(f"UPDATE fields SET {', '.join(updates)} WHERE id = ?", values)
        conn.commit()
    conn.close()


def delete_field(field_id: int) -> None:
    conn = get_connection()
    conn.execute("DELETE FROM fields WHERE id = ?", (field_id,))
    conn.commit()
    conn.close()
