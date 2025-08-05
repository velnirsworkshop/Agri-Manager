
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, List, Optional

from src.models import inventory as model

router = APIRouter(prefix="/inventory", tags=["inventory"])


class InventoryItem(BaseModel):
    item_name: str
    quantity: float
    unit: Optional[str] = None
    cost: Optional[float] = None
    expiration_date: Optional[str] = None


@router.get("/", response_model=List[Dict[str, Any]])
def list_inventory() -> List[Dict[str, Any]]:
    return model.list_inventory()


@router.get("/{item_id}", response_model=Dict[str, Any])
def get_inventory(item_id: int) -> Dict[str, Any]:
    item = model.get_inventory(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    return item


@router.post("/", response_model=Dict[str, Any])
def create_inventory(payload: InventoryItem) -> Dict[str, Any]:
    return model.create_inventory(payload.dict())


@router.put("/{item_id}", response_model=Dict[str, Any])
def update_inventory(item_id: int, payload: InventoryItem) -> Dict[str, Any]:
    updated = model.update_inventory(item_id, payload.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    return updated


@router.delete("/{item_id}", response_model=Dict[str, Any])
def delete_inventory(item_id: int) -> Dict[str, Any]:
    deleted = model.delete_inventory(item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    return deleted
