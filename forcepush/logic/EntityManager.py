# Todo: singleton
from forcepush.inputs import InputManager
from forcepush.logic.entity.Player import Player


class EntityManager(object):
    def __init__(self, input_manager: InputManager):
        self._input_manager = input_manager
        self.player = Player()
        self._input_manager.register_handler(self.player.movement_handler)

    def tick(self):
        pass
