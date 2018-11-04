# -*- coding: utf-8 -*-

import pygame

from forcepush.Character import Character

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

pygame.init()

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ForcePush")

character = Character()

run = True
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        character.jump()
    if keys[pygame.K_a]:
        character.move_left()
    if keys[pygame.K_s]:
        character.duck()
    if keys[pygame.K_d]:
        character.move_right()

    window.fill((0, 0, 0))
    pygame.draw.rect(window, (128, 0, 255), character.get_position())
    pygame.display.update()

pygame.quit()