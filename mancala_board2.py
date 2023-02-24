import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

# Set up screen dimensions
screen_width = 900
screen_height = 600

# Set up board dimensions and locations
board_x = 40
board_y = 120

# Set up seed dimensions
seed_size = 10

# Set up Pygame
font = pygame.font.SysFont('arial', 40, bold=True, italic=True)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Mancala')

# Set up the background
background_image = pygame.image.load("images/background.png").convert()

# Set up the board images
board_mancala = pygame.image.load("images/board.png").convert_alpha()

# get the images dimensions
image_width, image_height = board_mancala.get_size()

# set the new size of the images
new_width = int(image_width * 0.65)  # largura do tabuleiro
new_height = int(image_height * 0.65)  # altura do tabuleiro

# resize the images
board_image = pygame.transform.scale(board_mancala, (new_width, new_height))


# Set up the seed images
seed_image = pygame.image.load("images/seed.png").convert_alpha()
seed_width = seed_image.get_width()
seed_height = seed_image.get_height()


class Pit:
    def __init__(self, x, y, seeds=0, is_mancala=False):
        self.x = x
        self.y = y
        self.seeds = seeds
        self.is_mancala = is_mancala

    def add_seed(self):
        self.seeds += 1

    def remove_seed(self):
        seeds = self.seeds
        self.seeds = 0
        return seeds


class Board:
    def __init__(self):
        self.pits = []
        self.mancalas = []
        self.player_pits = []
        self.player_mancalas = []
        self.current_player = 1

        # Create pits and mancalas
        for i in range(6):
            x = board_x + 140 + i * 93
            y = board_y + 30
            pit = Pit(x, y)
            self.pits.append(pit)
            self.player_pits.append(pit)

        mancala1 = Pit(board_x + 32, board_y + 30, is_mancala=True)
        mancala2 = Pit(board_x + 678, board_y + 30, is_mancala=True)
        self.mancalas = [mancala1, mancala2]
        self.player_mancalas = [mancala1, mancala2]

        for i in range(6):
            x = board_x + 140 + i * 93
            y = board_y + 356
            pit = Pit(x, y)
            self.pits


clock = pygame.time.Clock()
x, y = (0, 0)
while True:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    # Draw the background
    screen.blit(background_image, (0, 0))

    # Draw the board
    screen.blit(board_image, (board_x, board_y))
    pygame.display.update()
pygame.quit()
