class Character(object):
    def __init__(self):
        self.height = 50
        self.width = 50
        self.pos_x = 250
        self.pos_y = 600
        self.vel_x = 0
        self.vel_y = 0
        self.vel_x_max = 8
        self.vel_y_max = 12
        self.acc_x = 2
        self.acc_y = 6
        self.moved = False
        self.jumping = False

    def move_left(self):
        self.vel_x = max(self.vel_x - self.acc_x, -self.vel_x_max)
        self.moved = True

    def move_right(self):
        self.vel_x = min(self.vel_x + self.acc_x, self.vel_x_max)
        self.moved = True

    def jump(self):
        self.vel_y = max(self.vel_y - self.acc_y, -self.vel_y_max)
        if not self.jumping:
            self.jumping = True
        self.moved = True

    def duck(self):
        self.moved = True

    def get_position(self):
        if not self.moved:
            if self.vel_x != 0:
                self.vel_x = self.vel_x + (1 if self.vel_x < 0 else -1)
            if self.vel_y != 0:
                self.vel_y = self.vel_y + (1 if self.vel_y < 0 else -1)
        self.moved = False
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
        return self.pos_x, self.pos_y, self.width, self.height
