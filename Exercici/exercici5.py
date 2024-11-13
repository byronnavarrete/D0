#!/usr/bin/env python3

import math
import random
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
        is_looping = app_events()  # Gestionem els esdeveniments de l'aplicació
        app_run()  
        app_draw() 
        
        clock.tick(60)  

    # Fora del bucle, tanquem l'aplicació
    pygame.quit()
    sys.exit()

# Gestionar esdeveniments
def app_events():
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:  
            return False 
    return True  

# Fer càlculs (en aquest cas, no hi ha càlculs específics a fer encara)
def app_run():
    global list  

# Dibuixar
def app_draw():
    screen.fill(WHITE)  # Omplim la pantalla de color blanc
    utils.draw_grid(pygame, screen, 50)  # Dibuixem una quadrícula a la pantalla
    
    # Determinarem el centre de la finestra per començar l'espiral des d'allà
    centre_x, centre_y = int(screen.get_width() / 2), int(screen.get_height() / 2)
    
    # Paràmetres de l'espiral rectangular
    x, y = centre_x, centre_y  # Iniciem a les coordenades del centre
    pas = 15  # Longitud inicial de cada segment de l'espiral
    direccio = 0  # 0 = dreta, 1 = amunt, 2 = esquerra, 3 = avall
    
    # Crearem una espiral amb 25 voltes
    for _ in range(25):
        # Calcularem el punt final de la línia segons la direcció
        if direccio == 0:  # Direcció dreta
            final_x, final_y = x + pas, y
        elif direccio == 1:  # Direcció amunt
            final_x, final_y = x, y - pas
        elif direccio == 2:  # Direcció esquerra
            final_x, final_y = x - pas, y
        elif direccio == 3:  # Direcció avall
            final_x, final_y = x, y + pas
        
        # Dibuixem una línia entre el punt inicial (x, y) i el punt final (final_x, final_y)
        pygame.draw.line(screen, RED, (x, y), (final_x, final_y), 4)
        
        # Actualitzem el punt inicial per a la següent línia
        x, y = final_x, final_y
        # Canviem la direcció de l'espiral i augmentem la longitud del següent segment
        direccio = (direccio + 1) % 4  # Canviem la direcció
        pas += 15  # Augmentem la longitud per fer l'espiral més gran

    pygame.display.update()  

if __name__ == "__main__":
    main()