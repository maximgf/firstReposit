from abstract_process import abstract_process
from Src.Models.storage_transaction_model import storage_transaction_model
from Src.Models.storage_turn_model import storage_turn_model


class process_storage_turn(abstract_process):
    
    @classmethod
    def create(cls, journal: list[storage_transaction_model]) -> list[storage_turn_model]:
        result = {}
        for transaction in journal:
            key = (transaction.nomenculature, transaction.storage, transaction.unit.to_base)
            value = transaction.counts * cls.operations[transaction.opearation]
            if key not in result.keys():
                result[key] = value
            else:
                result[key] += value

        turns = []
        for key, value in result.items():
            turn = storage_turn_model(storage_=key[1], remains=value, nomen=key[0], unit=key[2])
            turns.append(turn)

        return turns
