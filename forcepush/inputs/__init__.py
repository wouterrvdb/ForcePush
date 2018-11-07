from forcepush.logic import player
from .InputManager import InputManager

input_manager = InputManager()
input_manager.register_handler(player.movement_handler)