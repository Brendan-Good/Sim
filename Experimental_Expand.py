#!/usr/bin/python3

from bitstring import BitArray

import copy
import SimMCTest

def Expand(graph,cat_nodes):
    ' ' ' Takes in a BitArray and returns a list of all possible positions after taking one move. cat is short for both categorized and category. categories: 0 is nodes with no colored edges, 1 is nodes that are part of an isolated red edge, 2 is part of an isolated green/blue/2nd player edge. These edges will be put in by pairs based on the edge that connects them. Returns a list of graphs after distinct moves and a parallel list of metadata. cat_nodes is a list of node categories with numbers representing nodes inside them.' ' '

    move_list = []
    child_graphs = []
    new_categorized_nodes = []
    
    if len(cat_nodes[0])>1:
        child_graphs.append(color_red(cat_nodes[0][0], cat_nodes[0][1]))
        new_categorized_nodes.append(update_node_categories(cat_nodes,cat_nodes[0][0],cat_nodes[0][1])

    if len(cat_nodes[1])>2:
        child_graphs.append(color_red(cat_nodes[1][0], cat_nodes[1][2]))
        new_categorized_nodes.append(update_node_categories(cat_nodes,cat_nodes[1][0],cat_nodes[1][2])

    if len(cat_nodes[1])>2:
        child_graphs.append(color_red(cat_nodes[2][0], cat_nodes[2][2]))
        new_categorized_nodes.append(update_node_categories(cat_nodes,cat_nodes[2][0],cat_nodes[2][2])

    for cat_number in range(0,len(cat_nodes)-1):
        for cat_number2 in range(cat_number+1,len(cat_nodes)):    
            
            child_graphs.append(color_red(cat_nodes[cat_number][0], cat_nodes[cat_number2][0]))
            new_categorized_nodes.append(update_node_categories(cat_nodes,category[0],cat_number,category2[0],cat_number2)
    

    return move_list

    def update_node_categories(cat_nodes,n,ind_of_n,m,ind_of_m):
    
        if ind_of_n == 0 & ind_if_m == 0:
            x = 2
        return x
    




    
