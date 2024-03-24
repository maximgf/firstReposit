from unit import unit_model
from nomen import nomen_model
from storage_models import storage_model
from Src.Models import abstract_referance
from datetime import datetime
from Src.Models import *


class storage_transaction_model(abstract_referance):
    __storage: storage_model
    __nomen: nomen_model
    __operation: bool
    __contes: int
    __unit: unit_model
    __period: datetime


    def __init__(self, storage: storage_model, 
                nomen: nomen_model, operation: bool, countes: int, 
                unit: unit_model, period: datetime,  name: str = ''):
        super().__init__(name)
        self.__storage = storage
        self.__nomen = nomen
        self.__operation = operation
        self.__contes = countes
        self.__unit = unit
        self.__period = period

    
    @property
    def name(self):
        return self.name

    
    @name.setter
    def name(self, value):
        self.__name = value

    
    def storage(self):
        return self.__storage


    def nomenculature(self) -> nomen_model:
        return self.__nomen


    def opearation(self):
        return self.__operation



    def counts(self):
        return self.__contes


    def unit(self):
        return self.__unit


    def period(self):
        return self.__period