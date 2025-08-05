from __future__ import annotations

from typing import Any, Dict, List, Optional

from src.db.connection import get_connection


def create_dropdown_item(category: str, value: str) -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO dropdown_lists (category, value) VALUES (?, ?)",
        (category, value),
    )
    conn.commit()
    item_id = cur.lastrowid
    conn.close()
    return item_id


def get_dropdown_items(category: Optional[str] = None) -> List[Dict[str, Any]]:
    conn = get_connection()
    if category is not None:
        cur = conn.execute(
            "SELECT * FROM dropdown_lists WHERE category = ?", (category,)
        )
    else:
        cur = conn.execute("SELECT * FROM dropdown_lists")
    rows = [dict(row) for row in cur.fetchall()]
    conn.close()
    return rows


def get_dropdown_item(item_id: int) -> Optional[Dict[str, Any]]:
    conn = get_connection()
    cur = conn.execute("SELECT * FROM dropdown_lists WHERE id = ?", (item_id,))
    row = cur.fetchone()
    conn.close()
    return dict(row) if row else None


def update_dropdown_item(
    item_id: int,
    category: Optional[str] = None,
    value: Optional[str] = None,
) -> None:
    conn = get_connection()
    fields = {"category": category, "value": value}
    updates = [f"{k} = ?" for k, v in fields.items() if v is not None]
    values = [v for v in fields.values() if v is not None]
    if updates:
        values.append(item_id)
        conn.execute(
            f"UPDATE dropdown_lists SET {', '.join(updates)} WHERE id = ?",
            values,
        )
        conn.commit()
    conn.close()


def delete_dropdown_item(item_id: int) -> None:
    conn = get_connection()
    conn.execute("DELETE FROM dropdown_lists WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()
