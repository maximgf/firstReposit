import os
import json
import uuid
from src.settings import settings


class settings_manager (object):
    # Настройки инстанс
    __settings = None
     # Имя файла настроек
    __filename = "settings.json"
    # Словарь с данными
    __data = {}
    # Уникальный номер
    __unique_number = None


    def __init__(self) -> None:
        self.__unique_number =  uuid.uuid4()
        
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(settings_manager, cls).__new__(cls)
        return cls.instance

    @property
    def data(self):
        return self.__data
    
    @property
    def settings(self):
        return self.__settings
    
    def __convert(self):
        """
            Заполнить объект настроек
        Raises:
            Exception: Невозможно создать экземпляр класса настроек
        """
        if not self.__settings:
            self.__settings = settings()
        if not isinstance(self.__settings, settings):
            raise Exception("Невозможно создать экземпляр класса настроек")
        for key in self.__data.keys():
            if not hasattr(self.__settings, key): return
            setattr(self.__settings, key, self.__data[key])

    def open(self, filename):
        """
            Открыть файл с настройками
        Args:
            filename: Имя файла
        Raises:
            Exception: Неверный тип аргумента
            Exception: Неверная длина аргумента
        """
        if not isinstance(filename, str):
            raise Exception("Неверный тип аргумента")
        
        if len(filename) == 0:
            raise Exception("Неверная длина аргумента")
        
        self.__filename = filename.strip()
        return self.__open()

    def __open(self):
        """
            Открыть файл с настройками
        Raises:
            Exception: Ошибка при открытии файла
        """

        settings_file = self.__filename

        if not os.path.exists(settings_file):
            raise Exception("Невозможно загрузить файл настроек")
        
        with open(settings_file, "r", encoding="UTF-8") as read_file:
            self.__data = json.load(read_file)
        
        self.__convert()

        return True
    @property
    def number(self)-> str:
        return str(self.__unique_number.hex)