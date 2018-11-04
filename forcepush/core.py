# -*- coding: utf-8 -*-

import pygame

from forcepush.logic.EntityManager import EntityManager
from forcepush.renderer.Renderer import Renderer

pygame.init()

entity_manager = EntityManager()
renderer = Renderer()

run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    entity_manager.tick()

    renderer.render()

pygame.quit()