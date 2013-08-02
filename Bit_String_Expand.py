#!/usr/bin/python3

import copy
import is_terminal
import SimMCTest
from bitstring import BitArray

Graph_Size = "AIIEE"

def Test_Expand():
    n = 6
    l = 3

    global Graph_Size 
    Graph_Size = n

    abst = [n,0,0]
    scope = -1
    depth = n*(n-1)/2
    turn_number = 1
    game_over = False
    graph_rep = (n*(n-1))*BitArray(bin='0')
    red_edges = []
    blue_edges = []
    graph = {'abst':abst,'scope':scope,'depth':depth,'turn_number':turn_number,'game_over':False,'graph_rep':graph_rep,'red_edges':red_edges,'blue_edges':blue_edges}
    
    return Expand(graph)

def Expand(graph):
    ''' Takes in a graph dictionary and returns a list of all possible graphs
    after taking one move. abstract node types in graph["abst"]: 0 is the number
    of nodes with no colored edges, 1 is the number of isolated red edges, 2 is the
    number of isolated green/blue/2nd edges. Returns a list of graphs after
    distinct moves with an attached list of metadata (abstract node numbers).

    add_edge should probably be update_structure
    
    Recommended starting values:
    graph['turn_number']: 1
    graph['graph_rep']: full size, all zeros, bit_string object
    graph['abst']: graph['abst'][0]= number of nodes
    graph['scope']: -1
    graph['depth']: 1'''

    child_graphs = []
    new_graph = []
    
    for cat_num in range(0,len(graph['abst'])):
        for cat_num2 in range(cat_num,len(graph['abst'])):
            if graph['abst'][cat_num] != 0 and graph['abst'][cat_num2] != 0 and(cat_num != cat_num2 or graph['abst'][cat_num]>1):
                new_graph = layer_update(graph)
                update_abst_nodes(new_graph,cat_num,cat_num2)
                child_graphs.append(new_graph)

    for real_num in range(0,graph['scope']+1):
        for cat_num in range(0,len(graph['abst'])):
            if graph['abst'][cat_num]!=0:
                new_graph = layer_update(graph)
                update_real_abst(new_graph,real_num,cat_num)
                child_graphs.append(new_graph)
    
    for real_num in range(0,graph['scope']+1):
        for real_num2 in range(real_num+1,graph['scope']+1):
            if get_edge(graph,real_num,real_num2) == 0:
                new_graph = layer_update(graph)
                edge = [real_num,real_num2]
                color(edge,new_graph)
                child_graphs.append(new_graph)            
          
    return child_graphs

def layer_update(graph):
    new_graph = copy.deepcopy(graph)
    #new_graph['depth']+=1 currently unnecessary 
    new_graph['turn_number']+=1
    return new_graph

def update_abst_nodes(graph,cat1,cat2):
    '''changes the number of abstract nodes of differant kinds and kicks
    non-abstract nodes to the adj matrix '''

    if cat1 == 0 and cat2 == 0:
        graph['abst'][0]-=2
        graph['abst'][1]+=1
    else:
        graph['abst'][cat1]-=1
        vert_num1 = kick_to_graph(graph,cat1) 
        graph['abst'][cat2]-=1
        vert_num2 = kick_to_graph(graph,cat2)
        edge = [vert_num1,vert_num2]
        color(edge,graph)
                    
def kick_to_graph(graph,abst_type):
    '''Takes a graph and a kind of abstract structure and adds one
    of that abstract structure to the adj matrix.
    returns vert number of the first node kicked.
    It may someday return the locations of the begining and end of the
    abstract structure kicked if need be.'''
    
    if abst_type ==0:
        graph['scope']+=1
        vert_num = graph['scope']

    elif abst_type ==1:
        edge = [graph['scope']+1,graph['scope']+2]
        color(edge,graph)
        graph['scope']+=2
        vert_num = graph['scope']-1

    elif abst_type ==2:
        edge = [graph['scope']+1,graph['scope']+2]
        color(edge,graph)
        graph['scope']+=2
        vert_num = graph['scope']-1
    else:
        print("something's gone horribly wrong (1)")

    return vert_num

def kick_all(graph):
    while graph['abst'][1]!= 0:
        kick_to_graph(graph,1)
    while graph['abst'][2]!= 0:
        kick_to_graph(graph,2)


def update_real_abst(graph,real_coords,abst_type):
    '''This function could probably be inline as is, but it may grow if more
    abstract catagories are added, plus this is how the others are done'''
    graph['abst'][abst_type] -=1
    vert_num = kick_to_graph(graph,abst_type)
    edge = [real_coords,vert_num]
    color(edge,graph)
        
def get_edge(graph,n,m):
    edge_bit1 = graph['graph_rep'][2*m*Graph_Size-(m*(m+1))+2*n-2*m-2]
    edge_bit2 = graph['graph_rep'][2*m*Graph_Size-(m*(m+1))+2*n-2*m-1]
    return edge_bit1,edge_bit2

def color(edge,graph):
    if(graph['turn_number']%2==1):
        SimMCTest.color_red(edge,graph)
    else:
        SimMCTest.color_blue(edge,graph)


    
