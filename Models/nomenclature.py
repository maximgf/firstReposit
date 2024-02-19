from Models.abstract_references import abstract_referance
from Models.group_nomenclature import nomenclature_group_model
from Models.unit import unit_model


class nomenclature_model(abstract_referance):
    __full_name = ''
    __group = None
    __units = None


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