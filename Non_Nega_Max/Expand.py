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

    for real_num in range(0,graph['scope']+1):
        for real_num2 in range(real_num+1,graph['scope']+1):
            if graph['adj'][real_num][real_num2] == 0:
                new_graph = layer_update(graph)
                new_graph['adj'][real_num][real_num2]= play_num
                win_update(new_graph,real_num,real_num2)                
                child_graphs.append(new_graph)           

    for real_num in range(0,graph['scope']+1):
        for cat_num in range(0,len(graph['abst'])):
            if graph['abst'][cat_num]!=0:
                new_graph = layer_update(graph)
                update_real_abst(new_graph,real_num,cat_num)
                child_graphs.append(new_graph) 
    
    for cat_num in range(0,len(graph['abst'])):
        for cat_num2 in range(cat_num,len(graph['abst'])):
            if graph['abst'][cat_num] != 0 and graph['abst'][cat_num2] != 0 and(cat_num != cat_num2 or graph['abst'][cat_num]>1):
                new_graph = layer_update(graph)
                update_abst_nodes(new_graph,cat_num,cat_num2)
                child_graphs.append(new_graph)

    for child in child_graphs:
        child['turn_number']+=1
      
    return child_graphs

def layer_update(graph):
    new_graph = copy.deepcopy(graph)
    return new_graph

def win_update(graph,n,m):
    edge = [n,m]
    graph['game_over'] = is_terminal.is_terminal(graph['tuples'],edge,graph['turn_number'])
    graph['val'] = Eval.Eval(graph,edge)    

def update_abst_nodes(graph,cat1,cat2):
    '''changes the number of abstract nodes of differant kinds and kicks
    non-abstract nodes to the adj matrix '''
    
    play_num = set_play_num(graph)

    if cat1 == 0 and cat2 == 0:
        graph['abst'][0]-=2
        if play_num==1:
            graph['abst'][1]+=1
        else:
            graph['abst'][2]+=1
    else:
        graph['abst'][cat1]-=1
        vert_num1 = kick_to_adj(graph,cat1) 
        graph['abst'][cat2]-=1
        vert_num2 = kick_to_adj(graph,cat2)
        graph['adj'][vert_num1][vert_num2] = play_num
        win_update(graph,vert_num1,vert_num2)
                    
def kick_to_adj(graph,abst_type):
    '''Takes a graph and a kind of abstract structure and adds one
    of that abstract structure to the adj matrix.
    returns vert number of the first node kicked.
    It may someday return the locations of the begining and end of the
    abstract structure kicked if need be.'''
    
    if abst_type ==0:
        graph['scope']+=1
        vert_num = graph['scope']

    elif abst_type ==1:
        graph['adj'][graph['scope']+1][graph['scope']+2] = 1
        edge = [graph['scope']+1,graph['scope']+2]
        #lieing about who's turn it is
        graph['game_over'] = is_terminal.is_terminal(graph['tuples'],edge,1)
        graph['scope']+=2
        vert_num = graph['scope']-1

    elif abst_type ==2:
        graph['adj'][graph['scope']+1][graph['scope']+2] =-1
        edge = [graph['scope']+1,graph['scope']+2]
        #lieing about who's turn it is
        graph['game_over'] = is_terminal.is_terminal(graph['tuples'],edge,2)
        

        graph['scope']+=2
        vert_num = graph['scope']-1
    else:
        print("something's gone horribly wrong (1)")

    return vert_num

def update_real_abst(graph,real_coords,abst_type):
    '''This function could probably be inline as is, but it may grow if more
    abstract catagories are added, plus this is how the others are done'''
    play_num = set_play_num(graph)
    graph['abst'][abst_type] -=1
    vert_num = kick_to_adj(graph,abst_type)
    graph['adj'][real_coords][vert_num] = play_num
    win_update(graph,real_coords,vert_num)
        
def get_edge(graph,n,m):
    edge_bit1 = graph['graph_rep'][2*m*Graph_Size-(m*(m+1))+2*n-2*m-2]
    edge_bit2 = graph['graph_rep'][2*m*Graph_Size-(m*(m+1))+2*n-2*m-1]
    return edge_bit1,edge_bit2
