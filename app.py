import pygame
from pygame import *

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
    pygame.display.set_caption("Rein")
    timer = pygame.time.Clock()

    brains = [Brain(identifier=1,n=2) for i in range(15)] + [Brain(identifier=2,n=2) for i in range(15)]

    while True:
        field = Environment(ENV_WIDTH_CELLS, ENV_HEIGHT_CELLS)

        pac_button = Button(ENV_WIDTH_CELLS, 0, info='PC')
        mode_button = Button(ENV_WIDTH_CELLS, 1, info='mode')
        mode_button_1 = Button(ENV_WIDTH_CELLS, 2, info='mod1')
        mode_button_2 = Button(ENV_WIDTH_CELLS, 3, info='mod2')
        go_button = Button(5, 4, img='img/game_over2.png')
        pacman = Player(field=field,
                        x=0,
                        y=0,
                        health_points=1000,
                        brain=Brain(identifier=3, n=1),
                        img='img/pacman_1.png',
                        animation=['img/pacman_1.png', 'img/pacman_2.png'])

        group_one = [Player(field=field,
                            x=npr.randint(ENV_WIDTH_CELLS / 2),
                            y=npr.randint(ENV_HEIGHT_CELLS / 2),
                            health_points=HP,
                            brain=brains[i],
                            img='img/warrior_2.png') for i in range(15)]

        group_two = [Player(field=field,
                            x=npr.randint(ENV_WIDTH_CELLS / 2, ENV_WIDTH_CELLS),
                            y=npr.randint(ENV_HEIGHT_CELLS / 2, ENV_HEIGHT_CELLS),
                            health_points=HP,
                            brain=brains[i + 15],
                            img='img/warriorNew_1.png') for i in range(15)]

        while len(group_one) > 0 and len(group_two) > 0:
            pacman_list = ([pacman] if pac_button.pushed and pacman.flag != 'delete' else [])
            enteties = group_one + group_two + pacman_list
            timer.tick(7.5)
            for evt in pygame.event.get():
                event_handler(evt, pac_button)
                event_handler(evt, mode_button)
                event_handler(evt, mode_button_1)
                event_handler(evt, mode_button_2)

            pygame.display.update()

            if pac_button.pushed:
                pacman.update(pacman, enteties, mode=True)

            field.draw(screen)
            for g in enteties:
                if g.flag == 'delete':
                    continue
                if len(group_one) != 0 and len(group_two) != 0:
                    if g in group_one:
                        g.update(g, enteties, mode=not (mode_button.pushed or mode_button_1.pushed))
                    elif g in group_two:
                        g.update(g, enteties, mode=not (mode_button.pushed or mode_button_2.pushed))
                g.draw(screen)


            group_one = [i for i in group_one if i.flag != 'delete']
            group_two = [i for i in group_two if i.flag != 'delete']

            pac_button.draw(screen)
            mode_button.draw(screen)
            mode_button_1.draw(screen)
            mode_button_2.draw(screen)
            pygame.display.update()

        field.draw(screen)
        for g in enteties:
            g.draw(screen)

        wait = True
        while wait:
            timer.tick(7)
            go_button.draw(screen)
            for evt in pygame.event.get():
                event_handler(evt, go_button)

            if go_button.pushed:
                wait = False
            pygame.display.update()
    exit()


if __name__ == "__main__":
    main()
