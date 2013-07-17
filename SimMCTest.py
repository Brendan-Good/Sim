#!/usr/bin/python3

from bitstring import BitArray 
import sys 
import random

Graph_Size = 18

Graph_Rep = (Graph_Size*(Graph_Size-1))*BitArray(bin='0')#Create a bitarray which represents a complete graph of size Graph_Size where 
#each edge is uncolored

max_iterations = 10000

red_list = []

blue_list = []

class node:
    def __init__(self,parent,children,runs,wins,value):
        self.self = self
        self.parent = parent
        self.children = children
        self.runs = runs
        self.wins = wins
        self.value = value
        
def color_red(Edge,Graph_Rep,redlist=[]):
    ''' Given an edge represented as a list, the function sorts it and changes the bit corresponding to that edge 10 which 
    will be our convention for saying an edge is red.  ''' 
    Edge = sorted(Edge)
    m = Edge[0]
    n = Edge[1]
    Graph_Rep[2*m*Graph_Size-(m*(m+1))+2*n-2*m-1] = False
    Graph_Rep[2*m*Graph_Size-(m*(m+1))+2*n-2*m-2] = True
    redlist.append(Edge)
    return Graph_Rep
    
def color_blue(Edge,Graph_Rep,bluelist=[]):
    ''' Given an edge represented as a list, the function sorts it and changes the bit corresponding to that edge 01 which 
    will be our convention for saying an edge is blue.  ''' 

    Edge = sorted(Edge)
    m = Edge[0]
    n = Edge[1]
    Graph_Rep[2*m*Graph_Size-(m*(m+1))+2*n-2*m-2] = False
    Graph_Rep[2*m*Graph_Size-(m*(m+1))+2*n-2*m-1] = True
    bluelist.append(Edge)
    return Graph_Rep

def is_terminal(Color,Edges_to_Check,turn_number,past_iterations,win_subgraph):
    if(turn_number==(n*(n-1))/2 or check_win(Color,Edges_to_Check,turn_number,past_iterations,win_subgraph)):
        return true

#for is terminal take in an edge [x,y] and a list of colored edges that are of the color of the edge and if the length of this list is 
# less than (l*(l-1))/2 then it is not terminal. Else find all of the red edges with x as an endpoint and store them.
# If this is less than l-1, then no. else, 


#it is worth noting that, as it stands, this function is garbage but it IS salvagable!
def check_win(Edge,Edges_to_Check,win_subgraph):
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
                intermediary_edges=Edges_to_Check_0
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
            
#The following two lines are to see if the code works as expected.
color_blue([0,1],Graph_Rep)
print(Graph_Rep.bin)
