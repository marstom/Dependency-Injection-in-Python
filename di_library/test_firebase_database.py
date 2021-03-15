from dependency_injector import providers

from database_repo.in_memory_database_repo import InMemoryDatabase

from main import firebase_use_logger, sql_use_logger
from container import Container
import sys
import pytest


@pytest.mark.real_database
def test_firebase_logger_write_read():
    container = Container()
    container.init_resources()
    container.config.from_ini('./config.ini')
    container.wire(modules=[sys.modules[__name__]])
    firebase_use_logger()


def test_firebase_logger_write_read_override_original():
    container = Container()
    container.init_resources()
    container.firebase_client.override(providers.Singleton(
        InMemoryDatabase, connection=None, access_path="path/to/database.db"
    ))
    container.config.from_ini('./config.ini')
    container.wire(modules=[sys.modules[__name__]])
    firebase_use_logger()


def test_sqlite_logger_write_read():
    container = Container()
    container.init_resources()
    container.config.from_ini('./config.ini')
    container.wire(modules=[sys.modules[__name__]])
    sql_use_logger()
