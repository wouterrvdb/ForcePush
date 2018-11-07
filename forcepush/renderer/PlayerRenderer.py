import pygame

from .Renderer import Renderer


class PlayerRenderer(Renderer):
    def __init__(self, viewport):
        super().__init__(viewport)

    def render(self, surface : pygame.Surface):
        pygame.draw.rect(surface, (128, 0, 255), (400, 200, 50, 50))
