#!/usr/bin/env python3

import math
import os
import pygame
import sys
import utils

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
PINK = (255, 105, 180)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')


path_shinnosuke = os.path.join(os.path.dirname(__file__), "/shinnosuke.png")
im_shinnosuke = pygame.image.load(path_shinnosuke).convert_alpha()
im_shinnosuke = utils.scale_image(pygame, im_shinnosuke, target_width=100)

path_shiro = os.path.join(os.path.dirname(__file__), "/shiro.png")
im_shiro = pygame.image.load(path_shiro).convert_alpha()
im_shiro = utils.scale_image(pygame, im_shiro, target_width=75)

 while is_looping:
    is_looping = app_events()
    app_run()
   app_draw()

    clock.tick(60) # Limitar a 60 FPS

    # Fora del bucle, tancar l'aplicació
    pygame.quit()
    sys.exit()

# Gestionar events
def app_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
    return True

# Fer càlculs
def app_run():
    pass

# Dibuixar
def app_draw():
    global im_shinnosuke

    screen.fill(WHITE)
    utils.draw_grid(pygame, screen, 50)
    
    screen.blit(im_shinnosuke, (325, 160))
    screen.blit(im_shiro, (225, 205))

    pygame.display.update()

if __name__ == "__main__":
    main()