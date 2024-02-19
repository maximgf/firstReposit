from Models.abstract_references import abstract_referance


class unit_model(abstract_referance):

    __base = None
    __num : int
    __coefficient: int


    def __init__(self, base = None, num: int = 0, coefficient: int = 0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__base = base
        self.num = num
        self.__coefficient = coefficient


    @property
    def to_base(self):
        num = self.num*self.coefficient

        return unit_model(base=self.base.base, num=num, coefficient=self.base.coefficient, name=self.base.name)


    @property
    def num(self):
        return self.__num


    @num.setter
    def num(self, value: int):
        self.__num = value


    @property
    def base(self):
        return self.__base


    @property
    def coefficient(self):
        return self.__coefficient


    def __str__(self):
        return f"{self.num} {self.name}"