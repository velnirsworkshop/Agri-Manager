
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, List

from src.models import dropdowns as model

router = APIRouter(prefix="/dropdowns", tags=["dropdowns"])

class Dropdown(BaseModel):
    type: str
    value: str

@router.get("/", response_model=List[Dict[str, Any]])
def list_dropdowns():
    return model.list_dropdowns()

@router.post("/", response_model=Dict[str, Any])
def create_dropdown(payload: Dropdown):
    return model.create_dropdown(payload.dict())

@router.put("/{item_id}", response_model=Dict[str, Any])
def update_dropdown(item_id: int, payload: Dropdown):
    updated = model.update_dropdown(item_id, payload.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Dropdown not found")
    return updated

@router.delete("/{item_id}", response_model=Dict[str, Any])
def delete_dropdown(item_id: int):
    deleted = model.delete_dropdown(item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Dropdown not found")
    return deleted
