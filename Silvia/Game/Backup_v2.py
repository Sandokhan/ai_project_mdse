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
        self.playerOne = True #self.current_player = 0 # True if player One is playing else Player Two is playing
        self.message = 0
        self.give_away =0
        self.sideOne = 0
        self.sideTwo = 0
        self.UserInput = None
        self.Playing = True

    def print_message(self, playerOne):
        self.playerOne = playerOne
        if self.playerOne :
            self.message = "\n" + "Player One's turn "
        else: 
            self.message = "\n" + "Player Two's turn "
        print(self.message)
        self.message = 0

    def display_board(self):
        print("\n" +"+--"+"---" *pit_init + "--+" )
        print( "  ", end="")
        for i in range(self.total_pit, pit_init -1, -1):
            if i > self.store1 and i < self.store2:
                print(str(self.binAmount[i]).rjust(2), end=" ")
        print("\n", self.binAmount[self.store2], " "*self.blankspace, self.binAmount[self.store1])
        print("  ", end="")
        for i in range(pit_init):
            if i < self.store1:
                print(str(self.binAmount[i]).rjust(2), end=" ")
        print("\n" +"+--"+"---" *pit_init + "--+" + "\n" )

    def choose_pit(self):
        #valid_pits = [i for i in range(pit_init) if self.board[self.current_player][i] != 0]
        #return np.random.choice(valid_pits)
        self.binChosen = int(self.UserInput)
        if (self.binChosen < 0 or self.binChosen >= self.store2  or self.binChosen == self.store1 ):
            return -1
        else:
            if self.playerOne and self.binChosen < self.store1 :
                return self.binChosen
            elif self.playerOne and self.binChosen >=self.store1 :
                return -1
            elif not(self.playerOne) and self.binChosen < self.store2 and self.binChosen  > self.store1 :
                return  self.binChosen
            elif not(self.playerOne) and self.binChosen >= self.store2 and self.binChosen  <= self.store1 :
                return -1
            elif (self.binAmount[self.binChosen] == 0):
                return -1
            

    def make_move(self, pit):
        self.binChosen = pit
        self.give_away = self.binAmount[self.binChosen]
        self.binAmount[self.binChosen] = 0 
        self.recipient = self.binChosen + 1
        self.capture = False

        while (self.give_away > 0) :
            if self.playerOne and self.recipient == self.store2:
                self.recipient = 0 # dont add bins to opponents pit
            elif not(self.playerOne) and self.recipient == self.store1:
                self.recipient = self.store1 +1 # dont add bins to opponents pit
            elif self.recipient > self.store2: 
                self.recipient = 0 
            self.binAmount[self.recipient] += 1
            self.give_away -=1
            self.recipient += 1
        
        self.last_recipient = self.recipient
        self.oponent_recipient = self.store2 - 1 - self.last_recipient
                
        if self.playerOne and self.binAmount[self.last_recipient] == 1  and self.binAmount[self.oponent_recipient] > 0: #and self.last_recipient < self.store1
            self.capture = True
            self.binAmount[self.store1] += self.binAmount[self.last_recipient] + self.binAmount[self.oponent_recipient]
            self.binAmount[self.last_recipient] = 0
            self.binAmount[self.oponent_recipient ] = 0 # last seed ends on a empty pit and there's seeds on the opposite side - all seeds are captured into palyer One's store 
            #self.playerOne = not(self.playerOne)
            return self.capture, self.playerOne
        elif not(self.playerOne) and self.binAmount[self.last_recipient] == 1 and self.binAmount[self.oponent_recipient]: # and self.last_recipient > self.store1 
            self.capture = True
            self.binAmount[self.store2] += self.binAmount[self.last_recipient] + self.binAmount[self.oponent_recipient]
            self.binAmount[self.last_recipient] = 0
            self.binAmount[self.oponent_recipient ] = 0
            #self.playerOne = not(self.playerOne)
            return self.capture, self.playerOne# last seed ends on a empty pit and there's seeds on the opposite side - all seeds are captured into palyer Two's store 
        elif self.playerOne and self.binAmount[self.last_recipient] == self.store1:  
            self.playerOne = True # if the last seed of player One end on his store, he plays again
        elif not(self.playerOne) and self.last_recipient == self.store2:
            self.playerOne = False # if the last seed of player Two end on his store, he plays again
        
        return self.capture, self.playerOne

        
    def game_over(self):
        for j in range (self.store1) :
            self.sideOne += self.binAmount[j]
            self.sideTwo += self.binAmount[j + self.store1 +1]
        if self.sideOne == 0 or self.sideTwo == 0 :
            self.binAmount[self.store1] += self.sideOne
            self.binAmount[self.store2] += self.sideTwo
            for k in range (self.store1):
                self.binAmount[k] = 0
                self.binAmount[k+self.store1+1] = 0
            return True
        if self.sideOne == 0 and self.sideTwo == 0 :
            return True
        return False
        
    def determine_winner(self):
        if self.sideOne > self.sideTwo:
            return "Player 1 wins! Score: " + str(self.sideOne) + " vs " +str(self.sideTwo)
        elif self.sideTwo > self.sideOne :
            return "Player 2 wins! Score: " + str(self.sideTwo) + " vs " +str(self.sideOne)
        else:
            return "It's a tie!"
    
    def play(self):
        while not self.game_over():
            self.print_message(self.playerOne)
            self.display_board()
            self.UserInput = input("\n" + "Enter 'q' to quit the game or your next move to continue: ")
            if self.UserInput == 'q':
                break
            pit = self.choose_pit()
            while pit == -1:
                    self.UserInput = input("Invalide input, choose a valide pit or enter 'q' to quit the game: ")
                    pit = self.choose_pit()
                    if self.UserInput == 'q':
                        break
            self.capture, self.playerOne = self.make_move(pit)
            if self.capture:
                self.display_board()
                continue

        self.display_board()
        print("Game Over!" + "\n" +self.determine_winner())


game = Mancala(pit_init, seed)
game.play()