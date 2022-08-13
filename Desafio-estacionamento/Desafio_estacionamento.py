from Vehicle import Vehicle
from Car import Car
from Motorcycle import Motorcycle


class Parking_lot():
    def __init__(self):
        self._vagas = 0

    def estacionar(self, type):
        return f"{type} está estacionado"


class Vaga():
    def __init__(self):
        super().__init__()
        pass

    @property
    def vagas(self):
        return self._vagas

    @vagas.setter
    def vagas(self, value):
        self._vagas = value


car1 = Car('azul', 'toyota', "A000")
print(car1.wheels)
car1.velocity = 80
print(car1)
a = car1.turn_off()
print(car1)
# moto1 = Motorcycle('preta', 'Honda', "B000")
# moto1.velocity = 90
# print(moto1)
# moto1.slow_down()
# print(moto1)
