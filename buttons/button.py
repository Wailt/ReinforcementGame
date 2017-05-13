from pygame import *

from config import *


class Button(sprite.Sprite):

    def __init__(self, startX, startY, img=None):
        sprite.Sprite.__init__(self)
        self.myfont = font.SysFont("monospace", 24)
        self.rect = Rect(startX * PLAYER_WIDTH, startY * PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.image = Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        if img:
            self.image = image.load(img)
        else:
            self.image.fill(Color(255, 255, 255))

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        self.label = self.myfont.render("PC", 1, (0, 0, 0))
        screen.blit(self.label, (self.rect.x, self.rect.y))
