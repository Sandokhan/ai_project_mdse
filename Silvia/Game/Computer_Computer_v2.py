import numpy as np
import random 

pit_init = int(input("\n" + "Enter number of pits: "))
seed = int(input("Enter number of seeds: "))


## 0 palyer 1
## 1 palyer 2

class Mancala:
    def __init__(self, pit_init, seed):
        
        #self.binAmount = np.array([seed]*pit)
        self.current_player = 0
        self.pit_init = pit_init
        self.total_pit = pit_init * 2
        self.seed = seed
        self.store1 = pit_init
        self.store2 = self.total_pit -1
        self.binAmount = np.array([seed]*self.total_pit)
        self.binAmount[self.store1] = 0
        self.binAmount[self.store2] = 0
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