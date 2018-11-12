import numpy as np
from pygame.rect import Rect


class Terrain(object):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.TILE_SIZE = 50

        self.data = np.zeros((width, height))
        self.rects = []

        for x in range(10):
            for y in range(10):
                self.data[x + self.TILE_SIZE, y + self.TILE_SIZE] = 1
                self.data[x + 5 * self.TILE_SIZE, y + self.TILE_SIZE] = 1

        for x in range(100):
            self.data[2 * x + self.TILE_SIZE, self.TILE_SIZE] = 1

    def set_pixel(self, x: int, y: int, material):
        self.data[x, y] = material

    def get_pixel(self, x: int, y: int):
        return self.data[x, y]

    def get_terrain_iterator(self):
        return np.nditer(self.data, flags=['multi_index'])

    def update_collision(self):
        self.rects = []
        it = self.terrain.get_terrain_iterator()

        while not it.finished:
            x, y = it.multi_index
            if it[0] != 0:
                self.rects.append(Rect(x, y, self.TILE_SIZE, self.TILE_SIZE))

    # TODO: Optimise this
    def collides_with(self, other):
        other.collidelist(self.rects)
