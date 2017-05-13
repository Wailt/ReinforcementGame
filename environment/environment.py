from cell import Cell


# Game Field
class Environment:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.map = [[Cell(i, j, img='img/grass_1.png') for j in range(y)] for i in range(x)]

    def draw(self, screen):
        for i in self.map:
            for j in i:
                j.draw(screen)

