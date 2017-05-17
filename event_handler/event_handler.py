from pygame import *
import numpy as np

def event_handler(e, button):
    if e.type == QUIT:
        raise (SystemExit, "QUIT")
    if e.type == MOUSEBUTTONDOWN:
        if button.rect.collidepoint(mouse.get_pos()):
            button.pushed = not button.pushed


def group_handler(e, player, group):
    if e.type == KEYDOWN:
        if e.key == K_e:
            for g in group:
                metric = np.max(np.fabs([player.rect.x - g.rect.x, player.rect.y - g.rect.y]))
                if metric <= 1:
                    if player != g:
                        player.attack(g)
                        break