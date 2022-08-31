from Vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, color, model, license_plate):
        super().__init__(color, model, license_plate)
        self._wheels = 2
        self._type = 'motorcycle'
