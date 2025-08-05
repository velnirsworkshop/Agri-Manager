
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, List

from src.models import incomes as model

router = APIRouter(prefix="/incomes", tags=["incomes"])

class Income(BaseModel):
    source: str
    amount: float

@router.get("/", response_model=List[Dict[str, Any]])
def list_incomes():
    return model.list_incomes()

@router.post("/", response_model=Dict[str, Any])
def create_income(payload: Income):
    return model.create_income(payload.dict())

@router.put("/{item_id}", response_model=Dict[str, Any])
def update_income(item_id: int, payload: Income):
    updated = model.update_income(item_id, payload.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Income not found")
    return updated

@router.delete("/{item_id}", response_model=Dict[str, Any])
def delete_income(item_id: int):
    deleted = model.delete_income(item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Income not found")
    return deleted
