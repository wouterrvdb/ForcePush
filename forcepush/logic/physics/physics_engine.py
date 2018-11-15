import numpy as np

from forcepush.logic.physics import PhysicsCollisionSide
from forcepush.logic.terrain import Terrain


class PhysicsEngine(object):
    def __init__(self):
        self.objects = []
        self.terrain = None
        self.G = 0.01

        self._stop_map = {
            PhysicsCollisionSide.TOP: self._stop_top,
            PhysicsCollisionSide.BOTTOM: self._stop_bottom,
            PhysicsCollisionSide.RIGHT: self._stop_right,
            PhysicsCollisionSide.LEFT: self._stop_left
        }

    def register_object(self, obj):
        self.objects.append(obj)

    def set_terrain(self, terrain: Terrain):
        self.terrain = terrain

    def _stop_top(self, obj):
        obj.vel[1] = min(obj.vel[1], 0)

    def _stop_bottom(self, obj):
        obj.vel[1] = max(obj.vel[1], 0)

    def _stop_left(self, obj):
        obj.vel[0] = max(obj.vel[0], 0)

    def _stop_right(self, obj):
        obj.vel[0] = min(obj.vel[0], 0)

    def apply_physics(self):
        for obj in self.objects:

            if not obj.no_gravity:
                obj.vel[1] += self.G * obj.mass
            # print(obj.vel)

            if np.any(obj.vel):
                # Set any values close to 0, to exactly 0 to avoid bouncing
                obj.vel[abs(obj.vel) < 1e-8] = 0.0

                if obj.collision_box:
                    collision_sides = obj.collides_with(self.terrain.get_physics_rects())
                    for i in PhysicsCollisionSide:
                        if(collision_sides[i]):
                            print(i)

                            self._stop_map[i](obj)

                # TODO: Only add fraction of velocity, based on amount of ms passed since last frame
                obj.move(1)
