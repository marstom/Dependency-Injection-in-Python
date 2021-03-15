from typing import Dict

from .database_repo import Database


class SqliteDatabase(Database):
    def __init__(self, connection):
        self.conn = connection
        self.conn.row_factory = self._dict_factory
        self._cursor = self.conn.cursor()

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

    def _dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

