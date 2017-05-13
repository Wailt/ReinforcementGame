from pygame.constants import *


def event_handler(e, player):
    #processing events from keyboard
    if e.type == QUIT:
        raise (SystemExit, "QUIT")
    if e.type == KEYDOWN:
        if e.key == K_RIGHT:
            player.right = 1
        elif e.key == K_LEFT:
            player.right = -1
        elif e.key == K_UP:
            player.up = -1
        elif e.key == K_DOWN:
            player.up = 1
