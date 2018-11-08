import os
import pygame

from pygame.sprite import DirtySprite, LayeredDirty
from .Renderer import Renderer

class PlayerRenderer(Renderer):
    def __init__(self, viewport, player):
        super().__init__(viewport)

        self.player = player
        self.sprite = PlayerSprite(self)
        self.layered = LayeredDirty(self.sprite)

    def render(self, surface : pygame.Surface):
        self.layered.clear(self.sprite.image, surface)
        self.layered.update()
        self.layered.draw(surface)

class PlayerSprite(DirtySprite):
    def __init__(self, player_renderer):
        super().__init__()
        self.player_renderer = player_renderer
        try:
            image = pygame.image.load(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'sprites', 'player.png'))
        except pygame.error:
            print('Cannot load image for player')
        # self.image is a surface
        self.image = image.convert()
        self.rect = image.get_rect()
        self.rect.x = self.player_renderer.player.pos_x
        self.rect.y = self.player_renderer.player.pos_y
        self.dirty = 1

    def update(self):
        self.dirty = 1
        if self.player_renderer.player.updated:
            self.rect.x = self.player_renderer.player.pos_x
            self.rect.y = self.player_renderer.player.pos_y
