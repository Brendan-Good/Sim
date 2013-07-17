#!/usr/bin/python3


import copy
import SimMCTest
import itertools

def Expand(graph):
    ''' Takes in a graph dictionary and returns a list of all possible graphs
    after taking one move. abstract node types in graph["abst"]: 0 is the number
    of nodes with no colored edges, 1 is the number of isolated red edges, 2 is the
    number of isolated green/blue/2nd edges. Returns a list of graphs after
    distinct moves with an attached list of metadata (abstract node numbers).'''

    child_graphs = []
    new_graph = []
    for cat_num in range(0,len(graph['abst'])):
        for cat_num2 in range(cat_num,len(graph['abst'])):
            if graph['abst'][cat_num] != 0 and graph['abst'][cat_num2] != 0 and(cat_num != cat_num2 or graph['abst'][cat_num]>1):
                new_graph = copy.deepcopy(graph)
                new_graph['depth']+=1
                update_abst_nodes(new_graph,cat_num,cat_num2)
                child_graphs.append(new_graph)
    
    for real_num in range(0,graph['scope']):
        for cat_num in range(real_number,len(graph['abst'])):
            print("real_abst tripped")    
            new_graph = copy.deepcopy(graph)
            new_graph['depth']+=1
            update_real_abst(new_graph,real_num,cat_num)
            child_graphs.append(new_graph)
            
    for real_num in range(0,graph['scope']):
        for real_num2 in range(real_num+1,graph['scope']):
            print("real_real tripped")
            new_graph = copy.deepcopy(graph)
            new_graph['depth']+=1
            new_graph['adj'][real_num][real_num2]=1
            child_graphs.append(new_graph)            
    
        
    return child_graphs

def update_abst_nodes(graph,cat1,cat2):
    '''changes the number of abstract nodes of differant kinds and kicks
    non-abstract nodes to the adj matrix '''

    if cat1 == 0 and cat2 == 0:
        graph['abst'][0]-=2
        graph['abst'][1]+=1
    else:
        graph['abst'][cat1]-=1
        vert_num1 = kick_to_adj(graph,cat1) 
        graph['abst'][cat2]-=1
        vert_num2 = kick_to_adj(graph,cat2)
        graph['adj'][vert_num1][vert_num2] = 1
        
            

def kick_to_adj(graph,abst_type):
    '''Takes a graph and a kind of abstract structure and adds one
    of that abstract structure to the adj matrix.
    returns vert number of the first node kicked.
    It may someday return the locations of the begining and end of the
    abstract structure kicked if need be.'''
   
    scope = graph['scope']
            
    if abst_type ==0:
        graph['scope']+=1
        vert_num = graph['scope']

    elif abst_type ==1:
        graph['adj'][scope+1][scope+2] =1
        graph['scope']+=2
        vert_num = graph['scope']-1

    elif abst_type ==2:
        graph['adj'][scope+1][scope+2] =-1
        graph['scope']+=2
        vert_num = graph['scope']-1

    return vert_num

def update_real_abst(graph,real_coords,abst_type):
    '''This function could probably be inline as is, but it may grow if more
    abstract catagories are added'''
    vert_num = kick_to_adj(graph,abst_type)
    graph['adj'][real_coords][vert_num]
        
            

    
