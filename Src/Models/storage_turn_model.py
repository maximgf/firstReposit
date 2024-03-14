from Models.nomen import nomen_model
from Models.storage_models import storage_model
from Models.unit import unit_model
from Src.Models import abstract_referance
from Src.Models import *


class storage_turn_model(abstract_referance):
    __storage: storage_model
    __remains: int
    __nomen: nomen_model
    __unit: unit_model


    def __init__(self, storage_: storage_model, remains: int,
                nomen: nomen_model, unit: unit_model, name: str = ''):
        super().__init__(name)
        self.__storage = storage_
        self.__remains = remains
        self.__nomen = nomen
        self.__unit = unit


    def storage(self):
        return self.__storage



    def remains(self):
        return self.__remains


    def nomen(self):
        return self.__nomen


    def unit(self):
        return self.__unit