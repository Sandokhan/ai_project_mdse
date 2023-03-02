from game import play_game
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
                levelOne = int(input("Machine level (it should be a Number): "))
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
                levelTwo = int(input("Machine level (it should be a Number): "))
                break
            except ValueError:
                print("Error: Invalid input. Please enter a valid level.")

    stealing_mode = input("Turn on STEALING mode? (y/n) ").strip().lower() 
    while stealing_mode.strip().lower() != 'y' and stealing_mode.strip().lower() != 'n':
        stealing_mode = input("Turn on STEALING mode? (y/n) ").strip().lower()

    p_zero = "Human" if playerOne != 'm' else "Machine"
    p_one = "Human" if playerTwo != 'm' else "Machine"

    players_zero = Human(0) if playerOne != 'm' else Machine(1, levelOne)
    players_one = Human(1) if playerTwo != 'm' else Machine(0, levelTwo)

    print("\nReady, Players!\n")
    print(f"{p_zero} vs {p_one}")

    play_game(players_zero, players_one, stealing_mode)


if __name__ == "__main__":
    main()
