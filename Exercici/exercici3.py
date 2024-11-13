#!/usr/bin/env python3
import os
import pygame
import sys
import utils

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')

# Bucle de l'aplicació
def main():
    is_looping = True

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

# Fer càlculs 
def app_run():
   
    pass

# Dibuixar elements a la pantalla
def app_draw():
    screen.fill(WHITE)  # Omplim la pantalla amb el color blanc

    # Dibuixar la quadrícula (utilitzem una funció auxiliar per a això)
    utils.draw_grid(pygame, screen, 50)

    # Dibuixar cercles amb colors alternatius
    odd = True  # Comencem amb el primer cercle com a vermell
    for radius in range(225, 0, -25):
        color = RED if odd else WHITE  # Alternar colors entre vermell i blanc
        pygame.draw.circle(screen, color, (320, 240), radius)  # Dibuixar el cercle
        odd = not odd  # Invertim el valor de 'odd' per alternar colors

    # Dibuixar cercles amb contorn negre
    for radius in range(25, 250, 25):
        pygame.draw.circle(screen, BLACK, (320, 240), radius, 5)  # Contorn dels cercles

    pygame.display.update() 

if __name__ == "__main__":
    main()
