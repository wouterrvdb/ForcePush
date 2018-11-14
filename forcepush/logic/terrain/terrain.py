import numpy as np
from pygame.rect import Rect


class Terrain(object):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.data = np.zeros((width, height))
        self.rects = []

        for x in range(10):
            for y in range(10):
                self.data[x + 50, y + 150] = 1
                self.data[x + 250, y + 150] = 1

        for x in range(100):
            self.data[2 * x + 50, 159] = 1
        self.update_collision()

    def set_pixel(self, x: int, y: int, material):
        self.data[x, y] = material

    def get_pixel(self, x: int, y: int):
        return self.data[x, y]

    def get_terrain_iterator(self):
        return np.nditer(self.data, flags=['multi_index'])

    def update_collision(self):
        self.rects = []
        it = self.get_terrain_iterator()

        while not it.finished:
            x, y = it.multi_index
            if it[0] != 0:

                self.rects.append(Rect(x << 2, y << 2, 4, 4))

            it.iternext()

    # TODO: Optimise this (suggestion, calculate each side independently with custom collision check)
    def collides_with(self, other):
        # print(self.rects, other)
        collision = {}
        for i in other.collidelistall(self.rects):
            print(other, self.rects[i])
        return collision
