import pygame
from display_variables import screen, font
from color_pallete import black

def draw_to_button(color, x, width, y, height, text):
    task = pygame.draw.rect(screen, color, [x, y, width, height])
    display_text = text
    shown_text = font.render(str(display_text), True, black)
    text_rect = shown_text.get_rect(center=(x + width/2, y + height/2))
    screen.blit(shown_text, text_rect)
    return task
    