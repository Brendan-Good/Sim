#!/usr/bin/python3
#TO DO! Make sure the statistics are passed up correctly (sign flipping? I have not done that yet).  
#In Bit_String_Expand, use the kick_to_graph as an "unabstractor".
from bitstring import BitArray 
import sys 
import random
import math
import copy
import itertools
import Bit_String_Expand

Graph_Size = 6

win_subgraph = 3

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

red_edges = []

blue_edges = []

blank_edges = []

for x in range(Graph_Size-1):
    for y in range(x+1,Graph_Size):
        blank_edges.append([x,y])

abst = [6,0,0]

scope = -1

max_iterations = 10000#This currently does nothing

total_runs = 1

turn_number = 1

last_random_blue = []

last_random_red = []

graph = {'graph_rep':graph_rep,'total_runs':total_runs, 'red_edges':red_edges, 'blue_edges':blue_edges,'blank_edges':blank_edges,'abst':abst, 'scope':scope, 'turn_number':turn_number}

root = Node([],[],0,0,0,graph)

def monte_carlo(turn,max_iterations=10000,node=root):
    global last_random_red
    global last_random_blue
    global Graph_Size
    if(turn == 15):
        print("game over, I'll do some stuff to figure out who won later.")
    if(turn != 1 and turn%2==1 and check_win(last_random_red,node.board['red_edges'])):
        return best_child(node).board
    elif(turn%2==0 and check_win(last_random_blue,node.board['blue_edges'])):
        return best_child(node).board
    #while node.children != []:
    #    node = best_child(node)
    #    max_iterations -= 1
    for boards in Bit_String_Expand.Expand(node.board):
        (node.children).append(Node(node,[],0,0,float('inf'),boards))
    for nodes in node.children:
        thing = copy.deepcopy(nodes.board)
        play_random(nodes,Bit_String_Expand.kick_all(thing),nodes.board['turn_number'])
    print(node.board)
    print(Bit_String_Expand.kick_all(node.board))
    print("it is about to be turn:", turn+1)
    monte_carlo(turn+1,10000,best_child(node))

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
    if(node.runs == 0):
        value = float('inf')
    else:
        value = node.value+math.sqrt((2*math.log(total_runs))/node.runs)
    return value

def play_random(node,graph,player_turn,):
    global last_random_red
    global last_random_blue
    node.runs += 1
    random_games = 100 
    original_graph = graph
    last_graph = graph
    original_turn = player_turn
    while random_games > 0:
        while True:
            if(player_turn%2 == 1):
                if(last_random_blue==[]):
                    last_random_red = random.choice(graph['blank_edges'])
                    last_graph = color_red(last_random_red,graph)
                    player_turn += 1
                    continue
                elif(not check_win(last_random_blue,last_graph['blue_edges'])):
                    last_random_red = random.choice(last_graph['blank_edges'])
                    last_graph = color_red(last_random_red,last_graph)
                    player_turn += 1
                    continue
                else:
                    node = update_statistics(node,0)
                    break#I'm definitely going to have to change this later
            if(player_turn%2 == 0):
                if(last_random_red==[]):
                    print(graph['blank_edges'])
                    last_random_blue = random.choice(graph['blank_edges'])
                    last_graph = color_blue(last_random_blue,graph)
                    player_turn+=1
                    continue
                elif(not check_win(last_random_red,last_graph['red_edges'])):    
                    last_random_blue = random.choice(last_graph['blank_edges'])
                    last_graph = color_blue(last_random_blue,last_graph)
                    player_turn+=1
                    continue
                else:
                    node = update_statistics(node,1)
                    break#this too
        random_games -= 1
        print("game over")
        print("random_games is now", random_games)
        if(random_games == 0):
            break
        player_turn = original_turn
        last_random_blue = []
        last_random_red = []
        graph = original_graph

def color_red(edge,graph):
    '''Given an edge represented as a list, the function sorts it and changes the bit corresponding to that edge 10 which 
    will be our convention for saying an edge is red.''' 
    edge = sorted(edge)
    m = edge[0]
    n = edge[1]
    print("input for coloring red:")
    print(graph['red_edges'],"red")
    print(graph['blue_edges'],"blue")
    intermediate_graph = copy.deepcopy(graph)
    intermediate_graph['graph_rep'][2*m*Graph_Size-(m*(m+1))+2*n-2*m-1] = False
    intermediate_graph['graph_rep'][2*m*Graph_Size-(m*(m+1))+2*n-2*m-2] = True
    intermediate_graph['red_edges'].append(edge)
    intermediate_graph['blank_edges'].remove(edge)
    print("just colored red:")
    print(intermediate_graph['red_edges'])
    print(intermediate_graph['graph_rep'].bin)
    return copy.copy(intermediate_graph)
    
    
    
def color_blue(edge,graph):
    ''' Given an edge represented as a list, the function sorts it and changes the bit corresponding to that edge 01 which 
    will be our convention for saying an edge is blue.  ''' 
    edge = sorted(edge)
    m = edge[0]
    n = edge[1]
    #graph['graph_rep'][2*m*Graph_Size-(m*(m+1))+2*n-2*m-2] = False
    #graph['graph_rep'][2*m*Graph_Size-(m*(m+1))+2*n-2*m-1] = True
    #graph['blue_edges'] = copy.deepcopy(blue_edges)
    #graph['blue_edges'].append(edge)
    #graph['blank_edges'] = copy.deepcopy(blank_edges)
    #graph['blank_edges'].remove(edge)
    #return graph
    print("input for coloring blue:")
    print(graph['blue_edges'],"blue")
    print(graph['red_edges'],"red")
    intermediate_graph = copy.deepcopy(graph)
    intermediate_graph['graph_rep'][2*m*Graph_Size-(m*(m+1))+2*n-2*m-2] = False
    intermediate_graph['graph_rep'][2*m*Graph_Size-(m*(m+1))+2*n-2*m-1] = True
    intermediate_graph['blue_edges'].append(edge)
    intermediate_graph['blank_edges'].remove(edge)
    print("just colored blue:")
    print(intermediate_graph['blue_edges'])
    return copy.copy(intermediate_graph)


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
    original_edge = Edge
    colored_list = [[Edge[0],Edge[1]]]
    stored_vertices = []
    if (len(Edges_to_Check)<(win_subgraph*(win_subgraph-1))/2):#If there aren't enough edges of the same color as our edge, then false.
        print(Edges_to_Check,"Edges_to_Check")
        return False
    else:
        for edges in Edges_to_Check:#If any of our edges in Edges_to_Check has Edge[0] as an endpoint, add the other endpoint to our list of stored verticesn
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
            for combinations in range(len(l_minus_2_combinations)):
                iterator = 0
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
print(graph['graph_rep'].bin)
