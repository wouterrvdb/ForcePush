import numpy as np

from forcepush import logic


class PhysicsObject(object):
    def __init__(self):
        logic.entity_manager.physics_engine.register_object(self)
        self.pos = np.array([250.0, 250.0])
        self.vel = np.array([0.0, 0.0])
        self.vel_max = np.array([8.0, 12.0])
        self.acc = np.array([2.0, 6.0])
        self.mass = 1.0
        self.no_gravity = False
