from mancalaEngine import GameState
from players import Human, Machine

machine_level = 6


def humans_game():
    player_0 = Human(0)
    player_1 = Human(1)
    play_game(player_0, player_1)


def human_machine_game(ai_difficulty):
    player_0 = Human(0)
    player_1 = Machine(1, ai_difficulty)
    play_game(player_0, player_1)


def machine_player_game(ai_difficulty):
    player_0 = Machine(0, ai_difficulty)
    player_1 = Human(1)
    play_game(player_0, player_1)


def machine_machine_game(ai0_difficulty, ai1_difficulty):
    player_0 = Machine(0, ai0_difficulty)
    player_1 = Machine(1, ai1_difficulty)
    play_game(player_0, player_1)


def play_game(player_0, player_1, stealing_mode=True):
    game_state = GameState(stealing=stealing_mode)

    while not game_state.is_terminal():
        game_state.show()
        if game_state.player_turn == 0:
            game_state = player_0.move(game_state)
        else:
            game_state = player_1.move(game_state)
    game_state.show()
    game_state.show_winning_message()


if __name__ == "__main__":
    #machine_machine_game(machine_level, machine_level)
    human_machine_game(machine_level)