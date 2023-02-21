# Mancala Game
This is a Python implementation of the popular board game Mancala.

## 📏 Rules of the Game
Mancala is a two-player strategy game that is played on a board with two rows of six holes, or pits, in each row. 
At the beginning of the game, four stones are placed in each of the twelve holes, for a total of 48 stones.

Each player controls the six holes on their side of the board, and their goal is to collect as many stones as possible
in their "mancala", which is the large pit to their right.

Players take turns moving the stones from one of their holes, dropping one stone in each hole they pass over, including
their own mancala, but not their opponent's. If the last stone dropped lands in the player's mancala,
they get to take another turn.

The game ends when one player has no more stones in their holes, at which point the other player gets to move any
remaining stones from their side into their mancala. The player with the most stones in their mancala at the end
of the game is the winner.

## 🎮 How to Play
To play the game, simply run the mancala.py script in your terminal or command prompt. The game will prompt you to enter
the number of the hole you want to move from, and it will show you the resulting board state after each move.

The game includes a simple AI opponent that makes random moves, so you can play against the computer if you don't have
a friend to play with.

## Dependencies
This implementation of Mancala requires Python 3 and uses the built-in random module for the AI opponent.

## 🗓️ Future Improvements
Possible future improvements to the game could include a more sophisticated AI opponent that uses a heuristic to make 
better moves, a graphical user interface using a library like Pygame, or the ability to play the game over a network with a friend.

🏗️ Contributions and suggestions for improvements are welcome!