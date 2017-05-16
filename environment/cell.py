from pygame import *
from config import CELL_WIDTH, CELL_HEIGHT


class Cell(sprite.Sprite):
    def __init__(self, width, height, img=None):
        sprite.Sprite.__init__(self)
        self.cell_width = width
        self.cell_height = height
        self.occupied = False

        self.image = image.load(img)
        self.rect = Rect(self.cell_width * CELL_WIDTH, self.cell_height * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
