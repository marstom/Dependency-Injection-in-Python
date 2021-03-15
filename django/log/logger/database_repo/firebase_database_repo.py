from .database_repo import Database
from typing import Dict


class FireBaseDatabase(Database):

    def __init__(self, initialize_app, db_reference, certificate, access_path: str, credentials_filename: str):
        cred = certificate(credentials_filename)
        initialize_app(cred, {"databaseURL": access_path})
        self.db_reference = db_reference
        self.root = self.db_reference()

    def save_data(self, object_name: str, data: Dict):
        self.root.child(object_name).push(data)

    def load_data(self, object_name: str):
        rows = []
        for row in self.db_reference(object_name).get().values():
            rows.append(row)
        return rows
