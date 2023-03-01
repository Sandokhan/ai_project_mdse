from mancalaEngine import GameState
from players import Human, Machine
import time
import psutil

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


def run_n_matches(n, max_time=3600):
    start_time = time.time()

    results = [0, 0, 0]
    memory_used = 0
    while n > 0 and time.time() - start_time < max_time:
        n -= 1
        player_0 = Machine(0, machine_level)
        player_1 = Machine(1, machine_level)
        game_state = GameState()
        game_state.stealing = True
        while not game_state.is_terminal():
            if game_state.player_turn == 0:
                game_state = player_0.move(game_state)
            else:
                game_state = player_1.move(game_state)
        results[game_state.winner] += 1
        memory_used = max(memory_used, psutil.Process().memory_info().rss)

    print("\n=== Elapsed time: %s seconds ===" % (int(time.time() - start_time)))
    print(f"  Player 1: {results[1]} victories")
    print(f"  Player 2: {results[2]} victories")
    print(f"  Draws: {results[0]} ")
    print(f"  Maximum memory usage: {memory_used / (1024 * 1024)} MB")
    print("===============================")


if __name__ == "__main__":
    # machine_machine_game(machine_level, machine_level)
    # human_machine_game(machine_level)
    run_n_matches(2)
