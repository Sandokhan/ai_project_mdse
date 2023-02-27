import numpy as np
import random 

pit_init = int(input("\n" + "Enter number of pits: "))
seed = int(input("Enter number of seeds: "))


## 0 palyer 1
## 1 palyer 2

class Mancala:
    def __init__(self, pit_init, seed):
        
        #self.binAmount = np.array([seed]*pit)
        self.stores = [0, 0]
        self.current_player = 0
        self.pit_init = pit_init
        self.total_pit = pit_init * 2
        self.aux = pit_init -1
        self.seed = seed
        self.board = [[self.seed]*self.pit_init, [self.seed]*self.pit_init]
        self.blankspace = self.total_pit + 1


    def display_board(self):
        print("\n" + "  ", end="")
        for i in range(pit_init):
            print(str(self.board[1][i]).rjust(2), end=" ")
        print("\n", self.stores[1], " "*self.blankspace, self.stores[0])
        print("  ", end="")
        for i in range(pit_init):
            print(str(self.board[0][i]).rjust(2), end=" ")
        print("\n")

    def choose_pit(self):
        valid_pits = [i for i in range(pit_init) if self.board[self.current_player][i] != 0]
        return random.choice(valid_pits)
    
    def make_move(self, pit):
        player = pit // self.total_pit
        pit_index = pit % self.total_pit
        seeds = self.board[player][pit_index]
        self.board[player][pit_index] = 0
        while seeds > 0:
            pit_index = (pit_index + 1) % (2 * self.total_pit)
            if pit_index == pit:
                continue
            if pit_index // self.total_pit == player:
                self.board[player][pit_index % self.total_pit] += 1
            else:
                self.board[1 - player][pit_index % self.total_pit] += 1
            seeds -= 1
        if pit_index // self.total_pit == player and self.board[player][pit_index % self.total_pit] == 1:
            opposite_pit_index = (self.total_pit - 1) - (pit_index % self.total_pit)
            opposite_seeds = self.board[1 - player][opposite_pit_index]
            self.board[player][pit_index % self.total_pit] = 0
            self.board[1 - player][opposite_pit_index] = 0
            self.stores[player] += 1 + opposite_seeds
        else:
            self.stores[player] += 0

    '''def make_move(self, pit):
        stones = self.board[self.current_player][pit]
        self.board[self.current_player][pit] = 0
        self.player_store = self.stores[self.current_player]
        while stones:
            pit = (pit + 1) % self.total_pit
            if pit == pit_init and self.current_player == 1:
                continue
            elif pit == 0 and self.current_player == 0:
                continue
            self.board[self.current_player][pit % pit_init] += 1
            stones -= 1
        if pit % pit_init == pit_init:
            self.stores[self.current_player] += 1
            return True
        elif self.board[self.current_player][pit % pit_init] == 1:
            self.stores[self.current_player] += self.board[1 - self.current_player][self.aux - pit % pit_init] + 1
            self.board[1 - self.current_player][self.aux - pit % pit_init] = 0
        self.current_player = 1 - self.current_player
        return False '''
    
    '''
    def make_move(self, pit):
        stones = self.board[self.current_player][pit]
        self.board[self.current_player][pit] = 0
        self.player_store = self.stores[self.current_player]
        pits_per_player = len(self.board[0])
        while stones:
            pit = (pit + 1) % (pits_per_player * 2)
            if pit == pits_per_player and self.current_player == 1:
                continue
            elif pit == 0 and self.current_player == 0:
                continue
            self.board[self.current_player][pit % pits_per_player] += 1
            stones -= 1
        if pit % pits_per_player == pits_per_player - 1:
            self.stores[self.current_player] += 1
            return True
        elif self.board[self.current_player][pit % pits_per_player] == 1:
            opposite_pit = (pits_per_player * 2) - pit - 2
            self.stores[self.current_player] += self.board[1 - self.current_player][opposite_pit] + 1
            self.board[1 - self.current_player][opposite_pit] = 0
        self.current_player = 1 - self.current_player
        return False '''


    def game_over(self):
        return all(x == 0 for x in self.board[0]) or all(x == 0 for x in self.board[1])

    def determine_winner(self):
        if self.stores[0] > self.stores[1]:
            return "Player 1 wins! Score: " + str(self.stores[0]) + " vs " +str(self.stores[1])
        elif self.stores[1] > self.stores[0]:
            return "Player 2 wins! Score: " + str(self.stores[1]) + " vs " +str(self.stores[0])
        else:
            return "It's a tie!"

    def play(self):
        while not self.game_over():
            self.display_board()
            pit = self.choose_pit()
            capture = self.make_move(pit)
            if capture:
                self.display_board()
                continue
        self.display_board()
        print(self.determine_winner())

game = Mancala(pit_init, seed)
game.play()