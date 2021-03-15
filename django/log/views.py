from django.shortcuts import render, HttpResponse
from log.logger.container import Container
from dependency_injector.wiring import inject, Provide


@inject
def logs_list(
    request,
    logger_serivice: "Logger" = Provide(Container.firebase_logger_service)
):
    logs = ""
    for log in logger_serivice.read_logs():
        logs += f"<p>{log}</p>"
    return HttpResponse(logs)
