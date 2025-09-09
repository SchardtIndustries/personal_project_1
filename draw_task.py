import pygame
from display_variables import screen, font
from color_pallete import cabin_beige, black


def draw_task(color, y_coord, value, draw, length, speed, score):
    if draw and length < 200:
        length += speed
    elif length >= 200:
        draw = False
        length = 0
        score += value
    if value >= 100:
        display_value = f"{value:.0f}"  # no decimal points
    else:
        display_value = f"{value:.2f}"
    task = pygame.draw.circle(screen, color, (30, y_coord), 20, 5)
    pygame.draw.rect(screen, color, [70, y_coord - 15, 200, 30])
    pygame.draw.rect(screen, cabin_beige, [75, y_coord - 10, 190, 20])
    pygame.draw.rect(screen, color, [75, y_coord - 15, length, 30])
    val_txt = font.render(str(display_value), True, black)
    screen.blit(val_txt, (16, y_coord - 10))
    return task, draw, length, score