from pygame import *


def event_handler(event):
    if event.type == QUIT:
        raise (SystemExit, "QUIT")