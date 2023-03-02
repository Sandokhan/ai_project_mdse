import numpy as np
from mancalaEngine import PocketName

pinf = np.inf
ninf = - np.inf


def static_eval(game_state):
    if game_state.is_terminal():
        if game_state.state[PocketName.p0_mancala] > game_state.state[PocketName.p1_mancala]:
            value = 100
        elif game_state.state[PocketName.p0_mancala] == game_state.state[PocketName.p1_mancala]:
            value = 0
        else:
            value = -100
    else:
        value = game_state.state[PocketName.p0_mancala] - game_state.state[PocketName.p1_mancala]
    return value


def minimax(state, depth, maximizing_player):
    if depth <= 0 or state.is_terminal():
        return None, static_eval(state)
    if maximizing_player:
    # maximizer
        value = ninf
        best_move = None

    for move, child in state.children():
        _, child_value = minimax(child, depth - 1, False)
        if child_value > value:
            value = child_value
            best_move = move
            return best_move, value
    else:
    # minimizer
        value = pinf
        best_move = None
        for move, child in state.children():
            _, child_value = minimax(child, depth - 1, True)
            if child_value < value:
                value = child_value
                best_move = move
        return best_move, value


def minimax_alpha_beta(state, depth, alpha=ninf, beta=pinf):
    if depth == 0 or state.is_terminal():
        return None, static_eval(state)

    if state.player_turn == 0:  # maximizer
        value = ninf
        best_move = None

        for move, child in state.children():
            _, child_value = minimax_alpha_beta(child, depth - 1, alpha, beta)
            if child_value > value:
                value = child_value
                best_move = move
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_move, value

    else:  # player 1: minimizer
        value = pinf
        best_move = None

        for move, child in state.children():
            _, child_value = minimax_alpha_beta(child, depth - 1, alpha, beta)
            if child_value < value:
                value = child_value
                best_move = move
            beta = min(beta, value)
            if beta <= alpha:
                break
        return best_move, value
