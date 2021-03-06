#!/usr/bin/python3

from bitstring import BitArray 
import sys 
import random
import math
import copy
import itertools

Graph_Size = 5

def color_red(edge,graph):
    '''Given an edge represented as a list, the function sorts it and changes the bit corresponding to that edge 10 which 
    will be our convention for saying an edge is red.'''
    global Graph_Size 
    edge = sorted(edge)
    m = edge[0]
    n = edge[1]
    #print("input for coloring red:")
    #print(graph['red_edges'],"red")
    #print(graph['blue_edges'],"blue")
    graph['graph_rep'][2*m*Graph_Size-(m*(m+1))+2*n-2*m-1] = False
    graph['graph_rep'][2*m*Graph_Size-(m*(m+1))+2*n-2*m-2] = True
    graph['red_edges'].append(edge)
    #print("blank edges ",intermediate_graph['blank_edges'])
    #print("edge going in to color_red  ",edge)
    graph['blank_edges'].remove(edge)
    #print("just colored red:")
    #print(intermediate_graph['red_edges'])
    #print(intermediate_graph['graph_rep'].bin)

def color_blue(edge,graph):
    ''' Given an edge represented as a list, the function sorts it and changes the bit corresponding to that edge 01 which 
    will be our convention for saying an edge is blue.  '''
    global Graph_Size 
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
    #print("input for coloring blue:")
    #print(graph['blue_edges'],"blue")
    #print(graph['red_edges'],"red")

    graph['graph_rep'][2*m*Graph_Size-(m*(m+1))+2*n-2*m-2] = False
    graph['graph_rep'][2*m*Graph_Size-(m*(m+1))+2*n-2*m-1] = True
    graph['blue_edges'].append(edge)
    graph['blank_edges'].remove(edge)
    #print("just colored blue:")
    #print(intermediate_graph['blue_edges'])
