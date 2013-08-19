#!/usr/bin/python3

import copy
import is_terminal
import Eval

def set_play_num(graph):
    play_num = "all is lost"
    if graph['turn_number']%2 == 1:
        return 1
    else:
        return -1

def Expand(graph):
    ''' Takes in a graph dictionary and returns a list of all possible graphs
    after taking one move. abstract node types in graph["abst"]: 0 is the number
    of nodes with no colored edges, 1 is the number of isolated red edges, 2 is the
    number of isolated green/blue/2nd edges. Returns a list of graphs after
    distinct moves with an attached list of metadata (abstract node numbers).
    adapt to work with BitArray?
    
    Recommended starting values:
    graph['adj']: full size, all zeros
    graph['abst']: graph['abst'][0]= number of nodes
    graph['tuples']: check for win
    graph['scope']: -1
    graph['turn_number']
    graph['val'] = 0
    graph['depth']: 1
    graph['val']: 0'''
    
    play_num = set_play_num(graph)
    child_graphs = []
    new_graph = []

    # iterates through all pairs of non-abstract nodes-
    for real_num in range(0,graph['scope']+1):
        for real_num2 in range(real_num+1,graph['scope']+1):
            # -and if that edge is not taken-
            if graph['adj'][real_num][real_num2] == 0:
                new_graph = layer_update(graph)
                # -it draws an edge between them.
                new_graph['adj'][real_num][real_num2]= play_num
                win_update(new_graph,real_num,real_num2)                
                child_graphs.append(new_graph)           

    # iterates through all combinations of types of abstract nodes/edges
    # and individual non-abstract nodes.
    for real_num in range(0,graph['scope']+1):
        for cat_num in range(0,len(graph['abst'])):
            # if there is still an abstract node/edge of this type-
            if graph['abst'][cat_num]!=0:
                new_graph = layer_update(graph)
                # it draws an edge between the node and the abstract node/edge.
                update_real_abst(new_graph,real_num,cat_num)
                child_graphs.append(new_graph)
 
    # iterates through all pairs of abstract types-
    for cat_num in range(0,len(graph['abst'])):
        for cat_num2 in range(cat_num,len(graph['abst'])):
        # -and if there is one node/edge of both types (or two if the two types are the same type)-
            if graph['abst'][cat_num] != 0 and graph['abst'][cat_num2] != 0 and(cat_num != cat_num2 or graph['abst'][cat_num]>1):
                new_graph = layer_update(graph)
                # it draws an edge between them.
                update_abst_nodes(new_graph,cat_num,cat_num2)
                child_graphs.append(new_graph)
    # increments the turn number BEFORE returning (turn number will always be one ahead)
    for child in child_graphs:
        child['turn_number']+=1
      
    return child_graphs

def layer_update(graph):
    # copies the graph. Maybe make this do something at some point?
    new_graph = copy.deepcopy(graph)
    return new_graph

def win_update(graph,n,m):
    # updates is_terminal structure and game_over value for new edge drawn.
    edge = [n,m]
    graph['game_over'] = is_terminal.is_terminal(graph['tuples'],edge,graph['turn_number'],graph)

def update_abst_nodes(graph,cat1,cat2):
    '''changes the number of abstract nodes of differant kinds and kicks
    non-abstract nodes to the adj matrix '''
    
    play_num = set_play_num(graph)

    # connects two isolated vertices to make an edge of the current players color-
    if cat1 == 0 and cat2 == 0:
        graph['abst'][0]-=2
        if play_num==1:
            graph['abst'][1]+=1
        else:
            graph['abst'][2]+=1
    else:
         # -or un-abstracts anything more complicated by removing them from the abstract nodes/edges,-
        graph['abst'][cat1]-=1
        # -adding them to the BitArray,-
        vert_num1 = kick_to_adj(graph,cat1) 
        graph['abst'][cat2]-=1
        vert_num2 = kick_to_adj(graph,cat2)
        # - and drawing an edge between them.
        graph['adj'][vert_num1][vert_num2] = play_num
        win_update(graph,vert_num1,vert_num2)
                    
def kick_to_adj(graph,abst_type):
    '''Takes a graph and a kind of abstract structure and adds one
    of that abstract structure to the adj matrix.
    returns vert number of the first node kicked  so that it can be found later

    See top for abst_type meanings

    It may someday return the locations of the begining and end of the
    abstract structure kicked if need be.'''
    
    if abst_type ==0:
        # Adds an empty node to the BitArray by expanding the scope.
        graph['scope']+=1
        vert_num = graph['scope']

    elif abst_type ==1:
        # Adds a red edge just outsize of the scope-
        graph['adj'][graph['scope']+1][graph['scope']+2] = 1
        edge = [graph['scope']+1,graph['scope']+2]
        #- and increases scope to contain the edge.
        graph['scope']+=2
        
         #lieing about who's turn it is since this could be an edge from many turns ago.
        graph['game_over'] = is_terminal.is_terminal(graph['tuples'],edge,1,graph)
        vert_num = graph['scope']-1

    elif abst_type ==2:
        # same as above but with blue instead of red.
        graph['adj'][graph['scope']+1][graph['scope']+2] =-1
        edge = [graph['scope']+1,graph['scope']+2]
        graph['scope']+=2
        #lieing about who's turn it is
        graph['game_over'] = is_terminal.is_terminal(graph['tuples'],edge,2,graph)
        vert_num = graph['scope']-1
    else:
        print("something's gone horribly wrong (1)")

    return vert_num

def update_real_abst(graph,real_coords,abst_type):
    '''draws an edge between a real node and an abstract node/edge.'''
    play_num = set_play_num(graph)
    #removes the abstract node/edge-
    graph['abst'][abst_type] -=1
    #-adds it to the BitArray-
    vert_num = kick_to_adj(graph,abst_type)
     #- and draws an edge between the kicked abstract node/edge and the real node.
    graph['adj'][real_coords][vert_num] = play_num
    win_update(graph,real_coords,vert_num)
        
def get_edge(graph,n,m):
    edge_bit1 = graph['graph_rep'][2*m*Graph_Size-(m*(m+1))+2*n-2*m-2]
    edge_bit2 = graph['graph_rep'][2*m*Graph_Size-(m*(m+1))+2*n-2*m-1]
    return edge_bit1,edge_bit2
