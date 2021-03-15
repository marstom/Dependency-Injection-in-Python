import pytest

from logger import Logger
from database_repo.in_memory_database_repo import InMemoryDatabaseRepo
from database_repo.firebase_database_repo import FireBaseDatabaseRepo
from enums import LogType


# warning this is real database
def test_firebase_logger_write_read():
    logger = Logger(repo=FireBaseDatabaseRepo(
    ), database_path="https://secret.com/")
    logger.log(content="New Log", type=LogType.INFO)
    logger.log(content="Error log", type=LogType.ERROR)
    output_logs = logger.read_logs()
    print(output_logs)
