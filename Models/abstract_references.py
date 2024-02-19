import uuid
from abc import ABC
from src.argument_exception import argument_exception
from src.error_proxy import error_proxy


class abstract_referance(ABC):
    __id: uuid.UUID
    __name: str = ''
    __error: error_proxy = error_proxy()


    def __init__(self, name: str = None):
        self.name = name
        self.__id = uuid.uuid4()


    @property
    def name(self):
        return self.__name.strip()


    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise argument_exception("Неверный аргумент!")

        if not (len(value) >= 1 and len(value) <= 50):
            raise argument_exception("Несоответствующая длина аргумента")
        self.__name = value.strip()


    @property
    def error(self):
        return self.__error
    