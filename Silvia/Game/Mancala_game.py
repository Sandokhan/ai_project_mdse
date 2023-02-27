import numpy as np

class Mancala:
    def __init__(self, difficulty='easy'):
        self.board = np.array([[4]*6, [4]*6, [0,0]])
        self.player_turn = 0
        self.difficulty = difficulty

    def play(self):
        while not self.game_over():
            print(self.board)
            print("Player %d's turn" % (self.player_turn+1))
            if self.player_turn == 0:
                pit = int(input("Enter pit number: "))
                while not self.is_valid_move(pit):
                    pit = int(input("Enter valid pit number: "))
            else:
                pit = self.get_computer_move()
                print("Computer plays pit %d" % pit)

            self.make_move(pit)
            
        self.print_final_score()

    def get_computer_move(self):
        if self.difficulty == 'easy':
            valid_moves = np.where(self.board[self.player_turn]>0)[0]
            return np.random.choice(valid_moves)
        elif self.difficulty == 'medium':
            pit_scores = []
            for i in range(6):
                if self.is_valid_move(i):
                    board_copy = self.board.copy()
                    self.make_move(i)
                    score = self.get_player_score(self.player_turn)
                    pit_scores.append(score)
                    self.board = board_copy

                else:
                    pit_scores.append(-np.inf)

            return np.argmax(pit_scores)
        else:
            _, move = self.minimax(2, True)
            return move
        
    '''def is_maximizing(player, current_player):
        if player == current_player:
            return True
        else:
            return False'''

    def minimax(self, depth, q):
        if depth == 0 or self.game_over():
            score = self.get_player_score(self.player_turn)
            return score, None
        
        if is_maximizing:
            max_score = -np.inf
            best_move = None
            for i in range(6):
                if self.is_valid_move(i):
                    board_copy = self.board.copy()
                    self.make_move(i)
                    score, _ = self.minimax(depth-1, False)
                    if score > max_score:
                        max_score = score
                        best_move = i
                    self.board = board_copy
            return max_score, best_move
        else:
            min_score = np.inf
            for i in range(6):
                if self.is_valid_move(i):
                    board_copy = self.board.copy()
                    self.make_move(i)
                    score, _ = self.minimax(depth-1, True)
                    if score < min_score:
                        min_score = score
                    self.board = board_copy
            return min_score, None

    def make_move(self, pit):
        stones = self.board[self.player_turn][pit]
        self.board[self.player_turn][pit] = 0

        current_pit = pit
        while stones > 0:
            current_pit = (current_pit + 1) % 6
            if current_pit == 0 and self.player_turn == 1:
                continue
            elif current_pit == 5 and self.player_turn == 0:
                continue
            else:
                self.board[self.player_turn][current_pit] += 1
                stones -= 1
        
        if current_pit == 5 and self.player_turn == 0:
            self.player_turn = 0
        elif current_pit == 0 and self.player_turn == 1:
            self.player_turn = 1
        else:
                self.board[self.player_turn][current_pit] += 1
                stones -= 1
        
        if current_pit == 5 and self.player_turn == 0:
            self.player_turn = 0
        elif current_pit == 0 and self.player_turn == 1:
            self.player_turn = 1
        else:
            self.player_turn = (self.player_turn + 1) % 2

    def is_valid_move(self, pit):
        if self.board[self.player_turn][pit] == 0:
            return False
        elif pit == 5 and self.player_turn == 0:
            return False
        elif pit == 0 and self.player_turn == 1:
            return False
        else:
            return True

    def get_player_score(self, player):
        return np.sum(self.board[player][:-1])

    def game_over(self):
        if np.sum(self.board[0][:-1]) == 0 or np.sum(self.board[1][:-1]) == 0:
            return True
        else:
            return False

    def print_final_score(self):
        score1 = self.get_player_score(0)
        score2 = self.get_player_score(1)

        print("Final Score:")
        print("Player 1: %d" % score1)
        print("Player 2: %d" % score2)

        if score1 > score2:
            print("Player 1 wins!")
        elif score2 > score1:
            print("Player 2 wins!")
        else:
            print("Tie game!")