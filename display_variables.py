import pygame
pygame.init()

frame_rate = 60
width, height = 300, 450
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Unnamed Project')
timer = pygame.time.Clock()
font = pygame.font.Font("freesansbold.ttf", 16)