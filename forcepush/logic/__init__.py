from .EntityManager import EntityManager
from .entity.Player import Player

entity_manager = EntityManager()
player = Player()

entity_manager.register_entity(player)