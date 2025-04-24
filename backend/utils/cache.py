from datetime import datetime
from typing import Dict, Any

class Cache:
    def __init__(self, expiry=3600):
        self._cache: Dict[str, Dict[str, Any]] = {}
        self.expiry = expiry
    
    def get(self, key: str) -> Any:
        if key in self._cache:
            entry = self._cache[key]
            now = datetime.now().timestamp()
            if now - entry["timestamp"] < self.expiry:
                return entry["data"]
        return None
    
    def set(self, key: str, value: Any) -> None:
        self._cache[key] = {
            "timestamp": datetime.now().timestamp(),
            "data": value
        }
    
    def clear(self) -> None:
        self._cache.clear()

cache = Cache()