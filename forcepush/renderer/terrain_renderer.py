import pygame

from .renderer import Viewport
from .renderer import Renderer

from forcepush.logic.terrain import Terrain

class TerrainRenderer(Renderer):

    def __init__(self, viewport: Viewport):
        super().__init__(viewport)

        self.terrain = None

        self.pixel = pygame.Surface((1 << 2, 1 << 2), pygame.HWSURFACE, 32)
        self.pixel.fill(pygame.Color(0, 255, 0, 255))

        self.tmp_surface = pygame.Surface((viewport.width, viewport.height), pygame.HWSURFACE, 32).convert_alpha()
        self.tmp_surface.fill(pygame.Color(0, 0, 0, 0))

        self.updated = False

    def set_terrain(self, terrain: Terrain):
        self.terrain = terrain
        self.updated = True

    def render(self, surface : pygame.Surface):
        if not self.terrain:
            return

        if self.updated:
            it = self.terrain.get_terrain_iterator()

            while not it.finished:
                x, y = it.multi_index

                if it[0] != 0:
                    self.tmp_surface.blit(self.pixel, (x << 2, self.viewport.height - (y << 2)))

                it.iternext()
            self.updated = False

        surface.blit(self.tmp_surface, tuple(self.viewport.offset))