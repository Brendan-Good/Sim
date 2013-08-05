#!/usr/bin/python3

import copy
import is_terminal
import SimMCTest
from bitstring import BitArray

Graph_Size = 6

def Test_Expand():
    '''Returns an example graph declaration after one expand'''
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
    after taking one move. abstract node types in graph['abst']: 0 is the number
    of nodes with no colored edges, 1 is the number of isolated red edges, 2 is
    the number of isolated green/blue/2nd player edges. graph['abst'][0] is the 
    number of unconnected vertices, graph['abst'][1] is the number of isolated red 
    edges, and so on. Two isolated vertices become one isolated edge.
    
    Returns a list of graphs after all possible distinct moves with a list of
    metadata (abstract node numbers) in the graph dictionary under the name 'abst'.
    
    For recommended starting values see Test_Expand above

    Works by iterating through all combinations of abstract types and "real" 
    verticies and drawning a line between them.

    increments the turn number of all child graphs before returning them so that 
    they are ready to be expanded again without any modification.
    '''

    child_graphs = []
    new_graph = []
    
    for cat_num in range(0,len(graph['abst'])):
        for cat_num2 in range(cat_num,len(graph['abst'])):
            if graph['abst'][cat_num] != 0 and graph['abst'][cat_num2] != 0 and(cat_num != cat_num2 or graph['abst'][cat_num]>1):
                new_graph = layer_update(graph)
                new_graph = update_abst_nodes(new_graph,cat_num,cat_num2)
                child_graphs.append(new_graph)

    for real_num in range(0,graph['scope']+1):
        for cat_num in range(0,len(graph['abst'])):
            if graph['abst'][cat_num]!=0:
                new_graph = layer_update(graph)
                new_graph =  update_real_abst(new_graph,real_num,cat_num)
                child_graphs.append(new_graph)
    
    for real_num in range(0,graph['scope']+1):
        for real_num2 in range(real_num+1,graph['scope']+1):
            if get_edge(graph,real_num,real_num2) == [False,False]:
                new_graph = layer_update(graph)
                edge = [real_num,real_num2]
                new_graph = color(edge,new_graph)
                child_graphs.append(new_graph)            
    
    for child in child_graphs:
        child['turn_number']+=1
      
    return child_graphs

def layer_update(graph):
    ''' currently pointless '''
    new_graph = copy.deepcopy(graph)
    return new_graph

def update_abst_nodes(graph,cat1,cat2):
    '''changes the number of abstract nodes of differant kinds and kicks
    non-abstract nodes to the graph_rep. Copies and returns the graph with these
    changes'''

    if cat1 == 0 and cat2 == 0:
        graph['abst'][0]-=2
        if(graph['turn_number']%2==1):
            graph['abst'][1]+=1
        else:
            graph['abst'][2]+=1
    else:
        graph['abst'][cat1]-=1
        vert_num1,graph = kick_to_graph(graph,cat1) 
        graph['abst'][cat2]-=1
        vert_num2,graph = kick_to_graph(graph,cat2)
        edge = [vert_num1,vert_num2]
        graph = color(edge,graph)
     
    return graph
               
def kick_to_graph(graph,abst_type):
    '''Takes in a graph and a kind of abstract structure and adds one
    of that abstract structure to the graph_rep.
    returns vert number of the first node kicked and the modifed graph.
    It may someday return the locations of the begining and end of the
    abstract structure kicked if an abstract structure is allowed to have non
    isomorphic verticies.'''
    
    if abst_type ==0:
        graph['scope']+=1
        vert_num = graph['scope']

    elif abst_type ==1:
        edge = [graph['scope']+1,graph['scope']+2]
        graph = SimMCTest.color_red(edge,graph)
        graph['scope']+=2
        vert_num = graph['scope']-1

    elif abst_type ==2:
        edge = [graph['scope']+1,graph['scope']+2]
        graph = SimMCTest.color_blue(edge,graph)
        graph['scope']+=2
        vert_num = graph['scope']-1
    else:
        print("something's gone horribly wrong (1)")

    return vert_num,graph

def kick_all(graph):
   '''returns a copy of the graph with all abstract vertices made real via kicking.'''
    new_graph = copy.deepcopy(graph)
    while new_graph['abst'][0]!= 0:
        new_graph['abst'][0]-=1
        new_graph = kick_to_graph(new_graph,0)[1]    
    while new_graph['abst'][1]!= 0:
        new_graph['abst'][1]-=1
        new_graph =  kick_to_graph(new_graph,1)[1]
    while new_graph['abst'][2]!= 0:
        new_graph['abst'][2]-=1
        new_graph =  kick_to_graph(new_graph,2)[1]
    return new_graph

def update_real_abst(graph,real_coords,abst_type):
    '''drawns an edge of the current player's color between a real edge and an
    abstract structure by making that abstract strucure real, then adding the edge '''
    graph['abst'][abst_type] -=1
    vert_num,graph = kick_to_graph(graph,abst_type)
    edge = [real_coords,vert_num]
    graph = color(edge,graph)
    return graph
    
def get_edge(graph,m,n):
    '''returns the normal ones and zeros as trues and falses, but does find them in
    bit array as long as the global graph size is correct '''
    edge_bit1 = graph['graph_rep'][2*m*Graph_Size-(m*(m+1))+2*n-2*m-2]
    edge_bit2 = graph['graph_rep'][2*m*Graph_Size-(m*(m+1))+2*n-2*m-1]
    return [edge_bit1,edge_bit2]

def color(edge,graph):
    '''Adds an edge of the appropreate color to the graph_rep and other
    Brandon related variables.'''
    if(graph['turn_number']%2==1):
        return SimMCTest.color_red(edge,graph)
    else:
        return SimMCTest.color_blue(edge,graph)
    
