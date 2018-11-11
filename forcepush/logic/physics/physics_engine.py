import numpy as np


class PhysicsEngine(object):
    def __init__(self):
        self.objects = []

    def register_object(self, obj):
        self.objects.append(obj)

    def apply_physics(self):
        for obj in self.objects:
            if not obj.moved:
                if obj.vel[0] != 0:
                    obj.vel[0] = obj.vel[0] + (1 if obj.vel[0] < 0 else -1)
                if obj.vel[1] != 0:
                    obj.vel[1] = obj.vel[1] + (1 if obj.vel[1] < 0 else -1)
            obj.moved = False

            if np.any(obj.vel):
                obj.pos += obj.vel
