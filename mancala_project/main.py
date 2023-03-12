from game import play_game
from mancala_project.aiEngine import static_eval, simple_score, material_advantage
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
        eval_func = input("Choose evaluation function (1 for Static, 2 for Simple score, 3 for Material advantage): ")
        while eval_func.strip() != '1' and eval_func.strip() != '2' and eval_func.strip() != '3':
            eval_func = input("Invalid input. Please choose evaluation function (1 for Static, 2 for Simple score, "
                              "3 for Material advantage): ")
        eval_func = int(eval_func.strip())

    if eval_func == 1:
        eval_func = static_eval
    elif eval_func == 2:
        eval_func = simple_score
    else:
        eval_func = material_advantage

    players_zero = Human(0) if playerOne != 'm' else Machine(1, levelOne, eval_func=eval_func)
    players_one = Human(1) if playerTwo != 'm' else Machine(0, levelTwo, eval_func=eval_func)

    print("\nReady, Players!\n")
    print(f"{p_zero} vs {p_one}")
    play_game(players_zero, players_one, stealing_mode)


if __name__ == "__main__":
    main()
