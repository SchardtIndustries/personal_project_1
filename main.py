import pygame
pygame.init()
from color_pallete import *
from game_variables import *
from display_variables import *
from draw_task import draw_task
from draw_color_button import draw_color_button
import os
import json
import datetime
from menu_buttons import draw_to_button

save_data = {}


if os.path.exists("savegame.json"):
    with open("savegame.json", "r") as f:
        try:
            save_data = json.load(f)
            score = save_data.get("score", 0)
            pale_olive_owned = save_data.get("pale_olive_owned", False)
            olive_green_owned = save_data.get("olive_green_owned", False)
            pine_needle_owned = save_data.get("pine_needle_owned", False)
            forest_green_owned = save_data.get("forest_green_owned", False)
            dark_olive_owned = save_data.get("dark_olive_owned", False)
            pale_olive_cost = save_data.get("pale_olive_cost", pale_olive_cost)
            pale_olive_value = save_data.get("pale_olive_value", pale_olive_value)
            olive_green_cost = save_data.get("olive_green_cost", olive_green_cost)
            olive_green_value = save_data.get("olive_green_value", olive_green_value)
            pine_needle_cost = save_data.get("pine_needle_cost", pine_needle_cost)
            pine_needle_value = save_data.get("pine_needle_value", pine_needle_value)
            forest_green_cost = save_data.get("forest_green_cost", forest_green_cost)
            forest_green_value = save_data.get("forest_green_value", forest_green_value)
            dark_olive_cost = save_data.get("dark_olive_cost", dark_olive_cost)
            dark_olive_value = save_data.get("dark_olive_value", dark_olive_value)
            last_save = save_data.get("last_save", datetime.datetime.now().isoformat())
        except:
            score = 0
            pale_olive_owned = olive_green_owned = pine_needle_owned = forest_green_owned = dark_olive_owned = False
else:
    score = 0
    pale_olive_owned = save_data.get("pale_olive_owned", False)
    olive_green_owned = save_data.get("olive_green_owned", False)
    pine_needle_owned = save_data.get("pine_needle_owned", False)
    forest_green_owned = save_data.get("forest_green_owned", False)
    dark_olive_owned = save_data.get("dark_olive_owned", False)


