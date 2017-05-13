import pygame
from pygame import *

from time import time


import numpy.random as npr

from characters.player import Player
from environment.environment import Environment
from event_handler.event_handler import event_handler, group_handler

WIN_WIDTH = 480
WIN_HEIGHT = 480
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#FFFFFF"


def main():
    # Initializing PyGame
    pygame.init()

    # Screen
    screen = pygame.display.set_mode(DISPLAY)

    # Set game header
    pygame.display.set_caption("Rein Game")

    # Initialize visible surface
    background = Surface(DISPLAY)

    # Fill background with BACKGROUND_COLOR
    background.fill(Color(BACKGROUND_COLOR))

    # Game field
    field = Environment(10, 10)

    begin_time = time()
    timer = pygame.time.Clock()
    timer.tick(10)

    step = 0
    group = [Player(npr.randint(10), npr.randint(10), 100) for i in range(10)]
    group[0].image.fill(Color(0, 100, 0))
    try:
        while 1:
            step += 1
            for evt in pygame.event.get():
                event_handler(evt, group[0])
                group_handler(evt, group[0], group)

            pygame.display.update()
            field.draw(screen)
            for g in group:
                g.update()
                g.draw(screen)
            #print('step:', step/(time() - begin_time))
            #print(group[0].vertical)
            group = [i for i in group if i.flag != 'delete']

    except Exception as e:
        print('step:', step)
        print('time:', time() - begin_time)
        raise e


if __name__ == "__main__":
    main()
