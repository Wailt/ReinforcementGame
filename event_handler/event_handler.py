from pygame import *


def event_handler(event):
    #processing events from keyboard
    if event.type == QUIT:
        raise (SystemExit, "QUIT")