#!/usr/bin/python3

from bitstring import BitArray

import copy

def Expand(graph):
    ' ' ' Takes in a BitArray and returns a list of all possible positions after taking one move.' ' '

    move_list = []
    counter = 0
    while counter < len(graph):
        if graph[counter] == graph[counter+1]:    

            graph.set(True,counter)
            graph.set(False,counter+1)

            move_list.append(copy.copy(graph).bin)
            
            graph.set(False,counter)

        counter += 2

    return move_list

