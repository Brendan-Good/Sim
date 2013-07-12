#!/usr/bin/env python3

#Negamax implementation by Joshua Brule

import sys
import Expand
import SimMCTest

from collections import deque
from copy import deepcopy

N = 7
M = 8
MAX_DEPTH = 4

inf = float('inf')
    
def negamax(node, alpha, beta, player, depth = 15):
    '''Perform a depth limited negamax search using functions eval(), expand()
    and isTerminal() as appropriate
    
    Returns (optimal move, negamax value)
    
    Usage: negamax(new_board(), MAX_DEPTH, -inf, +inf, 1)'''
    

    if is_terminal(node):
        return (None, 1)
    elif depth == 0:
        return(None,0)
    
    else:
        candidate_move = None
        for move in Expand(node):
            val = -1 * negamax(move.reverse(0,len(move)), depth - 1, -beta, -alpha, -player)[1]
            if val >= beta:
                return (None, val)
            if val > alpha:
                candidate_move = move_extractor(move,node)
                alpha = val

        return (candidate_move, alpha)
# method by Tucker Bane
        
def move_extractor(changed_graph,unchanged_graph):
    '''Takes in two BitArrays and returns the index of the first diget the BitArrays differ on. Used on a graph and that graph after a move has been made to find what that move was.
    '''
    and_graph = changed_graph ^ unchanged_graph

    location = (and_graph.bin).find('1')

    if location %  2 == 1:
        location += -1

    return location
