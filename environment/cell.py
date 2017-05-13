from pygame.sprite import Sprite
from pygame import *

WIDTH = 48
HEIGHT = 48

class Cell(Sprite):
    def __init__(self, x, y, img = None):
        Sprite.__init__(self)
        self.x = x
        self.y = y

        #image for cell
        self.image = Surface((WIDTH, HEIGHT))
        if img:
            self.image = image.load(img)
        else:
            self.image.fill(Color(0, 0, 0))

        self.rect = Rect(int(self.x * WIDTH), int(self.y * HEIGHT))

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
