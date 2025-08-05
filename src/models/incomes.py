
from typing import Dict, Any, List, Optional
from .base import CRUDModel

_crud = CRUDModel()

def list_incomes() -> List[Dict[str, Any]]:
    return _crud.list()

def get_income(item_id: int) -> Optional[Dict[str, Any]]:
    return _crud.get(item_id)

def create_income(data: Dict[str, Any]) -> Dict[str, Any]:
    return _crud.create(data)

def update_income(item_id: int, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    return _crud.update(item_id, data)

def delete_income(item_id: int) -> Optional[Dict[str, Any]]:
    return _crud.delete(item_id)

from __future__ import annotations

from typing import Any, Dict, List, Optional

from src.db.connection import get_connection


def create_income(
    field_id: int,
    source: str,
    amount: float,
    income_date: str,
    notes: Optional[str] = None,
) -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO incomes (field_id, source, amount, income_date, notes)
        VALUES (?, ?, ?, ?, ?)
        """,
        (field_id, source, amount, income_date, notes),
    )
    conn.commit()
    income_id = cur.lastrowid
    conn.close()
    return income_id


def get_incomes() -> List[Dict[str, Any]]:
    conn = get_connection()
    cur = conn.execute("SELECT * FROM incomes")
    rows = [dict(row) for row in cur.fetchall()]
    conn.close()
    return rows


def get_income(income_id: int) -> Optional[Dict[str, Any]]:
    conn = get_connection()
    cur = conn.execute("SELECT * FROM incomes WHERE id = ?", (income_id,))
    row = cur.fetchone()
    conn.close()
    return dict(row) if row else None


def update_income(
    income_id: int,
    field_id: Optional[int] = None,
    source: Optional[str] = None,
    amount: Optional[float] = None,
    income_date: Optional[str] = None,
    notes: Optional[str] = None,
) -> None:
    conn = get_connection()
    fields = {
        "field_id": field_id,
        "source": source,
        "amount": amount,
        "income_date": income_date,
        "notes": notes,
    }
    updates = [f"{k} = ?" for k, v in fields.items() if v is not None]
    values = [v for v in fields.values() if v is not None]
    if updates:
        values.append(income_id)
        conn.execute(
            f"UPDATE incomes SET {', '.join(updates)} WHERE id = ?",
            values,
        )
        conn.commit()
    conn.close()


def delete_income(income_id: int) -> None:
    conn = get_connection()
    conn.execute("DELETE FROM incomes WHERE id = ?", (income_id,))
    conn.commit()
    conn.close()

