import os

import pygame
import numpy as np

from pygame.sprite import DirtySprite, LayeredDirty
from forcepush.logic.entity.player import Player
from .renderer import Renderer

class PlayerRenderer(Renderer):
    def __init__(self, viewport):
        super().__init__(viewport)

        self.sprite = PlayerSprite(self)
        self.layered = LayeredDirty(self.sprite)

        self.player = None
        self.bg = False

    def set_player(self, player: Player):
        self.player = player

        self.sprite.update()

    def render(self, surface : pygame.Surface):
        if not self.bg:
            self.layered.clear(self.sprite.image, surface)
            self.bg = True

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
        self.dirty = 1

        self._last_known_position = None

    def update(self):
        self.dirty = 1
        player = self.player_renderer.player

        if player and (not np.array_equal(self._last_known_position, player.pos) or not self._last_known_position is None):
            pos = self.player_renderer.viewport.offset + player.pos

            self.rect.x = pos[0]
            self.rect.y = pos[1]

            self._last_known_position = np.copy(player.pos)