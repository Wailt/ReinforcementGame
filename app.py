import pygame
from pygame import *

from time import time

display = (400, 400)
bg_color = "#FFFFFF"


def main():
    pygame.init()
    screen = pygame.display.set_mode(display)
    pygame.display.set_caption("Rein Game")
    bg = Surface(display)
    bg.fill(Color(bg_color))

    timer = pygame.time.Clock()

    step = 0
    begin_time = time()
    timer.tick(100)
    try:
        while 1:
            step += 1
            pygame.display.update()
            print('step:', step/(time() - begin_time))
    except Exception as e:
        print('step:', step)
        print('time:', time() - begin_time)
        raise e


if __name__ == "__main__":
    main()
