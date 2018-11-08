from forcepush.inputs.handler.player.PlayerMovementHandler import PlayerMovementHandler
from forcepush.logic.entity.Entity import Entity
from forcepush.renderer import renderer, viewport
from forcepush.renderer.PlayerRenderer import PlayerRenderer


class Player(Entity):
    def __init__(self):
        super().__init__()
        self.movement_handler = PlayerMovementHandler(self)
        self.pos_x = 250
        self.pos_y = 250
        self.vel_x = 0
        self.vel_y = 0
        self.vel_x_max = 8
        self.vel_y_max = 12
        self.acc_x = 2
        self.acc_y = 6
        self.moved = False
        self.updated = False
        renderer.add_renderer(PlayerRenderer(viewport, self))

    def move_left(self):
        self.vel_x = max(self.vel_x - self.acc_x, -self.vel_x_max)
        self.moved = True

    def move_right(self):
        self.vel_x = min(self.vel_x + self.acc_x, self.vel_x_max)
        self.moved = True

    def tick(self):
        if not self.moved:
            if self.vel_x != 0:
                self.vel_x = self.vel_x + (1 if self.vel_x < 0 else -1)
            if self.vel_y != 0:
                self.vel_y = self.vel_y + (1 if self.vel_y < 0 else -1)
        self.moved = False
        if self.vel_x == 0 and self.vel_y == 0:
            self.updated = False
        else:
            self.updated = True
            self.pos_x += self.vel_x
            self.pos_y += self.vel_y