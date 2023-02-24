import pygame

pygame.init()

# Set up the display
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('My Game')

# Set up the colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up the font
font = pygame.font.SysFont(None, 50)

# Set up the menu options
start_option = font.render('Start', True, white)
new_game_option = font.render('New Game', True, white)
exit_option = font.render('Exit', True, white)
pause_option = font.render('Pause', True, white)

# Set up the menu positions
start_position = (display_width / 2 - start_option.get_width() / 2, display_height / 2 - 100)
new_game_position = (display_width / 2 - new_game_option.get_width() / 2, display_height / 2 - 50)
pause_position = (display_width / 2 - pause_option.get_width() / 2, display_height / 2)
exit_position = (display_width / 2 - exit_option.get_width() / 2, display_height / 2 + 50)


# Main menu function
def game_menu():
    menu_running = True

    while menu_running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Check for mouse clicks on menu options
            if event.type == pygame.MOUSEBUTTONDOWN:

                mouse_pos = pygame.mouse.get_pos()

                if start_option.get_rect(center=start_position).collidepoint(mouse_pos):
                    start_game()

                if new_game_option.get_rect(center=new_game_position).collidepoint(mouse_pos):
                    new_game()

                if pause_option.get_rect(center=pause_position).collidepoint(mouse_pos):
                    pause_game()

                if exit_option.get_rect(center=exit_position).collidepoint(mouse_pos):
                    pygame.quit()
                    quit()

        # Draw the menu options
        game_display.fill(black)
        game_display.blit(start_option, start_position)
        game_display.blit(new_game_option, new_game_position)
        game_display.blit(pause_option, pause_position)
        game_display.blit(exit_option, exit_position)

        pygame.display.update()


# Start game function
def start_game():
    print('Starting game...')


# New game function
def new_game():
    print('Starting new game...')


# Pause game function
def pause_game():
    print('Pausing game...')


# Call the game menu function to start the menu
game_menu()