running = True
while running:
    timer.tick(frame_rate)


    if not show_task_screen and not show_manager_screen and not show_upgrade_screen and not show_ach_screen and not show_store_screen:
        screen.fill(background)
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
            if event.type == pygame.VIDEORESIZE:
                width, height = event.size
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
                if task6.collidepoint(mouse_pos):
                    saddle_draw = True
                if task7.collidepoint(mouse_pos):
                    rustic_draw = True
                if task8.collidepoint(mouse_pos):
                    show_upgrade_screen = True
                if task9.collidepoint(mouse_pos):
                    show_manager_screen = True
                if task10.collidepoint(mouse_pos):
                    show_task_screen = True
                if task11.collidepoint(mouse_pos):
                    show_ach_screen = True
                if task12.collidepoint(mouse_pos):
                    show_store_screen = True    
        task1, pale_olive_draw, pale_olive_length, score = draw_task(pale_olive, 50, pale_olive_value, pale_olive_draw, pale_olive_length, pale_olive_speed, score)
        task2, olive_green_draw, olive_green_length, score = draw_task(olive_green, 95, olive_green_value, olive_green_draw, olive_green_length, olive_green_speed, score)
        task3, pine_needle_draw, pine_needle_length, score = draw_task(pine_needle, 140, pine_needle_value, pine_needle_draw, pine_needle_length, pine_needle_speed, score)
        task4, forest_green_draw, forest_green_length, score = draw_task(forest_green, 185, forest_green_value, forest_green_draw, forest_green_length, forest_green_speed, score)
        task5, dark_olive_draw, dark_olive_length, score = draw_task(dark_olive, 230, dark_olive_value, dark_olive_draw, dark_olive_length, dark_olive_speed, score)
        task6, saddle_draw, saddle_length, score = draw_task(saddle_brown, 275, saddle_value, saddle_draw, saddle_length, saddle_speed, score)
        task7, rustic_draw, rustic_length, score = draw_task(rustic_brown, 320, rustic_value, rustic_draw, rustic_length, rustic_speed, score)
        task8 = draw_to_button(mountain_gray, 5, 90, 410, 30, "Upgrades")
        task9 = draw_to_button(mountain_gray, 105, 90, 410, 30, "Managers")
        task10 = draw_to_button(mountain_gray, 205, 90, 410, 30, "Tasks")
        task11 = draw_to_button(mountain_gray, 10, 135, 370, 30, "Trophies")
        task12 = draw_to_button(mountain_gray, 155, 135, 370, 30, "Store")


    if show_task_screen and not show_manager_screen and not show_upgrade_screen and not show_ach_screen and not show_store_screen:
        task_screen.fill(misty_dawn)
        if score >= 100:
            display_score_value = f"{score:.0f}"
        else:
            display_score_value = f"{score:.2f}"
            text_surface = font.render(f"Money: ${display_score_value}", True, black)
            task_screen.blit(text_surface, (10, 10))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.VIDEORESIZE:
                width, height = event.size
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if task8.collidepoint(mouse_pos):
                    show_upgrade_screen = True
                    show_task_screen = False
                if task9.collidepoint(mouse_pos):
                    show_manager_screen = True
                    show_task_screen = False
                if task10.collidepoint(mouse_pos):
                    show_task_screen = False
                if task11.collidepoint(mouse_pos):
                    show_ach_screen = True
                    show_task_screen = False
                if task12.collidepoint(mouse_pos):
                    show_store_screen = True
                    show_task_screen = False    
        task8 = draw_to_button(mountain_gray, 5, 90, 410, 30, "Upgrades")
        task9 = draw_to_button(mountain_gray, 105, 90, 410, 30, "Managers")
        task10 = draw_to_button(mountain_gray, 205, 90, 410, 30, "Home")
        task11 = draw_to_button(mountain_gray, 10, 135, 370, 30, "Trophies")
        task12 = draw_to_button(mountain_gray, 155, 135, 370, 30, "Store")    


    if not show_task_screen and show_manager_screen and not show_upgrade_screen and not show_ach_screen and not show_store_screen:
        manager_screen.fill(misty_dawn)
        if score >= 100:
            display_score_value = f"{score:.0f}"
        else:
            display_score_value = f"{score:.2f}"
            text_surface = font.render(f"Money: ${display_score_value}", True, black)
            manager_screen.blit(text_surface, (10, 10))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.VIDEORESIZE:
                width, height = event.size
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if task8.collidepoint(mouse_pos):
                    show_upgrade_screen = True
                    show_manager_screen = False
                if task9.collidepoint(mouse_pos):
                    show_manager_screen = False
                if task10.collidepoint(mouse_pos):
                    show_manager_screen = False
                if task11.collidepoint(mouse_pos):
                    show_ach_screen = True
                    show_manager_screen = False
                if task12.collidepoint(mouse_pos):
                    show_store_screen = True
                    show_manager_screen = False    
        task8 = draw_to_button(mountain_gray, 5, 90, 410, 30, "Upgrades")
        task9 = draw_to_button(mountain_gray, 105, 90, 410, 30, "Home")
        task10 = draw_to_button(mountain_gray, 205, 90, 410, 30, "Tasks")
        task11 = draw_to_button(mountain_gray, 10, 135, 370, 30, "Trophies")
        task12 = draw_to_button(mountain_gray, 155, 135, 370, 30, "Store")


    if not show_task_screen and not show_manager_screen and show_upgrade_screen and not show_ach_screen and not show_store_screen:
        manager_screen.fill(misty_dawn)
        if score >= 100:
            display_score_value = f"{score:.0f}"
        else:
            display_score_value = f"{score:.2f}"
            text_surface = font.render(f"Money: ${display_score_value}", True, black)
            manager_screen.blit(text_surface, (10, 10))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.VIDEORESIZE:
                width, height = event.size
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if task8.collidepoint(mouse_pos):
                    show_upgrade_screen = False
                if task9.collidepoint(mouse_pos):
                    show_manager_screen = True
                    show_upgrade_screen = False
                if task10.collidepoint(mouse_pos):
                    show_task_screen = True
                    show_upgrade_screen = False
                if task11.collidepoint(mouse_pos):
                    show_ach_screen = True
                    show_upgrade_screen = False
                if task12.collidepoint(mouse_pos):
                    show_store_screen = True
                    show_upgrade_screen = False    
        task8 = draw_to_button(mountain_gray, 5, 90, 410, 30, "Home")
        task9 = draw_to_button(mountain_gray, 105, 90, 410, 30, "Managers")
        task10 = draw_to_button(mountain_gray, 205, 90, 410, 30, "Tasks")
        task11 = draw_to_button(mountain_gray, 10, 135, 370, 30, "Trophies")
        task12 = draw_to_button(mountain_gray, 155, 135, 370, 30, "Store")


    if not show_task_screen and not show_manager_screen and not show_upgrade_screen and show_ach_screen and not show_store_screen:
        achivements_screen.fill(misty_dawn)
        if score >= 100:
            display_score_value = f"{score:.0f}"
        else:
            display_score_value = f"{score:.2f}"
            text_surface = font.render(f"Money: ${display_score_value}", True, black)
            achivements_screen.blit(text_surface, (10, 10))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.VIDEORESIZE:
                width, height = event.size
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if task8.collidepoint(mouse_pos):
                    show_upgrade_screen = True
                    show_ach_screen = False
                if task9.collidepoint(mouse_pos):
                    show_manager_screen = True
                    show_ach_screen = False
                if task10.collidepoint(mouse_pos):
                    show_task_screen = True
                    show_ach_screen = False
                if task11.collidepoint(mouse_pos):
                    show_ach_screen = False
                if task12.collidepoint(mouse_pos):
                    show_store_screen = True
                    show_ach_screen = False    
        task8 = draw_to_button(mountain_gray, 5, 90, 410, 30, "Upgrades")
        task9 = draw_to_button(mountain_gray, 105, 90, 410, 30, "Managers")
        task10 = draw_to_button(mountain_gray, 205, 90, 410, 30, "Tasks")
        task11 = draw_to_button(mountain_gray, 10, 135, 370, 30, "Home")
        task12 = draw_to_button(mountain_gray, 155, 135, 370, 30, "Store")


    if not show_task_screen and not show_manager_screen and not show_upgrade_screen and not show_ach_screen and show_store_screen:
        store_screen.fill(misty_dawn)
        if score >= 100:
            display_score_value = f"{score:.0f}"
        else:
            display_score_value = f"{score:.2f}"
            text_surface = font.render(f"Money: ${display_score_value}", True, black)
            store_screen.blit(text_surface, (10, 10))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.VIDEORESIZE:
                width, height = event.size
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if task8.collidepoint(mouse_pos):
                    show_upgrade_screen = True
                    show_store_screen = False
                if task9.collidepoint(mouse_pos):
                    show_manager_screen = True
                    show_store_screen = False
                if task10.collidepoint(mouse_pos):
                    show_task_screen = True
                    show_store_screen = False
                if task11.collidepoint(mouse_pos):
                    show_ach_screen = True
                    show_store_screen = False
                if task12.collidepoint(mouse_pos):
                    show_store_screen = False    
        task8 = draw_to_button(mountain_gray, 5, 90, 410, 30, "Upgrades")
        task9 = draw_to_button(mountain_gray, 105, 90, 410, 30, "Managers")
        task10 = draw_to_button(mountain_gray, 205, 90, 410, 30, "Tasks")
        task11 = draw_to_button(mountain_gray, 10, 135, 370, 30, "Trophies")
        task12 = draw_to_button(mountain_gray, 155, 135, 370, 30, "Home")
    
    if score >= 100:
        display_score_value = f"{score:.0f}"
    else:
        display_score_value = f"{score:.2f}"
    text_surface = font.render(f"Money: ${display_score_value}", True, black)
    screen.blit(text_surface, (10, 10))

    pygame.display.flip()

    save_data = {
        "score": score,
        "pale_olive_owned": pale_olive_owned,
        "olive_green_owned": olive_green_owned,
        "pine_needle_owned": pine_needle_owned,
        "forest_green_owned": forest_green_owned,
        "dark_olive_owned": dark_olive_owned,
        "pale_olive_cost": pale_olive_cost,
        "pale_olive_value": pale_olive_value,
        "olive_green_cost": olive_green_cost,
        "olive_green_value": olive_green_value,
        "pine_needle_cost": pine_needle_cost,
        "pine_needle_value": pine_needle_value,
        "forest_green_cost": forest_green_cost,
        "forest_green_value": forest_green_value,
        "dark_olive_cost": dark_olive_cost,
        "dark_olive_value": dark_olive_value,
        "last_save": datetime.datetime.now().isoformat()
    }

    with open("savegame.json", "w") as f:
        json.dump(save_data, f)

pygame.quit()