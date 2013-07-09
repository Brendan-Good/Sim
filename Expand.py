#!/usr/bin/python3

from bitstring import BitArray

import copy

def Expand(edge_data):
    ' ' ' Takes in a BitArray and returns a list of all possible positions after taking one move.
    ' ' '

    move_list = []
    counter = 0
    bit_one = 0
    bit_two = 0
    while counter < len(edge_data):
        if edge_data[counter] == edge_data[counter+1]:

            bit_one = edge_data[counter]
            bit_two = edge_data[counter+1]

            edge_data.set(True,counter)
            edge_data.set(False,counter+1)

            move_list.append(copy.copy(edge_data).bin)

            edge_data.set(bit_one,counter)
            edge_data.set(bit_two,counter+1)

        counter += 2

    return move_list
