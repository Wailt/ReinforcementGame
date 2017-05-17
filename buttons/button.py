from pygame import *

from config import *


class Button(sprite.Sprite):

    def __init__(self, startX, startY, img=None, info=''):
        sprite.Sprite.__init__(self)
        self.font = font.SysFont("monospace", 20)
        self.img = img
        if not img:
            self.rect = Rect(startX * PLAYER_WIDTH, startY * PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
        else:
            self.rect = Rect(startX * PLAYER_WIDTH, startY * PLAYER_HEIGHT, 500, 100)
        self.image = Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.pushed = False
        self.info=info
        if img:
            self.image = image.load(img)

    def draw(self, screen):
        if self.pushed and not self.img:
            self.image.fill(Color(200, 200, 0))
        elif not self.img:
            self.image.fill(Color(255, 255, 255))

        screen.blit(self.image, (self.rect.x, self.rect.y))
        screen.blit(self.font.render(self.info, 1, (0, 0, 0)), (self.rect.x, self.rect.y))
