from Models.abstract_references import abstract_referance
from Models.nomen import nomen_model
from Models.nomen_grope import nomen_group_model
from Models.unit import unit_model
from Src.Logics.storage_prototype import storage_prototype
from Src.Logics.start_factory import start_factory
from Src.settings_manager import settings_manager
from Src.Storage.Storage import storage
from datetime import datetime
from Src.Models import *
import unittest

class period(abstract_referance):
    __start: datetime
    __end: datetime

    def __init__(self, start: datetime, end: datetime, *args, **kwargs):
        self.__start: datetime = start
        self.__end: datetime = end
        super().__init__(*args, **kwargs)


    @property
    def start(self) -> datetime:
        return self.__start

    @property
    def end(self) -> datetime:
        return self.__end


class test_prototype(unittest.TestCase):

    def test_prototype_period(self):
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()

        key = storage.journal_key()
        data = start.storage.data[key]

        prototype = storage_prototype( data )

        start_date = datetime.strptime("2024-01-01", '%Y-%m-%d')
        stop_date = datetime.strptime("2024-01-10", '%Y-%m-%d')

        result = prototype.filter_by( period(start_date, stop_date) )

        print(result.data)
        assert isinstance(result, storage_prototype)


    def test_prototype_nomenculature(self):
        manager = settings_manager()
        start = start_factory(manager.settings)
        start.create()

        key = storage.journal_key()
        data = start.storage.data[key]

        prototype = storage_prototype( data )

        nomen = nomen_model(name='Сливочное масло', group=nomen_group_model.create_group(), units=unit_model.create_gramm())

        result = prototype.filter_by( nomen )

        print(result.data)
        assert isinstance(result, storage_prototype)