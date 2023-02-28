import numpy as np

pit_init = int(input("\n" + "Enter number of pits: "))
seed = int(input("Enter number of seeds: "))


## 0 palyer 1
## 1 palyer 2

class Mancala:
    def __init__(self, pit_init, seed):
        
        self.pit_init = pit_init
        self.total_pit = pit_init *2 +2
        self.seed = seed
        self.store1 = pit_init
        self.store2 = self.total_pit -1
        self.binAmount = np.array([seed]*self.total_pit)
        self.binAmount[self.store1] = 0
        self.binAmount[self.store2] = 0
        self.blankspace = self.pit_init * 2 + (self.pit_init)
        self.playing = True
        self.playerOne = True #self.current_player = 0
        self.invalide_bin = False
        self.message = 0
        self.give_away =0

    def print_message(self,playerOne,message):
        if playerOne and message == 0:
            message = "Player One's turn "
        elif not(playerOne) and message == 0:
            message = "Player Two's turn "
        elif message == -1:
            message = "Invalide input, Try again"
        else:
            UserInput = input("\n" + "Enter 'q' to quit the game or your next move to continue: ")
            
        print(message)
        message = 0

    def display_board(self):
        print("\n" +"+--"+"---" *self.pit_init + "--+" )
        print( "  ", end="")
        for i in range(self.total_pit, pit_init -1, -1):
            if i > self.store1 and i < self.store2:
                print(str(self.binAmount[i]).rjust(2), end=" ")
        print("\n", self.binAmount[self.store2], " "*self.blankspace, self.binAmount[self.store1])
        print("  ", end="")
        for i in range(pit_init):
            if i < self.store1:
                print(str(self.binAmount[i]).rjust(2), end=" ")
        print("\n" +"+--"+"---" *self.pit_init + "--+" + "\n" )




myclass =Mancala(pit_init,seed)
myclass.display_board()