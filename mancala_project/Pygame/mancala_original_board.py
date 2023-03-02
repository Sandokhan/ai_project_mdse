import pygame
from pygame.locals import *
from sys import exit
from random import randint

# Set up screen dimensions
screen_width = 900
screen_height = 600

# Set up board dimensions and locations
board_x = 40
board_y = 120

# Set up seed dimensions
seed_size = 10

# add_seed = pygame.mixer.Sound('sound/add_seed.wav')
# add_seed.play(-1)

# Set up Pygame
pygame.init()
font = pygame.font.SysFont('arial', 40, bold=True, italic=True)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Mancala')

# Set up the background
background_image = pygame.image.load("mancala_project/Pygame/images/background.png").convert()

# Set up the board images
board_mancala = pygame.image.load("mancala_project/Pygame/images/board.png").convert_alpha()

# get the images dimensions
image_width, image_height = board_mancala.get_size()

# set the new size of the images
new_width = int(image_width * 0.65)  # largura do tabuleiro
new_height = int(image_height * 0.65)  # altura do tabuleiro

# resize the images
board_image = pygame.transform.scale(board_mancala, (new_width, new_height))


# Set up the seed images
seed_image = pygame.image.load("mancala_project/Pygame/images/seed.png").convert_alpha()

# Set up the board
board = [
    [4, 4, 4, 4, 4, 4],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [4, 4, 4, 4, 4, 4],
    [0, 0, 0, 0, 0, 0]
]

# Set up the player's turn
player_turn = 1

clock = pygame.time.Clock()

while True:
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Draw the background
    screen.blit(background_image, (0, 0))

    # Draw the board
    screen.blit(board_image, (board_x, board_y))

    # Draw the seeds
    for i in range(6):
        for j in range(6):
            seed_count = board[i][j]
            if seed_count > 0:
                x = board_x + 140 + j * 93
                y = board_y + 30 + i * 40
                for k in range(seed_count):
                    screen.blit(seed_image, (x, y))
                    y += seed_size

    # Update the display
    pygame.display.flip()

    