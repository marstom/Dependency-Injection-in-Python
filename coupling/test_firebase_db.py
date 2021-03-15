import pytest
import firebase_db
from firebase_db import LogType, FirebaseLogger
import unittest

from unittest.mock import patch, MagicMock



def test_log():
    with patch.object(firebase_db, "credentials"):
        with patch.object(firebase_db, "initialize_app"):
            with patch.object(firebase_db, "db") as db:
                list_of_logs = []
                class Child:
                    def push(self, value):
                        list_of_logs.append(value)
                        print(list_of_logs)
                mock_root = MagicMock()
                logs_list = Child()
                mock_root.child.return_value = logs_list
                db.reference.return_value = mock_root
                
                logger = FirebaseLogger()
                logger.log("I am test", LogType.WARNING)
                logger.read_logs()
                assert len(list_of_logs) == 1

