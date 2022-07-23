# definição da classe

class TV:
    def __init__(self):
        self.connected = False
        self.channel = 3
        self.channel_min = 1
        self.channel_max = 1
        self.vol = 8
        self.vol_min = 0
        self.vol_max = 100

    def turn_on(self):
        self.connected = True

    def turn_off(self):
        self.connected = False

    def change_channel_up(self):
        if not self.connected:
            return
        elif self.change_channel < self.channel_max:
            self.change_channel += 1

    def change_channel_down(self):
        if not self.connected:
            return
        elif self.change_channel > self.channel_min:
            self.change_channel -= 1

    def vol_up(self):
        if not self.connected:
            return
        elif self.vol < self.vol_max:
            self.vol += 1

    def vol_down(self):
        if not self.connected:
            return
        elif self.vol > self.vol_min:
            self.vol -= 1

    def __str__(self) -> str:
        return f"TV está ligada {self.connected} - canal {self.channel}, volume {self.vol}"


# criar instâncias da classe
tv_one = TV()
tv_two = TV()
tv_one.turn_on()
print(tv_one.connected)
print(tv_two.connected)


for _ in range(3):
    tv_one.vol_up()

print(tv_one.vol)
print(tv_one)
