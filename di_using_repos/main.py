from logger import Logger
from database_repo.firebase_database_repo import FireBaseDatabaseRepo
from enums import LogType

if __name__ == "__main__":
    logger = Logger(repo=FireBaseDatabaseRepo(
    ), database_path="https://secret.com/")
    logger.log(content="New Log", type=LogType.INFO)
    logger.log(content="Error log", type=LogType.ERROR)
    output_logs = logger.read_logs()
    print(output_logs)
