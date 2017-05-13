import pygame
from pygame import *

from time import time

from environment.environment import Environment
from event_handler.event_handler import event_handler
from characters.sceleton import Sceleton

WIN_WIDTH = 400
WIN_HEIGHT = 400
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
    timer.tick(100)

    step = 0
    group = [Sceleton(0, 0, 100)]

    try:
        while 1:
            for evt in pygame.event.get():
                event_handler(evt, group[0])
            step += 1
            pygame.display.update()
            field.draw(screen)
            for g in group:
                g.draw(screen)
            print('step:', step/(time() - begin_time))
    except Exception as e:
        print('step:', step)
        print('time:', time() - begin_time)
        raise e


if __name__ == "__main__":
    main()
