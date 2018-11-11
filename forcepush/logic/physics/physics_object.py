import numpy as np

from forcepush import logic


class PhysicsObject(object):
    def __init__(self):
        logic.entity_manager.physics_engine.register_object(self)
        self.pos = np.array([250, 250])
        self.vel = np.array([0, 0])
        self.vel_max = np.array([8, 12])
        self.acc = np.array([2, 6])
        self.moved = False
