from abc import ABC, abstractmethod
from Src.settings import Settings
from Storage.Storage import storage


class report(ABC):

    _storage: storage
    _settings: Settings
    
    def __init__(self, storage_: storage, settings: Settings):
        self._storage = storage_
        self._settings = settings

    @abstractmethod
    def create(self) -> str:
        pass