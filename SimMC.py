#!/usr/bin/python3

from bitstring import BitArray 
import sys 
import random

Graph_Size = int(sys.argv[1])

Graph_Rep = (Graph_Size*(Graph_Size-1))*BitArray([0])#Create a bitarray which represents a complete graph of size Graph_Size where 
#each edge is uncolored

max_iterations = 10000

class node:
    def __init__(self,parent,children,runs,wins,value):
        self.self = self
        self.parent = parent
        self.children = children
        self.runs = runs
        self.wins = wins
        self.value = value
        
def color_red(Edge,Graph_Rep):
    ''' Given an edge represented as a list, the function sorts it and changes the bit corresponding to that edge 10 which 
    will be our convention for saying an edge is red.  ''' 
    Edge = sorted(Edge)
    m = Edge[0]
    n = Edge[1]
    Graph_Rep[2*m*Graph_Size-(m*(m+1))+2*n-2*m-1] = False
    Graph_Rep[2*m*Graph_Size-(m*(m+1))+2*n-2*m-2] = True
    return Graph_Rep
    
def color_blue(Edge,Graph_Rep):
    ''' Given an edge represented as a list, the function sorts it and changes the bit corresponding to that edge 01 which 
    will be our convention for saying an edge is blue.  ''' 

    Edge = sorted(Edge)
    m = Edge[0]
    n = Edge[1]
    Graph_Rep[2*m*Graph_Size-(m*(m+1))+2*n-2*m-2] = False
    Graph_Rep[2*m*Graph_Size-(m*(m+1))+2*n-2*m-1] = True
    return Graph_Rep

def check_win(Graph,Recent_Edge,Color,turn):
    ''' this takes in the most recent edge colored and the graph representation and checks to see if the colored graph now makes 
    a k_n '''
             
    '''Expands node for player'''
    moves = []
    
    for i in range(0, N):
        new_node = deepcopy(node)
        for j in range(0, M):
            if new_node[i][j] == 0:
                new_node[i][j] = player
                moves.append(new_node)
                break
            
    return moves
    
def is_terminal(Color,Edges_to_Check,turn_number,past_iterations,win_subgraph):
    if(turn_number==(n*(n-1))/2):
        return true
    colored_list = [];
    for edges in Edges_to_Check:
        if(color(Edges)==Color):
            colored_list.append(Edges)
    if(len.colored_list<win_subgraph-past_iterations-1):
        return false
    else:
        past_iterations += 1
        if(past_iterations==win_subgraph):
            return true
        else:
            isterminal(Color,colored_list,turn_number+1,past_iterations,win_subgraph)
            
def eval(node):
    '''Returns the static evaluation of node
    
    This is a very naive implementation that assigns every square a value
    based on its surrounding (up, left, diag up, diag down) squares
    '''
    val = 0
    for i in range(0, N):
        for j in range(0, M):
            val += point_val(node, i, j)
    
    return val


#The following two lines are to see if the code works as expected.
color_blue([0,1],Graph_Rep)
print(Graph_Rep.bin)
       

