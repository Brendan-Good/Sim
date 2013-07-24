#!/usr/bin/python
import numpy
import scipy
import math
import itertools

end_condition = 3

graph_size = 6

vertices_set=set(range(graph_size))

possible_kl = list(map(set, itertools.combinations(vertices_set,end_condition)))

def generate_structure(n,l):
    graph_size = n
    end_condition = l
    return numpy.zeros(shape=[n]*l,dtype=float)
    
def is_terminal(structure,edge,turn):
    relevant_kl=update_structure(structure,edge,turn)[1]
    kl_checked = 0
    for index in range(len(relevant_kl)):#For changed kl's check to see if they have value equal to l*(l-1)/2. If so, it's a win. Otherwise increment a counter.
        if(structure[relevant_kl[index]]==(end_condition*(end_condition-1))/2 or structure[relevant_kl[index]]== -1*((end_condition*(end_condition-1))/2)):
            return True 
        else:
            kl_checked+=1
    if(kl_checked==len(relevant_kl)):
        return False

def update_structure(structure,edge,turn):
   
    changed_kls = changed_kl(structure,edge)
    for kls in range(len(changed_kls)):
        if(structure[changed_kls[kls]] != float("-inf")):
            if(turn%2==1):
                if(structure[changed_kls[kls]]>=0):
                    structure[changed_kls[kls]]+=1
                else:
                    structure[changed_kls[kls]]=float("-inf")
            else:
                if(structure[changed_kls[kls]]<=0):
                    structure[changed_kls[kls]]-=1
                else:
                    structure[changed_kls[kls]]=float("-inf")
    return(structure,changed_kls)

def changed_kl(structure,edge): 
    relevant_kl = []
    for index in range(len(possible_kl)):
        if({edge[0],edge[1]}<=possible_kl[index]):#if the edge is a subset of all of the possible kl's, add it to the list of changed kl's
            relevant_kl.append(tuple(possible_kl[index]))
    return relevant_kl
