from log.logger.database_repo.sqlite_database_repo import SqliteDatabase

import sqlite3

def test_sqlite(log_info_data, log_warn_data):
    connection = sqlite3.connect( ':memory:')
    repo = SqliteDatabase(connection)
    repo.save_data(object_name="logs", data=log_info_data)
    repo.save_data(object_name="logs", data=log_warn_data)

    print(repo.load_data("logs"))

    assert len(repo.load_data(object_name="logs")) == 2
    assert repo.load_data(object_name="logs")[1]["content"] == "this is warning"
    assert repo.load_data(object_name="logs")[1]["type"] == "WARNING"

