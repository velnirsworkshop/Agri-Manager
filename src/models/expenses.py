
from typing import Dict, Any, List, Optional
from .base import CRUDModel

_crud = CRUDModel()

def list_expenses() -> List[Dict[str, Any]]:
    return _crud.list()

def get_expense(item_id: int) -> Optional[Dict[str, Any]]:
    return _crud.get(item_id)

def create_expense(data: Dict[str, Any]) -> Dict[str, Any]:
    return _crud.create(data)

def update_expense(item_id: int, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    return _crud.update(item_id, data)

def delete_expense(item_id: int) -> Optional[Dict[str, Any]]:
    return _crud.delete(item_id)
  
from __future__ import annotations

from typing import Any, Dict, List, Optional

from src.db.connection import get_connection


def create_expense(
    field_id: int,
    description: str,
    amount: float,
    expense_date: str,
    notes: Optional[str] = None,
) -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO expenses (field_id, description, amount, expense_date, notes)
        VALUES (?, ?, ?, ?, ?)
        """,
        (field_id, description, amount, expense_date, notes),
    )
    conn.commit()
    expense_id = cur.lastrowid
    conn.close()
    return expense_id


def get_expenses() -> List[Dict[str, Any]]:
    conn = get_connection()
    cur = conn.execute("SELECT * FROM expenses")
    rows = [dict(row) for row in cur.fetchall()]
    conn.close()
    return rows


def get_expense(expense_id: int) -> Optional[Dict[str, Any]]:
    conn = get_connection()
    cur = conn.execute("SELECT * FROM expenses WHERE id = ?", (expense_id,))
    row = cur.fetchone()
    conn.close()
    return dict(row) if row else None


def update_expense(
    expense_id: int,
    field_id: Optional[int] = None,
    description: Optional[str] = None,
    amount: Optional[float] = None,
    expense_date: Optional[str] = None,
    notes: Optional[str] = None,
) -> None:
    conn = get_connection()
    fields = {
        "field_id": field_id,
        "description": description,
        "amount": amount,
        "expense_date": expense_date,
        "notes": notes,
    }
    updates = [f"{k} = ?" for k, v in fields.items() if v is not None]
    values = [v for v in fields.values() if v is not None]
    if updates:
        values.append(expense_id)
        conn.execute(
            f"UPDATE expenses SET {', '.join(updates)} WHERE id = ?",
            values,
        )
        conn.commit()
    conn.close()


def delete_expense(expense_id: int) -> None:
    conn = get_connection()
    conn.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()

