from typing import Dict, Any, List, Optional
from .base import CRUDModel

_crud = CRUDModel()

def list_treatments() -> List[Dict[str, Any]]:
    return _crud.list()

def get_treatment(item_id: int) -> Optional[Dict[str, Any]]:
    return _crud.get(item_id)

def create_treatment(data: Dict[str, Any]) -> Dict[str, Any]:
    return _crud.create(data)

def update_treatment(item_id: int, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    return _crud.update(item_id, data)

def delete_treatment(item_id: int) -> Optional[Dict[str, Any]]:
    return _crud.delete(item_id)
