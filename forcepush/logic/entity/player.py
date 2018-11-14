from pygame import Rect
from forcepush.logic.entity.physics_entity import PhysicsEntity


WIDTH = 20
HEIGHT = 40

class Player(PhysicsEntity):
    def __init__(self):
        super().__init__()
        self.physics_object.collision_box = Rect(self.physics_object.pos[0], self.physics_object.pos[1], WIDTH, HEIGHT)

    def move_left(self):
        self.physics_object.vel[0] = self.physics_object.vel[0] - self.physics_object.acc[0]

    def move_right(self):
        self.physics_object.vel[0] = self.physics_object.vel[0] + self.physics_object.acc[0]

    def tick(self):
        pass
