from pygame.constants import *
import numpy as np

def event_handler(e, player):
    if e.type == QUIT:
        raise (SystemExit, "QUIT")
    if e.type == KEYDOWN:
        if e.key == K_RIGHT:
            player.horizontal = 1
        elif e.key == K_LEFT:
            player.horizontal = -1
        elif e.key == K_UP:
            player.vertical = -1
        elif e.key == K_DOWN:
            player.vertical = 1

def group_handler(e, player, group):
    if e.type == KEYDOWN:
        if e.key == K_e:
            for g in group:
                metric = np.max([player.rect.x - g.rect.x, player.rect.y - g.rect.y])
                if metric <= 1:
                    if player != g:
                        player.attack(g)
                        break