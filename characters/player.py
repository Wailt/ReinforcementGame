import pygame
from pygame import *

import numpy as np

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
        self.rect = Rect(x, y, WIDTH, HEIGHT)

        # Moving direction
        self.horizontal = 0
        self.vertical = 0

        # Health points
        self.health_points = health_points

        # Load Image on the Environment
        if img:
            self.image = image.load(img)
        else:
            self.image = Surface((WIDTH, HEIGHT))
            self.image.fill(Color(COLOR))

        # Flag: None, 'commander', 'delete'
        self.flag = None
    def move(self):
        self.rect.x += self.horizontal
        self.rect.y += self.vertical

    def attack(self):
        pass

    def defend(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x * WIDTH, self.rect.y * HEIGHT))


