from forcepush.inputs.handler.player.PlayerMovementHandler import PlayerMovementHandler
from forcepush.logic.entity.Entity import Entity


class Player(Entity):
    def __init__(self):
        self.movement_handler = PlayerMovementHandler()

    def tick(self):
        pass