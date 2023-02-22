import pygame
import random

WIDTH = 800
HEIGHT = 600

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class Mancala:
    def __init__(self, player1_avatar, player2_avatar, difficulty, game_mode):
        self.board = [[4] * 6, [4] * 6]
        self.stores = [0, 0]
        self.current_player = 0
        self.player1_avatar = player1_avatar
        self.player2_avatar = player2_avatar
        self.difficulty = difficulty
        self.game_mode = game_mode
        self.game_over = False
        self.winner = None
        self.ai_turn = False

        # Initialize Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Mancala")

        # Load images
        self.board_img = pygame.image.load("board.png")
        self.pit_img = pygame.image.load("pit.png")
        self.store_img = pygame.image.load("store.png")
        self.avatars = {
            0: pygame.image.load(player1_avatar),
            1: pygame.image.load(player2_avatar),
        }

        # Set font
        self.font = pygame.font.SysFont(None, 48)

    def display_board(self):
        # Draw background
        self.screen.fill(BLACK)

        # Draw board
        self.screen.blit(self.board_img, (0, 0))

        # Draw pits
        for i in range(6):
            x = 98 + i * 103
            y = 123
            for j in range(self.board[1][i]):
                self.screen.blit(self.pit_img, (x, y))
                y += 23
            x = 98 + i * 103
            y = 342
            for j in range(self.board[0][i]):
                self.screen.blit(self.pit_img, (x, y))
                y += 23

        # Draw stores
        self.screen.blit(self.store_img, (8, 180))
        self.screen.blit(self.store_img, (688, 180))
        text1 = self.font.render(str(self.stores[0]), True, WHITE)
        text2 = self.font.render(str(self.stores[1]), True, WHITE)
        self.screen.blit(text1, (50, 250))
        self.screen.blit(text2, (730, 250))

        # Draw avatars
        self.screen.blit(self.avatars[0], (8, 430))
        self.screen.blit(self.avatars[1], (688, 430))

        # Draw current player indicator
        if not self.game_over:
            if self.current_player == 0:
                pygame.draw.circle(self.screen, RED, (70, 550), 10)
            else:
                pygame.draw.circle(self.screen, RED, (730, 550), 10)

        # Update display
        pygame.display.update()

    def choose_pit(self):
        if self.game_mode == "human-human":
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game_over = True
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        x, y = event.pos
                        if 114 <= x < 114 + 618 and 123 <= y < 123 + 138:
                            pit = (x - 114) // 103
                            if self.current_player == 0 and self.board[0][pit] != 0:
                                return pit
                            elif self.current_player == 1 and self.board[1][pit] != 0:
                                return pit
                    if self.game_over:
                        return None

        elif self.game_mode == "human-computer":
            if self.current_player == 0:
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.game_over = True
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            x, y = event.pos
                            if 114 <= x < 114 + 618 and 123 <= y < 123 + 138:
                                pit = (x - 114) // 103
                                if self.board[0][pit] != 0:
                                    return pit
                        if self.game_over:
                            return None
            else:
                if self.difficulty == "easy":
                    pits = [i for i in range(6) if self.board[1][i] != 0]
                    return random.choice(pits)
                elif self.difficulty == "hard":
                    pits = [i for i in range(6) if self.board[1][i] != 0]
                    max_score = float("-inf")
                    best_pit = None
                    for pit in pits:
                        temp_board = self.board.copy()
                        temp_stores = self.stores.copy()
                        score = self.make_move(self.current_player, pit, temp_board, temp_stores)
                        if score > max_score:
                            max_score = score
                            best_pit = pit
                    return best_pit

        elif self.game_mode == "computer-computer":
            if self.difficulty == "easy":
                pits = [i for i in range(6) if self.board[1][i] != 0]
                return random.choice(pits)
            elif self.difficulty == "hard":
                pits = [i for i in range(6) if self.board[1][i] != 0]
                max_score = float("-inf")
                best_pit = None
                for pit in pits:
                    temp_board = self.board.copy()
                    temp_stores = self.stores.copy()
                    score = self.make_move(self.current_player, pit, temp_board, temp_stores)
                    if score > max_score:
                        max_score = score
                        best_pit = pit
                return best_pit

    def make_move(self, player, pit, board, stores):
        score = 0
        stones = board[player][pit]
        board[player][pit] = 0
        while stones > 0:
            pit = (pit + 1) % 6
            if pit == 0 and player == 1:
                continue
            elif pit == 0 and player == 0:
                player = 1
            elif pit == 5 and player == 0:
                continue
            elif pit == 5 and player == 1:
                player = 0
            else:
                board[player][pit] += 1
                stones -= 1
        if pit != 0 and board[player][pit] == 1:
            score = board[1 - player][5 - pit]
            stores[player] += score
            board[1 - player][5 - pit] = 0
            board[player][pit] = 0
        return score

    def switch_player(self):
        self.current_player = 1 - self.current_player

    def check_game_over(self):
        if all(x == 0 for x in self.board[0]) or all(x == 0 for x in self.board[1]):
            self.game_over = True
            self.stores[0] += sum(self.board[0])
            self.stores[1] += sum(self.board[1])
            self.board = [[0] * 6 for _ in range(2)]

    def get_winner(self):
        if not self.game_over:
            return None
        if self.stores[0] > self.stores[1]:
            return 0
        elif self.stores[1] > self.stores[0]:
            return 1
        else:
            return -1
