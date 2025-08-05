
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, List

from src.models import fields as model

router = APIRouter(prefix="/fields", tags=["fields"])

class Field(BaseModel):
    name: str
    area: float | None = None

@router.get("/", response_model=List[Dict[str, Any]])
def list_fields():
    return model.list_fields()

@router.post("/", response_model=Dict[str, Any])
def create_field(payload: Field):
    return model.create_field(payload.dict())

@router.put("/{item_id}", response_model=Dict[str, Any])
def update_field(item_id: int, payload: Field):
    updated = model.update_field(item_id, payload.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Field not found")
    return updated

@router.delete("/{item_id}", response_model=Dict[str, Any])
def delete_field(item_id: int):
    deleted = model.delete_field(item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Field not found")
    return deleted
