"""
COMP30024 Artificial Intelligence, Semester 1 2019
Solution to Project Part B

This file contains the State class which holds all infomation about
the current state of the game and can be used to derive possible subsequent
states.
"""

from SyntheticStupidity import const, hex

from itertools import chain
from copy import deepcopy
from collections import defaultdict

class State:
    def __init__(self, colour, board, exits, seen_dict):

        self.colour = colour

        # If no board is inputted then set board as starting board
        if not board:
            self.board = dict(const.STARTING_HEXES)
        else:
            self.board = board

        # If no exits are inputted then no exits have been made
        if not exits:
            self.exits = (0, 0, 0)
        else:
            self.exits = exits

        # If no seen_dict inputted must be initial state
        if not seen_dict:
            self.seen_dict = dict()
            self.seen_dict[self] = 1
        else:
            self.seen_dict = seen_dict

    def update(self, colour, action):
        """
        Given a colour and an action updates the state
        """

        action_type, action_loc = action

        if action_type == 'PASS':
            return

        if action_type == 'EXIT':
            self.board[colour].discard(action_loc)
            self.exits = tuple(self.exits[i] + (col == colour) \
                               for i, col in enumerate(const.COLOURS))
            return

        action_start, action_end = action_loc
        self.board[colour].discard(action_start)
        self.board[colour].add(action_end)
            
        if action_type == 'JUMP':
            taken_piece = (set(hex.neighbours(action_start)) & \
                           set(hex.neighbours(action_end))).pop()
            for col in const.COLOURS:
                self.board[col].discard(taken_piece)
                self.board[colour].add(taken_piece)

        # Update what states have been seen
        if self in self.seen_dict:
            self.seen_dict[self] += 1
        else:
            self.seen_dict[self] = 1

        return


    def subsequent_states(self):
        """
        Generates all the subsequent states that can be made by actions from
        this state in a list.
        """

        states = []
        for action in self.available_actions():
            new_state = State(self.colour, deepcopy(self.board), self.exits,
                              deepcopy(self.seen_dict))
            new_state.update(self.colour, action)
            new_state.colour = const.NEXT_COLOUR[self.colour]

            # If this state will cause the game to end avoid it
            if new_state in self.seen_dict.keys():
                if self.seen_dict[new_state] >= const.MAX_REPEAT_STATES-1:
                    continue
            else:
                states.append(new_state)
        return states

    def available_actions(self):
        """
        Retuns a list of all possible actions that can be made from this state,
        in the format required by the referee package.
        """

        actions = []

        # Iterate through all pieces of own colour
        for piece in self.board[self.colour]:

            # Add exits moves if possible
            if piece in const.FINISHING_HEXES[self.colour]:
                actions.append(('EXIT', piece))

            # Iterate through all neighbours on the board
            for neighbour, direction in zip(hex.neighbours(piece),
                                            const.DIRECTIONS):
                if neighbour in const.HEXES:

                    # If neighbour can be jumped over add jump move
                    if self._is_piece(neighbour):
                        leap_neighbour = hex.add(neighbour, direction)
                        if leap_neighbour in const.HEXES and \
                           not self._is_piece(leap_neighbour):
                           actions.append(('JUMP', (piece, leap_neighbour)))

                    # Otherwise add normal move
                    else:
                        actions.append(('MOVE', (piece, neighbour)))
        
        # If no moves add pass move
        if not actions:
            actions.append(('PASS', None))

        return actions

    def action_to_target_state(self, target_state):
        """
        Given a target sub state returns the action that leads to it
        """
        for action, state in zip(self.available_actions(),
                                 self.subsequent_states()):
            if state == target_state:
                return action

    def _is_piece(self, h):
        """
        Checks if the given location is a piece on the board.
        """
        for piece_set in self.board.values():
            if h in piece_set:
                return True
        return False

    def __eq__(self, other):
        return (self.colour == other.colour and self.board == other.board)

    def __hash__(self):
        hash_board = dict()
        for colour in const.COLOURS:
            hash_board[colour] = frozenset(self.board[colour])
        return hash(tuple(hash_board.items()))