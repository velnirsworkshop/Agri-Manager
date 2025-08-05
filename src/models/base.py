from typing import Any, Dict, List, Optional


class CRUDModel:
    """Simple in-memory CRUD helper."""

    def __init__(self) -> None:
        self._db: Dict[int, Dict[str, Any]] = {}
        self._counter: int = 0

    def list(self) -> List[Dict[str, Any]]:
        return list(self._db.values())

    def get(self, item_id: int) -> Optional[Dict[str, Any]]:
        return self._db.get(item_id)

    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        self._counter += 1
        record = {"id": self._counter, **data}
        self._db[self._counter] = record
        return record

    def update(self, item_id: int, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        if item_id in self._db:
            self._db[item_id].update(data)
            return self._db[item_id]
        return None

    def delete(self, item_id: int) -> Optional[Dict[str, Any]]:
        return self._db.pop(item_id, None)
