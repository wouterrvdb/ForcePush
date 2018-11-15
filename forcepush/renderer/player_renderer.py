import pygame

from forcepush.logic.entity.player import Player
from .renderer import Renderer

from forcepush.renderer.spritesheet import SpriteSheet


class PlayerRenderer(Renderer):
    def __init__(self, viewport):
        super().__init__(viewport)

        sprite_images = 11

        self.animation_index = 0
        self.animation_index_max = sprite_images -1
        self.surface = None

        self.sprite = SpriteSheet('./forcepush/renderer/sprites/player.png', 3, 4, count=sprite_images)

        self.player = None
        self.bg = False

    def set_player(self, player: Player):
        self.player = player
        self._update()

    def walk(self):
        self._update()

    def render(self, surface: pygame.Surface):
        self.surface = surface
        self._update()
        if not self.bg:
            self.bg = True

    def _update(self):
        self.animation_index = (self.animation_index + 1) % self.animation_index_max
        self.sprite.update(self.surface, self.animation_index, 420, 420)  # TODO update location of alien dude "0, 0)"
