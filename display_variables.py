import pygame
pygame.init()
from color_pallete import misty_dawn
#universal display variables
frame_rate = 60
width, height = 300, 450
#main display:
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption('Unnamed Project')
timer = pygame.time.Clock()
font = pygame.font.Font("freesansbold.ttf", 16)
#welcome pupup:
popup_width = 400
popup_height = 200
popup_surface = pygame.Surface((popup_width, popup_height))
popup_surface.fill((misty_dawn))
#upgrade screen:
upg_screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
show_upgrade_screen = False