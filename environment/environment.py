from environment.cell import Cell
import numpy.random as npr


class Environment:
    def __init__(self, width, height):
        self.map = []
        for i in range(width):
            f = []
            for j in range(height):
                if npr.randint(19):
                    #place grass
                    f.append(Cell(i, j, img='img/grass_' + str(npr.randint(1, 4)) + '.png'))
                else:
                    #place stone
                    cell = Cell(i, j, img='img/stone.png')
                    cell.occupied = True
                    f.append(cell)
            self.map.append(f)


    def draw(self, screen):
        [j.draw(screen) for i in self.map for j in i]

