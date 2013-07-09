#!/usr/bin/python3

from bitstring import BitArray 
import sys 

Graph_Size = int(sys.argv[1])

Graph_Rep = (Graph_Size*(Graph_Size-1))*BitArray([0])#Create a bitarray which represents a complete graph of size Graph_Size where 
#each edge is uncolored

def Color_Red(Edge,Graph_Rep):
    ''' Given an edge represented as a list, the function sorts it and changes the bit corresponding to that edge 10 which 
    will be our convention for saying an edge is red.  ''' 
    Edge = sorted(Edge)
    m = Edge[0]
    n = Edge[1]
    Graph_Rep[2*m*Graph_Size-(m*(m+1))+2*n-2*m-2] = True
    return Graph_Rep
    
def Color_Blue(Edge,Graph_Rep):
    ''' Given an edge represented as a list, the function sorts it and changes the bit corresponding to that edge 01 which 
    will be our convention for saying an edge is blue.  ''' 

    Edge = sorted(Edge)
    m = Edge[0]
    n = Edge[1]
    Graph_Rep[2*m*Graph_Size-(m*(m+1))+2*n-2*m-1] = True
    return Graph_Rep

def Check_Win(Graph,Recent_Edge,Color):
    ''' this takes in the most recent edge colored and the graph representation and checks to see if the colored graph now makes 
a k_n '''
             
def negamax(node, depth, alpha, beta, player):
    '''Perform a depth limited negamax search using functions eval(), expand()
    and isTerminal() as appropriate
    
    Returns (optimal move, negamax value)
    
    Usage: negamax(new_board(), MAX_DEPTH, -inf, +inf, 1)'''
    
    if depth == 0 or is_terminal(node):
        return (None, player * eval(node))
    else:
        candidate_move = None
        for move in expand(node, player):
            val = -1 * negamax(move, depth - 1, -beta, -alpha, -player)[1]
            if val >= beta:
                return (None, val)
            if val > alpha:
                candidate_move = move
                alpha = val
                
        return (candidate_move, alpha)

def expand(node, player):
    '''Expands node for player'''
    moves = []
    
    for i in range(0, N):
        new_node = deepcopy(node)
        for j in range(0, M):
            if new_node[i][j] == 0:
                new_node[i][j] = player
                moves.append(new_node)
                break
            
    return moves
    
def is_terminal(node):
    '''Returns true iff node is a terminal position'''
    
    #check for a win (naive)
    for i in range(0, N):
        for j in range(0, M):
            if (col_win(node, i, j) or row_win(node, i, j) or
                slash_win(node, i, j) or backslash_win(node, i, j)):
                return True
    
    #return false if there are still open spaces
    for i in range(0, N):
        for j in range(0, M):
            if not (node[i][j] == -1 or node[i][j] == 1):
                return False
        
    #fall-through (board is drawn)
    return True
    
def eval(node):
    '''Returns the static evaluation of node
    
    This is a very naive implementation that assigns every square a value
    based on its surrounding (up, left, diag up, diag down) squares
    '''
    val = 0
    for i in range(0, N):
        for j in range(0, M):
            val += point_val(node, i, j)
    
    return val


#The following two lines are to see if the code works as expected.
Color_Blue([0,1],Graph_Rep)
print(Graph_Rep.bin)
       

