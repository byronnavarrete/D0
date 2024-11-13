#!/usr/bin/env python3

import math
import pygame
import sys
import utils

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (127, 184, 68)
YELLOW = (240, 187, 64)
ORANGE = (226, 137, 50)
RED = (202, 73, 65)
PURPLE = (135, 65, 152)
BLUE  = (75, 154, 217)
colors = [GREEN, YELLOW, ORANGE, RED, PURPLE, BLUE]

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')

# Bucle de l'aplicació
def main():
    is_looping = True

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
 # Pintar el fons de blanc
    screen.fill(WHITE)

    # Dibuixar la graella
    utils.draw_grid(pygame, screen, 50)

    # Dibuixar quadres amb els colors de la llista
    for q in range(0, len(colors)):
        size = 50 
        x = 50 + (q * 100) 
        pygame.draw.rect(screen, colors[q], (x, 50, size, size))  # Dibuixar el rectangle

        radius = 25  # Radi per al cercle
        x = 50 + (q * 100) + radius  
        pygame.draw.circle(screen, colors[q], (x, 150 + radius), radius, 2) 

    # Dibuixar polígons grisos (triangles i pentàgons)
    grey = 0 
    for q in range(0, 10):  # Recorrem 10 iteracions per a polígons grisos
        radius = 25  # Radi del polígon
        x = 50 + (q * 100) + radius 
        color = (grey, grey, grey)  
        draw_polygon(screen, color, (x, 250 + radius), radius, 3)  # Dibuixem un triangle
        draw_polygon(screen, color, (x, 350 + radius), radius, 5)  # Dibuixem un pentàgon
        grey = grey + 25  # Apliquem un augment de 25 per cada iteració

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

# Funció per dibuixar polígons (triangle, pentàgon, etc.)
def draw_polygon(screen, color, center, radius, num_vertices, angle_offset=(math.pi / 3)):
    points = [
        (
            center[0] + radius * math.cos(angle_offset + i * 2 * math.pi / num_vertices),
            center[1] + radius * math.sin(angle_offset + i * 2 * math.pi / num_vertices)
        )
        for i in range(num_vertices)
    ]
    pygame.draw.polygon(screen, color, points)  # Dibuixem el polígon

if __name__ == "__main__":
    main()