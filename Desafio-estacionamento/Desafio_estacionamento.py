class Vehicle:
    def __init__(self, color, model, license_plate):
        self.connected = False
        self.color = color
        self.model = model
        self._velocity = 0
        self._wheels = 0
        self._type = 'Vehicle'
        self._license_plate = license_plate

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        self._velocity = value

    @property
    def wheels(self):
        return self._wheels

    @wheels.setter
    def wheels(self, value):
        self._wheels = value

    def turn_on(self):
        self.connected = True
        return 'turned on'

    def turn_off(self):
        if(self.velocity > 0):
            while self.velocity > 0:
                self.slow_down()
        self.connected = False
        return 'turned off'

    def speed_up(self, value):
        self.velocity += value

    def slow_down(self):
        if(self.velocity > 0):
            self.velocity -= 10

    def __str__(self):
        return f"{self._type} on? {self.connected}, model: {self.model}, color: {self.color}, velocity: {self.velocity}"


class Car(Vehicle):
    def __init__(self, color, model, license_plate):
        super().__init__(color, model, license_plate)
        self._wheels = 4
        self._license_plate = license_plate
        self.__type = 'Car'


class Motorcycle(Vehicle):
    def __init__(self, color, model, license_plate):
        super().__init__(color, model, license_plate)
        self._wheels = 2
        self._type = 'motorcycle'


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
