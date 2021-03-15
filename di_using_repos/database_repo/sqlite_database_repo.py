from abc import ABC, abstractclassmethod
from typing import Optional
from firebase_admin import credentials, initialize_app, db
from datetime import datetime

from copy import deepcopy
from typing import Dict

import sqlite3

from .database_repo import DatabaseRepo



class SqliteDatabaseRepo(DatabaseRepo):
    def __init__(self):
        self._db = None
        self.conn = None

    def init_database(self, access_path: str):
        self.conn = sqlite3.connect(access_path)
        self.conn.row_factory = self.dict_factory
        self._cursor = self.conn.cursor()
        
    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d


    def save_data(self, object_name: str, data: Dict):

        self._cursor.execute(f"""create table if not exists {object_name}
        ([id] INTEGER PRIMARY KEY,[content] text, [type] text, [date] text)
        ;""")
        query = f"""
            insert into {object_name} (content, type ,date)
            values ('{data['content']}', '{data['type']}', '{data['date']}');"""
        print(query)
        self._cursor.execute(
            query
        )
        self.conn.commit()


    def load_data(self, object_name: str):
        self._cursor.execute(f"""
        select content, type, date from {object_name};
        """)
        fetched = self._cursor.fetchall()
        return fetched

