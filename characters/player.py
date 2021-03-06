from pygame import *

from characters.stats import Stats
from config import ENV_WIDTH_CELLS, ENV_HEIGHT_CELLS, PLAYER_WIDTH, PLAYER_HEIGHT, HP_COLOUR_GREEN

import numpy as np
import numpy.random as npr


class Player(sprite.Sprite):

    def __init__(self, field, x, y, health_points, brain, img, animation=[]):
        sprite.Sprite.__init__(self)
        self.rect = Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.image = image.load(img)
        self.animation = animation
        self.field = field
        self.field.map[x][y].occupied = True
        self.hp_line = Surface((PLAYER_WIDTH - 5, 5))
        self.hp_line.fill(Color('#00FF00'))
        self.health = Rect(x, y, PLAYER_WIDTH, 5)
        self.brain = brain
        self.horizontal = 0
        self.vertical = 0
        self.health_points = health_points
        self.max_hp = health_points
        self.stats = Stats()
        self.flag = None
        self.dec_list = None
        self.strategy_name = 'init'
        self.frame = 0

    def update(self, npc, world, mode=False):
        if self.strategy_name != mode:
            self.strategy_name = mode
            self.dec_list = None

        self.move()
        self.update_skills()

        if not self.dec_list:
            self.dec_list = self.brain.decide(npc, world, strategy_name=self.strategy_name)
        self.implement_dec_list(world)

    def update_skills(self):
        for key in self.stats.skills:
            self.stats.skills[key] += self.stats.skills_upgrade[key]
            self.stats.skills_upgrade[key] = 0

    def implement_dec_list(self, group):
        dec = self.dec_list[0]
        if dec != 'move':
            self.dec_list = tuple(self.dec_list[1:])
        res = 0
        if dec == 'attack':
            for g in group:
                if np.max(np.fabs([self.rect.x - g.rect.x, self.rect.y - g.rect.y])) <= 1:
                    if self != g and self.brain.identifier != g.brain.identifier:
                        res = self.attack(g) / 10
        elif dec == 'move':
            enemy = sorted([g for g in group if self.brain.identifier != g.brain.identifier],
                   key=lambda x: np.max(np.fabs([self.rect.x - x.rect.x, self.rect.y - x.rect.y])))
            if enemy:
                if max(np.abs([(self.rect.x - enemy[0].rect.x), (self.rect.y - enemy[0].rect.y)])) <= 1:
                    self.dec_list = tuple(self.dec_list[1:])
                else:
                    self.horizontal = (((enemy[0].rect.x - self.rect.x) >= 0) * 2 - 1) if npr.randint(0, 3) else 0
                    self.vertical = (((enemy[0].rect.y - self.rect.y) >= 0) * 2 - 1) if npr.randint(0, 3) else 0
                    res = (abs(self.horizontal) + abs(self.horizontal))/50
            else:
                self.horizontal = npr.randint(0, 3) - 1
                self.vertical = npr.randint(0, 3) - 1
        elif dec == 'pass':
            pass

        self.brain.count_loss(res, self.strategy_name)

    def move(self):
        # Don't go out from border
        if (self.rect.x == 0 and self.horizontal == -1) or (self.rect.x == ENV_WIDTH_CELLS - 1 and self.horizontal == 1):
            self.horizontal = 0
        if (self.rect.y == 0 and self.vertical == -1) or (self.rect.y == ENV_HEIGHT_CELLS - 1 and self.vertical == 1):
            self.vertical = 0

        if self.field.map[self.rect.x + self.horizontal][self.rect.y + self.vertical].occupied:
            self.horizontal = 0
            self.vertical = 0

        # occupation
        self.field.map[self.rect.x][self.rect.y].occupied = False
        self.rect.x += self.horizontal
        self.rect.y += self.vertical
        self.field.map[self.rect.x][self.rect.y].occupied = True

        # skill update
        temp = 10 * float(self.stats.skills["athletics"])
        self.stats.skills_upgrade["athletics"] = (abs(self.horizontal) + abs(self.vertical)) / temp
        self.horizontal = self.vertical = 0

    def attack(self, g):
        damage = self.stats.skills["fight"] * self.stats.attributes["strength"]
        res = g.defend(damage)
        self.stats.skills_upgrade["fight"] = 1 / damage
        return res

    def defend(self, damage):
        blocked_damage = self.stats.skills["defence"] * self.stats.attributes["stamina"] / 10
        self.health_points -= damage - blocked_damage
        if self.health_points <= 0:
            self.flag = 'delete'
            self.field.map[self.rect.x][self.rect.y].occupied = False
        self.stats.skills_upgrade["defence"] = blocked_damage / float(self.stats.skills["defence"])
        return damage - blocked_damage

    def draw(self, screen):
        if len(self.animation) > 0:
            self.image = image.load(
                self.animation[self.frame % 2])
            self.frame += 1
        screen.blit(self.image, (self.rect.x * PLAYER_WIDTH, self.rect.y * PLAYER_HEIGHT))

        self.health = Rect(self.rect.x, self.rect.y, 0, 0)
        self.hp_line = Surface((int((PLAYER_WIDTH - 5) * abs(self.health_points) / self.max_hp), 5))
        self.hp_line.fill(Color(int(min(255 * (1 - self.health_points / self.max_hp), 255)),
                                int(max(255 * (self.health_points / self.max_hp), 0)),
                                0))
        screen.blit(self.hp_line, (self.health.x * PLAYER_WIDTH, self.health.y * PLAYER_HEIGHT))



