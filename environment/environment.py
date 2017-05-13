
# Game Field
from environment.cell import Cell
import numpy.random as npr
from pygame import *
class Environment:
    def __init__(self, width, height):
        self.x = width
        self.y = height
        self.map = [[Cell(i, j, img='img/grass_' + str(npr.randint(1,4)) + '.png') for j in range(height)] for i in range(width)]

    def draw(self, screen):
        for i in self.map:
            for j in i:
                j.draw(screen)

    def update(self):
        for i in self.map:
            for j in i:
                #self.image = image.load(img)
                if npr.randint(10) == 0:
                    j.image = image.load('img/grass_' + str(npr.randint(1,4)) + '.png')

