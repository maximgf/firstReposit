from Src.Logics.reports.converter import convertor
import json
from exceptions import argument_exception


class convertor_basic(convertor):

    @staticmethod
    def convert(obj):
        try:
            json.dumps(obj)
        except TypeError:
            raise argument_exception("Not standart type to serialize!")

        return obj