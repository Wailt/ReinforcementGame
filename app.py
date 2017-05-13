import pygame
from pygame import *

from time import time


import numpy.random as npr

from characters.brain import Brain
from characters.player import Player
from environment.environment import Environment
from event_handler.event_handler import event_handler, group_handler

WIN_WIDTH = 960
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
    field = Environment(20, 10)

    begin_time = time()
    timer = pygame.time.Clock()
    timer.tick(5)

    step = 0
    brain = Brain()
    group = [Player(startX=npr.randint(10),
                    startY=npr.randint(10),
                    health_points=100,
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
            #print('step:', step/(time() - begin_time))
            print(group[0].stats.skills["fight"], " , ", group[0].stats.skills["athletics"])
            group = [i for i in group if i.flag != 'delete']

    except Exception as e:
        print('step:', step)
        print('time:', time() - begin_time)
        raise e


if __name__ == "__main__":
    main()
