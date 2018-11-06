# -*- coding: utf-8 -*-

import pygame

from forcepush.logic.EntityManager import EntityManager
from forcepush.logic.terrain import Terrain
from forcepush.renderer import renderer, terrain_renderer, clock

pygame.init()

entity_manager = EntityManager()
terrain = Terrain(500, 200)

terrain_renderer.setTerrain(terrain)

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    entity_manager.tick()

    renderer._render()

    clock.tick(120)

pygame.quit()