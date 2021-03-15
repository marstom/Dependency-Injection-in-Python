from abc import ABC, abstractclassmethod
from typing import Dict


class DatabaseRepo(ABC):
    
    @abstractclassmethod
    def init_database(self, access_path: str):
        ...

    @abstractclassmethod
    def save_data(self, object_name: str, data: Dict):
        ...


    @abstractclassmethod
    def load_data(self, object_name: str):
        ...