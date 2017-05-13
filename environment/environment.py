from ReinforcementGame.environment.cell import Cell


class Environment():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.map = [[Cell(i, j) for j in range(y)] for i in range(x)]