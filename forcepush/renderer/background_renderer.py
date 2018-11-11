import pygame

from .renderer import Renderer
from .viewport import Viewport


class BackgroundRenderer(Renderer):

    def __init__(self, viewport : Viewport):
        super().__init__(viewport)

        self.background_color = pygame.Color(135, 206, 235, 255)

        self.surface = pygame.Surface((viewport.width, viewport.height), pygame.HWSURFACE, 32)
        self.surface.fill(self.background_color)

    def render(self, surface : pygame.Surface):
        surface.blit(self.surface, (0, 0))