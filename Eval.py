from bitstring import BitArray
import SimMCTest

def Eval(move_graph, edge_drawn):
    '''Only works for finding K3's. Static evaluator for moves. move_graph is a BitString. edge_drawn is a list.'''
    total = 0
    curr_edges = []
    opp_edges = []
    curr_edges_connected1 = []    #List of vertices with current turn edges that are connected to vertice1 of edge_drawn
    curr_edges_connected2 = []    #List of vertices with current turn edges that are connected to vertice2 of edge_drawn
    opp_edges_connected1 = []    #List of vertices with opposing turn edges that are connected to vertice1 of edge_drawn
    opp_edges_connected2 = []    #List of vertices with opposing turn edges that are connected to vertice2 of edge_drawn
    if (total_runs-1)%2==1:
        curr_edges = get_edges(3)
        opp_edges = get_edges(2)
    else:
        curr_edges = get_edges(2)
        opp_edges = get_edges(3)
    for s in range(len(curr_edges)):    #Adds all vertices with current turn edges connected to vertice1 to a list
        if curr_edges[s][0]==edge_drawn[0]:
            curr_edges_connected1.append(curr_edges[s][1])
        elif curr_edges[s][1]==edge_drawn[0]:
            curr_edges_connected1.append(curr_edge[s][0])
    for t in range(len(curr_edges)):    #Adds all vertices with current turn edges connected to vertice2 to a list
        if curr_edges[t][0]==edge_drawn[1]:
            curr_edges_connected2.append(curr_edges[t][1])
        elif curr_edges[t][1]==edge_drawn[1]:
            curr_edges_connected2.append(curr_edges[t][0])
    for u in range(len(opp_edges)):    #Adds all vertices with opposing turn edges connected to vertice1 to a list
        if opp_edges[u][0]==edge_drawn[0]:
            opp_edges_connected1.append(opp_edges[u][1])
        elif opp_edges[u][1]==edge_drawn[0]:
            opp_edges_connected1.append(opp_edges[u][0])
    for v in range(len(opp_edges)):    #Adds all vertices with opposing turn edges connected to vertice2 to a list
        if opp_edges[v][0]==edge_drawn[1]:
            opp_edges_connected2.append(opp_edges[v][1])
        elif opp_edges[v][1]==edge_drawn[1]:
            opp_edges_connected2.append(opp_edges[v][0])
    for w in range(len(curr_edges_connected1)):    #Returns infinity if edge_drawn is the winning move
        for x in range(len(curr_edges_connected2)):
            if curr_edges_connected1[w]==curr_edges_connected2[x]:
                total = float(inf)
                return total
    for y in range(len(opp_edges_connected1)):    #Adds 10 to total score for every opposing potential K3 that is blocked by edge_drawn
        for z in range(len(opp_edges_connected2)):
            if opp_edges_connected1[y]==opp_edges_connected2[z]:
                total += 10
    total += 5*len(curr_edges_connected1)    #Adds 5 to total score for every chain of two current color edges
    total += 5*len(curr_edges_connected2)
    return total
    
