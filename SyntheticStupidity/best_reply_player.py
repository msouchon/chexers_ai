"""
COMP30024 Artificial Intelligence, Semester 1 2019
Solution to Project Part B

UNUSED IN FINAL PROJECT

This file contains a player who chooses moves according to best reply search.
"""

from SyntheticStupidity.state import State
from SyntheticStupidity.best_reply import best_reply_search

class Player:
    def __init__(self, colour):
        self.state = State(colour, None, None, None)

    def action(self):
        depth = 3
        _, target_state = best_reply_search(self.state, depth, float('-inf'),
        									float('inf'), True)
        return self.state.action_to_target_state(target_state)

    def update(self, colour, action):
        self.state.update(colour, action)