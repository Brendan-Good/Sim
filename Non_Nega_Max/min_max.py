#!/usr/bin/env python3

import sys
import Expand
import is_terminal
from collections import deque
import copy
import random

nodes_visited = 0
inf = float('inf')


def make_statistic():
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

    for x in range(10000):
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



def play_game():
    global nodes_visited
    adj = [[0 for col in range(6)] for row in range(6)]
    abst = [6,0,0]
    tuples = is_terminal.generate_structure(6,3)
    scope = -1
    turn_number = 1
    game_over = False
    val = 0
    graph = {'tuples':tuples,'abst':abst,'adj':adj,'scope':scope,'turn_number':turn_number,'game_over':False,'val':val}

    grand_nodes_visited = 0
    while not game_over:
        
        print("turn number going in is ", graph['turn_number']) 
        graph = max_manager(graph)
        print("Smart? red move below")
        display_graph(graph)
        global nodes_visited
        print("nodes visited = ", nodes_visited)
        if graph['game_over']:
            return 1
        elif graph['turn_number']==16:
            print("that graph was a red win, right?")
            return 1

        game_over = graph['game_over']
        if not game_over:
            print("turn number going in is ", graph['turn_number'])
            graph = random.choice(Expand.Expand(graph))           
            print("Random blue move below")
            display_graph(graph)
        if graph['game_over']:
            return -1
        elif graph['turn_number']>=16:
            print("turn number is not working")
            return "turn number is not working"
        
        game_over = graph['game_over']
        #print("turn number is ", graph['turn_num'])
        #print(graph['game_over'])

    print("turn number = ",graph['turn_number'])
    print("game over =  ",graph['game_over'])
    display_graph(graph)
    
    if graph['turn_number']%2 == 0:
        print("error?")
        return 1
    elif graph['turn_number']%2 == 1:
        print("error?")
        return 2
    else:
        print("error?")
        return 0  
    '''
        if not game_over:
            graph = max_manager(graph,start_height)
            display_graph(graph)
            print("nodes visted = ", nodes_visited)
            grand_nodes_visited += nodes_visited
            nodes_visited = 0  

    print("grand total nodes = ", grand_nodes_visited)
    '''
def max_manager(graph):
    '''??? '''
    global nodes_visited
    nodes_visited +=1
    global inf

    new_graph = "the unthinkable error"
    val = -1*inf
    for child in Expand.Expand(graph):
        if child['game_over']:
            return child
        m =  min_of(child,-1*inf,inf)
        if m  >= val:
            new_graph = child
            val = m
    return new_graph

def min_manager(graph):
    '''??? non funtional ??? '''
    global nodes_visited
    nodes_visited +=1
    global inf

    new_graph = "the unthinkable error"
    val = inf
    for child in Expand.Expand(graph):
        if child['game_over']:
            return -1*inf
        elif max_of(child,-1*inf,inf)<= val:
            new_graph = child
    return new_graph

def max_of(graph,alpha ="oh dear",beta="quite a problem"):
    global nodes_visited
    nodes_visited +=1
    global inf
    
    m = alpha
    for child in Expand.Expand(graph):
        if child['game_over']:
            return inf
        m = max(m,min_of(child,m,beta))
        if m >= beta:
            return m
    return m

def min_of(graph,alpha,beta):
        
    global nodes_visited
    nodes_visited +=1
    global inf

    m = beta
    for child in Expand.Expand(graph):
        if child['game_over']:
            return -1*inf
        m  = min(m,max_of(child,alpha,m))
        if m <= alpha:
            return m
    return m

def game_test():
    adj = [[0 for col in range(4)] for row in range(4)]
    abst = [4,0,0]
    tuples = is_terminal.generate_structure(4,3)
    scope = -1
    depth = 10
    turn_number = 1
    game_over = False
    graph = {'tuples':tuples,'abst':abst,'adj':adj,'scope':scope,'depth':depth,'turn_number':turn_number,'game_over':False}
    
    print("original graph = ",)
    display_graph(graph)
 
    print("                       begin x")
    x = Expand.Expand(graph)
    display_graph(x[0])
    print('abst = ',x[0]['abst'])
    print("                       begin y's")

    y = Expand.Expand(x[0])
    for grap in y:
        display_graph(grap)
        print('abst = ',grap['abst'])
        print('scope = ',grap['scope'])

    z = Expand.Expand(y[0])

    print("                       begin z's")
    for grap in z:
        display_graph(grap)
        print('abst = ',grap['abst'])
        print('scope = ',grap['scope'])
    Q = Expand.Expand(z[0])

    display_graph(z[0])

    print("                       begin Q's")
    for grap in Q:
        display_graph(grap)
        print('abst = ',grap['abst'])
        print('scope = ',grap['scope'])

    print("original graph = ")
    display_graph(graph)
    

def test_is_terminal():
    ter = is_terminal
    tuples = ter.generate_structure(6,3)
    re1 = ter.is_terminal(tuples,[0,2],1)
    re2 = ter.is_terminal(tuples,[0,3],1)
    re3 = ter.is_terminal(tuples,[0,5],1)
    re4 = ter.is_terminal(tuples,[1,2],1)
    re5 = ter.is_terminal(tuples,[1,3],1)
    re6 = ter.is_terminal(tuples,[3,4],1)
 
    bu1 = ter.is_terminal(tuples,[0,1],2)
    bu2 = ter.is_terminal(tuples,[1,4],2)
    bu3 = ter.is_terminal(tuples,[2,3],2)
    bu4 = ter.is_terminal(tuples,[2,4],2)
    bu5 = ter.is_terminal(tuples,[3,5],2)
    bu6 = ter.is_terminal(tuples,[4,5],2)
   
    return [re1,re2,re3,re4,re5,re6,bu1,bu2,bu3,bu4,bu5,bu6]

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

def move_extractor(changed_graph,unchanged_graph):
    '''Takes in two BitArrays and returns the index of the first diget the BitArrays differ on. Used on a graph and that graph after a move has been made to find what that move was.'''
    and_graph = changed_graph ^ unchanged_graph

    location = (and_graph.bin).find('1')

    if location %  2 == 1:
        location += -1

    return location
