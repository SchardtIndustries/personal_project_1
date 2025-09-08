import pygame
pygame.init()
from color_pallete import *
from game_variables import *
from display_variables import *
from draw_task import draw_task
from draw_button import draw_button

global score
score = 0

running = True
while running:
    timer.tick(frame_rate)
    if pale_olive_owned and not pale_olive_draw:
        pale_olive_draw = True
    if olive_green_owned and not olive_green_draw:
        olive_green_draw = True
    if pine_needle_owned and not pine_needle_draw:
        pine_needle_draw = True
    if forest_green_owned and not forest_green_draw:
        forest_green_draw = True
    if dark_olive_owned and not dark_olive_draw:
        dark_olive_draw = True
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
            if pale_olive_manager_buy and pale_olive_manager_buy.collidepoint(mouse_pos) and score >= pale_olive_manager_cost and not pale_olive_owned:
                score -= pale_olive_manager_cost
                pale_olive_owned = True
            if olive_manager_buy and olive_manager_buy.collidepoint(mouse_pos) and score >= olive_manager_cost and not olive_green_owned:
                score -= olive_manager_cost
                olive_green_owned = True
            if pine_manager_buy and pine_manager_buy.collidepoint(mouse_pos) and score >= pine_manager_cost and not pine_needle_owned:
                score -= pine_manager_cost
                pine_needle_owned = True
            if forest_manager_buy and forest_manager_buy.collidepoint(mouse_pos) and score >= forest_manager_cost and not forest_green_owned:
                score -= forest_manager_cost
                forest_green_owned = True
            if dark_manager_buy and dark_manager_buy.collidepoint(mouse_pos) and score >= dark_manager_cost and not dark_olive_owned:
                score -= dark_manager_cost
                dark_olive_owned = True
            if pale_olive_buy and pale_olive_buy.collidepoint(mouse_pos) and score >= pale_olive_cost:
                pale_olive_value += (pale_olive_value * 1.1)
                score -= pale_olive_cost
                pale_olive_cost = (pale_olive_cost * 1.1)
            if olive_green_buy and olive_green_buy.collidepoint(mouse_pos) and score >= olive_green_cost:
                olive_green_value += (olive_green_value * 1.15)
                score -= olive_green_cost
                olive_green_cost = (olive_green_cost * 1.25)
            if pine_needle_buy and pine_needle_buy.collidepoint(mouse_pos) and score >= pine_needle_cost:
                pine_needle_value += (pine_needle_value * 1.2)
                score -= pine_needle_cost
                pine_needle_cost = (pine_needle_cost * 1.5)
            if forest_green_buy and forest_green_buy.collidepoint(mouse_pos) and score >= forest_green_cost:
                forest_green_value = (forest_green_value * 1.3)
                score -= forest_green_cost
                forest_green_cost = (forest_green_cost * 1.75)
            if dark_olive_buy and dark_olive_buy.collidepoint(mouse_pos) and score >= dark_olive_cost:
                dark_olive_value = (dark_olive_value * 1.4)
                score -= dark_olive_cost
                dark_olive_cost = (dark_olive_cost * 2)


            
    screen.fill(background)

    task1, pale_olive_draw, pale_olive_length, score = draw_task(pale_olive, 50, pale_olive_value, pale_olive_draw, pale_olive_length, pale_olive_speed, score)
    pale_olive_buy, pale_olive_manager_buy = draw_button(pale_olive, 10, pale_olive_cost, pale_olive_owned, pale_olive_manager_cost)
    
    task2, olive_green_draw, olive_green_length, score = draw_task(olive_green, 110, olive_green_value, olive_green_draw, olive_green_length, olive_green_speed, score)
    olive_green_buy, olive_manager_buy = draw_button(olive_green, 70, olive_green_cost, olive_green_owned, olive_manager_cost)

    task3, pine_needle_draw, pine_needle_length, score = draw_task(pine_needle, 170, pine_needle_value, pine_needle_draw, pine_needle_length, pine_needle_speed, score)
    pine_needle_buy, pine_manager_buy = draw_button(pine_needle, 130, pine_needle_cost, pine_needle_owned, pine_manager_cost)

    task4, forest_green_draw, forest_green_length, score = draw_task(forest_green, 230, forest_green_value, forest_green_draw, forest_green_length, forest_green_speed, score)
    forest_green_buy, forest_manager_buy = draw_button(forest_green, 190, forest_green_cost, forest_green_owned, forest_manager_cost)   

    task5, dark_olive_draw, dark_olive_length, score = draw_task(dark_olive, 290, dark_olive_value, dark_olive_draw, dark_olive_length, dark_olive_speed, score)
    dark_olive_buy, dark_manager_buy = draw_button(dark_olive, 250, dark_olive_cost, dark_olive_owned, dark_manager_cost)   

    display_score = font.render("Cash:" + str(round(score, 2)), True, black)
    screen.blit(display_score, (200, 10))


    buymore = font.render("Buy More", True, black)
    screen.blit(buymore, (10, 330))
    hiremanager = font.render("Hire Manager", True, black)
    screen.blit(hiremanager, (10, 385))
    pygame.display.flip()
pygame.quit
