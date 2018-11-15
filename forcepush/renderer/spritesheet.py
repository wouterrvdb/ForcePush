import pygame


class SpriteSheet:

    def __init__(self, filename, cols, rows, count=None):
        self.sheet = pygame.image.load(filename).convert_alpha()

        self.cols = cols  # Number of columns on the sprite
        self.rows = rows  # Number of rows on the sprite

        if count is None:  # Number of actual images on the sprite, can be less than cols * rows
            self.count = cols * rows
        else:
            self.count = count

        self.cell_width = self.sheet.get_rect().width / cols  # Width of one image
        self.cell_height = self.sheet.get_rect().height / rows  # Height of one image

        # Pygame.surface.blit needs (cell_index_x, cell_index_y, cell_width, cell_height)
        self.cells = [(index % self.cols * self.cell_width, index // self.cols * self.cell_height, self.cell_width,
                       self.cell_height) for index in range(self.count)]

        # Handles are to create offset (index 0 is topleft, index 4 is center)
        self.handle = [
            (0, 0), (-self.cell_width / 2, 0), (-self.cell_width, 0), (0, -self.cell_height / 2),
            (-self.cell_width / 2, -self.cell_height / 2), (-self.cell_width, -self.cell_height / 2),
            (0, -self.cell_height), (-self.cell_width / 2, -self.cell_height), (-self.cell_width, -self.cell_height)]

    def update(self, surface, cell_index, x, y, handle=0):
        if surface:
            surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]), self.cells[cell_index])
