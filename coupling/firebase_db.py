from firebase_admin import credentials, initialize_app, db
from datetime import datetime
from enum import Enum, auto

class LogType(Enum):
    INFO = auto()
    DEBUG = auto()
    WARNING = auto()
    ERROR = auto()

class FirebaseLogger:
    root = None

    def __init__(self):
        cred = credentials.Certificate("../cred.json")
        default_app = initialize_app(cred, { "databaseURL": "https://secret.com/"})
        self.root = db.reference()
        


    def log(self, content: str, type: LogType):
        self.root.child('logs').push({
            'content': content,
            'type': type.name,
            'date': datetime.now().timestamp()
        })


    def read_logs(self):
        logs=[]
        for log in db.reference('logs').get().values():
            logs.append(f"({log['type']}) {log['content']} date: {log['date']}")
        return logs



if __name__ == "__main__":
    logger = FirebaseLogger()
    logger.log("hi there!", LogType.INFO)
    print(logger.read_logs())
