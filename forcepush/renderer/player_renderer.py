import pygame

from forcepush.logic.entity.player import Player
from .renderer import Renderer

from forcepush.renderer.spritesheet import SpriteSheet


class PlayerRenderer(Renderer):
    def __init__(self, viewport):
        super().__init__(viewport)

        self.surface = None
        self.sprite_images = 11

        self.sprite = SpriteSheet('./forcepush/renderer/sprites/player.png', 3, 4, count=self.sprite_images)

        self.animation_index = 0  # Index of current animation
        self.animation_tick_index = 0  # Index of current animation tick
        self.animation_tick_speed = 5  # New animation every X ticks

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
        if self.animation_tick_index == 0:
            self.animation_index = (self.animation_index + 1) % (self.sprite_images - 1)
        self.animation_tick_index = (self.animation_tick_index + 1) % self.animation_tick_speed
        self.sprite.update(self.surface, self.animation_index, 420, 420)  # TODO update location of alien "420, 420)"
