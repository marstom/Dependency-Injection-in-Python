from abc import ABC, abstractclassmethod
from typing import Dict


class Database(ABC):

    @abstractclassmethod
    def save_data(self, object_name: str, data: Dict):
        ...

    @abstractclassmethod
    def load_data(self, object_name: str):
        ...
