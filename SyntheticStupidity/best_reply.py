"""
COMP30024 Artificial Intelligence, Semester 1 2019
Solution to Project Part B

UNUSED IN FINAL PROJECT

This file contains an implementation of best reply search.
"""

from SyntheticStupidity import score, const
from SyntheticStupidity.state import State
from SyntheticStupidity.score import evaluate

def best_reply_search(state, depth, alpha, beta, is_max):
	if not depth:
		return evaluate(state), None
	sub_states = []
	if is_max:
		sub_states = state.subsequent_states()
	else:
		# Iterate through oponents colours
		orig_colour = state.colour
		for colour in [c for c in const.COLOURS if c != orig_colour]:
			state.colour = colour
			sub_states += state.subsequent_states()
		state.colour = orig_colour
	best_state = None
	value = float('-inf')
	for sub_state in sub_states:
		value = max(value, -best_reply_search(sub_state, depth-1, -beta, -alpha, not is_max)[0])
		if value > alpha:
			alpha = value
			best_state = sub_state
			sub_state.colour = const.NEXT_COLOUR[state.colour]
		if alpha >= beta:
			break
	return value, best_state
