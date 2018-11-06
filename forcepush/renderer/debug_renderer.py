import pygame

from .Renderer import Renderer
from .Viewport import Viewport

pygame.init()

class DebugRenderer(Renderer):

    def __init__(self, viewport : Viewport, clock: pygame.time.Clock):
        super().__init__(viewport)

        self.font = pygame.font.SysFont("Arial", 12)
        self.clock = clock

        self.bg = None

    def render(self, surface : pygame.Surface):
        if not self.bg:
            self.bg = pygame.Surface((24,12), pygame.HWSURFACE)
            self.bg.blit(surface, (0, 0), (50, self.viewport.height - 50, 74, self.viewport.height - 38))

        fps = self.font.render(str(int(self.clock.get_fps())), True, pygame.Color('white'))
        surface.blit(self.bg, (50, self.viewport.height - 50))
        surface.blit(fps, (50, self.viewport.height - 50))