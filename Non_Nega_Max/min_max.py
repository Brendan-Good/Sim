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
    
    for x in range(10000):
        print(x)
        winner = play_game()
        if winner == 1: 
            red_wins+=1
        elif winner == -1:
            blue_wins+=1
        else:
            ties +=1
        if x%10 ==0:
            print(x, " trials have been run")
            print("red wins = ", red_wins)
            print("blue wins = ", blue_wins)
            print("red wins ",red_wins/(red_wins+blue_wins)," of games")
    print("final red wins = ", red_wins)
    print("final blue wins = ", blue_wins)
    print("final red wins ",red_wins/(red_wins+blue_wins)," of games")



def play_game():
    global nodes_visited
    adj = [[0 for col in range(6)] for row in range(6)]
    abst = [6,0,0]
    tuples = is_terminal.generate_structure(6,3)
    scope = -1
    start_height = 15
    turn_num = 0
    game_over = False
    val = 0
    graph = {'tuples':tuples,'abst':abst,'adj':adj,'scope':scope,'start_height':start_height,'turn_num':turn_num,'game_over':False,'val':val}

    grand_nodes_visited = 0
    while not game_over:
        
        graph['turn_num']+=1
        graph =  random.choice(Expand.Expand(graph))
        #print("Random red move below")
        #display_graph(graph)
        if graph['turn_num']==15:
            graph['game_over'] = True

        game_over = graph['game_over']
        if not game_over:
            graph = max_manager(graph,start_height)
            #print("Random blue move below")
            #display_graph(graph)
        if graph['turn_num']==15:
            graph['game_over'] = True
        
        game_over = graph['game_over']
        #print("turn number is ", graph['turn_num'])
        #print(graph['game_over'])

    #display_graph(graph)
    #print("turn number = ",graph['turn_num'])
    #print("game over =  ",graph['game_over'])
    
    if graph['turn_num']%2 == 0:
        return -1
    elif graph['turn_num']%2 == 1:
        return 1
    else:
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
def max_manager(graph,start_height):
    '''contains the default values for max '''
    global nodes_visited
    nodes_visited +=1

    new_graph = "the unthinkable error"
    val = -1*inf
    for child in Expand.Expand(graph):
        child['turn_num']+=1
        if min_of(graph,-1*inf,inf,start_height)>= val:
            new_graph = child
    return new_graph

def min_manager(graph,start_height):
    '''contains the default values for max '''
    global nodes_visited
    nodes_visited +=1

    new_graph = "the unthinkable error"
    val = inf
    for child in Expand.Expand(graph):
        child['turn_num']+=1
        if max_of(graph,-1*inf,inf,start_height-1)<= val:
            new_graph = child
    return new_graph

def max_of(graph,alpha ="oh dear",beta="quite a problem" ,height = "we have" ):
    global nodes_visited
    nodes_visited +=1

    if graph['game_over']:
        return inf
    elif height <= 0:
        return 0

    m = alpha
    for child in Expand.Expand(graph):
        child['turn_num']+=1
        m = max(m,min_of(child,m,beta,height-1))
        if m >= beta:
            return m
    return m

def min_of(graph,alpha ,beta ,height):
    
    global nodes_visited
    nodes_visited +=1

    if graph['game_over']:
        return inf
    elif height <= 0:
        return 0

    m = beta
    for child in Expand.Expand(graph):
        child['turn_num']+=1
        m  = min(m,max_of(child,alpha,m,height-1))
        if m <= alpha:
            return m
    return m

def game_test():
    adj = [[0 for col in range(5)] for row in range(5)]
    abst = [5,0,0]
    tuples = is_terminal.generate_structure(5,3)
    scope = -1
    depth = 10
    turn_num = 1
    game_over = False
    graph = {'tuples':tuples,'abst':abst,'adj':adj,'scope':scope,'depth':depth,'turn_num':turn_num,'game_over':False}
     
    print("                       begin x")
    x = Expand.Expand(graph)
    display_graph(x[0])
    print('abst = ',x[0]['abst'])
    print("                       begin y's")
    x[0]['turn_num'] +=1
    y = Expand.Expand(x[0])
    for grap in y:
        display_graph(grap)
        print('abst = ',grap['abst'])
        print('scope = ',grap['scope'])
    y[0]['turn_num'] +=1
    z = Expand.Expand(y[0])

    print("                       begin z's")
    for grap in z:
        display_graph(grap)
        print('abst = ',grap['abst'])
        print('scope = ',grap['scope'])
    z[0]['turn_num'] +=1
    Q = Expand.Expand(z[0])

    print("                       begin Q's")
    for grap in Q:
        display_graph(grap)
        print('abst = ',grap['abst'])
        print('scope = ',grap['scope'])

    
    '''
    while not game_over:
        graph = max()[0]
        
        print(graph['abst']," abst ")
        display_graph(graph)
        print(graph['adj'])
        print(graph['game_over'], "game over")
        graph['turn_num']+=1
        game_over = graph['game_over']
        #if not game_over:
        #    vert1 = int(input('player turn:'))
        #    vert2 = int(input('player turn:'))
        #    graph['adj'][vert1][vert2]=-1
        #    graph['scope']+=2
        #    graph['abst'][0]-=2
        #    display_graph(graph)

    print("nodes visited = ", nodes_visited)
    '''

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
            if Expand.get_edge(graph,x,y):
                display+=" "
            display+=str(graph['adj'][x][y])
        print(display) 
        display = ""

def move_extractor(changed_graph,unchanged_graph):
    '''Takes in two BitArrays and returns the index of the first diget the BitArrays differ on. Used on a graph and that graph after a move has been made to find what that move was.'''
    and_graph = changed_graph ^ unchanged_graph

    location = (and_graph.bin).find('1')

    if location %  2 == 1:
        location += -1

    return location
