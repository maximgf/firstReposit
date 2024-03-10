class Settings:
    '''
    Класс хранения настроек.
    '''
    __firstname = ""
    __INN = 0
    __account = 0
    __corr_account = 0
    __BIK = 0
    __type = ""
    __first_start = True


    @property
    def first_name(self) -> str:
        return self.__firstname


    def first_name(self, value: str):
        '''
        Полное наименование
        '''
        self.__firstname = value.strip()


    @property
    def INN(self) -> int:
        return self.__INN


    def INN(self, value: int):
        '''
        ИНН
        '''
        self.__INN = value


    @property
    def account(self):
        return self.__account


    
    def account(self, value: int):
        '''
        Счёт
        '''
        self.__account = value


    @property
    def correspondent_account(self):
        return self.__corr_account
    
    def correspondent_account(self, value: int):
        '''
        Корреспонденский счёт
        '''
        self.__corr_account = value

    @property
    def BIK(self):
        return self.__BIK

    def BIK(self, value: int):
        '''
        БИК
        '''
        self.__BIK = value

    @property
    def type(self):
        return self.__type
    
    def type(self, value: str):
        '''
        Вид собственности
        '''
        if len(value) > 5: raise Exception("Некооректный вид собственности")

        self.__type = value.strip()

    @property
    def is_first_start(self):
        return self.__first_start

    def is_first_start(self, value: bool):
        self.__first_start = value

    @property
    def report_format(self):
        return self.__rep_format

    def report_format(self, value: str):
        self.__rep_format = value