from environment.cell import Cell
import numpy.random as npr
from pygame import *


class Environment:
    def __init__(self, width, height):
        self.env_width = width
        self.env_height = height
        self.map = [[Cell(i, j, img=('img/grass_' + str(npr.randint(1, 4)) + '.png') if npr.randint(10) else 'img/stone.png')
                     for j in range(height)] for i in range(width)]

    def draw(self, screen):
        for i in self.map:
            for j in i:
                j.draw(screen)

