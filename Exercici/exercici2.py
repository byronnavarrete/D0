#!/usr/bin/env python3

import os
import sys
import pygame
import utils

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
PINK = (255, 105, 180)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Inicialització de Pygame
pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')

# Comprovació de les rutes de les imatges
def carregar_imatges():
    # Definir les rutes de les imatges
    path_shinnosuke = os.path.join(os.path.dirname(__file__), "shinnosuke.png")
    path_shiro = os.path.join(os.path.dirname(__file__), "shiro.png")
    
    # Comprovar si les imatges existeixen abans de carregar-les
    if not os.path.exists(path_shinnosuke) or not os.path.exists(path_shiro):
        print("Error: una o més imatges no es poden trobar.")
        sys.exit(-1)

    # Carregar les imatges
    im_shinnosuke = pygame.image.load(path_shinnosuke).convert_alpha()
    im_shiro = pygame.image.load(path_shiro).convert_alpha()
    
    # Escalar les imatges a les mides desitjades
    im_shinnosuke = utils.scale_image(pygame, im_shinnosuke, target_width=100)
    im_shiro = utils.scale_image(pygame, im_shiro, target_width=75)
    
    return im_shinnosuke, im_shiro

# Bucle de l'aplicació
def main():
    global im_shinnosuke, im_shiro
    is_looping = True

    # Càrrega d'imatges
    im_shinnosuke, im_shiro = carregar_imatges()

    while is_looping:
        # Gestió d'esdeveniments
        is_looping = app_events()

        # Actualitzar l'aplicació
        app_run()

        # Dibuixar els elements a la pantalla
        app_draw()

        # Limitar a 60 FPS
        clock.tick(60)

    # Fora del bucle, tancar l'aplicació
    pygame.quit()
    sys.exit()

# Gestionar esdeveniments
def app_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Botó per tancar la finestra
            return False
    return True

# Fer càlculs o actualitzacions de l'aplicació
def app_run():
    pass  # Aquí es poden fer càlculs o accions en el futur

# Dibuixar elements a la pantalla
def app_draw():
    global im_shinnosuke, im_shiro

    screen.fill(WHITE)
    
    # Dibuixar la quadrícula (si és necessària)
    utils.draw_grid(pygame, screen, 50)
    
    # Dibuixar les imatges
    screen.blit(im_shinnosuke, (325, 160))
    screen.blit(im_shiro, (225, 205))

    # Actualitzar la pantalla
    pygame.display.update()


if __name__ == "__main__":
    main()
