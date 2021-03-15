from datetime import datetime

from log.logger.database_repo.database_repo import Database
from log.logger.enums import LogType


class Logger:
    object_name = "logs"

    def __init__(self, db_service: Database):
        self.db_service = db_service

    def log(self, content: str, type: LogType):
        self.db_service.save_data(object_name=self.object_name, data={
            "content": content,
            "type": type.name,
            "date": datetime.now().timestamp()
        })

    def read_logs(self):
        logs = []
        for log in self.db_service.load_data(object_name=self.object_name):
            logs.append(
                f"({log['type']}) {log['content']} date: {log['date']}")
        return logs

