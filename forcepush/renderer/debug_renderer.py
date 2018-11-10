import pygame

from .Renderer import Renderer
from .Viewport import Viewport

pygame.init()

class DebugRenderer(Renderer):

    def __init__(self, viewport : Viewport, clock: pygame.time.Clock):
        super().__init__(viewport)

        self.font = pygame.font.SysFont("Arial", 12)
        self.clock = clock

    def render(self, surface : pygame.Surface):
        fps = self.font.render(str(int(self.clock.get_fps())), True, pygame.Color('white'))
        surface.blit(fps, (50, self.viewport.height - 50))