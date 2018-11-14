import numpy as np

from forcepush.logic.terrain import Terrain


class PhysicsEngine(object):
    def __init__(self):
        self.objects = []
        self.terrain = None
        self.G = 0.01

    def register_object(self, obj):
        self.objects.append(obj)

    def set_terrain(self, terrain: Terrain):
        self.terrain = terrain

    def apply_physics(self):
        for obj in self.objects:

            if not obj.no_gravity:
                obj.vel[1] += self.G * obj.mass
            # print(obj.vel)

            if np.any(obj.vel):
                # Set any values close to 0, to exactly 0 to avoid bouncing
                obj.vel[abs(obj.vel) < 1e-8] = 0.0

                if obj.collision_box:
                    self.terrain.collides_with(obj.collision_box)
                # TODO: Only add fraction of velocity, based on amount of ms passed since last frame
                obj.move(1)
