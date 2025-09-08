import pygame
pygame.init()

width, height = 300, 450
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Unnamed Project')
frame_rate = 60
timer = pygame.time.Clock()
font = pygame.font.Font("freesansbold.ttf", 16)

pale_olive_value = 1
pale_olive_cost = 1
pale_olive_speed = 5
pale_olive_manager_cost = 100
pale_olive_owned = False
pale_olive_draw = False
pale_olive_length = 0

olive_green_value = 2
olive_green_cost = 2
olive_green_speed = 4
olive_manager_cost = 200
olive_green_owned = False
olive_green_draw = False
olive_green_length = 0

pine_needle_value = 3
pine_needle_cost = 3
pine_needle_speed = 3
pine_manager_cost = 300
pine_needle_owned = False
pine_needle_draw = False
pine_needle_length = 0

forest_green_value = 4
forest_green_cost = 4
forest_green_speed = 2
forest_manager_cost = 400
forest_green_owned = False
forest_green_draw = False
forest_green_length = 0

dark_olive_value = 5
dark_olive_cost = 5
dark_olive_speed = 1
dark_manager_cost = 500
dark_olive_owned = False
dark_olive_draw = False
dark_olive_length = 0





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

def draw_button(color, x_coord, color_cost, owned, manager_cost):
    color_button = pygame.draw.rect(screen, color, [x_coord, 350, 50, 30])
    color_text = font.render(str(round(color_cost,2)), True, black)
    screen.blit(color_text, (x_coord + 6, 350))
    if not owned:
        manager_button = pygame.draw.rect(screen, color, [x_coord, 405, 50, 30])
        manager_text = font.render(str(round(manager_cost,2)), True, black)
        screen.blit(manager_text, (x_coord + 6, 410))
    return color_button, manager_button


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
    pale_olive_buy, pale_olive_manager_buy = draw_button(pale_olive, 10, pale_olive_cost, pale_olive_owned, pale_olive_manager_cost)
    
    task2, olive_green_draw, olive_green_length = draw_task(olive_green, 110, olive_green_value, olive_green_draw, olive_green_length, olive_green_speed)
    olive_green_buy, olive_manager_buy = draw_button(olive_green, 70, olive_green_cost, olive_green_owned, olive_manager_cost)

    task3, pine_needle_draw, pine_needle_length = draw_task(pine_needle, 170, pine_needle_value, pine_needle_draw, pine_needle_length, pine_needle_speed)
    pine_needle_buy, pine_manager_buy = draw_button(pine_needle, 130, pine_needle_cost, pine_needle_owned, pine_manager_cost)

    task4, forest_green_draw, forest_green_length = draw_task(forest_green, 230, forest_green_value, forest_green_draw, forest_green_length, forest_green_speed)
    forest_green_buy, forest_manager_buy = draw_button(forest_green, 190, forest_green_cost, forest_green_owned, forest_manager_cost)   

    task5, dark_olive_draw, dark_olive_length = draw_task(dark_olive, 290, dark_olive_value, dark_olive_draw, dark_olive_length, dark_olive_speed)
    dark_olive_buy, dark_manager_buy = draw_button(dark_olive, 250, dark_olive_cost, dark_olive_owned, dark_manager_cost)   

    display_score = font.render("Cash:" + str(round(score, 2)), True, black)
    screen.blit(display_score, (200, 10))


    buymore = font.render("Buy More", True, black)
    screen.blit(buymore, (10, 330))
    hiremanager = font.render("Hire Manager", True, black)
    screen.blit(hiremanager, (10, 385))
    pygame.display.flip()
pygame.quit
