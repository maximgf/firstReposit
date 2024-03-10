from nomen import nomen_model
from Models.unit import unit_model
from Src.Models.abstract_references import abstract_referance

class recipe_row_model(abstract_referance):
    __nomenculatures: nomen_model = None
    __size: int = 0
    __unit: unit_model = None

    def __init__(self, nomenculature: nomen_model, size: int, unit: unit_model):
        self.__nomenculatures = nomenculature
        self.__size = size
        self.__unit = unit

        super().__init__(name=f"{self.__nomenculatures.name}, {size} {self.__unit.name}")

    @property
    def nomenculature(self):
        return self.__nomenculatures

    @property
    def size(self):
        return self.__size

    def size(self, value : int):
        self.__size = value
    
    @property
    def unit(self):
        return self.__unit


class recipe_model(abstract_referance):
    __rows: list
    __description: str

    def __init__(self, name: str, rows: list[recipe_row_model], description: str = ''):
        self.__rows = rows
        self.description = description
        super().__init__(name)

    @property
    def description(self):
        return self.__description

    def description(self, value: str):
        self.__description = value
    
    def rows(self):
        return self.__rows
    