"""
COMP30024 Artificial Intelligence, Semester 1 2019
Solution to Project Part B

This file contains functions to manipulate hex's.
Hex's are defined as tuples of length two.
"""

from SyntheticStupidity import const

# Hex Indexes
Q = 0
R = 1

def add(a, b):
	"""
    Returns the sum of two coordinates.
    """
	return (a[Q] + b[Q], a[R] + b[R])

def distance(a, b):
	"""
    Returns the distance between two coordinates.
    """
	return (abs(a[Q] - b[Q]) +
		    abs(a[Q] + a[R] - b[Q] - b[R]) +
		    abs(a[R] - b[R])) / 2

def neighbours(h):
	"""
	Returns all possible neighbours of a piece, ignoring board size.
	"""
	return [add(h, direction) for direction in const.DIRECTIONS]