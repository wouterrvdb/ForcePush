from forcepush.logic import player
from .input_manager import InputManager

input_manager = InputManager()
input_manager.register_handler(player.movement_handler)