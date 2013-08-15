#!/usr/bin/env python3

from bitstring import BitArray
import sys
import Expand
import is_terminal
from collections import deque
import copy
import random

inf = float('inf')
nodes_visited = 0
glob_turn_num = 1

def make_statistic():
   '''plays many games and reports the statistics of who wins. '''
    red_wins = 0
    blue_wins = 0
    ties = 0
    winner = play_game()
    if winner == 1: 
        red_wins+=1
    elif winner == -1:
        blue_wins+=1
    else:
        ties +=1    

    for x in range(100):
        print("final red wins = ", red_wins)
        print("final blue wins = ", blue_wins)
        print("final red wins ",red_wins/(red_wins+blue_wins)," of games")
        winner = play_game()
        if winner == 1: 
            red_wins+=1
        elif winner == -1:
            blue_wins+=1
        else:
            ties +=1
        
    print("final red wins = ", red_wins)
    print("final blue wins = ", blue_wins)
    print("final red wins ",red_wins/(red_wins+blue_wins)," of games")

def initialize_graph():
    ''' sets all the recomended starting values for a graph.'''
    n = 5
    l = 3
    abst = [n,0,0]
    tuples = is_terminal.generate_structure(n,l)
    scope = -1
    turn_number = 1
    game_over = False
    val = 0
    depth_limit = 23
    graph_rep = (n*(n-1))*BitArray(bin='0')
    red_edges = []
    blue_edges = []
    blank_edges = []

    for x in range(n-1):
        for y in range(x+1,n):
            blank_edges.append([x,y])



    graph = {'tuples':tuples,'abst':abst,'scope':scope,'turn_number':turn_number,'game_over':False,'val':val,'depth_limit':depth_limit,'graph_rep':graph_rep,'red_edges':red_edges,'blue_edges':blue_edges,'blank_edges':blank_edges}

    return graph,n

def play_game():
    '''plays a game. Global (glob) turn number and the differance between it and the current turn number is used to find tree depth.'''
    graph,n = initialize_graph()

    #double checks global values.
    global nodes_visited
    nodes_visited = 0
    global glob_turn_num
    glob_turn_num = graph['turn_number']
    #can initialize the board randomly to produce non-identical games between perfect/consistant players.
    #graph = random.choice(Expand.Expand(graph))
    #graph = random.choice(Expand.Expand(graph))
    #graph = random.choice(Expand.Expand(graph))
    #graph = random.choice(Expand.Expand(graph))

    game_over = graph['game_over']
    while not game_over:
        
        #handy testing code
        print("turn number going in is ", graph['turn_number'])
        print("global turn number going in is ", glob_turn_num)
        #sets depth of search for the next player.
        graph['depth_limit'] = 23
        # makes a move.
        graph = max_manager(graph)
        glob_turn_num = graph['turn_number']
        # pretty prints the graph.
        display_graph_b(graph,n)
        print("nodes visited = ", nodes_visited)
        nodes_visited = 0
        # red just went, so if game_over red won, return 1 (the number of red)
        if graph['game_over']:
            return 1
        #checks for a tie
        elif graph['turn_number']==(n*(n-1)/2)+1:
            print("Tie?")
            return 0

        game_over = graph['game_over']
        if not game_over:
            print("turn number going in is ", graph['turn_number'])
            print("global turn number going in is ", glob_turn_num)
            # here incase it's needed.
            graph['depth_limit'] = 23
            #plays random
            graph = random.choice(Expand.Expand(graph))
            glob_turn_num = graph['turn_number'] 
            #pretty print
            display_graph_b(graph,n)
        if graph['game_over']:
            return -1
        elif graph['turn_number']==(n*(n-1)/2)+1:
            #having ties happen can be a very bad sign for some board sizes.
            print("TIE!?!?!?!")
            return 0
        
        game_over = graph['game_over']
 

    print("turn number = ",graph['turn_number'])
    print("game over =  ",graph['game_over'])
    display_graph_b(graph,n)
    
   
def max_manager(graph):
    '''basically just here so that the first level of min_max can return a graph
    instead of a number'''

    global inf

    # This is totally what min_max is. Look it up.
    new_graph = "the unthinkable error"
    val = -1*inf
    for child in Expand.Expand(graph):
        if child['game_over']:
            return child
        m =  min_of(child,-1*inf,inf)
        if m  >= val:
            new_graph = child
            val = m
    print("Best val is ", new_graph['val'])
    print("Nodes visited  ", nodes_visited)
    return new_graph

def min_manager(graph):
    '''??? non funtional ??? '''

    global inf

    new_graph = "the unthinkable error"
    val = inf
    for child in Expand.Expand(graph):
        #short circuits wining moves.
        if child['game_over']:
            return child
        m =  max_of(child,-1*inf,inf)
        if m <= val:
            new_graph = child
            val = m
    return new_graph

def max_of(graph,alpha ="oh dear",beta="quite a problem"):
    global nodes_visited
    nodes_visited +=1
    global inf
    global glob_turn_num
    global depth_limit
    
    m = alpha
    for child in Expand.Expand(graph):
        if child['game_over']:
            return inf
        elif (child['turn_number']-glob_turn_num)>graph['depth_limit']:
            m = child['val']
        else:
            m = max(m,min_of(child,m,beta))
        if m >= beta:
            return m
    return m

def min_of(graph,alpha,beta):
        
    global nodes_visited
    nodes_visited +=1
    global inf
    global glob_turn_num
    global depth_limit

    m = beta
    for child in Expand.Expand(graph):
        if child['game_over']:
            return -1*inf
        elif (child['turn_number']-glob_turn_num)>graph['depth_limit']:
            m = child['val']
        else:
            m  = min(m,max_of(child,alpha,m))
        if m <= alpha:
            return m
    return m

def display_graph(graph):
    display = ""
    dis = "   "
    
    for x in range(len(graph['adj'])):
        dis += str(x)
        if x <10:
            dis += " "
    print(dis)
    print(" ")
    for x in range(len(graph['adj'])):
        display+=str(x)
        if x <10:
            display+=" "
        for y in range(len(graph['adj'][x])):
            if graph['adj'][x][y] != -1:
                display+=" "
            display+=str(graph['adj'][x][y])
        print(display) 
        display = ""

    print('abst = ',graph['abst'],'scope = ', graph['scope'])

def get_edge(graph,m,n,Graph_Size):
    edge_bit1 = graph['graph_rep'][2*m*Graph_Size-(m*(m+1))+2*n-2*m-2]
    edge_bit2 = graph['graph_rep'][2*m*Graph_Size-(m*(m+1))+2*n-2*m-1]
    return [edge_bit1,edge_bit2]

def display_graph_b(graph,Graph_Size):
    display = ""
    disp = "   "
    
    for x in range(0,Graph_Size):
        disp += str(x)
        disp += " "
    print(disp)
    print(" ")
    for x in range(0,Graph_Size):
        display+=str(x)
        display+=" "
        for y in range(0,Graph_Size):
            if y > x:
                if get_edge(graph,x,y,Graph_Size) == [False,True]:
                    display+="-1"
                elif get_edge(graph,x,y,Graph_Size) == [True,False]:
                    display+=" 1"
                else:
                    display+=" 0"
            else:
                display+=" 0"
        print(display) 
        display = ""
    print('abst = ',graph['abst'],'scope = ', graph['scope'])
