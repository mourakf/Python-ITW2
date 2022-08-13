from Vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, color, model, license_plate):
        super().__init__(color, model, license_plate)
        self._wheels = 4
        self._license_plate = license_plate
        self.__type = 'Car'
