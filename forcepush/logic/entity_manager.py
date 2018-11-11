from .entity.entity import Entity


class EntityManager(object):
    def __init__(self):
        self.entities = {}

    def register_entity(self, entity: Entity):
        if entity.id in self.entities:
            # TODO: Throw exception
            return None
        self.entities[entity.id] = entity

    def tick(self):
        for entity in self.entities.values():
            entity.tick()
