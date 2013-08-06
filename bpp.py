def get_edge(graph,m,n,Graph_Size):
    edge_bit1 = graph['graph_rep'][2*m*Graph_Size-(m*(m+1))+2*n-2*m-2]
    edge_bit2 = graph['graph_rep'][2*m*Graph_Size-(m*(m+1))+2*n-2*m-1]
    return [edge_bit1,edge_bit2]

def princess_print(graph,Graph_Size):
    display = ""
    disp = "   "
    
    for x in range(0,Graph_Size):
        disp += str(x)
        disp += " "
    print(disp)
    print(" ")
    for x in range(0,Graph_Size):
        display+=str(x)
        display+=" "
        for y in range(0,Graph_Size):
            if y > x:
                if get_edge(graph,x,y,Graph_Size) == [False,True]:
                    display+="-1"
                elif get_edge(graph,x,y,Graph_Size) == [True,False]:
                    display+=" 1"
                else:
                    display+=" 0"
            else:
                display+=" 0"
        print(display) 
        display = ""
