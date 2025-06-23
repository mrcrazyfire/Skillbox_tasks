class CanFly:
    def __init__(self):
        self.height = 0
        self.speed = 0

    def fly_up(self):
        pass

    def fly(self):
        pass

    def land(self):
        self.height = 0
        self.speed = 0

    def __str__(self):
        return f"Height: {self.height}, speed:{self.speed}"


class Butterfly(CanFly):
    def fly_up(self):
        self.height += 1

    def fly(self):
        self.speed += 0.5


class Rocket(CanFly):
    def fly_up(self):
        self.height += 500
        self.speed += 1000

    def land(self):
        super().land()
        self.boom()

    def boom(self):
        print("Ракета взорвалась")