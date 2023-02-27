import pygame
import random
import sys
import numpy as np
import pandas as pd
import matplotlib as mpl
import warnings


# Suppress the warning message
warnings.filterwarnings("ignore", category=UserWarning)

# Set up the board


board_color = (255, 255, 255)
pit_color = (200, 200, 200)
store_color = (100, 100, 100)
seed_color = (255, 255, 0)
seed_radius = 10
pit_size = 50 *1.5
store_size = 80 
pit_spacing = 10*2
pit_rows = 2
pit_cols = 7
board_width = pit_cols * (pit_size + pit_spacing) + store_size * 2.4
board_height = pit_rows * (pit_size + pit_spacing) + store_size
board_x = 20 #(800 - board_width) // 2
board_y = 80 #(600 - board_height) // 2

pygame.init()
window = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Initialize the game
player_turn = 0
stone_count = 4
board = [[stone_count for _ in range(pit_cols)] for _ in range(pit_rows)]
board[0][-1] = 0
board[1][0] = 0


def draw_board():
    window.fill(board_color)
    for row in range(pit_rows):
        for col in range(pit_cols):
            pit_x = board_x + 20+ col * (pit_size + pit_spacing) + store_size 
            pit_y = board_y + 10+ row * (pit_size + pit_spacing)  
            pygame.draw.rect(window, pit_color, (pit_x, pit_y, pit_size, pit_size))
            seeds = board[row][col]

            for k in range(seeds):
                seed_x = pit_x + pit_size// 2 + (k % 3 - 1) * seed_radius * 2
                seed_y = pit_y + pit_size // 2 + (k // 3 - 1) * seed_radius * 2
                pygame.draw.circle(window, seed_color, (seed_x, seed_y), seed_radius)


    for side in range(2):
        store_x = board_x + side * (board_width - store_size)
        store_y = board_y + 10 #side * (board_height - store_size)
        pygame.draw.rect(window, store_color, (store_x, store_y, store_size, board_height))

draw_board()
pygame.display.flip()

# Create the game loop
running = True
player1_score = []
player1_score = []

