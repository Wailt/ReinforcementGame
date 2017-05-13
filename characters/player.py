from pygame import *
from config import *


class Player(sprite.Sprite):
    WIDTH = 48
    HEIGHT = 48

    def __init__(self, startX, startY,  health_points, img=None):
        sprite.Sprite.__init__(self)
        # Initial location
        self.x = startX
        self.y = startY
        self.rect = Rect(self.x, self.y, PLAYER_WIDTH, PLAYER_HEIGHT)

        # Moving direction
        self.horizontal = 0
        self.vertical = 0

        # Health points
        self.health_points = health_points

        # Load Image on the Environment
        if img:
            self.image = image.load(img)
        else:
            self.image = Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
            self.image.fill(Color(COLOR))

        # Flag: None, 'commander', 'delete'
        self.flag = None

    def update(self):
        self.move()

    def move(self):
        # Don't go out from borders
        if (self.rect.x == 0 and self.horizontal == -1) or (self.rect.x == 19 and self.horizontal == 1):
            self.horizontal = 0
        if (self.rect.y == 0 and self.vertical == -1) or (self.rect.y == 9 and self.vertical == 1):
            self.vertical = 0

        self.rect.x += self.horizontal
        self.rect.y += self.vertical

        self.horizontal = self.vertical = 0

    def attack(self, g):
        g.flag = 'delete'

    def defend(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x * PLAYER_WIDTH, self.rect.y * PLAYER_HEIGHT))


