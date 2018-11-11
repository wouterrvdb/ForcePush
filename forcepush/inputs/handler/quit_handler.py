import pygame

from forcepush.inputs.handler.handler import Handler


class QuitHandler(Handler):
    def __init__(self):
        self.quit = False

    def handle(self, _):
        self.quit = True

    def get_event_types(self):
        return [("event", pygame.QUIT, self), ("key", pygame.K_ESCAPE, self)]

    def has_quit(self):
        return self.quit
