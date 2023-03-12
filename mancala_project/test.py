from aiEngine import Machine, material_advantage
from gameEngine import GameState, Human

state = GameState()
p1 = Human(1)
p2 = Machine(0, 2, 3)
players = [p1, p2]

while not state.is_terminal():
    state.show()
    player = players[state.player_turn]
    state = player.move(state)

state.show()
state.show_winning_message()