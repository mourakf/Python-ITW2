class Quadrado:
    def __init__(self):
        self._altura = 0
        self._base = 0

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        self._altura = valor

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor):
        self._base = valor

    def area(self):
        return self._altura * self._base


quadr1 = Quadrado()
a = quadr1.altura = 3
b = quadr1.base = 5
calc = quadr1.area()
print(calc)

