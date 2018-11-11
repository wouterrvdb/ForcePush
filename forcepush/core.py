# -*- coding: utf-8 -*-

import pygame

from forcepush.inputs import input_manager
from forcepush.inputs.handler.quit_handler import QuitHandler
from forcepush.logic import entity_manager, player
from forcepush.logic.terrain import Terrain
from forcepush.renderer import renderer, terrain_renderer, player_renderer, clock, viewport

pygame.init()

terrain = Terrain(500, 200)

terrain_renderer.set_terrain(terrain)
player_renderer.set_player(player)
viewport.set_focus(player)

quit_manager = QuitHandler()
input_manager.register_handler(quit_manager)

while True:

    input_manager.handle_pygame()
    if quit_manager.has_quit():
        break

    entity_manager.tick()

    renderer._render()

    clock.tick(120)

pygame.quit()
