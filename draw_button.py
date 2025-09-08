import pygame
from display_variables import screen, font
from color_pallete import black, cabin_beige

def draw_button(color, x_coord, color_cost, owned, manager_cost):
    color_button = pygame.draw.rect(screen, color, [x_coord, 350, 50, 30])
    color_text = font.render(str(round(color_cost,2)), True, black)
    screen.blit(color_text, (x_coord + 6, 350))
    manager_button = None
    if not owned:
        manager_button = pygame.draw.rect(screen, color, [x_coord, 405, 50, 30])
        manager_text = font.render(str(round(manager_cost,2)), True, black)
        screen.blit(manager_text, (x_coord + 6, 410))
    else:
        pygame.draw.rect(screen, cabin_beige, [x_coord, 405, 50, 30]) 

    return color_button, manager_button