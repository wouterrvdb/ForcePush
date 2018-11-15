from forcepush.logic.entity.entity import Entity
from forcepush.logic.physics.physics_object import PhysicsObject


class PhysicsEntity(Entity):
    def __init__(self, pos, size):
        super().__init__()
        self.physics_object = PhysicsObject(pos, size)
