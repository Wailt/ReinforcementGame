from pygame.sprite import Sprite
from pygame import *

import numpy.random as npr

from config import CELL_WIDTH, CELL_HEIGHT


# Cell for field
class Cell(Sprite):
    def __init__(self, width, height, img=None):
        Sprite.__init__(self)
        self.x = width
        self.y = height
        self.occupied = False

        # Image for cell
        self.image = Surface((CELL_WIDTH, CELL_HEIGHT))
        if img:
            self.image = image.load(img)
        else:
            self.image.fill(Color(0, npr.randint(255), 0))

        self.rect = Rect(int(self.x * CELL_WIDTH), int(self.y * CELL_HEIGHT), CELL_WIDTH, CELL_HEIGHT)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
