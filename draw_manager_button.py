import pygame
from color_pallete import black
from display_variables import font, manager_screen

def draw_manager_button(color, x, width, y, height, color_owned, owned, manager_cost):
    if not owned and  color_owned: 
        manager_button = pygame.draw.rect(manager_screen, color, [x, y, width, height])
        if manager_cost >= 100:
            display_value = f"{manager_cost:.0f}"
        else:
            display_value = f"{manager_cost:.2f}"
        manager_text = font.render(str(display_value), True, black)
        manager_screen.blit(manager_text, (x + width/2, y + height/2))
    else:
        manager_button = pygame.draw.rect(manager_screen, color, [x, y, width, height])
    return manager_button
