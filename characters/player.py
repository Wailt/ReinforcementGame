import pygame
from pygame import *

MOVE_SPEED = 7
WIDTH = 48
HEIGHT = 48
COLOR = "#888888"


class Player(sprite.Sprite):
    WIDTH = 48
    HEIGHT = 48

    def __init__(self, x, y,  health_points, img=None):
        sprite.Sprite.__init__(self)
        # Initial location
        self.startX = x
        self.startY = y

        # Health points
        self.health_point = health_points

        # Image of the Character on Environment
        self.image = Surface((WIDTH, HEIGHT))

        # Load Image on the Environment
        if img:
            self.image = image.load(img)
        else:
            self.image.fill(Color(100, 100, 100)) # Color - ?
            self.rect = Rect(int(self.startX) * WIDTH, int(self.startY) * WIDTH, WIDTH, HEIGHT)

    def go(self):
        pass

    def attack(self):
        pass

    def defend(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


