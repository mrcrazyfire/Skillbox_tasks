class Coordinate:

    def __init__(self, x = 0, y = 0):
        self.set_x(x)
        self.set_y(y)

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    def __str__(self):
        return f"Coordinate({self.__x}, {self.__y})"


coordinate = Coordinate(3, 4)

print(coordinate)
print(coordinate.get_x())