import random

class Mancala:
    def __init__(self):
        self.board = [[4]*6, [4]*6]
        self.stores = [0, 0]
        self.current_player = 0

    def display_board(self):
        print("  ", end="")
        for i in range(6):
            print(str(self.board[1][i]).rjust(2), end=" ")
        print("\n", self.stores[1], " "*11, self.stores[0])
        print("  ", end="")
        for i in range(6):
            print(str(self.board[0][i]).rjust(2), end=" ")
        print("\n")

    def choose_pit(self):
        valid_pits = [i for i in range(6) if self.board[self.current_player][i] != 0]
        return random.choice(valid_pits)

    def make_move(self, pit):
        stones = self.board[self.current_player][pit]
        self.board[self.current_player][pit] = 0
        player_store = self.stores[self.current_player]
        while stones:
            pit = (pit + 1) % 12
            if pit == 6 and self.current_player == 1:
                continue
            elif pit == 0 and self.current_player == 0:
                continue
            self.board[self.current_player][pit % 6] += 1
            stones -= 1
        if pit % 6 == 6:
            self.stores[self.current_player] += 1
            return True
        elif self.board[self.current_player][pit % 6] == 1:
            self.stores[self.current_player] += self.board[1 - self.current_player][5 - pit % 6] + 1
            self.board[1 - self.current_player][5 - pit % 6] = 0
        self.current_player = 1 - self.current_player
        return False

    def game_over(self):
        return all(x == 0 for x in self.board[0]) | all(x == 0 for x in self.board[1])

    def determine_winner(self):
        if self.stores[0] > self.stores[1]:
            return "Player 1 wins!"
        elif self.stores[1] > self.stores[0]:
            return "Player 2 wins!"
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

game = Mancala()
game.play()