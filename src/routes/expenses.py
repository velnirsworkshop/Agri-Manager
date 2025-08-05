
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, List

from src.models import expenses as model

router = APIRouter(prefix="/expenses", tags=["expenses"])

class Expense(BaseModel):
    item: str
    amount: float

@router.get("/", response_model=List[Dict[str, Any]])
def list_expenses():
    return model.list_expenses()

@router.post("/", response_model=Dict[str, Any])
def create_expense(payload: Expense):
    return model.create_expense(payload.dict())

@router.put("/{item_id}", response_model=Dict[str, Any])
def update_expense(item_id: int, payload: Expense):
    updated = model.update_expense(item_id, payload.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Expense not found")
    return updated

@router.delete("/{item_id}", response_model=Dict[str, Any])
def delete_expense(item_id: int):
    deleted = model.delete_expense(item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Expense not found")
    return deleted
