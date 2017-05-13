from environment.cell import Cell


# Game Field
class Environment:
    def __init__(self, width, height):
        self.x = width
        self.y = height
        self.map = [[Cell(i, j, img='img/grass_1.png') for j in range(height)] for i in range(width)]

    def draw(self, screen):
        for i in self.map:
            for j in i:
                j.draw(screen)

