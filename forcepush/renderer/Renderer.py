import pygame

from .Viewport import Viewport

class Renderer(object):
    def __init__(self, viewport: Viewport):
        self.renderers = []
        self.window = pygame.display.set_mode((viewport.width, viewport.height), pygame.HWSURFACE, 32)
        self.window.fill((0, 0, 0))

        self.viewport = viewport

        pygame.display.set_caption("ForcePush")

    def render(self, surface : pygame.Surface):

        for renderer in self.renderers:
            renderer.render(surface)

        pygame.display.update()

    def _render(self):
        self.render(self.window)

    def add_renderer(self, renderer):
        # Todo: double check no duplicate
        self.renderers.append(renderer)

    def remove_renderer(self, renderer):
        self.renderers.remove(renderer)
