from game import play_game
from players import Human, Machine


def main():
    print("\nWelcome to Mancala Project!\n")

    print("Which player do you want: Human(h) or Machine(m)")

    playerOne = input("Player 1: ").strip().lower()
    if playerOne == 'm':
        levelOne = int(input("Machine level (it should be a Number): "))

    playerTwo = input("Player 2: ").strip().lower()
    if playerTwo == 'm':
        levelTwo = int(input("Machine level (it should be a Number): "))

    stealing_mode = input("Turn on STEALING mode? (y/n) ").strip().lower() == 'y'

    p_zero = "Human" if playerOne != 'm' else "Machine"
    p_one = "Human" if playerTwo != 'm' else "Machine"

    players_zero = Human(0) if playerOne != 'm' else Machine(0, levelOne)
    players_one = Human(1) if playerTwo != 'm' else Machine(1, levelTwo)

    print("Ready, Players!\n")
    print(f"{p_zero} vs {p_one}")

    play_game(players_zero, players_one, stealing_mode)


if __name__ == "__main__":
    main()
