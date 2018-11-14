import os

import pygame
import glob as glob
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

    def walk(self):
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
            images = glob.glob(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), 'sprites', 'player_walk', 'p1_walk*.png'))
            images.sort()
            self.converted_images = []
            for x in images:
                im = pygame.image.load(x)
                im = im.convert()
                self.converted_images.append(im)
        except pygame.error:
            print('Cannot load image for player')

        # sprite variables
        self.animation_speed_init = 20
        self.animation_speed = self.animation_speed_init
        self.animation_index = 0
        self.animation_max_index = len(self.converted_images) - 1
        # self.image is a surface
        self.dirty = 1
        self.image = self.converted_images[0]
        self.rect = self.converted_images[0].get_rect()
        self._last_known_position = None

    def update(self):
        self.dirty = 1
        player = self.player_renderer.player

        if player and (not np.array_equal(self._last_known_position, player.physics_object.pos) or not self._last_known_position is None):
            pos = self.player_renderer.viewport.offset + player.physics_object.pos

            self.rect.x = pos[0]
            self.rect.y = pos[1]

            self._last_known_position = np.copy(player.physics_object.pos)

        self.animation_speed -= 1
        if self.animation_speed == 0:
            self.image = self.converted_images[self.animation_index]
            self.animation_speed =self.animation_speed_init
            if self.animation_index == self.animation_max_index:
                self.animation_index = 0
            else:
                self.animation_max_index += 1
