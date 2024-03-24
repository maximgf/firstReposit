
from functools import singledispatchmethod
from Models.abstract_references import abstract_referance
from Models.nomen import nomen_model
from Models.recipe import recipe_model
from Models.storage_models import storage_model
from Models.storage_transaction_model import storage_transaction_model
from Src.Logics.processes.process_factory import process_factory
from Src.Logics.reports.converter.convert_factory import convert_factory
from Src.Logics.storage_prototype import storage_prototype
from Src.exceptions import argument_exception, exception_proxy, operation_exception
from datetime import datetime
import json
from Storage.Storage import storage

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
    
class storage_service:
    __data = []
    
    def __init__(self, data: list) -> None:
        if len(data) == 0:
            raise argument_exception("Некорректно переданы параметры!")
        
        self.__data = data
        self.__convert = convert_factory()
        
        
    @singledispatchmethod
    def create_turns(self, obj, **kwargs):
        raise operation_exception(f"Нет сервиса для {type(obj)}.")


    @create_turns.register
    def _(self, obj: period, **kwargs):
        prototype = storage_prototype( self.__data )
        transactions = prototype.filter_by( obj ).data
        processing = process_factory().create(storage.process_turn_key())
        rests = processing.create(transactions)
        return rests


    @create_turns.register
    def _(self, obj: nomen_model, **kwargs):
        prototype = storage_prototype( self.__data )
        transactions = prototype.filter_by( obj ).data
        processing = process_factory().create(storage.process_turn_key())
        rests = processing.create(transactions)
        return rests


    @create_turns.register
    def _(self, obj: recipe_model, **kwargs):
        if 'storage' not in kwargs.keys(): raise argument_exception("Для создания оборотов по рецепту, нужно передать склад!")
        prototype = storage_prototype( self.__data )
        transactions = prototype.filter_by( kwargs['storage'] ).filter_by( obj ).data
        processing = process_factory().create(storage.process_turn_key())
        rests = processing.create(transactions)
        return rests


    def create_debits(self, obj: recipe_model, storage_: storage_model):
        turns = self.create_turns(obj, storage=storage_)

        recipe_need = {}
        for recipe_row in obj.rows:
            recipe_need[recipe_row.nomenculature.name] = recipe_row.size

        transactions = []
        for turn in turns:
            if recipe_need[turn.nomen.name] > turn.remains:
                raise operation_exception('Не удалось произвести списование! Остатков на складе не достаточно!')
            transactions.append(storage_transaction_model(storage=storage_, nomen=turn.nomen, operation=False, 
                                                        countes=recipe_need[turn.nomen.name], unit=turn.unit, period=datetime.now()))

        return transactions

        
    @staticmethod
    def create_response(data: list | dict, app):
        data = convert_factory.create(data).convert(data)
        data = json.dumps(data, indent=4, ensure_ascii=False)

        result = app.response_class(
            response = data,
            status=200,
            mimetype="application/json; charset=utf-8"
        )
        return result


    @property
    def data(self) -> list:
        return self.__data