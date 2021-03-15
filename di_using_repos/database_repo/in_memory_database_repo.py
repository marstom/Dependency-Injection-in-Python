from abc import ABC, abstractclassmethod
from typing import Optional
from firebase_admin import credentials, initialize_app, db
from datetime import datetime
from enum import Enum, auto
import uuid
from copy import deepcopy
from typing import Dict

from .database_repo import DatabaseRepo




class InMemoryDatabaseRepo(DatabaseRepo):
    def __init__(self):
        self._db = None

    def init_database(self, access_path: str):
        self._db = {}


    def save_data(self, object_name: str, data: Dict):
        if self._db.get(object_name) is None:
            self._db[object_name] = []
        self._db[object_name].append(data)
    

    def load_data(self, object_name: str):
        return deepcopy(self._db[object_name])

