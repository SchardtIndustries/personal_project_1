import pygame
from display_variables import upg_screen, font
from color_pallete import black

def draw_color_button(x, width, y, height, color, color_cost):
    color_button = pygame.draw.rect(upg_screen, color, [x, y, width, height])
    if color_cost >= 100:
        display_c_value = f"{color_cost:.0f}"
    else:
        display_c_value = f"{color_cost:.2f}"
    color_text = font.render(str(display_c_value), True, black)
    upg_screen.blit(color_text, (x + width/2, y + height/2))
    
    return color_button