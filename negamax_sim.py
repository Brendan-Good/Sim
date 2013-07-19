#!/usr/bin/env python3

#Negamax implementation by Joshua Brule

import sys
import Adj_Maxtix_Expand
import is_terminal

from collections import deque
from copy import deepcopy

N = 7
M = 8
MAX_DEPTH = 15

inf = float('inf')

def play_game()
    adj = [[0 for col in range(6)] for row in range(6)]
    abst = [6,0,0]
    tuples = is_terminal.generate_structure(6,3)
    scope = -1
    depth = 1
    graph = {'adj':adj,'abst':abst,'tuples':tuples,'scope':scope,'depth':depth}
    
    game_over = False

    while (!game_over):
        move = negamax(graph,-inf,+inf,1,15)

        game_over = is_terminal.is_terminal(graph['tuples'],edge)

    


def negamax(node, alpha, beta, player, depth):
    '''Perform a depth limited negamax search using functions eval(), expand()
    and isTerminal() as appropriate
    
    Returns (optimal move, negamax value)
    
    Usage: negamax(new_board(), -inf, +inf, 1, MAX_DEPTH)'''
    

    if is_termial.is_terminal(node):
        return (None, +inf)
    elif depth == 0:
        return(None,0)

    else:
        candidate_move = None
        for move in Adj_Maxtox.Expand.Expand(node):
            val = -1 * negamax(move.reverse(0,len(move)), depth - 1, -beta, -alpha, -player)[1]
            if val >= beta:
                return (None, val)
            if val > alpha:
                candidate_move = move
                alpha = val


        return (candidate_move, alpha)
# method by Tucker Bane
        
def move_extractor(changed_graph,unchanged_graph):
    '''Takes in two BitArrays and returns the index of the first diget the BitArrays differ on. Used on a graph and that graph after a move has been made to find what that move was.'''
    and_graph = changed_graph ^ unchanged_graph

    location = (and_graph.bin).find('1')

    if location %  2 == 1:
        location += -1

    return location
