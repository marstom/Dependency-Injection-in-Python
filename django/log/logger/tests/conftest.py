import pytest
from log.logger.enums import LogType


@pytest.fixture
def log_info_data():
    return {
            'content': "info",
            'type': LogType.INFO.name,
            'date': '234242424'
        }

@pytest.fixture
def log_warn_data():
    return {
            'content': "this is warning",
            'type': LogType.WARNING.name,
            'date': '234242424'
        }