#!/usr/bin/python3

from bitstring import BitArray

import copy
import SimMCTest

def Expand(graph):
    ' ' ' Takes in a BitArray and returns a list of all possible positions after taking one move. abstract node types in graph["abst"]: 0 is the number of nodes with no colored edges, 1 is the number of isolated red edges, 2 is the number of isolated green/blue/2nd edges. Returns a list of graphs after distinct moves and a parallel list of metadata.' ' '

    child_graphs = []
    new_graph = []
    for cat_num in range(0,len(graph['abst'])):
        for cat_num2 in range(cat_num,len(graph['abst'])):
            #print(graph['abst'][cat_num])
            #print(graph['abst'][cat_num2])
            if graph['abst'][cat_num] != 0 and graph['abst'][cat_num2] != 0 and(cat_num != cat_num2 or graph['abst'][cat_num]>1):
               # print("if statment passed!")
                print(cat_num)
                print(cat_num2)
                new_graph = copy.deepcopy(graph)
                new_graph['abst'] = update_abst_nodes(new_graph['abst'],cat_num,cat_num2)
                child_graphs.append(new_graph)
    
    

    #print(child_graphs[0]['abst'])
    return child_graphs

def update_abst_nodes(abst,cat1,cat2):
  
    if cat1 == 0 and cat2 == 0:
        abst[0]-=2
        abst[1]+=1
    else:
        abst[cat1]-=1 
        abst[cat2]-=1
    return abst
    

    
    

    
