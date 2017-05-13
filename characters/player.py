from pygame import *

from characters.stats import Stats
from config import *

WIDTH = 48
HEIGHT = 48

class Player(sprite.Sprite):


    def __init__(self, startX, startY, health_points, brain, img=None):
        sprite.Sprite.__init__(self)

    # Initial location
        self.x = startX
        self.y = startY
        self.rect = Rect(self.x, self.y, WIDTH, HEIGHT)

        self.brain = brain

        # Moving direction
        self.horizontal = 0
        self.vertical = 0

        # Health points
        self.health_points = health_points

        # Statistics
        self.stats = Stats()

        # Load Image on the Environment
        if img:
            self.image = image.load(img)
        else:
            self.image = Surface((WIDTH, HEIGHT))
        #self.image.fill(Color(COLOR))
        # Flag: None, 'commander', 'delete'
        self.flag = None

    def update(self, npc, world):
        self.move()
        self.update_skills()
        self.brain.decide(npc, world)

    def update_skills(self):
        for key in self.stats.skills:
            self.stats.skills[key] += self.stats.skills_upgrade[key]
            self.stats.skills_upgrade[key] = 0

    def move(self):
        # Don't go out from border
        if (self.rect.x == 0 and self.horizontal == -1) or (self.rect.x == 19 and self.horizontal == 1):
            self.horizontal = 0
        if (self.rect.y == 0 and self.vertical == -1) or (self.rect.y == 9 and self.vertical == 1):
            self.vertical = 0

        self.rect.x += self.horizontal
        self.rect.y += self.vertical

        temp = 10 * float(self.stats.skills["athletics"])
        self.stats.skills_upgrade["athletics"] = (abs(self.horizontal) + abs(self.vertical)) / temp
        # self.stats.skills["athletics"] += self.stats.skills_upgrade["athletics"]

        self.horizontal = self.vertical = 0

    def attack(self, g):
        damage = self.stats.skills["fight"] * self.stats.attributes["strength"]
        # damage = 45
        g.defend(damage)
        self.stats.skills_upgrade["fight"] = 1 / damage  # self.stats.skills["fight"]
        # self.stats.skills["fight"] += self.stats.skills_upgrade["fight"]

    def defend(self, damage):
        blocked_damage = self.stats.skills["defence"] * self.stats.attributes["stamina"] / 10
        self.health_points -= damage - blocked_damage
        if self.health_points <= 0:
            self.flag = 'delete'
        self.stats.skills_upgrade["defence"] = blocked_damage / float(self.stats.skills["defence"])

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x * PLAYER_WIDTH, self.rect.y * PLAYER_HEIGHT))


