"""
COMP30024 Artificial Intelligence, Semester 1 2019
Solution to Project Part B

This file contains a scorer for a state based on inputted weights.
"""


from SyntheticStupidity import const, hex
from SyntheticStupidity.state import State


def basic_score(state, piece_factor=1.5, exit_factor=2, exit_dist_factor=0.01):
    """
    A basic score which includes number of pieces, number of exits
    and distance to exits
    """
    
    piece_score = 0
    for colour in const.COLOURS:
        if colour == state.colour:
            piece_score += len(state.board[colour])
        else:
            piece_score -= len(state.board[colour])

    exit_score = 0
    for colour_index, colour in enumerate(const.COLOURS):
        if colour == state.colour:
            exit_score += state.exits[colour_index]
        else:
            exit_score -= state.exits[colour_index]

    exit_dist_score = 0
    for piece in state.board[state.colour]:
        exit_dist_score -= min(hex.distance(piece, exit) for exit
                               in const.FINISHING_HEXES[state.colour])

    score = (
        piece_score * piece_factor +
        exit_score * exit_factor +
        exit_dist_score * exit_dist_factor
        )

    if exit_score > 4:
        score = float('inf')
        
    return score

def good_position_score(state, factor=0.01):
    """
    A good position score is defined as being in a corner hex, this
    is due to the fact that they cannot be taken in that location.
    """
    score = 0
    for colour in const.COLOURS:
        for piece in state.board[colour]:
            if piece in const.GOOD_HEXES:
                if colour == state.colour:
                    score += 1
    return score * factor

def block_exit_score(state, factor=0.01):
    """
    If a piece is blocking an exit of an opponent.
    """
    score = 0
    for colour in [c for c in const.COLOURS if c != state.colour]:
        for piece in state.board[state.colour]:
            if piece in const.FINISHING_HEXES[colour]:
                orig_colour = state.colour
                state.colour = colour
                score += 1
                state.colour = orig_colour
    return score * factor

def evaluate(state):
    return basic_score(state) + good_position_score(state) + block_exit_score(state)