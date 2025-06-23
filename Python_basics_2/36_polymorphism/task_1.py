class Unit:
    def __init__(self, hit_points=100):
        self.hit_points = hit_points

    def get_hit(self, hit=0):
        print(f"Получил {hit} урона.")
        self.hit_points -= hit


class Soldier(Unit):
    def get_hit(self, hit):
        self.hit_points -= hit
        print(f"Солдат получил {hit} урона.")


class Citizen(Unit):
    def get_hit(self, hit):
        self.hit_points -= hit * 2
        print(f"Получил {hit * 2} урона.")
