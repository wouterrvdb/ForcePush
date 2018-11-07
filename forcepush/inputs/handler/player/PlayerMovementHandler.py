import pygame

from forcepush.inputs.handler.Handler import Handler


class PlayerMovementHandler(Handler):
    def __init__(self):
        self.move_left_handler = MoveLeftHandler()
        self.move_right_handler = MoveRightHandler()

    def get_event_types(self):
        return [("key", pygame.K_a, self.move_left_handler), ("key", pygame.K_d, self.move_right_handler)]


class MoveLeftHandler(Handler):
    def handle(self, move_left_event):
        print('Player moved left')


class MoveRightHandler(Handler):
    def handle(self, move_right_event):
        print('Player moved right')
