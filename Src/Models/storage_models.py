from Src.Models import abstract_referance


class storage_model(abstract_referance):
    __adress: str = ''


    def __init__(self, adress: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__adress = adress


    def adress(self) -> str:
        return self.__adress