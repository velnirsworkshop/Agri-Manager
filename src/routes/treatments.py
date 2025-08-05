
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, List

from src.models import treatments as model

router = APIRouter(prefix="/treatments", tags=["treatments"])

class Treatment(BaseModel):
    field_id: int
    description: str

@router.get("/", response_model=List[Dict[str, Any]])
def list_treatments():
    return model.list_treatments()

@router.post("/", response_model=Dict[str, Any])
def create_treatment(payload: Treatment):
    return model.create_treatment(payload.dict())

@router.put("/{item_id}", response_model=Dict[str, Any])
def update_treatment(item_id: int, payload: Treatment):
    updated = model.update_treatment(item_id, payload.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Treatment not found")
    return updated

@router.delete("/{item_id}", response_model=Dict[str, Any])
def delete_treatment(item_id: int):
    deleted = model.delete_treatment(item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Treatment not found")
    return deleted
