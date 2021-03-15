from logger import Logger
from database_repo.in_memory_database_repo import InMemoryDatabaseRepo
from database_repo.firebase_database_repo import FireBaseDatabaseRepo
from enums import LogType
import freezegun


@freezegun.freeze_time("01-01-2020")
def test_memory_logger_write_read():
    logger = Logger(repo=InMemoryDatabaseRepo(), database_path="./path/to/db")
    logger.log(content="New Log", type=LogType.INFO)
    logger.log(content="Error log", type=LogType.ERROR)
    output_logs = logger.read_logs()
    assert output_logs[0] == "(INFO) New Log date: 1577836800.0"
    assert output_logs[1] == "(ERROR) Error log date: 1577836800.0"
