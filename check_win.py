#!/usr/bin/python3
def check_win(Edge,Edges_to_Check,win_subgraph):
    colored_list = []
    stored_vertices = [Edge[0]]
    if (len(Edges_to_Check)<(win_subgraph*(win_subgraph-1))/2):
        return False
    else:
        for edges in Edges_to_Check:
            if(edges[0] == Edge[0]):
                colored_list.append(edges)
                stored_vertices.append(edges[1])
            else:
                if(edges[1]==Edge[0]):
                    colored_list.append(edges)
                    stored_vertices.append(edges[0])
        print(stored_vertices)
        if(len(colored_list)<win_subgraph-1):
            return False
        else:
            Edges_to_Check_0 = []
            for x in range(len(stored_vertices)-1):
                for y in range(x,len(stored_vertices)):
                    if(connect(stored_vertices[x],stored_vertices[y]) in Edges_to_Check):
                        Edges_to_Check_0.append(connect(stored_vertices[x],stored_vertices[y]))
            print(Edges_to_Check_0)
            if(len(Edges_to_Check_0)<(win_subgraph*(win_subgraph-1))/2):
                return False
            else:
                return True
