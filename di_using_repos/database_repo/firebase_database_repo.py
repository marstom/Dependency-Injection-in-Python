from abc import ABC, abstractclassmethod

from .database_repo import DatabaseRepo

from firebase_admin import credentials, initialize_app, db
from datetime import datetime
from enum import Enum, auto
from typing import Dict


class FireBaseDatabaseRepo(DatabaseRepo):
    
    def init_database(self, access_path: str):
        cred = credentials.Certificate("../cred.json")
        initialize_app(cred, { "databaseURL": access_path})
        self.root = db.reference()
        print("Db init succesfully!")


    def save_data(self, object_name: str, data: Dict):
        self.root.child(object_name).push(data)
    

    def load_data(self, object_name: str):
        rows = []
        for row in db.reference(object_name).get().values():
            rows.append(row)
        return rows