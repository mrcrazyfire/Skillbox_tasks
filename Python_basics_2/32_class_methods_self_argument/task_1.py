class Car:
    color = 'red'
    price = 1_000_000
    max_speed = 200
    curr_speed = 0

    def info(self):
        print(self.color)
        print(self.price)
        print(self.max_speed)
        print(self.curr_speed)

    def set_speed(self, speed):
        self.curr_speed = speed