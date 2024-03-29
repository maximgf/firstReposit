import uuid
from abc import ABC
from Src.error_proxy import error_proxy


class abstract_referance(ABC):
    __id: uuid.UUID
    __name: str = ''
    __error: error_proxy = error_proxy()


    def __init__(self, name: str = ''):
        self.name = name
        self.__id = str(uuid.uuid4())


    def __str__(self):
        return str(self.id)


    def __repr__(self):
        return self.__str__()

    
    def __hash__(self) -> int:
        return hash(self.name)


    def name(self):
        return self.__name.strip()


    @name.setter
    def name(self, value: str):
        self.__name = value.strip()


    @property
    def _error(self):
        return self.__error

    def id(self):
        return self.__id