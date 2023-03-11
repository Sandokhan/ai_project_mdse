from aiEngine import minimax, minimax_alpha_beta
from mancalaEngine import PocketName, GameState


class Player:
    def __init__(self, player_id):
        self.player_id = player_id

    def move(self, state):
        pass


class Human(Player):
    def __init__(self, player_id):
        super().__init__(player_id)

    def move(self, state):
        move = None
        print()
        while move not in state.possible_moves():
            move = int(input("Enter move [0," + str(PocketName.p0_mancala - 1) + "]: "))

            if self.player_id == 1:
                move = move + PocketName.p0_mancala + 1

        new_state = state.make_move(move)
        return new_state


class Machine(Player):
    def __init__(self, player_id, difficulty, eval_func):
        super().__init__(player_id)
        self.max_depth = 2 * difficulty - 1
        self.eval_func = eval_func

    def move(self, state):
        move, value = minimax_alpha_beta(state, self.max_depth, eval_func=self.eval_func)

        printed_move = move - PocketName.p0_mancala + 1 if self.player_id == 1 else move

        print()
        print(f"Board Value: {value}. Move: {printed_move}")

        new_state = state.make_move(move)
        return new_state
