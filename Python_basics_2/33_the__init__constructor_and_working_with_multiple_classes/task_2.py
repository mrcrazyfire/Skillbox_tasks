class Coordinate:
    count = 0

    def __init__(self, x = 0, y = 0):
        Coordinate.count += 1
        self.x = x
        self.y = y



    def info(self):
        print(f"Coordinate: {self.x}, {self.y}")
        print(f"Count: {self.count}")


coord_1 = Coordinate()
coord_1.info()
coord_2 = Coordinate(1, 1)
coord_2.info()
coord_3 = Coordinate(2, 2)
coord_3.info()

