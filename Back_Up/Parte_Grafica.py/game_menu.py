import pygame
from pygame.locals import *
import button
# import mancala_board

pygame.init()

# Create game window
screen_width = 900
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Main Menu")

# game variables
game_paused = False
menu_state = "main"

# Fonts and colour
font = pygame.font.SysFont("arialblack", 40)
TEXT_COL = (255, 255, 255)

# load button images
start_img = pygame.image.load('./images/start_btn.png').convert_alpha()
exit_img = pygame.image.load('./images/exit_btn.png').convert_alpha()

# create button instances
start_button = button.Button(200, 200, start_img, 0.8)
exit_button = button.Button(500, 200, exit_img, 0.8)


def draw_text(text, font, text_coulor, x, y):
    img = font.render(text, True, text_coulor)
    screen.blit(img, (x, y))


# game loop
run = True
while run:

    screen.fill((52, 78, 91))

    if not game_paused:
        if menu_state == "main":
            if start_button.draw(screen):
                game_paused = False
            if exit_button.draw(screen):
                run = False
        else:
            draw_text("Press SPACE to pause", font, TEXT_COL, 200, 250)
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pressed = pygame.key.get_pressed()

    if pressed[K_SPACE]:
        game_paused = True

    pygame.display.update()
