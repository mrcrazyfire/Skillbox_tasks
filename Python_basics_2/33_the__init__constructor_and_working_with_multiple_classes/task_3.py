class Potato:
    count = 0
    stages = {
        1: "Росток",
        2: "Зеленая",
        3: "Зрелая",
        4: "Перезрела",
    }

    def __init__(self):
        Potato.count += 1
        self.index = Potato.count
        self.stage = 0

    def grow(self):
        if self.stage < 3:
            self.stage += 1
        self.print_state()

    def is_ripe(self):
        if self.stage == 3:
            return True
        return False

    def print_state(self):
        print(f"Картошка {self.index} сейчас {self.stages[self.stage]}")


class PotatoBed:

    def __init__(self, n):
        self.potatoes = [Potato() for _ in range(5)]


    def grow_all(self):
        for potato in self.potatoes:
            potato.grow()

    def are_all_right(self):
        if all(potato.is_ripe() for potato in self.potatoes):
            print("Картошка созрела")
        else:
            print("Картошка еще не созрела")


potatobed = PotatoBed(5)

potatobed.are_all_right()

potatobed.grow_all()
potatobed.are_all_right()
potatobed.grow_all()
potatobed.grow_all()
potatobed.are_all_right()
