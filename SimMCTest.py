#!/usr/bin/python3
#TO DO! Make sure the statistics are passed up correctly (sign flipping? I have not done that yet).  
#In Bit_String_Expand, use the kick_to_graph as an "unabstractor".
from bitstring import BitArray 
import sys 
import random
import math
import copy
import itertools
import Adj_Maxtix_Expand

Graph_Size = 18

win_subgraph = 4

graph_rep = (Graph_Size*(Graph_Size-1))*BitArray(bin='0')#Create a bitarray which represents a complete graph of size Graph_Size where 
#each edge is uncolored

class Node:
    def __init__(self,parent,children,runs,wins,value,board):
        self.self = self
        self.parent = parent
        self.children = children
        self.runs = runs
        self.wins = wins
        self.value = value
        self.board = board

root = Node([],[],0,0,0,Graph_Rep)

total_runs = 0

red_edges = []

blue_edges = []

blank_edges = []

max_iterations = 10000

random_games = 100

total_runs = 0

graph = {'graph_rep':graph_rep,'total_runs':total_runs, 'red_edges':red_edges, 'blue_edges':blue_edges,'blank_edges':blank_edges}

def monte_carlo(max_iterations,node=root):
    while node.children != [] or max_iterations > 0:
        node = best_child(node)
    for boards in Adj_Maxtix_Expand.Expand(best_child(node)):
        node.append(Node(node,[],0,0,float('inf'),boards))

def update_statistics(node,value):
    node.runs += 1
    global total_runs
    total_runs += 1
    node.value = (node.wins+value)/node.runs
    iterative_update(node)
    return node

def iterative_update(node):
    while node!=root:
        node = node.parent
        for children in node.children:
            node.value = (children.runs/total_runs)*children.value

def best_child(node):
    return max(node.children,key=value)

def value(node):
    value = node.value+math.sqrt((2*math.log(total_runs))/node.runs)
    return value

#I actually do not want to expand, but to just play a random game until it's over.
def play_random(node,graph,player_turn,):
    node.runs += 1
    while True:
        if(player_turn%2 == 1):
            if(not check_win(graph['blue_edges'],turn_number)):
                color_red(random.choice(graph['blank_edges'])
                player_turn+=1
            else:
                return node
        if(player_turn%2 == 0):
            if(not check_win(graph['red_edges'],turn_number)):    
                color_blue(random.choice(graph['blank_edges']))
                player_turn+=1
            else:
                node.wins += 1
                return node 

def color_red(edge,graph):
    '''Given an edge represented as a list, the function sorts it and changes the bit corresponding to that edge 10 which 
    will be our convention for saying an edge is red.''' 
    edge = sorted(edge)
    m = edge[0]
    n = edge[1]
    graph['graph_rep'[2*m*Graph_Size-(m*(m+1))+2*n-2*m-1]] = False
    graph['graph_rep'[2*m*Graph_Size-(m*(m+1))+2*n-2*m-2]] = True
    global red_edges
    graph['red_edges'] = copy.deepcopy(red_edges)
    graph['red_edges'].append(edge)
    return graph
    
def color_blue(edge,graph_rep):
    ''' Given an edge represented as a list, the function sorts it and changes the bit corresponding to that edge 01 which 
    will be our convention for saying an edge is blue.  ''' 

    edge = sorted(edge)
    m = edge[0]
    n = edge[1]
    graph['graph_rep'[2*m*Graph_Size-(m*(m+1))+2*n-2*m-2]] = False
    graph['graph_rep'[2*m*Graph_Size-(m*(m+1))+2*n-2*m-1]] = True
    global blue_edges
    graph['blue_edges'] = copy.deepcopy(blue_edges)
    graph['blue_edges'].append(edge)
    return graph

def is_terminal(Edge,Edges_to_Check,turn_number):
    if(turn_number==(n*(n-1))/2 or check_win(Edge,Edges_to_Check)):
        return true

#for is terminal take in an edge [x,y] and a list of colored edges that are of the color of the edge and if the length of this list is 
# less than (l*(l-1))/2 then it is not terminal. Else find all of the red edges with x as an endpoint and store them.
# If this is less than l-1, then no. else, 

def check_win(Edge,Edges_to_Check):
    '''
    takes in the edge just colored and all edges of that color and checks to see if that satisfies the condition for a win.
    Example: [x,y] colored blue. check_win takes[x,y] and all of the blue_edges as input.
    '''
    colored_list = [[Edge[0],Edge[1]]]
    stored_vertices = []
    if (len(Edges_to_Check)<(win_subgraph*(win_subgraph-1))/2):#If there aren't enough edges of the same color as our edge, then false.
        return False
    else:
        for edges in Edges_to_Check:#If any of our edges in Edges_to_Check has Edge[0] as an endpoint, add the other endpoint to our list of stored vertices
            if(edges==Edge):
                continue
            if(edges[0] == Edge[0]):
                colored_list.append(edges)
                stored_vertices.append(edges[1])
            else:
                if(edges[1]==Edge[0]):
                    colored_list.append(edges)
                    stored_vertices.append(edges[0])
        print(stored_vertices,"stored_vertices")
        print(colored_list,"colored_list")
        if(len(colored_list)<win_subgraph-1):
            return False
        else:
            l_minus_2_combinations = list(itertools.combinations(stored_vertices,win_subgraph-2))#create an l-2 combination of the stored vertices (we omit the two endpoints of Edge as it is guaranteed to be in a k_l if Edge forms a new k_l)
            iterator = 0
            for combinations in range(len(l_minus_2_combinations)):
                l_minus_2_combinations[combinations]=list(l_minus_2_combinations[combinations])
                l_minus_2_combinations[combinations].append(Edge[0])
                l_minus_2_combinations[combinations].append(Edge[1])
                print(l_minus_2_combinations,"l-2 combinations")
                potential_kl = []
                for x in range(win_subgraph-1):#For every combination, check if every vertex is connected to every other vertex.
                    for y in range(x+1,win_subgraph):
                        if(connect(l_minus_2_combinations[combinations][x],l_minus_2_combinations[combinations][y]) in Edges_to_Check):
                            potential_kl.append(connect(l_minus_2_combinations[combinations][x],l_minus_2_combinations[combinations][y]))
                            print(potential_kl,"potential_kl")
                if(len(potential_kl)>=(win_subgraph*(win_subgraph-1))/2):
                    return True
                else:
                    iterator+=1
                    print(iterator)
            if(iterator==len(l_minus_2_combinations)):
                return False
                        
def connect(vertex1,vertex2):
    edge = [min(vertex1,vertex2),max(vertex1,vertex2)]
    return edge #return the edge connecting vertex1 and vertex2           

def get_edges(turns):
    if(turns%2==1):
        return red_edges
    else:
        return blue_edges

#The following line(s) is/are to see if the code works as expected.
print(Graph_Rep.bin)
