from copy import deepcopy
from typing import Dict

from .database_repo import Database




class InMemoryDatabase(Database):
    def __init__(self, connection, access_path: str):
        self._db = {}

    def save_data(self, object_name: str, data: Dict):
        if self._db.get(object_name) is None:
            self._db[object_name] = []
        self._db[object_name].append(data)
    

    def load_data(self, object_name: str):
        return deepcopy(self._db[object_name])

