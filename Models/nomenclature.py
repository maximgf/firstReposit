from Models import abstract_referance, nomenclature_group_model, unit_model
from Utils.typecheck import typecheck


class nomenclature_model(abstract_referance):
    __full_name = ''
    __group = None
    __units = None


    @typecheck(expression = lambda x: len(x['full_name']) < 256)
    def __init__(self, full_name: str, group: nomenclature_group_model, units: unit_model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__full_name = full_name
        self.__units = units
        self.__group = group


    @property
    def full_name(self):
        return self.__full_name


    @property
    def group(self):
        return self.__group


    @property
    def units(self):
        return self.__units