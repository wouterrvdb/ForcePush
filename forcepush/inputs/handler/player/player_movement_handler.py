import pygame

from forcepush.inputs.handler.handler import Handler
from forcepush.logic.entity.player import Player


class PlayerMovementHandler(Handler):
    def __init__(self, player: Player):
        self.player = player
        self.move_left_handler = MoveLeftHandler(self)
        self.move_right_handler = MoveRightHandler(self)

    def get_event_types(self):
        return [("key", pygame.K_a, self.move_left_handler), ("key", pygame.K_d, self.move_right_handler)]


class MoveLeftHandler(Handler):
    def __init__(self, player_movement_handler: PlayerMovementHandler):
        self.player_movement_handler = player_movement_handler

    def handle(self, move_left_event):
        self.player_movement_handler.player.move_left()


class MoveRightHandler(Handler):
    def __init__(self, player_movement_handler: PlayerMovementHandler):
        self.player_movement_handler = player_movement_handler

    def handle(self, move_right_event):
        self.player_movement_handler.player.move_right()
