import numpy as np
from pygame.rect import Rect

from forcepush import logic
from forcepush.logic.physics import PhysicsCollisionSide

class PhysicsObject(object):
    def __init__(self, pos, size):
        logic.entity_manager.physics_engine.register_object(self)
        self.pos = pos
        self.size = size
        self.vel = np.array([0.0, 0.0])
        self.vel_max = np.array([8.0, 12.0])
        self.vel_min = np.array(-self.vel_max)
        self.acc = np.array([2.0, 6.0])
        self.mass = 1.0
        self.no_gravity = False
        self.collision_box: Rect = Rect(pos[0], pos[1], size[0], size[1])

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
        collision_sides = np.array([False, False, False, False])

        current_pos = np.copy(self.pos)

        collision_sides_current_pos = np.array([
            self.collision_box.centery + (self.collision_box.height / 2.0),
            self.collision_box.centery - (self.collision_box.height / 2.0),
            self.collision_box.centerx + (self.collision_box.width / 2.0),
            self.collision_box.centerx - (self.collision_box.width / 2.0)
        ])

        self.move(1)

        collision_sides_next_pos = np.array([
            self.collision_box.centery + (self.collision_box.height / 2.0),
            self.collision_box.centery - (self.collision_box.height / 2.0),
            self.collision_box.centerx + (self.collision_box.width / 2.0),
            self.collision_box.centerx - (self.collision_box.width / 2.0)
        ])

        for i in self.collision_box.collidelistall(rects):
            collision.append(rects[i])

            rect: Rect = rects[i]

            sides_rect = np.array([
                rect.centery + (rect.height / 2.0),
                rect.centery - (rect.height / 2.0),
                rect.centerx + (rect.width / 2.0),
                rect.centerx - (rect.width / 2.0)
            ])

            if collision_sides_current_pos[PhysicsCollisionSide.TOP] < sides_rect[PhysicsCollisionSide.BOTTOM] < collision_sides_next_pos[PhysicsCollisionSide.TOP]:
                collision_sides[PhysicsCollisionSide.TOP] = True

            if collision_sides_current_pos[PhysicsCollisionSide.BOTTOM] > sides_rect[PhysicsCollisionSide.TOP] > collision_sides_next_pos[PhysicsCollisionSide.BOTTOM]:
                collision_sides[PhysicsCollisionSide.BOTTOM] = True

            if collision_sides_current_pos[PhysicsCollisionSide.LEFT] < sides_rect[PhysicsCollisionSide.RIGHT] < collision_sides_next_pos[PhysicsCollisionSide.LEFT]:
                collision_sides[PhysicsCollisionSide.LEFT] = True

            if collision_sides_current_pos[PhysicsCollisionSide.RIGHT] > sides_rect[PhysicsCollisionSide.LEFT] > collision_sides_next_pos[PhysicsCollisionSide.RIGHT]:
                collision_sides[PhysicsCollisionSide.RIGHT] = True

        self.pos = current_pos

        return collision_sides
