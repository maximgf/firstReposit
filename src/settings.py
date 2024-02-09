

class settings:
    __first_name = ""
    __INN = 0
    __BIK = 0
    __CHET = 0
    __CORESP = 0
    __NAMEE = ""
    __WID_SOB = ""
    
    @property
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self, value: str):
        """
            Полное наименование
        Args:
            value (str): Полное наименование

        Raises:
            Exception: Некорректный аргумента
        """
        if not isinstance(value, str):
            raise Exception("Некорректный аргумент!")
        
        self.__first_name = value.strip()

    @property
    def INN(self):
        return self.__INN
    
    @INN.setter
    def INN(self, value: int):
        """
            ИНН
        Args:
            value (int): Значение ИНН, 12 символов

        Raises:
            Exception: Некорректный тип аргумента
            Exception: Некорректная длина аргумента
        """

        if not isinstance(value, int):
            raise Exception("Некорректный тип аргумента")
        
        if not len(str(value)) == 12:
            raise Exception("Некорректная длина аргумента")

        self.__INN = value
    
    @property
    def BIK(self):
        return self.__BIK
    
    @BIK.setter
    def BIK(self, value: int):
        """
            БИК
        Args:
            value (int): Значение БИК, 9 символов

        Raises:
            Exception: Некорректный тип аргумента
            Exception: Некорректная длина аргумента
        """

        if not isinstance(value, int):
            raise Exception("Некорректный тип аргумента")
        
        if not len(str(value)) == 9:
            raise Exception("Некорректная длина аргумента")

        self.__BIK = value

    
    @property
    def CHET(self):
        return self.__CHET
    
    @CHET.setter
    def CHET(self, value: int):
        """
            Номер банковского счета
        Args:
            value (int): Номер банковского счета, 11 символов

        Raises:
            Exception: Некорректный тип аргумента
            Exception: Некорректная длина аргумента
        """

        if not isinstance(value, int):
            raise Exception("Некорректный тип аргумента")
        
        if not len(str(value)) == 11:
            raise Exception("Некорректная длина аргумента")

        self.__CHET = value
        

    @property
    def CORESP(self):
        return self.__CORESP
    
    @CORESP.setter
    def CORESP(self, value: int):
        """
            Номер корреспондентского счёта
        Args:
            value (int): Номер корреспондентского счёта, 11 символов

        Raises:
            Exception: Некорректный тип аргумента
            Exception: Некорректная длина аргумента
        """

        if not isinstance(value, int):
            raise Exception("Некорректный тип аргумента")
        
        if not len(str(value)) == 11:
            raise Exception("Некорректная длина аргумента")

        self.__CORESP = value


    @property
    def NAMEE(self):
        return self.__NAMEE
    
    @NAMEE.setter
    def NAMEE(self, value: str):
        """
            Наименование собственности
        Args:
            value (str): Наименование собственности

        Raises:
            Exception: Некорректный тип аргумента
        """

        if not isinstance(value, str):
            raise Exception("Некорректный тип аргумента")
        

        self.__NAMEE = value

    
    @property
    def WID_SOB(self):
        return self.__WID_SOB
    
    @WID_SOB.setter
    def WID_SOB(self, value: str):
        """
            Тип собственности
        Args:
            value (str): Тип собственности, 5 символов

        Raises:
            Exception: Некорректный тип аргумента
            Exception: Некорректная длина аргумента
        """

        if not isinstance(value, str):
            raise Exception("Некорректный тип аргумента")
        
        if not len(str(value)) == 5:
            raise Exception("Некорректная длина аргумента")

        self.__WID_SOB = value