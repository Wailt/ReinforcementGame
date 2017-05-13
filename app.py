import pygame
from pygame import *

from time import time

import numpy.random as npr

from characters.player import Player
from characters.brain import Brain

from environment.environment import Environment
from event_handler.event_handler import event_handler, group_handler

from config import *


def main():
    print("GOOD LUCK HAVE FUN!")
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
    field = Environment(ENV_WIDTH_CELLS, ENV_HEIGHT_CELLS)

    begin_time = time()
    timer = pygame.time.Clock()
    timer.tick(10)

    step = 0

    brain = Brain()

    group = [Player(startX=npr.randint(ENV_WIDTH_CELLS),
                    startY=npr.randint(ENV_HEIGHT_CELLS),
                    health_points=HP,
                    brain = brain,
                    img='img/warrior_1.png') for i in range(10)]
    try:
        while 1:
            step += 1
            for evt in pygame.event.get():
                event_handler(evt, group[0])
                group_handler(evt, group[0], group)

            pygame.display.update()
            field.draw(screen)
            for g in group:
                g.update(g, group)
                g.draw(screen)

            group = [i for i in group if i.flag != 'delete']

    except Exception as e:
        print('Time:', time() - begin_time)
        print("THX FOR THE GAME!")
        raise e
        exit()


if __name__ == "__main__":
    main()
