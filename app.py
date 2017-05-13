import pygame
from pygame import *

from time import time, sleep

import numpy.random as npr

from characters.player import Player
from characters.brain import Brain

from environment.environment import Environment
from event_handler.event_handler import event_handler

from buttons.button import Button

from config import *


def main():
    print("GOOD LUCK HAVE FUN!")

    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Rein Game")

    field = Environment(ENV_WIDTH_CELLS, ENV_HEIGHT_CELLS)

    begin_time = time()
    timer = pygame.time.Clock()

    pac_button = Button(ENV_WIDTH_CELLS, 0, info='PC')
    mode_button = Button(ENV_WIDTH_CELLS, 1, info='mode')
    pacman = Player(field=field,
                    startX=0,
                    startY=0,
                    health_points=2000,
                    brain=Brain(identifier=3, n=1),
                    img='img/pacman_1.png',
                    anima=['img/pacman_1.png', 'img/pacman_2.png'])

    group_one = [Player(field=field,
                    startX=npr.randint(ENV_WIDTH_CELLS/2),
                    startY=npr.randint(ENV_HEIGHT_CELLS/2),
                    health_points=HP,
                    brain = Brain(identifier=1),
                    img='img/warrior_2.png') for i in range(15)]

    group_two = [Player(field=field,
                    startX=npr.randint(ENV_WIDTH_CELLS/2, ENV_WIDTH_CELLS),
                    startY=npr.randint(ENV_HEIGHT_CELLS/2, ENV_HEIGHT_CELLS),
                    health_points=HP,
                    brain = Brain(identifier=2),
                    img='img/warriorNew_1.png') for i in range(15)]

    try:
        while 1:
            timer.tick(5)
            for evt in pygame.event.get():
                event_handler(evt, pac_button)
                event_handler(evt, mode_button)
                #group_handler(evt, (group_one + group_two)[0], group_one + group_two)

            pygame.display.update()
            #field.update()
            field.draw(screen)
            for g in group_one + group_two:
                if g.flag == 'delete':
                    continue
                if len(group_one) != 0 and len(group_two) != 0:
                    g.update(g, group_one + group_two, mode=not mode_button.pushed)
                g.draw(screen)

            group_one = [i for i in group_one if i.flag != 'delete']
            group_two = [i for i in group_two if i.flag != 'delete']

            pac_button.draw(screen)
            mode_button.draw(screen)
            if pac_button.pushed:
                pacman.draw(screen)
                pacman.update(pacman, group_one + group_two, mode=True)
    except Exception as e:
        print('Time:', time() - begin_time)
        print("THX FOR THE GAME!")
        raise e
        exit()


if __name__ == "__main__":
    main()
