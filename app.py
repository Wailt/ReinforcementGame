import pygame
from pygame import *

from time import time, sleep

import numpy.random as npr

from characters.player import Player
from characters.brain import Brain

from environment.environment import Environment
from event_handler.event_handler import event_handler, group_handler

from config import *


def main():
    print("GOOD LUCK HAVE FUN!")

    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Rein Game")

    field = Environment(ENV_WIDTH_CELLS, ENV_HEIGHT_CELLS)

    begin_time = time()
    timer = pygame.time.Clock()
    timer.tick(10)

    brain_one = Brain(identifier=1)
    brain_two = Brain(identifier=2)

    group_one = [Player(field=field,
                    startX=npr.randint(ENV_WIDTH_CELLS/2),
                    startY=npr.randint(ENV_HEIGHT_CELLS/2),
                    health_points=HP,
                    brain = brain_one,
                    img='img/warrior_2.png') for i in range(15)]

    group_two = [Player(field=field,
                    startX=npr.randint(ENV_WIDTH_CELLS/2, ENV_WIDTH_CELLS),
                    startY=npr.randint(ENV_HEIGHT_CELLS/2, ENV_HEIGHT_CELLS),
                    health_points=HP,
                    brain = brain_two,
                    img='img/warriorNew_1.png') for i in range(15)]

    try:
        while 1:

            for evt in pygame.event.get():
                pass
                #event_handler(evt, group_one[0])
                #group_handler(evt, (group_one + group_two)[0], group_one + group_two)

            pygame.display.update()
            #field.update()
            field.draw(screen)
            for g in group_one + group_two:
                if g.flag == 'delete':
                    continue
                g.update(g, group_one + group_two)
                g.draw(screen)

            group_one = [i for i in group_one if i.flag != 'delete']
            group_two = [i for i in group_two if i.flag != 'delete']
            sleep(0.25)
    except Exception as e:
        print('Time:', time() - begin_time)
        print("THX FOR THE GAME!")
        raise e
        exit()


if __name__ == "__main__":
    main()
