
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, List

from src.models import inventory as model

router = APIRouter(prefix="/inventory", tags=["inventory"])

class InventoryItem(BaseModel):
    item: str
    quantity: int

@router.get("/", response_model=List[Dict[str, Any]])
def list_inventory():
    return model.list_inventory()

@router.post("/", response_model=Dict[str, Any])
def create_inventory(payload: InventoryItem):
    return model.create_inventory(payload.dict())

@router.put("/{item_id}", response_model=Dict[str, Any])
def update_inventory(item_id: int, payload: InventoryItem):
    updated = model.update_inventory(item_id, payload.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="InventoryItem not found")
    return updated

@router.delete("/{item_id}", response_model=Dict[str, Any])
def delete_inventory(item_id: int):
    deleted = model.delete_inventory(item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="InventoryItem not found")
    return deleted
