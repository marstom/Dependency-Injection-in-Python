from datetime import datetime

from database_repo.database_repo import DatabaseRepo
from enums import LogType


class Logger:
    object_name = "logs"
    
    def __init__(self, repo: DatabaseRepo, database_path: str):
        self.repo = repo
        self.repo.init_database(database_path)

    def log(self, content: str, type: LogType):
        self.repo.save_data(object_name=self.object_name, data={
            "content": content,
            "type": type.name,
            "date": datetime.now().timestamp()
        })

    def read_logs(self):
        logs=[]
        for log in self.repo.load_data(object_name=self.object_name):
            logs.append(f"({log['type']}) {log['content']} date: {log['date']}")
        return logs


