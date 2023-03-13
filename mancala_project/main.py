from game import play_game
from aiEngine import static_eval, simple_score, material_advantage, extra_turn, rightside_pit,many_moves, keep_on_own_side, closest_to_opponent
from players import Human, Machine


def main():
    print("\nWhich player do you want: Human(h) or Machine(m)")

    playerOne = input("Player 1: ").strip().lower()
    while playerOne != 'm' and playerOne != 'h':
        print("Invalid input.\n")
        playerOne = input("Player 1: ").strip().lower()

    if playerOne == 'm':
        while True:
            try:
                levelOne = int(input("Machine level (2 for easy, 4 for medium, and 6 for hard): "))
                break
            except ValueError:
                print("Error: Invalid input. Please enter a valid level.")

    playerTwo = input("Player 2: ").strip().lower()
    while playerTwo != 'm' and playerTwo != 'h':
        print("Invalid input.\n")
        playerTwo = input("Player 1: ").strip().lower()

    if playerTwo == 'm':
        while True:
            try:
                levelTwo = int(input("Machine level (2 for easy, 4 for medium, and 6 for hard): "))
                break
            except ValueError:
                print("Error: Invalid input. Please enter a valid level.")

    stealing_mode = input("Turn on STEALING mode? (y/n) ").strip().lower()
    while stealing_mode.strip().lower() != 'y' and stealing_mode.strip().lower() != 'n':
        stealing_mode = input("Turn on STEALING mode? (y/n) ").strip().lower()

    p_zero = "Human" if playerOne != 'm' else "Machine"
    p_one = "Human" if playerTwo != 'm' else "Machine"

    eval_func = None
    if levelOne or levelTwo:
        while True:
            try:
                eval_func = int(input("\nChoose evaluation function:\n 1 - Static\n 2 - Simple Score\n 3 - Material Advantage\n 4 - Extra Turn"
                    +"\n 5 - Right Side Pit\n 6 - Many Moves\n 7 - Keep on Own side\n 8 - Closest to Opponent: "))
                break
            except ValueError:
                print("Error: Invalid input. Please enter a valid level.")
       
        while eval_func < 1 or eval_func  > 8  :
            eval_func = int(input("\nChoose evaluation function:\n 1 - Static\n 2 - Simple Score\n 3 - Material Advantage\n 4 - Extra Turn"
                +"\n 5 - Right Side Pit\n 6 - Many Moves\n 7 - Keep on Own side\n 8 - Closest to Opponent: "))

    if eval_func == 1:
        eval_func = static_eval
    elif eval_func == 2:
        eval_func = simple_score
    elif eval_func == 3:
        eval_func = material_advantage
    elif eval_func == 4:
        eval_func = extra_turn
    elif eval_func == 5:
        eval_func = rightside_pit
    elif eval_func == 6:
        eval_func = many_moves
    elif eval_func == 7:
        eval_func = keep_on_own_side
    else:
        eval_func = closest_to_opponent
    

    players_zero = Human(0) if playerOne != 'm' else Machine(1, levelOne, eval_func=eval_func)
    players_one = Human(1) if playerTwo != 'm' else Machine(0, levelTwo, eval_func=eval_func)

    print("\nReady, Players!\n")
    print(f"{p_zero} vs {p_one}")
    play_game(players_zero, players_one, stealing_mode)


if __name__ == "__main__":
    main()
