from Src.Logics.reports.converter import convertor
from Src.Models import abstract_referance

class convertor_models(convertor):

    @staticmethod
    def convert(obj: abstract_referance):
        from Src.Logics.reports.converter import convert_factory
        return {key:convert_factory.create(value).convert(value) for key, value in obj.get_by_attr('head').items()}