if 'last_save' in save_data:
    try:
        last_save_time = datetime.datetime.fromisoformat(save_data['last_save'])
        now = datetime.datetime.now()
        elapsed = now - last_save_time

        hours, remainder = divmod(int(elapsed.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)

        time_str = f"{hours} hours, {minutes} minutes, {seconds} seconds"

        welcome_message = "Welcome back!!"
        time_message = "You were gone for:"
        time_diff = f"{time_str}"
        welcome_surface = font.render(welcome_message, True, (255, 255, 255))
        time_surface = font.render(time_message, True, (255,255,255))
        time_diff_surface = font.render(time_diff, True, (255, 255, 255))

        popup_width = 400
        popup_height = 200
        popup_surface = pygame.Surface((popup_width, popup_height))
        popup_surface.fill((misty_dawn))
        
        def show_welcome_popup():
            padding = 20
            popup_surface.blit(welcome_surface, (padding, padding))
            popup_surface.blit(time_surface, (padding, padding + welcome_surface.get_height() + 10))
            popup_surface.blit(time_diff_surface, (padding, padding + welcome_surface.get_height() + time_surface.get_height() + 20))
            pygame.display.flip()

        show_welcome_popup()
    
    except Exception as e:
        print("Error parsing last save time:", e)

show_startup_popup = True  
popup_display_time = 3000  
popup_start_time = None
overlay = pygame.Surface((width, height))
overlay.set_alpha(200)
overlay.fill((0, 0, 0)) 
