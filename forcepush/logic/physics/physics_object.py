import numpy as np
from pygame.rect import Rect

from forcepush import logic
from forcepush.logic.physics import PhysicsCollisionSide

class PhysicsObject(object):
    def __init__(self):
        logic.entity_manager.physics_engine.register_object(self)
        self.pos = np.array([250.0, 250.0])
        self.vel = np.array([0.0, 0.0])
        self.vel_max = np.array([8.0, 12.0])
        self.vel_min = np.array(-self.vel_max)
        self.acc = np.array([2.0, 6.0])
        self.mass = 1.0
        self.no_gravity = False
        self.collision_box: Rect = None

    def move(self, amount):
        self.vel = np.maximum(self.vel, self.vel_min)
        self.vel = np.minimum(self.vel, self.vel_max)

        self.pos += self.vel * amount
        if self.collision_box:
            self.update_collision_box()

    def update_collision_box(self):
        self.collision_box[0] = self.pos[0]
        self.collision_box[1] = self.pos[1]

    # TODO: Optimise this (suggestion, calculate each side independently with custom collision check)
    def collides_with(self, rects):
        # print(self.rects, other)
        collision = []
        collision_sides = np.array([ False, False, False, False ])
        collision_sides_pos = [
            self.collision_box.centery + self.collision_box.height / 2.0,
            self.collision_box.centery - self.collision_box.height / 2.0
        ]
        for i in self.collision_box.collidelistall(rects):
            collision.append(rects[i])

            rect: Rect = rects[i]

            if collision_sides_pos[PhysicsCollisionSide.TOP] >= (rect.centery - rect.height / 2.0):
                collision_sides[PhysicsCollisionSide.TOP] = True

            if collision_sides_pos[PhysicsCollisionSide.BOTTOM] <= (rect.centery + rect.height / 2.0):
                collision_sides[PhysicsCollisionSide.BOTTOM] = True

        return collision_sides
