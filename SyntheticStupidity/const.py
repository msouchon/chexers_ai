"""
COMP30024 Artificial Intelligence, Semester 1 2019
Solution to Project Part B

This file contains constants used in other files in this project.
"""

COLOURS = ('red', 'green', 'blue')
COLOUR_INDEX = {
	'red': 0,
	'green': 1,
	'blue': 2,
}
NEXT_COLOUR = {'red': 'green',
               'green': 'blue',
               'blue': 'red',
}
STARTING_HEXES = {
    'red':   {(-3,3), (-3,2), (-3,1), (-3,0)},
    'green': {(0,-3), (1,-3), (2,-3), (3,-3)},
    'blue':  {(3, 0), (2, 1), (1, 2), (0, 3)},
}
FINISHING_HEXES = {
    'red':   {(3,-3), (3,-2), (3,-1), (3,0)},
    'green': {(-3,3), (-2,3), (-1,3), (0,3)},
    'blue':  {(-3,0),(-2,-1),(-1,-2),(0,-3)},
}

GOOD_HEXES = {
	(0,-3), (3,-3), (3,0), (0,3), (-3,3), (-3,0)
}

MAX_REPEAT_STATES = 4

DIRECTIONS = ((-1,+0),(+0,-1),(+1,-1),(+1,+0),(+0,+1),(-1,+1))

BOARD_RADIUS = 3

BOARD_RAN = range(-BOARD_RADIUS, +BOARD_RADIUS+1)
HEXES = {(q,r) for q in BOARD_RAN for r in BOARD_RAN if -q-r in BOARD_RAN}