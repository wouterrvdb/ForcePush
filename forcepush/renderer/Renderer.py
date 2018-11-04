import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


class Renderer(object):
    def __init__(self):
        self.renderers = []
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("ForcePush")

    def render(self):
        self.window.fill((0, 0, 0))
        pygame.display.update()
        pass

    def add_renderer(self, renderer):
        # Todo: double check no duplicate
        self.renderers.append(renderer)

    def remove_renderer(self, renderer):
        self.renderers.remove(renderer)
