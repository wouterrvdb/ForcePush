from .entity_manager import EntityManager
from .entity.player import Player
from forcepush.inputs.handler.player.player_movement_handler import PlayerMovementHandler

entity_manager = EntityManager()
player = Player()

player.movement_handler = PlayerMovementHandler(player)
entity_manager.register_entity(player)
