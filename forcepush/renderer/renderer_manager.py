import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


class RendererManager(object):
    def __init__(self):
        self.renderers = []
        self.surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("ForcePush")

    def render(self):
        self.surface.fill((0, 0, 0))
        for renderer in self.renderers:
            renderer.render(self.surface)
        pygame.display.update()

    def add_renderer(self, renderer):
        # Todo: double check no duplicate
        self.renderers.append(renderer)

    def remove_renderer(self, renderer):
        self.renderers.remove(renderer)
