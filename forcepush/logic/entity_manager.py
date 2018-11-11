from .entity.entity import Entity
from .physics.physics_engine import PhysicsEngine


class EntityManager(object):
    def __init__(self):
        self.entities = {}
        self.physics_engine = PhysicsEngine()

    def register_entity(self, entity: Entity):
        if entity.id in self.entities:
            # TODO: Throw exception
            return None
        self.entities[entity.id] = entity

    def tick(self):
        for entity in self.entities.values():
            entity.tick()
        self.physics_engine.apply_physics()
