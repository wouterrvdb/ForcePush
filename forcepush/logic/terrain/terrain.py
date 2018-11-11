import numpy as np

class Terrain(object):
    def __init__(self, width : int, height : int):
        self.width = width
        self.height = height

        self.data = np.zeros((width, height))

        for x in range(10):
            for y in range(10):
                self.data[x + 50, y + 50] = 1
                self.data[x + 250, y + 50] = 1

        for x in range(100):
            self.data[2*x + 50, 50] = 1

    def set_pixel(self, x : int, y : int, material):
        self.data[x, y] = material

    def get_pixel(self, x : int, y : int):
        return self.data[x, y]

    def get_terrain_iterator(self):
        return np.nditer(self.data, flags=['multi_index'])