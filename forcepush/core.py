# -*- coding: utf-8 -*-

import pygame

from forcepush.logic.EntityManager import EntityManager
from forcepush.renderer import renderer
pygame.init()

entity_manager = EntityManager()

run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    entity_manager.tick()

    renderer._render()

pygame.quit()