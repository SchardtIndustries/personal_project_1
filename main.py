import pygame
pygame.init()

width, height = 300, 450
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Unnamed Project')
frame_rate = 60
timer = pygame.time.Clock()
font = pygame.font.Font("freesansbold.ttf", 16)

pale_olive_value = 1
olive_green_value = 2
pine_needle_value = 3
forest_green_value = 4
dark_olive_value = 5
dark_olive_draw = False
pale_olive_draw = False
olive_green_draw = False
pine_needle_draw = False
forest_green_draw = False
dark_olive_length = 0
pale_olive_length = 0
olive_green_length = 0
pine_needle_length = 0
forest_green_length = 0
pale_olive_speed = 5
olive_green_speed = 4
pine_needle_speed = 3
forest_green_speed = 2
dark_olive_speed = 1
score = 0


black = (0, 0, 0)
white = (255, 255, 255)
cabin_beige = (245, 222, 179)
pale_olive = (143, 188, 143)
olive_green = (107, 142, 35)
pine_needle = (85, 107, 47)
forest_green = (34, 139, 34)
dark_olive = (153, 101, 21)        
rustic_brown = (139, 69, 19)
mountain_gray = (112, 128, 144)
misty_dawn = (211, 211, 211)
saddle_brown = (160, 82, 45)
tan = (210, 180, 140)
slate_brown = (72, 61, 139)
saddle_brown = (139, 69, 19)
autumn_orange = (244, 164, 66)

background = cabin_beige

def draw_task(color, y_coord, value, draw, length, speed):
    global score
    if draw and length < 200:
        length += speed
    elif length >= 200:
        draw = False
        length = 0
        score += value
    task = pygame.draw.circle(screen, color, (30, y_coord), 20, 5)
    pygame.draw.rect(screen, color, [70, y_coord - 15, 200, 30])
    pygame.draw.rect(screen, cabin_beige, [75, y_coord - 10, 190, 20])
    pygame.draw.rect(screen, color, [75, y_coord - 15, length, 30])
    val_txt = font.render(str(value), True, black)
    screen.blit(val_txt, (16, y_coord - 10))
    return task, draw, length

running = True
while running:
    timer.tick(frame_rate)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if task1.collidepoint(mouse_pos):
                pale_olive_draw = True
            if task2.collidepoint(mouse_pos):
                olive_green_draw = True
            if task3.collidepoint(mouse_pos):
                pine_needle_draw = True
            if task4.collidepoint(mouse_pos):
                forest_green_draw = True
            if task5.collidepoint(mouse_pos):
                dark_olive_draw = True
    screen.fill(background)
    task1, pale_olive_draw, pale_olive_length = draw_task(pale_olive, 50, pale_olive_value, pale_olive_draw, pale_olive_length, pale_olive_speed)
    task2, olive_green_draw, olive_green_length = draw_task(olive_green, 110, olive_green_value, olive_green_draw, olive_green_length, olive_green_speed)
    task3, pine_needle_draw, pine_needle_length = draw_task(pine_needle, 170, pine_needle_value, pine_needle_draw, pine_needle_length, pine_needle_speed)
    task4, forest_green_draw, forest_green_length = draw_task(forest_green, 230, forest_green_value, forest_green_draw, forest_green_length, forest_green_speed)
    task5, dark_olive_draw, dark_olive_length = draw_task(dark_olive, 290, dark_olive_value, dark_olive_draw, dark_olive_length, dark_olive_speed)
    display_score = font.render("Cash:" + str(round(score, 2)), True, black)
    screen.blit(display_score, (200, 10))

    pygame.display.flip()
pygame.quit
