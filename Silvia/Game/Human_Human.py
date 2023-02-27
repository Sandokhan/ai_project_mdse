import numpy as pd

class Mancala:
    def __init__(self):
        self.board = [[4]*6, [4]*6]
        self.stores = [0, 0]
        self.current_player = 0