import numpy as np
from mancalaEngine import PocketName

pinf = np.inf
ninf = - np.inf


def static_eval(game_state):
    """
       Evaluate the given game state and return a numeric value representing the expected outcome of the game.

       The returned value is positive if the current player is expected to win, negative if they are expected to lose,
       and zero if the game is expected to end in a tie.

       Args:
           game_state: A `GameState` object representing the current state of the game.

       Returns:
           A numeric value representing the expected outcome of the game.

       """
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


def simple_score(game_state):
    """
    Simple Score: An evaluation function that returns the difference between the current player's score
    and the opponent's score. This function encourages the current player to maximize their own score while
    minimizing their opponent's score.

    Args:
        game_state: A `GameState` object representing the current state of the game.

    Returns:
        The difference between the current player's score and the opponent's score, where the current
        player is determined by the `current_player_id` property of the `game_state` object. If the difference
        is positive, the current player is in the lead, and if it is negative, the current player is behind.
        If the difference is zero, the game is tied.
    """
    player_score = game_state.state[PocketName.p0_mancala]
    opponent_score = game_state.state[PocketName.p1_mancala]
    player = game_state.current_player_id
    if player == 1:
        player_score, opponent_score = opponent_score, player_score
    return player_score - opponent_score


def minimax(state, depth):
    """
        The minimax algorithm is a recursive algorithm used to find the optimal move in a two-player, zero-sum game.
        It explores the game tree by alternating between maximizing and minimizing the value of each node until it
        reaches a leaf node or a specified depth.

        Args:
            state: A `GameState` object representing the current state of the game.
            depth: An integer representing the maximum depth to explore the game tree.

        Returns:
            A tuple containing the best move and its corresponding value for the current player. If the current player is
            the maximizer, the best move is the move that leads to the maximum value, and if the current player is the
            minimizer, the best move is the move that leads to the minimum value. The value of the best move is returned
            as the second element of the tuple. If the game has ended or the maximum depth has been reached, the function
            returns None as the best move and the static evaluation of the current state as the value.
        """
    if depth <= 0 or state.is_terminal():
        return None, static_eval(state)

    if state.player_turn == 0:  # maximizer
        value = ninf
        best_move = None

        for move, child in state.children():
            _, child_value = minimax(child, depth - 1)
            if child_value > value:
                value = child_value
                best_move = move
        return best_move, value

    else:  # player 1: minimizer
        value = pinf
        best_move = None

        for move, child in state.children():
            _, child_value = minimax(child, depth - 1)
            if child_value < value:
                value = child_value
                best_move = move
        return best_move, value


def minimax_alpha_beta(state, depth, alpha=ninf, beta=pinf):
    """
    Perform minimax search with alpha-beta pruning to find the optimal move for the current player at a given state.
    Args:
    - state: the current game state
    - depth: the maximum search depth
    - alpha: the alpha value used for alpha-beta pruning, defaults to negative infinity
    - beta: the beta value used for alpha-beta pruning, defaults to positive infinity

    Returns:
    - best_move: the optimal move for the current player
    - value: the value of the best move found by the search algorithm
    """

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
