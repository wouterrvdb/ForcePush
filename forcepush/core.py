# -*- coding: utf-8 -*-

import pygame

from forcepush.logic.EntityManager import EntityManager
from forcepush.renderer.Renderer import Renderer

pygame.init()

entity_manager = EntityManager()
renderer = Renderer()

# image loading
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))


def background(x,y):
    image = pygame.image.load('catgirls.jpg')
    game_display.blit(image, (x, y))

# text


def text(text, x, y):
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    text_thing = my_font.render(text, False, (255, 0, 0))
    game_display.blit(text_thing, (x, y))


run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # 100 px downwards
    background(0, 100)
    #
    text('Elon approves of waifus', 200, 0)
    pygame.display.update()
    entity_manager.tick()

    # starts to make stuff flicker this render thing
    #renderer.render()

pygame.quit()