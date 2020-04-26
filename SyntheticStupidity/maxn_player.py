"""
COMP30024 Artificial Intelligence, Semester 1 2019
Solution to Project Part B

UNUSED IN FINAL PROJECT

This file contains a player who chooses moves according to maxn.
"""

from SyntheticStupidity.state import State
from SyntheticStupidity.maxn import maxn

class Player:
    def __init__(self, colour):
        self.state = State(colour, None, None, None)

    def action(self):
        depth = 3
        _, target_state = maxn(self.state, depth)

        return self.state.action_to_target_state(target_state)

    def update(self, colour, action):
        self.state.update(colour, action)