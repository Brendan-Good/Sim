#!/usr/bin/python
import numpy
import scipy
import math
import itertools

end_condition = "type clash!"

graph_size = "type clash!"

vertices_set = "type clash!"

possible_kl = "type clash!" 

def generate_structure(n,l):
    global graph_size
    graph_size = n
    global vertices_set
    vertices_set=set(range(graph_size))
    global end_condition
    end_condition = l
    global possible_kl
    possible_kl = list(map(set, itertools.combinations(vertices_set,end_condition)))
    return numpy.zeros(shape=[n]*l,dtype=float)
    
def is_terminal(structure,edge,turn,graph):
    relevant_kl=update_structure(structure,edge,turn,graph)[1]
    kl_checked = 0
    for index in range(len(relevant_kl)):#For changed kl's check to see if they have value equal to l*(l-1)/2. If so, it's a win. Otherwise increment a counter.
        if(structure[relevant_kl[index]]==(end_condition*(end_condition-1))/2 or structure[relevant_kl[index]]== -1*((end_condition*(end_condition-1))/2)):
            return True 
        else:
            kl_checked+=1
    if(kl_checked==len(relevant_kl)):
        return False

def update_structure(structure,edge,turn,graph):
   
    changed_kls = changed_kl(structure,edge)
    for kls in range(len(changed_kls)):
        if(structure[changed_kls[kls]] != float("-inf")):
            if(turn%2==1):
                if(structure[changed_kls[kls]]>=0):
                    structure[changed_kls[kls]]+=1
                    graph['val']+= structure[changed_kls[kls]] **2
                    #graph['val']+= structure[changed_kls[kls]] **3
                else:
                    n = structure[changed_kls[kls]]
                    graph['val']-= (n*(n+1)*(2*n+1))/6
                    #graph['val']-= (n*(n+1)/2)**2
                    structure[changed_kls[kls]]=float("-inf")
            else:
                if(structure[changed_kls[kls]]<=0):
                    structure[changed_kls[kls]]-=1
                    graph['val']-= structure[changed_kls[kls]] **2
                    #graph['val']-= structure[changed_kls[kls]] **3
                else:
                    n = structure[changed_kls[kls]]
                    graph['val']+= (n*(n+1)*(2*n+1))/6
                    #graph['val']+= (n*(n+1)/2)**2
                    structure[changed_kls[kls]]=float("-inf")
    return(structure,changed_kls)

def changed_kl(structure,edge): 
    relevant_kl = []
    for index in range(len(possible_kl)):
        if({edge[0],edge[1]}<=possible_kl[index]):#if the edge is a subset of all of the possible kl's, add it to the list of changed kl's
            relevant_kl.append(tuple(possible_kl[index]))
    return relevant_kl
