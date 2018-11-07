# -*- coding: utf-8 -*-

import pygame

from forcepush.inputs.InputManager import InputManager
from forcepush.inputs.handler.QuitHandler import QuitHandler
from forcepush.logic.EntityManager import EntityManager
from forcepush.logic.terrain import Terrain
from forcepush.renderer import renderer, terrain_renderer, clock

pygame.init()

input_manager = InputManager()
entity_manager = EntityManager(input_manager)
terrain = Terrain(500, 200)

terrain_renderer.setTerrain(terrain)

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