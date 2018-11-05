# -*- coding: utf-8 -*-

import pygame

from forcepush.inputs.InputManager import InputManager
from forcepush.inputs.handler.QuitHandler import QuitHandler
from forcepush.logic.EntityManager import EntityManager
from forcepush.renderer import renderer

pygame.init()

input_manager = InputManager()
entity_manager = EntityManager(input_manager)

quit_manager = QuitHandler()
input_manager.register_handler(quit_manager)

while True:
    pygame.time.delay(50)

    input_manager.handle_pygame()
    if quit_manager.has_quit():
        break

    entity_manager.tick()
    renderer._render()

pygame.quit()
