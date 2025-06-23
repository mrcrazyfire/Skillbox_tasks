class Robot:
    def __init__(self, model):
        self.model = model


class RobotVacuum(Robot):
    def __init__(self, model):
        super().__init__(model)
        self.trash_bin = 0

    def operate(self):
        print(f"{self.model} начинает пылесосить.")
        self.trash_bin += 1
        print(f"Текущая заполненность мешка: {self.trash_bin}")


class SecurityRobot(Robot):
    def __init__(self, model):
        super().__init__(model)
        self.signaling = False

    def operate(self):
        self.signaling = True
        print(f'{self.model} включил сигнализацию и начал патрулирование.')


class PoolRobot(SecurityRobot):
    def __init__(self, model, depth):
        super().__init__(model)
        self.depth = depth

    def operate(self):
        super().operate()
        print(f"{self.model} ведет патрулирование на глубине {self.depth} метров.")

robot_vacuum = RobotVacuum("Robot Vacuum")
robot_vacuum.operate()

security_robot = SecurityRobot("Security Robot")
security_robot.operate()

pool_robot = PoolRobot("Pool Robot", 5)
pool_robot.operate()
