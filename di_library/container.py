from dependency_injector import containers, providers
import logger
import sqlite3
from database_repo.firebase_database_repo import FireBaseDatabase
from database_repo.sqlite_database_repo import SqliteDatabase
from database_repo.in_memory_database_repo import InMemoryDatabase
from firebase_admin import credentials, initialize_app, db

import firebase_admin


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    # Gateways
    sqlite_client = providers.Singleton(
        sqlite3.connect,
        config.sqlite.dbname
    )

    firebase_client = providers.Singleton(
        FireBaseDatabase,
        initialize_app=initialize_app,
        db_reference=db.reference,
        certificate=credentials.Certificate,
        access_path=config.firebase.access_path,
        credentials_filename=config.firebase.credentials_filename
    )

    # Services
    sqlite_db_service = providers.Factory(
        SqliteDatabase,
        connection=sqlite_client,
    )

    sqlite_logger_service = providers.Factory(
        logger.Logger,
        db_service=sqlite_db_service,
    )

    firebase_logger_service = providers.Factory(
        logger.Logger,
        db_service=firebase_client,
    )

    in_memory_logger_service = providers.Factory(
        InMemoryDatabase,
        connection=None,
    )
