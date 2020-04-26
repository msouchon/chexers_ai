"""
COMP30024 Artificial Intelligence, Semester 1 2019
Solution to Project Part B

UNUSED IN FINAL PROJECT

This file contains a player who chooses moves greedily.
"""

from SyntheticStupidity.state import State
from SyntheticStupidity.score import evaluate
from SyntheticStupidity import const

import random

class Player:
    def __init__(self, colour):
        self.state = State(colour, None, None, None)

    def action(self):
        best_score = float('-inf')
        for sub_state in self.state.subsequent_states():
            sub_state.colour = self.state.colour
            if evaluate(sub_state) > best_score:
                best_score = evaluate(sub_state)
                target_state = sub_state
        target_state.colour = const.NEXT_COLOUR[self.state.colour]
        return self.state.action_to_target_state(target_state)

    def update(self, colour, action):
        self.state.update(colour, action)