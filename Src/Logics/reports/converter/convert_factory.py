from Logics.reports.converter.convertor_basic import convertor_basic
from functools import singledispatch
from datetime import datetime
from Logics.reports.converter.convertor_datetime import convertor_datetime
from Logics.reports.converter.convertor_iterator import convertor_iterator
from Logics.reports.converter.convertor_models import convertor_models
from Models.abstract_references import abstract_referance

class convert_factory:
    
    @singledispatch
    @staticmethod
    def create(obj):
        return convertor_basic


    @create.register
    def create_model(obj: abstract_referance):
        return convertor_models


    @create.register
    def create_datetime(obj: datetime):
        return convertor_datetime


    @create.register
    def create_iterator(obj: list):
        return convertor_iterator