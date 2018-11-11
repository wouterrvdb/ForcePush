from forcepush.logic.entity.physics_entity import PhysicsEntity


class Player(PhysicsEntity):
    def __init__(self):
        super().__init__()

    def move_left(self):
        self.physics_object.vel[0] = max(self.physics_object.vel[0] - self.physics_object.acc[0], -self.physics_object.vel_max[0])
        self.physics_object.moved = True

    def move_right(self):
        self.physics_object.vel[0] = min(self.physics_object.vel[0] + self.physics_object.acc[0], self.physics_object.vel_max[0])
        self.physics_object.moved = True

    def tick(self):
        pass