while running:
    # Handle events
    clock.tick(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Handle user input
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for row in range(pit_rows):
                for col in range(pit_cols):
                    pit_x = board_x + store_size + col * (pit_size + pit_spacing)
                    pit_y = board_y + row * (pit_size + pit_spacing)
                    if pit_x <= mouse_x < pit_x + pit_size and pit_y <= mouse_y < pit_y + pit_size:
                        if row == player_turn and board[row][col] > 0:
                            # Move stones around the board
                            stones = board[row][col]
                            board[row][col] = 0
                            pit = (row, col)
                            while stones > 0:
                                pit = (pit[0], (pit[1] + 1) % pit_cols)
                                if pit == (player_turn, 0):
                                    continue  # Skip opponent's store
                                board[pit[0]][pit[1]] += 1
                                stones -= 1
                            if pit[0] == player_turn and board[pit[0]][pit[1]] == 1:
                                # Capture stones on opposite side
                                opposite_pit = (1 - player_turn, pit_cols - pit[1] - 1)
                                board[player_turn][-1] += board[player_turn][pit[1]] + board[opposite_pit[0]][opposite_pit[1]]
                                board[player_turn][pit[1]] = board[opposite_pit[0]][opposite_pit[1]] = 0
                                # Check for end of game
                                if all(stones == 0 for stones in board[0][:-1]) or all(stones == 0 for stones in board[1][:-1]):
                                    running = False
                            elif pit[1] != 0:
                                # Check for end of turn
                                player_turn = 1 - player_turn
                                break

            # Update the display
            draw_board()
            pygame.display.flip()

# Display the winner
player1_score = sum(board[0])
player2_score = sum(board[1])
if player1_score > player2_score:
    winner = "Player 1 wins!"
elif player2_score > player1_score:
    winner = "Player 2 wins!"
else:
    winner = "It's a tie!"
font = pygame.font.SysFont("Arial", 64)
text = font.render(winner, True, (0, 0, 0))
text_rect = text.get_rect(center=(400, 300))
window.fill(board_color)
window.blit(text, text_rect)
pygame.display.flip()


# Wait for the user to quit
#while True:
    #for event in pygame.event.get():
        #if event.type == pygame.QUIT:
            #pygame.quit()
                #sys.exit()

'''

# Define constants for the game
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
BOARD_WIDTH = 0
BOARD_HEIGHT = 0
BOARD_X = 40
BOARD_Y = 120
NUM_PITS_PER_PLAYER = 6
NUM_SEEDS_PER_PIT = 4
SEED_SIZE = 10
SEED_SPACING = 5


class Mancala:
    def __init__(self, board_image_path, seed_image_path, background_image_path): #board_image_path, seed_image_path, background_image_path
        # Initialize Pygame
        pygame.init()
        # Set up the screen
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Mancala")

        self.clock = pygame.time.Clock()

        # Load images
        self.board_image_init = pygame.image.load(board_image_path) #.convert_alpha()
        self.seed_image = pygame.image.load(seed_image_path)    #.convert_alpha()
        self.background_image = pygame.image.load(background_image_path).convert()
        
        # set the new size of the images
        self.image_width, self.image_height = self.board_image_init.get_size()
        self.new_width = int(self.image_width * 0.65)  # largura do tabuleiro
        self.new_height = int(self.image_height * 0.65)  # altura do tabuleiro

        # resize the images
        self.board_image = pygame.transform.scale(self.board_image_init, (self.new_width, self.new_height))

        # Create the board
        self.board = [[0 for _ in range(NUM_PITS_PER_PLAYER + 1)] for _ in range(2)]
        for player in range(2):
            for pit in range(NUM_PITS_PER_PLAYER):
                self.board[player][pit] = NUM_SEEDS_PER_PIT
                
        # Set up the current player
        self.current_player = 0
        # Set up the game state
        self.game_over = False
        self.clock.tick(1)

    def draw_board(self):
        # Draw the background image
        self.screen.blit(self.background_image, (0, 0))
        # Draw the board image
        self.screen.blit(self.board_image, (BOARD_X, BOARD_Y))
        
        # Draw the seeds in the pits
        
        for player in range(2):
            for pit in range(NUM_PITS_PER_PLAYER):
                num_seeds = self.board[player][pit]
                x = BOARD_X + 140 + pit * 93
                y = BOARD_Y  + 30 + pit * 40
                x = BOARD_X + (NUM_PITS_PER_PLAYER - pit - 1) * (SEED_SIZE + SEED_SPACING) + SEED_SPACING
                y = BOARD_Y + (player * (BOARD_HEIGHT - SEED_SIZE - SEED_SPACING)) + SEED_SPACING
                for i in range(num_seeds):
                    self.screen.blit(self.seed_image, (x, y))
                    if player == 0:
                        y += SEED_SIZE + SEED_SPACING
                    else:
                        y -= SEED_SIZE + SEED_SPACING

    def update_board(self, pit):
        # Move the seeds from the selected pit
        num_seeds = self.board[self.current_player][pit]
        self.board[self.current_player][pit] = 0
        player_pit = pit
        while num_seeds > 0:
            player_pit = (player_pit + 1) % (NUM_PITS_PER_PLAYER + 1)
            if player_pit == NUM_PITS_PER_PLAYER:
                if self.current_player == 0:
                    player_pit = 0
                else:
                    player_pit = NUM_PITS_PER_PLAYER - 1
            self.board[self.current_player][player_pit] += 1
            num_seeds -= 1

        # Check if the last seed landed in an empty pit on the current player's side
        opposite_pit = NUM_PITS_PER_PLAYER - player_pit - 1
        if player_pit < NUM_PITS_PER_PLAYER and self.board[self.current_player][player_pit] == 1:
            self.board[self.current_player][NUM_PITS_PER_PLAYER] += self.board[1 - self.current_player][opposite_pit] + 1
            self.board[self.current_player][player_pit] = 0
            self.board[1 - self.current_player][opposite_pit] = 0

        # Switch to the other player if the turn is over
        if player_pit == NUM_PITS_PER_PLAYER:
            self.current_player = 1 - self.current_player

        # Check if the game is over
        if sum(self.board[0][:NUM_PITS_PER_PLAYER]) == 0 or sum(self.board[1][:NUM_PITS_PER_PLAYER]) == 0:
            self.game_over = True
            self.current_player = None

            # Move all remaining seeds to each player's store
            for player in range(2):
                self.board[player][NUM_PITS_PER_PLAYER] += sum(self.board[player][:NUM_PITS_PER_PLAYER])
                for pit in range(NUM_PITS_PER_PLAYER):
                    self.board[player][pit] = 0

    def play_game(self):
        # Main game loop
        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                    x, y = event.pos
                    if BOARD_X <= x < BOARD_X + BOARD_WIDTH and BOARD_Y <= y < BOARD_Y + BOARD_HEIGHT:
                        row = y - BOARD_Y
                        col = x - BOARD_X
                        player = row // ((BOARD_HEIGHT - SEED_SIZE - SEED_SPACING) // 2)
                        pit = (NUM_PITS_PER_PLAYER - col // (SEED_SIZE + SEED_SPACING)) % NUM_PITS_PER_PLAYER
                        if player == self.current_player and self.board[player][pit] > 0:
                            self.update_board(pit)
                            
            # Check if the game is over
            if self.game_over:
                winner = None
                if self.board[0][NUM_PITS_PER_PLAYER] > self.board[1][NUM_PITS_PER_PLAYER]:
                    winner = 0
                elif self.board[1][NUM_PITS_PER_PLAYER] > self.board[0][NUM_PITS_PER_PLAYER]:
                    winner = 1
                else:
                    winner = -1
                self.draw_board(winner)
                continue
            # Redraw the game board
            self.draw_board()
            pygame.display.flip()
            

'''

