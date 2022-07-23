class Car:
    def __init__(self, color, model, velocity):
        self.connected = False
        self.color = color
        self.model = model
        self.velocity = velocity

    def turn_on(self):
        self.connected = True

    def turn_off(self):
        self.connected = False

    def speed_up(self, velocity):
        self.velocity += velocity

    def slow_down(self):
        self.velocity -= 10

    def __str__(self):
        return f"Car on? {self.connected}, model: {self.model}, color: {self.color}, velocity: {self.velocity}"


blue_car = Car('blue', 'toyota', 55)
blue_car.turn_on()
blue_car.speed_up(5)
# for _ in range(6):
#     blue_car.slow_down()
print(blue_car)
while(blue_car.velocity > 0):
    blue_car.slow_down()

blue_car.turn_off()
print(blue_car)
