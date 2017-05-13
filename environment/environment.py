from ReinforcementGame.environment.cell import Cell


class Environment():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.map = [[Cell(i, j) for j in range(y)] for i in range(x)]

    def draw(self, screen):
        for i in self.map:
            for j in i:
                j.draw(screen)