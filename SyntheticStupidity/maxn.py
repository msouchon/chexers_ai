"""
COMP30024 Artificial Intelligence, Semester 1 2019
Solution to Project Part B

This file contains an implementation of maxn, using a State object to choose
the best subsequent state. Based off the implementation in the lecture slides.
"""


from SyntheticStupidity import score, const
from SyntheticStupidity.state import State
from SyntheticStupidity.score import evaluate

def maxn(state, depth):
    if not depth:
        return (_evaluate_v(state), None)
    v_max = tuple(float('-inf') for _ in const.COLOURS)
    best_state = None

    for sub_state in state.subsequent_states():
        v, _ = maxn(sub_state, depth-1)
        if v[const.COLOUR_INDEX[state.colour]] > \
           v_max[const.COLOUR_INDEX[state.colour]]:
            v_max = v
            best_state = sub_state

    return v_max, best_state

def _evaluate_v(state):
    orig_colour = state.colour
    v = tuple()
    for colour in const.COLOURS:
        state.colour = colour
        v += (evaluate(state),)
    state.colour = orig_colour
    return v