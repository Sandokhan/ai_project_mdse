from aiEngine import minimax, minimax_alpha_beta


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
            move = int(input("Enter move [0,5]: "))

            if self.player_id == 1:
                move = move + 7

        new_state = state.make_move(move)
        return new_state


class Machine(Player):
    def __init__(self, player_id, difficulty):
        super().__init__(player_id)
        self.max_depth = 2 * difficulty - 1

    def move(self, state):
        move, value = minimax_alpha_beta(state, self.max_depth)

        printed_move = move - 7 if self.player_id == 1 else move

        print()
        print(f"Board Value: {value}. Move: {printed_move}")

        new_state = state.make_move(move)
        return new_state
