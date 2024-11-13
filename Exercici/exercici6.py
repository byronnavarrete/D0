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


# Bucle de l'aplicació
def main():
    is_looping = True 
    while is_looping: 
        is_looping = app_events()  
        app_run()  
        app_draw() 

        clock.tick(60)  # Limitem la velocitat a 60 fotogrames per segon (FPS)

    # Un cop acabem el bucle, tanquem l'aplicació
    pygame.quit()
    sys.exit()

# Gestionar esdeveniments
def app_events():
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            return False  
    return True  

# Fer càlculs (aquesta funció ara no fa res, però aquí podries afegir càlculs en el futur)
def app_run():
    pass

# Dibuixar
def app_draw():
    
    # Omplim la pantalla de blanc
    screen.fill(WHITE)

    # Dibuixem una graella de fons
    utils.draw_grid(pygame, screen, 50)  # Dibuixem una graella de 50x50 píxels

    # Dibuixem un tauler de dames (8x8) amb colors alternatius
    for row in range(8): 
        for column in range(8): 
            # Assignem el color segons la posició
            color = GRAY if (row + column) % 2 == 0 else BLACK
                
            # Calculem les coordenades x, y per a cada quadrat del tauler
            x = 50 + column * 50  # Espai horitzontal
            y = 50 + row * 50     # Espai vertical
            
            # Dibuixem el quadrat amb el color assignat
            pygame.draw.rect(screen, color, (x, y, 50, 50))

    # Actualitzem la pantalla per mostrar el que hem dibuixat
    pygame.display.update()


if __name__ == "__main__":
    main()