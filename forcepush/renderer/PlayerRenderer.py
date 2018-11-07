import pygame

class PlayerRenderer(Renderer):
    def __init__(self):
        

    def render(self, surface):
        pygame.draw.rect(surface, (128, 0, 255), (400, 200, 50, 50))