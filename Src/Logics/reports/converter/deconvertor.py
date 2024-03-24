import json
from Src.Models import *
from functools import singledispatch

class deconvertor:

    @staticmethod
    def load(url: str):
        pass

    @staticmethod
    @singledispatch
    def desirialize(obj: dict, obj_type):
        pass