import numpy as np


class PhysicsEngine(object):
    def __init__(self):
        self.objects = []
        self.FRICTION = 0.2

    def register_object(self, obj):
        self.objects.append(obj)

    def apply_physics(self):
        for obj in self.objects:
            if obj.vel[0] != 0:
                obj.vel[0] = obj.vel[0] + (1 if obj.vel[0] < 0 else -1) * self.FRICTION
            if obj.vel[1] != 0:
                obj.vel[1] = obj.vel[1] + (1 if obj.vel[1] < 0 else -1) * self.FRICTION

            if np.any(obj.vel):
                # Set any values close to 0, to exactly 0 to avoid bouncing
                obj.vel[abs(obj.vel) < 1e-8] = 0.0
                obj.pos += obj.vel
