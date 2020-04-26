"""
COMP30024 Artificial Intelligence, Semester 1 2019
Solution to Project Part B

This file contains a player who uses a list of opening moves then plays out
using maxn.
"""

from SyntheticStupidity.state import State
from SyntheticStupidity.maxn import maxn
from SyntheticStupidity import opening_moves

class Player:
    def __init__(self, colour):
        # Uses wrap initial position
        self.state = State(colour, None, None, None)
        self.opening_moves = opening_moves.WRAP[self.state.colour]

    def action(self):
        while self.opening_moves:
            return self.opening_moves.pop(0)

        depth = 3
        _, target_state = maxn(self.state, depth)
        return self.state.action_to_target_state(target_state)

    def update(self, colour, action):
        self.state.update(colour, action)