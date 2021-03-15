from django.apps import AppConfig
from example import container
from . import views


class LogConfig(AppConfig):
    name = 'log'

    def ready(self):
        container.wire([views])

