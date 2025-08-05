
from typing import Dict, Any, List, Optional
from .base import CRUDModel

_crud = CRUDModel()

def list_treatments() -> List[Dict[str, Any]]:
    return _crud.list()

def get_treatment(item_id: int) -> Optional[Dict[str, Any]]:
    return _crud.get(item_id)

def create_treatment(data: Dict[str, Any]) -> Dict[str, Any]:
    return _crud.create(data)

def update_treatment(item_id: int, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    return _crud.update(item_id, data)

def delete_treatment(item_id: int) -> Optional[Dict[str, Any]]:
    return _crud.delete(item_id)

from __future__ import annotations

from typing import Any, Dict, List, Optional

from src.db.connection import get_connection


def create_treatment(
    field_id: int,
    treatment_type: str,
    treatment_date: str,
    product: str,
    quantity: Optional[float] = None,
    cost: Optional[float] = None,
    notes: Optional[str] = None,
) -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO treatments (field_id, treatment_type, treatment_date, product, quantity, cost, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (field_id, treatment_type, treatment_date, product, quantity, cost, notes),
    )
    conn.commit()
    treatment_id = cur.lastrowid
    conn.close()
    return treatment_id


def get_treatments() -> List[Dict[str, Any]]:
    conn = get_connection()
    cur = conn.execute("SELECT * FROM treatments")
    rows = [dict(row) for row in cur.fetchall()]
    conn.close()
    return rows


def get_treatment(treatment_id: int) -> Optional[Dict[str, Any]]:
    conn = get_connection()
    cur = conn.execute("SELECT * FROM treatments WHERE id = ?", (treatment_id,))
    row = cur.fetchone()
    conn.close()
    return dict(row) if row else None


def update_treatment(
    treatment_id: int,
    field_id: Optional[int] = None,
    treatment_type: Optional[str] = None,
    treatment_date: Optional[str] = None,
    product: Optional[str] = None,
    quantity: Optional[float] = None,
    cost: Optional[float] = None,
    notes: Optional[str] = None,
) -> None:
    conn = get_connection()
    fields = {
        "field_id": field_id,
        "treatment_type": treatment_type,
        "treatment_date": treatment_date,
        "product": product,
        "quantity": quantity,
        "cost": cost,
        "notes": notes,
    }
    updates = [f"{k} = ?" for k, v in fields.items() if v is not None]
    values = [v for v in fields.values() if v is not None]
    if updates:
        values.append(treatment_id)
        conn.execute(
            f"UPDATE treatments SET {', '.join(updates)} WHERE id = ?",
            values,
        )
        conn.commit()
    conn.close()


def delete_treatment(treatment_id: int) -> None:
    conn = get_connection()
    conn.execute("DELETE FROM treatments WHERE id = ?", (treatment_id,))
    conn.commit()
    conn.close()
