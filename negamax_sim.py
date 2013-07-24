#!/usr/bin/env python3

#Negamax implementation by Joshua Brule

import sys
import Adj_Maxtix_Expand
import is_terminal
import Nega

from collections import deque
from copy import deepcopy

MAX_DEPTH = 15
nodes_visited = 0

inf = float('inf')
def test_is_terminal():
    ter = is_terminal
    tuples = ter.generate_structure(6,3)
    re1 = ter.is_terminal(tuples,[0,1],1)
    re2 = ter.is_terminal(tuples,[0,2],1)
    re3 = ter.is_terminal(tuples,[1,2],1)
    qa1 = ter.is_terminal(tuples,[3,4],2)
    qa2 = ter.is_terminal(tuples,[3,5],2)
    qa3 = ter.is_terminal(tuples,[1,2],2)
    return [re1,re2,re3,qa1,qa2,qa3]

def play_game():
    adj = [[0 for col in range(6)] for row in range(6)]
    abst = [6,0,0]
    tuples = is_terminal.generate_structure(6,3)
    scope = -1
    depth = 15
    turn_number = 1
    game_over = False
    graph = {'tuples':tuples,'abst':abst,'adj':adj,'scope':scope,'depth':depth,'turn_number':turn_number,'game_over':False}

    while not game_over:
        graph = negamax(graph,-1 * inf, inf ,1,15)[0]
        print(graph['abst']," abst ")
        print(graph['adj']," adj ") 
        #print(graph['scope']," scope ")
        print(graph['turn_number']," turn_number ")
        #print(graph['tuples']," tuples ",)
        Nega.Nega(graph)
        game_over = graph['game_over']
    print("nodes visited = ", nodes_visited)


def negamax(node, alpha, beta, player, depth):
    '''Perform a depth limited negamax search using functions eval(), expand()
    and isTerminal() as appropriate
    
    Returns (optimal move, negamax value)
    
    Usage: negamax(new_board(), -inf, +inf, 1, MAX_DEPTH)'''
  
    global nodes_visited
    nodes_visited +=1
    print(" nodes visited = ", nodes_visited)    

    game_over = node['game_over']

    if game_over:
        return (node, -inf)
    elif depth == 0:
        return(node,0)
    else:
        candidate_move = None
        for move in Adj_Maxtix_Expand.Expand(node):
            Nega.Nega(move)
            val = -1 * negamax(move, -1 * alpha, -1 * beta, -1 * player, depth - 1 )[1]
            Nega.Nega(move)
            if val >= beta:
                return (move, val)
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
