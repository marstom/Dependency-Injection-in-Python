from datetime import datetime
import pytest

from enums import LogType
from database_repo.sqlite_database_repo import SqliteDatabaseRepo



def test_sqlite(log_info_data, log_warn_data):
    repo = SqliteDatabaseRepo()
    repo.init_database(access_path=":memory:")
    repo.save_data(object_name="logs", data=log_info_data)
    repo.save_data(object_name="logs", data=log_warn_data)

    print(repo.load_data("logs"))

    assert len(repo.load_data(object_name="logs")) == 2
    assert repo.load_data(object_name="logs")[1]["content"] == "this is warning"
    assert repo.load_data(object_name="logs")[1]["type"] == "WARNING"

