def Nega(graph):
    '''Nega function for graph'''
    for s in range(len(graph['adj'])):    #Switches red edges and blue edges for the adjacency matrix
        for t in range(len(graph['adj'][0])):
            if graph['adj'][s][t]==1:
                graph['adj'][s][t]==-1
            elif graph['adj'][s][t]==-1:
                graph['adj'][s][t]==1
    temp1 = graph['abst'][1]    #Switches the number of red edges and blue edges for abst
    temp2 = graph['abst'][2]
    graph['abst'][1] = temp2
    graph['abst'][2] = temp1

