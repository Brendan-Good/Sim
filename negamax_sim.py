#!/usr/bin/env python3

#Negamax implementation by Joshua Brule

import sys
import Adj_Maxtix_Expand
import is_terminal
import Nega

from collections import deque
import copy

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

def display_graph(graph):
    display = ""
    dis = "   "
    
    for x in range(len(graph['adj'])):
        dis += str(x)
        dis += " "
    print(dis)
    print(" ")
    for x in range(len(graph['adj'])):
        display+=str(x)
        display+=" "
        for y in range(len(graph['adj'][x])):
            if graph['adj'][x][y] != -1:
                display+=" "
            display+=str(graph['adj'][x][y])
        print(display) 
        display = ""

def display_graph_b(graph,size):
    display = ""
    dis = "   "
    
    for x in range(0,size):
        dis += str(x)
        dis += " "
    print(dis)
    print(" ")
    for x in range(0,size):
        display+=str(x)
        display+=" "
        for y in range(0,size):
            if Adj_Maxtix_Expand.get_edge(graph,x,y):
                display+=" "
            display+=str(graph['adj'][x][y])
        print(display) 
        display = ""



def play_game():
    adj = [[0 for col in range(5)] for row in range(5)]
    abst = [5,0,0]
    tuples = is_terminal.generate_structure(5,3)
    scope = -1
    depth = 15
    turn_number = 1
    game_over = False
    graph = {'tuples':tuples,'abst':abst,'adj':adj,'scope':scope,'depth':depth,'turn_number':turn_number,'game_over':False}

    while not game_over:
        graph = negamax(graph,-1 * inf, inf ,1,15)[0]
        print(graph['abst']," abst ")
        graph['adj'][1][2]=-1
        display_graph(graph)
        print(graph['adj'])
        print(graph['game_over'], "game over")
        
        game_over = graph['game_over']
        if not game_over:
            vert1 = int(input('player turn:'))
            vert2 = int(input('player turn:'))
            graph['adj'][vert1][vert2]=-1
            graph['scope']+=2
            graph['abst'][0]-=2
            display_graph(graph)

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
            new_move = copy.deepcopy(move)
            new_move['turn_number']+=1
            Nega.Nega(new_move)   
            val = -1 * negamax(new_move, -1 * alpha, -1 * beta, -1 * player, depth - 1 )[1]
            
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


