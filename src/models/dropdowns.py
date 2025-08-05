from typing import Dict, Any, List, Optional
from .base import CRUDModel

_crud = CRUDModel()

def list_dropdowns() -> List[Dict[str, Any]]:
    return _crud.list()

def get_dropdown(item_id: int) -> Optional[Dict[str, Any]]:
    return _crud.get(item_id)

def create_dropdown(data: Dict[str, Any]) -> Dict[str, Any]:
    return _crud.create(data)

def update_dropdown(item_id: int, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    return _crud.update(item_id, data)

def delete_dropdown(item_id: int) -> Optional[Dict[str, Any]]:
    return _crud.delete(item_id)
