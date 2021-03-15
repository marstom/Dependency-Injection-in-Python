from dependency_injector.wiring import inject, Provide
from logger import Logger
from enums import LogType
from container import Container

import sys


@inject
def firebase_use_logger(
    logger_service: Logger = Provide[Container.firebase_logger_service]
):
    logger = logger_service
    logger.log(content="New Log", type=LogType.INFO)
    logger.log(content="Error log", type=LogType.ERROR)
    output_logs = logger.read_logs()
    print(output_logs)

@inject
def sql_use_logger(
    logger_service: Logger = Provide[Container.sqlite_logger_service]
):
    logger = logger_service
    logger.log(content="New Log", type=LogType.INFO)
    logger.log(content="Error log", type=LogType.ERROR)
    output_logs = logger.read_logs()
    print(output_logs)


if __name__ == "__main__":
    container = Container()
    container.init_resources()
    container.config.from_ini('./config.ini')
    container.wire(modules=[sys.modules[__name__]])
    firebase_use_logger()
