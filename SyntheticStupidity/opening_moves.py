"""
COMP30024 Artificial Intelligence, Semester 1 2019
Solution to Project Part B

This file contains opening move lists for each colour.
Centred tries to begin the game with centred pieces in a V.
Split tries to go round the sides in a split in a defensive opening
Wrap tries to focus all on going one way round the board and using
as many jumps as possible in the opening to get into play as quick as possible.
"""

CENTRED = {
	'red': [
		('MOVE', ((-3,0), (-2,0))),
		('MOVE', ((-3,3), (-2,2))),
		('MOVE', ((-3,1), (-2,1))),
		('JUMP', ((-3,2), (-1,0)))
	],
	'green': [
		('MOVE', ((0,-3), (0,-2))),
		('MOVE', ((3,-3), (2,-2))),
		('MOVE', ((1,-3), (1,-2))),
		('JUMP', ((2,-3), (0,-1))),
	],
	'blue': [
		('MOVE', ((3,0), (2,0))),
		('MOVE', ((0,3), (0,2))),
		('MOVE', ((1,2), (1,1))),
		('JUMP', ((2,1), (0,1))),
	],
}

SPLIT = {
	'red': [
		('MOVE', ((-3,0), (-2,1))),
		('MOVE', ((-3,3), (-2,3))),
		('MOVE', ((-3,1), (-3,0))),
		('MOVE', ((-3,2), (-3,3))),
	],
	'green': [
		('MOVE', ((0,-3), (-1,-2))),
		('MOVE', ((3,-3), (3,-2))),
		('MOVE', ((1,-3), (0,-3))),
		('MOVE', ((2,-3), (3,-3))),
	],
	'blue': [
		('MOVE', ((3,0), (3,-1))),
		('MOVE', ((0,3), (-1,3))),
		('MOVE', ((1,2), (0,3))),
		('MOVE', ((2,1), (3,0))),
	],
}

WRAP = {
	'red': [
		('MOVE', ((-3,0), (-2,0))),
		('JUMP', ((-3,1), (-1,-1))),
		('JUMP', ((-3,3), (-3,1))),
		('JUMP', ((-3,2), (-3,0))),
	],
	'green': [
		('MOVE', ((3,-3), (2,-2))),
		('JUMP', ((2,-3), (2,-1))),
		('JUMP', ((0,-3), (2,-3))),
		('JUMP', ((1,-3), (3,-3))),
	],
	'blue': [
		('MOVE', ((0,3), (0,2))),
		('JUMP', ((1,2), (-1,2))),
		('JUMP', ((3,0), (1,2))),
		('JUMP', ((2,1), (0,3))),
	],
}