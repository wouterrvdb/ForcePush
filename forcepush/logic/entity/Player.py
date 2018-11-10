import numpy as np

from forcepush.inputs.handler.player.PlayerMovementHandler import PlayerMovementHandler
from forcepush.logic.entity.Entity import Entity

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.movement_handler = PlayerMovementHandler(self)
        self.pos = np.array([250, 250])
        self.vel = np.array([0, 0])
        self.vel_max = np.array([8, 12])
        self.acc = np.array([2, 6])
        self.moved = False

    def move_left(self):
        self.vel[0] = max(self.vel[0] - self.acc[0], -self.vel_max[0])
        self.moved = True

    def move_right(self):
        self.vel[0] = min(self.vel[0] + self.acc[0], self.vel_max[0])
        self.moved = True

    def tick(self):
        if not self.moved:
            if self.vel[0] != 0:
                self.vel[0] = self.vel[0] + (1 if self.vel[0] < 0 else -1)
            if self.vel[1] != 0:
                self.vel[1] = self.vel[1] + (1 if self.vel[1] < 0 else -1)
        self.moved = False

        if np.any(self.vel):
            self.pos += self.vel
