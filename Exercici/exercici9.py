#!/usr/bin/env python3

import math
import pygame
import sys
import utils

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')

# Definir el taulell
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (127, 184, 68)
YELLOW = (240, 187, 64)
ORANGE = (226, 137, 50)
RED = (202, 73, 65)
PURPLE = (135, 65, 152)
BLUE  = (75, 154, 217)

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
dades = [ 
    {'nom': 'Pelut', 'any': 2018, 'pes': 6.5, 'especie': 'Gos'},
    {'nom': 'Pelat', 'any': 2020, 'pes': 5.0, 'especie': 'Gos'},
    {'nom': 'Mia', 'any': 2022, 'pes': 3.0, 'especie': 'Gat'},
    {'nom': 'Nemo', 'any': 2003, 'pes': 0.1, 'especie': 'Peix'},
    {'nom': 'Mickey', 'any': 1928, 'pes': 0.5, 'especie': 'Ratolí'},
    {'nom': 'Donald', 'any': 1934, 'pes': 0.5, 'especie': 'Ànec'}
]

# Inicialitzar pygame
pygame.init()

# Configuració de la finestra
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Taula d'Informació")
clock = pygame.time.Clock()

# Carregar fonts
font_name = pygame.font.SysFont("Arial", 18)
font_details = pygame.font.SysFont("Arial", 16)


# Dibuixar
def app_draw():
    screen.fill(WHITE)

    # Posició inicial de la taula
    x_offset = 5
    y_offset = 20
    cell_height = 30  # Alçada de cada fila

    # Titols de les columnes
    titols = ['Nom', 'Any', 'Pes', 'Espècie']
    titols_color = BLUE

    # Dibuixar línies horitzontals per cada fila
    for i, titol in enumerate(titols):
        text = font_name.render(titol, True, titols_color)
        screen.blit(text, (x_offset + i * 140, y_offset))
    
    y_offset += cell_height

    # Dibuixar les files de dades
    for dada in dades:
        # Dibuixar cada fila
        for i, key in enumerate(dada):
            text = font_details.render(str(dada[key]), True, BLACK)
            screen.blit(text, (x_offset + i * 140, y_offset))

        y_offset += cell_height  # Incrementar la posició vertical per la següent fila
 # Actualitzar el dibuix a la finestra
    pygame.display.update()


if __name__ == "__main__":
    main()