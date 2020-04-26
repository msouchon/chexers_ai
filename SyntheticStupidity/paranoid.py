"""
COMP30024 Artificial Intelligence, Semester 1 2019
Solution to Project Part B

UNUSED IN FINAL PROJECT

This file contains an implementation of minimax with alpha-beta pruning
for a paranoid implementation of the game.
"""

from SyntheticStupidity import score, const
from SyntheticStupidity.state import State
from SyntheticStupidity.score import evaluate

def paranoid(state, depth, alpha, beta, max_colour):
    if not depth:
        return evaluate(state), None
    best_state = None
    if max_colour:
        value = float('-inf')

        for sub_state in state.subsequent_states():
            
            value = max(value, paranoid(sub_state, depth-1, alpha, beta, max_colour)[0])
            if value > alpha:
                alpha = value
                best_state = sub_state
            if alpha >= beta:
                break
        
    else:
        value = float('inf')

        for sub_state in state.subsequent_states():
            value = min(value, paranoid(sub_state, depth-1, alpha, beta, max_colour)[0])
            if value < beta:
                beta = value
                best_state = sub_state
            if alpha >= beta:
                break

    return value, best_state