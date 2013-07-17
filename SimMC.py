#!/usr/bin/python3

from bitstring import BitArray 
import sys 
import random
import math

Graph_Size = int(sys.argv[1]) 

win_subgraph = int(sys.argv[2])

Graph_Rep = (Graph_Size*(Graph_Size-1))*BitArray(bin='0')#Create a bitarray which represents a complete graph of size Graph_Size where 
#each edge is uncolored

red_edges = []
blue_edges = []

max_iterations = 10000

def monte_carlo():



def update_statistics(node,value,depth):
    
    while depth > 0:

def play_random(node,player_turn,):
    original_node=node
    while(!is_terminal(Edges_to_Check,turn_number)):
        expand(node)
        node = random.choice(node.children)
        player_turn+=1
    if(player_turn%2==1):
        original_node.wins+=1

class node:
    def __init__(self,parent,children,runs,wins,value,board):
        self.self = self
        self.parent = parent
        self.children = children
        self.runs = runs
        self.wins = wins
        self.value = value
        self.board = board
        
def color_red(edge,graph_rep):
    '''Given an edge represented as a list, the function sorts it and changes the bit corresponding to that edge 10 which 
    will be our convention for saying an edge is red.''' 
    edge = sorted(edge)
    m = edge[0]
    n = edge[1]
    graph_rep[2*m*Graph_Size-(m*(m+1))+2*n-2*m-1] = False
    graph_rep[2*m*Graph_Size-(m*(m+1))+2*n-2*m-2] = True
    return graph_rep 
    
def color_blue(edge,graph_rep):
    ''' Given an edge represented as a list, the function sorts it and changes the bit corresponding to that edge 01 which 
    will be our convention for saying an edge is blue.  ''' 

    edge = sorted(edge)
    m = edge[0]
    n = edge[1]
    graph_rep[2*m*Graph_Size-(m*(m+1))+2*n-2*m-2] = False
    graph_rep[2*m*Graph_Size-(m*(m+1))+2*n-2*m-1] = True
    return graph_rep

#def check_win(Color,Edges_to_Check,turn_number,past_iterations,win_subgraph):
#    ''' this takes in the most recent edge colored and the graph representation and checks to see if the colored graph now makes 
#    a k_n '''
#    colored_list = []
#    for edges in Edges_to_Check:
#        if(color(Edges)==Color):
#            colored_list.append(Edges)
#    if(len(colored_list)<win_subgraph-past_iterations-1):
#        return false
#    else:
#        past_iterations += 1
#        if(past_iterations==win_subgraph):
#            print("Winning move") 
#            return true
#        else:
#            isterminal(Color,colored_list,turn_number,past_iterations,win_subgraph)
             
def is_terminal(Edge,Edges_to_Check,turn_number):
    if(turn_number==(n*(n-1))/2 or check_win(Edge,Edges_to_Check)):
        return true

#for is terminal take in an edge [x,y] and a list of colored edges that are of the color of the edge and if the length of this list is 
# less than (l*(l-1))/2 then it is not terminal. Else find all of the red edges with x as an endpoint and store them.
# If this is less than l-1, then no. else, 

def check_win(Edge,Edges_to_Check):
    colored_list = []
    stored_vertices = [Edge[0]]
    if (len(Edges_to_Check)<(win_subgraph*(win_subgraph-1))/2):
        return False
    else:
        for edges in Edges_to_Check:
            if(edges[0] == Edge[0]):
                colored_list.append(edges)
                stored_vertices.append(edges[1])
            else:
                if(edges[1]==Edge[0]):
                    colored_list.append(edges)
                    stored_vertices.append(edges[0])
        print(stored_vertices)
        if(len(colored_list)<win_subgraph-1):
            return False
        else:
            Edges_to_Check_0 = []
            for x in range(len(stored_vertices)-1):
                for y in range(x,len(stored_vertices)):
                    if(connect(stored_vertices[x],stored_vertices[y]) in Edges_to_Check):
                        Edges_to_Check_0.append(connect(stored_vertices[x],stored_vertices[y]))
            print(Edges_to_Check_0)
            if(len(Edges_to_Check_0)<(win_subgraph*(win_subgraph-1))/2):
                return False
            else:
                return True
                        
def connect(vertex1,vertex2):
    edge = [min(vertex1,vertex2),max(vertex1,vertex2)]
    return edge            

def get_edges(turns)
    if(turns%2==1):
        return red_edges
    else:
        return blue_edges
        

#The following two lines are to see if the code works as expected.
color_blue([0,1],Graph_Rep)
print(Graph_Rep.bin)
