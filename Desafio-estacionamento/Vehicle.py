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
